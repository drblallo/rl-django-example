import os
import sys

import tic_tac_toe.wrapper as tic_tac_toe
from django.http import HttpResponse
from django.template import loader
from rlc import Program, State
from filelock import FileLock


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# implementation that uses the python libraries to simplify the
# inspection of RLC data structures
def slow_load():
    program = Program(tic_tac_toe)
    state = State(program)

    with FileLock("game_state.lock", timeout=10):
        if os.path.exists("game_state.txt"):
            file = "\n".join(open("game_state.txt").readlines())
            state.load_string(file)
    return state


def game_state_simple(request):
    state = slow_load()
    return make_game_page(state.state, request)


# helper functions to easity convert between rlc and python strings objects
# (maybe in the future this will be implicit)
def to_rl_string(string):
    return tic_tac_toe.rl_s__strlit_r_String(string)


def to_python_string(string):
    first_character = getattr(getattr(string, "__data"), "__data")
    return tic_tac_toe.cast(first_character, tic_tac_toe.c_char_p).value.decode("utf-8")

def to_python_list(rlc_vector):
    return [
        tic_tac_toe.functions.get(rlc_vector, x).contents.copy()
        for x in range(tic_tac_toe.functions.size(rlc_vector))
    ]

# saves the content the game on disk, locking the file to avoid races
def store(state):
    with FileLock("game_state.lock", timeout=10):
        string = to_python_string(tic_tac_toe.functions.to_string(state))
        with open("game_state.txt", "w+") as f:
            f.write(string)


# implementation that uses raw access to the python RLC
# wrapper, and thus get autocomplete support
def efficient_load():
    state = None
    with FileLock("game_state.lock", timeout=10):
        if not os.path.exists("game_state.txt"):
            # get state to be the start of the game
            state = tic_tac_toe.functions.play()
        else:
            # allocate a empty game
            state = tic_tac_toe.Game()
            # allocate a empty string
            content = tic_tac_toe.String()
            # manually load the file and turn it into a rlc string
            string = to_rl_string("\n".join(open("game_state.txt", "r").readlines()))
            # manually parse the string and turn it into a game
            tic_tac_toe.functions.from_string(state, string)
    return state


def make_game_page(state, request):
    template = loader.get_template("tic_tac_toe/game_state.html")
    string = to_python_string(tic_tac_toe.functions.to_string(state))
    action = tic_tac_toe.AnyGameAction()
    actions = to_python_list(tic_tac_toe.functions.enumerate(action))

    filtered_serialized_actions = [
        to_python_string(tic_tac_toe.functions.to_string(x))
        for x in actions
        if tic_tac_toe.functions.can_apply(x, state)
    ]

    context = {
        "board": [
            [state.board.slots[i * 3 + y].value for i in range(3)] for y in range(3)
        ],
        "current_player": state.board.playerTurn,
        "serialized": string,
        "actions": filtered_serialized_actions,
    }
    return HttpResponse(template.render(context, request))


def game_state_efficient(request):
    state = efficient_load()
    return make_game_page(state, request)


def act(request, action):
    state = efficient_load()
    parsed = tic_tac_toe.AnyGameAction()
    # validate the user provided string
    if tic_tac_toe.functions.from_string(parsed, to_rl_string(action)):
        # check if the action is applicable
        if tic_tac_toe.functions.can_apply(parsed, state):
            # apply it
            tic_tac_toe.functions.apply(parsed, state)
            store(state)
    return make_game_page(state, request)


def reset(request):
    state = tic_tac_toe.functions.play()
    store(state)
    return make_game_page(state, request)

# converter to be able to use rlc types
# in url formats.
def make_converter(rlc_type):
    class Converter:
        regex = ".*"
        def to_url(self, value):
            return to_python_string(tic_tac_toe.functions.to_string(value))

        def to_python(self, value):
            obj = rlc_type()
            if tic_tac_toe.functions.parse_string(obj, to_rl_string(value), 0):
                return obj
            return None

    return Converter


# Custom implementation that may be required to create animations
def mark(request, x, y):
    state = None
    with FileLock("game_state.lock", timeout=10):
        if not os.path.exists("game_state.txt"):
            state = tic_tac_toe.functions.play()
        else:
            state = tic_tac_toe.Game()
            content = tic_tac_toe.String()
            string = to_rl_string("\n".join(open("game_state.txt", "r").readlines()))
            tic_tac_toe.functions.from_string(state, string)
            if tic_tac_toe.functions.can_mark(state, x, y):
                print(f"CLICKED ON {x}, {y}")
                tic_tac_toe.functions.mark(state, x, y)
                string = to_python_string(tic_tac_toe.functions.to_string(state))
                with open("game_state.txt", "w+") as f:
                    f.write(string)
    return make_game_page(state, request)
