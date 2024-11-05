import os

# NOTICE, THIS IS A TRICK TO FORCE THE RECOMPILATION OF THE GAME RULES EVERY
# TIME YOU RUN THE SERVER. YOU CAN INSTEAD RUN THEM JUST ONCE WHEN YOU CHANGE
# THE RULES. THIS SHOULD THEREFORE BE IN A MAKE FILE OR SIMILAR
os.system("rlc tic_tac_toe/tic_tac_toe.rl -o tic_tac_toe/lib.so --shared -O2")
os.system("rlc tic_tac_toe/tic_tac_toe.rl -o tic_tac_toe/wrapper.py --python")

# WE COULD HAVE USED RLC UTILITIES TO DYNAMICALLY LOAD RLC STUFF, BUT IF
# WE DO LIKE THIS WE GET AUTOCOMPLETION
import tic_tac_toe.wrapper as tic_tac_toe
from django.urls import path, register_converter

from . import views

# register the argument type of action mark, which
# has a templetized argument that specifies acceptable
# min and max
register_converter(views.make_converter(tic_tac_toe.BIntT0T3T), "bint0-3")

app_name = "tic_tac_toe"
urlpatterns = [
    path("", views.game_state_simple, name="index"),
    path("efficient/", views.game_state_efficient, name="efficient"),
    path("reset/", views.reset, name="reset"),
    path("mark/<bint0-3:x>/<bint0-3:y>", views.mark, name="mark"),
    path("act/<str:action>", views.act, name="act"),
]
