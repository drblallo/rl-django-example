from ctypes import *
import os
from typing import overload
from pathlib import Path
import builtins
from collections import defaultdict

lib = CDLL(os.path.join(Path(__file__).resolve().parent, "lib.so"))
actions = defaultdict(list)
wrappers = defaultdict(list)
args_info = {}
signatures = {}
actionToAnyFunctionType= {}
class VectorTboolT(Structure):
    _fields_ = [("__data", POINTER(c_bool)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTboolT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(c_bool):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(c_bool):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



class BIntT0T3T(Structure):
    _fields_ = [("_value", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = BIntT0T3T()
        functions.assign(copy, self)
        return copy

    @property
    def value(self) -> builtins.int:
        return self._value

    @value.setter
    def value(self, value) -> builtins.int:
        self._value = value



class VectorTint8_tT(Structure):
    _fields_ = [("__data", POINTER(c_byte)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTint8_tT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(c_byte):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(c_byte):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



class VectorTdoubleT(Structure):
    _fields_ = [("__data", POINTER(c_double)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTdoubleT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(c_double):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(c_double):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



class String(Structure):
    _fields_ = [("__data", VectorTint8_tT), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = String()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> VectorTint8_tT:
        return self.__data

    @_data.setter
    def _data(self, value) -> VectorTint8_tT:
        self.__data = value



class VectorTStringT(Structure):
    _fields_ = [("__data", POINTER(String)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTStringT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(String):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(String):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



class Board(Structure):
    _fields_ = [("_slots", BIntT0T3T * 9), ("_playerTurn", c_bool), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = Board()
        functions.assign(copy, self)
        return copy

    @property
    def slots(self) -> BIntT0T3T * 9:
        return self._slots

    @slots.setter
    def slots(self, value) -> BIntT0T3T * 9:
        self._slots = value

    @property
    def playerTurn(self) -> builtins.bool:
        return self._playerTurn

    @playerTurn.setter
    def playerTurn(self, value) -> builtins.bool:
        self._playerTurn = value



class GameMark(Structure):
    _fields_ = [("_x", BIntT0T3T), ("_y", BIntT0T3T), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = GameMark()
        functions.assign(copy, self)
        return copy

    @property
    def x(self) -> BIntT0T3T:
        return self._x

    @x.setter
    def x(self, value) -> BIntT0T3T:
        self._x = value

    @property
    def y(self) -> BIntT0T3T:
        return self._y

    @y.setter
    def y(self, value) -> BIntT0T3T:
        self._y = value



class _GameMarkOr(Union):
    _fields_ = [("_field0", GameMark), ]

    @property
    def field0(self) -> GameMark:
        return self._field0

    @field0.setter
    def field0(self, value) -> GameMark:
        self._field0 = value

class GameMarkOr(Structure):
    _fields_ = [("_content", _GameMarkOr), ("_active_index", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = GameMarkOr()
        functions.assign(copy, self)
        return copy

    @property
    def content(self) -> _GameMarkOr:
        return self._content

    @content.setter
    def content(self, value) -> _GameMarkOr:
        self._content = value

    @property
    def active_index(self) -> c_longlong:
        return self._active_index

    @active_index.setter
    def active_index(self, value) -> c_longlong:
        self._active_index = value

class VectorTalt_GameMarkT(Structure):
    _fields_ = [("__data", POINTER(GameMarkOr)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTalt_GameMarkT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(GameMarkOr):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(GameMarkOr):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



class Game(Structure):
    _fields_ = [("_resume_index", c_longlong), ("_board", Board), ("_score", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = Game()
        functions.assign(copy, self)
        return copy

    @property
    def resume_index(self) -> builtins.int:
        return self._resume_index

    @resume_index.setter
    def resume_index(self, value) -> builtins.int:
        self._resume_index = value

    @property
    def board(self) -> Board:
        return self._board

    @board.setter
    def board(self, value) -> Board:
        self._board = value

    @property
    def score(self) -> builtins.int:
        return self._score

    @score.setter
    def score(self, value) -> builtins.int:
        self._score = value



class VectorTGameMarkT(Structure):
    _fields_ = [("__data", POINTER(GameMark)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTGameMarkT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(GameMark):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(GameMark):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



class VectorTBIntT0T3TT(Structure):
    _fields_ = [("__data", POINTER(BIntT0T3T)), ("__size", c_longlong), ("__capacity", c_longlong), ]

    def __init__(self):
        self.to_erase = True
        functions.init(self)

    def copy(self):
        copy = VectorTBIntT0T3TT()
        functions.assign(copy, self)
        return copy

    def __del__(self):
        if hasattr(self, "to_erase") and self.to_erase:
            functions.drop(self)

    @property
    def _data(self) -> POINTER(BIntT0T3T):
        return self.__data

    @_data.setter
    def _data(self, value) -> POINTER(BIntT0T3T):
        self.__data = value

    @property
    def _size(self) -> builtins.int:
        return self.__size

    @_size.setter
    def _size(self, value) -> builtins.int:
        self.__size = value

    @property
    def _capacity(self) -> builtins.int:
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value) -> builtins.int:
        self.__capacity = value



AnyGameAction = GameMarkOr
@overload
def init(arg0: POINTER(BIntT0T3T)):
    pass

def rl_m_init__BIntT0T3TPtr(arg0: POINTER(BIntT0T3T)):
    var0 = lib.rl_m_init__BIntT0T3TPtr
    var0(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__BIntT0T3TPtr)
signatures[rl_m_init__BIntT0T3TPtr] = [None, POINTER(BIntT0T3T), ]
@overload
def can_init(arg0: POINTER(BIntT0T3T)) -> builtins.bool:
    pass

def rl_m_can_init__BIntT0T3TPtr_r_bool(arg0: POINTER(BIntT0T3T)) -> builtins.bool:
    var1 = lib.rl_m_can_init__BIntT0T3TPtr_r_bool
    var2 = (c_bool)()
    var1(byref(var2), byref(arg0), )
    return var2

wrappers["can_init"].append(rl_m_can_init__BIntT0T3TPtr_r_bool)
signatures[rl_m_can_init__BIntT0T3TPtr_r_bool] = [builtins.bool, POINTER(BIntT0T3T), ]
@overload
def init(arg0: POINTER(GameMark)):
    pass

def rl_m_init__GameMarkPtr(arg0: POINTER(GameMark)):
    var3 = lib.rl_m_init__GameMarkPtr
    var3(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__GameMarkPtr)
signatures[rl_m_init__GameMarkPtr] = [None, POINTER(GameMark), ]
@overload
def can_init(arg0: POINTER(GameMark)) -> builtins.bool:
    pass

def rl_m_can_init__GameMarkPtr_r_bool(arg0: POINTER(GameMark)) -> builtins.bool:
    var4 = lib.rl_m_can_init__GameMarkPtr_r_bool
    var5 = (c_bool)()
    var4(byref(var5), byref(arg0), )
    return var5

wrappers["can_init"].append(rl_m_can_init__GameMarkPtr_r_bool)
signatures[rl_m_can_init__GameMarkPtr_r_bool] = [builtins.bool, POINTER(GameMark), ]
@overload
def init(arg0: POINTER(GameMarkOr)):
    pass

def rl_m_init__alt_GameMarkPtr(arg0: POINTER(GameMarkOr)):
    var6 = lib.rl_m_init__alt_GameMarkPtr
    var6(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__alt_GameMarkPtr)
signatures[rl_m_init__alt_GameMarkPtr] = [None, POINTER(GameMarkOr), ]
@overload
def can_init(arg0: POINTER(GameMarkOr)) -> builtins.bool:
    pass

def rl_m_can_init__alt_GameMarkPtr_r_bool(arg0: POINTER(GameMarkOr)) -> builtins.bool:
    var7 = lib.rl_m_can_init__alt_GameMarkPtr_r_bool
    var8 = (c_bool)()
    var7(byref(var8), byref(arg0), )
    return var8

wrappers["can_init"].append(rl_m_can_init__alt_GameMarkPtr_r_bool)
signatures[rl_m_can_init__alt_GameMarkPtr_r_bool] = [builtins.bool, POINTER(GameMarkOr), ]
@overload
def init(arg0: POINTER(c_bool)):
    pass

def rl_m_init__boolPtr(arg0: POINTER(c_bool)):
    var9 = lib.rl_m_init__boolPtr
    var9(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__boolPtr)
signatures[rl_m_init__boolPtr] = [None, POINTER(c_bool), ]
@overload
def can_init(arg0: POINTER(c_bool)) -> builtins.bool:
    pass

def rl_m_can_init__boolPtr_r_bool(arg0: POINTER(c_bool)) -> builtins.bool:
    var10 = lib.rl_m_can_init__boolPtr_r_bool
    var11 = (c_bool)()
    var10(byref(var11), byref(arg0), )
    return var11

wrappers["can_init"].append(rl_m_can_init__boolPtr_r_bool)
signatures[rl_m_can_init__boolPtr_r_bool] = [builtins.bool, POINTER(c_bool), ]
@overload
def init(arg0: POINTER(c_double)):
    pass

def rl_m_init__doublePtr(arg0: POINTER(c_double)):
    var12 = lib.rl_m_init__doublePtr
    var12(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__doublePtr)
signatures[rl_m_init__doublePtr] = [None, POINTER(c_double), ]
@overload
def can_init(arg0: POINTER(c_double)) -> builtins.bool:
    pass

def rl_m_can_init__doublePtr_r_bool(arg0: POINTER(c_double)) -> builtins.bool:
    var13 = lib.rl_m_can_init__doublePtr_r_bool
    var14 = (c_bool)()
    var13(byref(var14), byref(arg0), )
    return var14

wrappers["can_init"].append(rl_m_can_init__doublePtr_r_bool)
signatures[rl_m_can_init__doublePtr_r_bool] = [builtins.bool, POINTER(c_double), ]
@overload
def init(arg0: POINTER(String)):
    pass

def rl_m_init__StringPtr(arg0: POINTER(String)):
    var15 = lib.rl_m_init__StringPtr
    var15(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__StringPtr)
signatures[rl_m_init__StringPtr] = [None, POINTER(String), ]
@overload
def can_init(arg0: POINTER(String)) -> builtins.bool:
    pass

def rl_m_can_init__StringPtr_r_bool(arg0: POINTER(String)) -> builtins.bool:
    var16 = lib.rl_m_can_init__StringPtr_r_bool
    var17 = (c_bool)()
    var16(byref(var17), byref(arg0), )
    return var17

wrappers["can_init"].append(rl_m_can_init__StringPtr_r_bool)
signatures[rl_m_can_init__StringPtr_r_bool] = [builtins.bool, POINTER(String), ]
@overload
def init(arg0: POINTER(c_byte)):
    pass

def rl_m_init__int8_tPtr(arg0: POINTER(c_byte)):
    var18 = lib.rl_m_init__int8_tPtr
    var18(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__int8_tPtr)
signatures[rl_m_init__int8_tPtr] = [None, POINTER(c_byte), ]
@overload
def can_init(arg0: POINTER(c_byte)) -> builtins.bool:
    pass

def rl_m_can_init__int8_tPtr_r_bool(arg0: POINTER(c_byte)) -> builtins.bool:
    var19 = lib.rl_m_can_init__int8_tPtr_r_bool
    var20 = (c_bool)()
    var19(byref(var20), byref(arg0), )
    return var20

wrappers["can_init"].append(rl_m_can_init__int8_tPtr_r_bool)
signatures[rl_m_can_init__int8_tPtr_r_bool] = [builtins.bool, POINTER(c_byte), ]
@overload
def init(arg0: GameMarkOr):
    pass

def rl_m_init__alt_GameMark(arg0: GameMarkOr):
    var21 = lib.rl_m_init__alt_GameMark
    var21(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__alt_GameMark)
signatures[rl_m_init__alt_GameMark] = [None, GameMarkOr, ]
@overload
def can_init(arg0: GameMarkOr) -> builtins.bool:
    pass

def rl_m_can_init__alt_GameMark_r_bool(arg0: GameMarkOr) -> builtins.bool:
    var22 = lib.rl_m_can_init__alt_GameMark_r_bool
    var23 = (c_bool)()
    var22(byref(var23), byref(arg0), )
    return var23

wrappers["can_init"].append(rl_m_can_init__alt_GameMark_r_bool)
signatures[rl_m_can_init__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def init(arg0: Game):
    pass

def rl_m_init__Game(arg0: Game):
    var24 = lib.rl_m_init__Game
    var24(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__Game)
signatures[rl_m_init__Game] = [None, Game, ]
@overload
def can_init(arg0: Game) -> builtins.bool:
    pass

def rl_m_can_init__Game_r_bool(arg0: Game) -> builtins.bool:
    var25 = lib.rl_m_can_init__Game_r_bool
    var26 = (c_bool)()
    var25(byref(var26), byref(arg0), )
    return var26

wrappers["can_init"].append(rl_m_can_init__Game_r_bool)
signatures[rl_m_can_init__Game_r_bool] = [builtins.bool, Game, ]
@overload
def init(arg0: Board):
    pass

def rl_m_init__Board(arg0: Board):
    var27 = lib.rl_m_init__Board
    var27(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__Board)
signatures[rl_m_init__Board] = [None, Board, ]
@overload
def can_init(arg0: Board) -> builtins.bool:
    pass

def rl_m_can_init__Board_r_bool(arg0: Board) -> builtins.bool:
    var28 = lib.rl_m_can_init__Board_r_bool
    var29 = (c_bool)()
    var28(byref(var29), byref(arg0), )
    return var29

wrappers["can_init"].append(rl_m_can_init__Board_r_bool)
signatures[rl_m_can_init__Board_r_bool] = [builtins.bool, Board, ]
@overload
def init(arg0:  list ):
    pass

def rl_m_init__BIntT0T3T_9(arg0:  list ):
    var30 = lib.rl_m_init__BIntT0T3T_9
    var30(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__BIntT0T3T_9)
signatures[rl_m_init__BIntT0T3T_9] = [None,  list , ]
@overload
def can_init(arg0:  list ) -> builtins.bool:
    pass

def rl_m_can_init__BIntT0T3T_9_r_bool(arg0:  list ) -> builtins.bool:
    var31 = lib.rl_m_can_init__BIntT0T3T_9_r_bool
    var32 = (c_bool)()
    var31(byref(var32), byref(arg0), )
    return var32

wrappers["can_init"].append(rl_m_can_init__BIntT0T3T_9_r_bool)
signatures[rl_m_can_init__BIntT0T3T_9_r_bool] = [builtins.bool,  list , ]
@overload
def init(arg0: builtins.str):
    pass

def rl_m_init__strlit(arg0: builtins.str):
    var33 = lib.rl_m_init__strlit
    var34 = c_char_p(arg0.encode("utf-8"))
    var33(byref(var34), )
    return

wrappers["init"].append(rl_m_init__strlit)
signatures[rl_m_init__strlit] = [None, builtins.str, ]
@overload
def can_init(arg0: builtins.str) -> builtins.bool:
    pass

def rl_m_can_init__strlit_r_bool(arg0: builtins.str) -> builtins.bool:
    var35 = lib.rl_m_can_init__strlit_r_bool
    var36 = c_char_p(arg0.encode("utf-8"))
    var37 = (c_bool)()
    var35(byref(var37), byref(var36), )
    return var37

wrappers["can_init"].append(rl_m_can_init__strlit_r_bool)
signatures[rl_m_can_init__strlit_r_bool] = [builtins.bool, builtins.str, ]
@overload
def init(arg0:  list ):
    pass

def rl_m_init__int8_t_1(arg0:  list ):
    var38 = lib.rl_m_init__int8_t_1
    var38(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__int8_t_1)
signatures[rl_m_init__int8_t_1] = [None,  list , ]
@overload
def can_init(arg0:  list ) -> builtins.bool:
    pass

def rl_m_can_init__int8_t_1_r_bool(arg0:  list ) -> builtins.bool:
    var39 = lib.rl_m_can_init__int8_t_1_r_bool
    var40 = (c_bool)()
    var39(byref(var40), byref(arg0), )
    return var40

wrappers["can_init"].append(rl_m_can_init__int8_t_1_r_bool)
signatures[rl_m_can_init__int8_t_1_r_bool] = [builtins.bool,  list , ]
@overload
def init(arg0:  list ):
    pass

def rl_m_init__int8_t_8(arg0:  list ):
    var41 = lib.rl_m_init__int8_t_8
    var41(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__int8_t_8)
signatures[rl_m_init__int8_t_8] = [None,  list , ]
@overload
def can_init(arg0:  list ) -> builtins.bool:
    pass

def rl_m_can_init__int8_t_8_r_bool(arg0:  list ) -> builtins.bool:
    var42 = lib.rl_m_can_init__int8_t_8_r_bool
    var43 = (c_bool)()
    var42(byref(var43), byref(arg0), )
    return var43

wrappers["can_init"].append(rl_m_can_init__int8_t_8_r_bool)
signatures[rl_m_can_init__int8_t_8_r_bool] = [builtins.bool,  list , ]
@overload
def init(arg0: GameMark):
    pass

def rl_m_init__GameMark(arg0: GameMark):
    var44 = lib.rl_m_init__GameMark
    var44(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__GameMark)
signatures[rl_m_init__GameMark] = [None, GameMark, ]
@overload
def can_init(arg0: GameMark) -> builtins.bool:
    pass

def rl_m_can_init__GameMark_r_bool(arg0: GameMark) -> builtins.bool:
    var45 = lib.rl_m_can_init__GameMark_r_bool
    var46 = (c_bool)()
    var45(byref(var46), byref(arg0), )
    return var46

wrappers["can_init"].append(rl_m_can_init__GameMark_r_bool)
signatures[rl_m_can_init__GameMark_r_bool] = [builtins.bool, GameMark, ]
@overload
def init(arg0: BIntT0T3T):
    pass

def rl_m_init__BIntT0T3T(arg0: BIntT0T3T):
    var47 = lib.rl_m_init__BIntT0T3T
    var47(byref(arg0), )
    return

wrappers["init"].append(rl_m_init__BIntT0T3T)
signatures[rl_m_init__BIntT0T3T] = [None, BIntT0T3T, ]
@overload
def can_init(arg0: BIntT0T3T) -> builtins.bool:
    pass

def rl_m_can_init__BIntT0T3T_r_bool(arg0: BIntT0T3T) -> builtins.bool:
    var48 = lib.rl_m_can_init__BIntT0T3T_r_bool
    var49 = (c_bool)()
    var48(byref(var49), byref(arg0), )
    return var49

wrappers["can_init"].append(rl_m_can_init__BIntT0T3T_r_bool)
signatures[rl_m_can_init__BIntT0T3T_r_bool] = [builtins.bool, BIntT0T3T, ]
@overload
def assign(arg0: Game, arg1: Game) -> None:
    pass

def rl_m_assign__Game_Game(arg0: Game, arg1: Game) -> None:
    var50 = lib.rl_m_assign__Game_Game
    var50(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__Game_Game)
signatures[rl_m_assign__Game_Game] = [None, Game, Game, ]
@overload
def can_assign(arg0: Game, arg1: Game) -> builtins.bool:
    pass

def rl_m_can_assign__Game_Game_r_bool(arg0: Game, arg1: Game) -> builtins.bool:
    var51 = lib.rl_m_can_assign__Game_Game_r_bool
    var52 = (c_bool)()
    var51(byref(var52), byref(arg0), byref(arg1), )
    return var52

wrappers["can_assign"].append(rl_m_can_assign__Game_Game_r_bool)
signatures[rl_m_can_assign__Game_Game_r_bool] = [builtins.bool, Game, Game, ]
@overload
def assign(arg0: Board, arg1: Board) -> None:
    pass

def rl_m_assign__Board_Board(arg0: Board, arg1: Board) -> None:
    var53 = lib.rl_m_assign__Board_Board
    var53(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__Board_Board)
signatures[rl_m_assign__Board_Board] = [None, Board, Board, ]
@overload
def can_assign(arg0: Board, arg1: Board) -> builtins.bool:
    pass

def rl_m_can_assign__Board_Board_r_bool(arg0: Board, arg1: Board) -> builtins.bool:
    var54 = lib.rl_m_can_assign__Board_Board_r_bool
    var55 = (c_bool)()
    var54(byref(var55), byref(arg0), byref(arg1), )
    return var55

wrappers["can_assign"].append(rl_m_can_assign__Board_Board_r_bool)
signatures[rl_m_can_assign__Board_Board_r_bool] = [builtins.bool, Board, Board, ]
@overload
def assign(arg0:  list , arg1:  list ) -> None:
    pass

def rl_m_assign__BIntT0T3T_9_BIntT0T3T_9(arg0:  list , arg1:  list ) -> None:
    var56 = lib.rl_m_assign__BIntT0T3T_9_BIntT0T3T_9
    var56(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__BIntT0T3T_9_BIntT0T3T_9)
signatures[rl_m_assign__BIntT0T3T_9_BIntT0T3T_9] = [None,  list ,  list , ]
@overload
def can_assign(arg0:  list , arg1:  list ) -> builtins.bool:
    pass

def rl_m_can_assign__BIntT0T3T_9_BIntT0T3T_9_r_bool(arg0:  list , arg1:  list ) -> builtins.bool:
    var57 = lib.rl_m_can_assign__BIntT0T3T_9_BIntT0T3T_9_r_bool
    var58 = (c_bool)()
    var57(byref(var58), byref(arg0), byref(arg1), )
    return var58

wrappers["can_assign"].append(rl_m_can_assign__BIntT0T3T_9_BIntT0T3T_9_r_bool)
signatures[rl_m_can_assign__BIntT0T3T_9_BIntT0T3T_9_r_bool] = [builtins.bool,  list ,  list , ]
@overload
def assign(arg0: builtins.str, arg1: builtins.str) -> None:
    pass

def rl_m_assign__strlit_strlit(arg0: builtins.str, arg1: builtins.str) -> None:
    var59 = lib.rl_m_assign__strlit_strlit
    var60 = c_char_p(arg0.encode("utf-8"))
    var61 = c_char_p(arg1.encode("utf-8"))
    var59(byref(var60), byref(var61), )
    return

wrappers["assign"].append(rl_m_assign__strlit_strlit)
signatures[rl_m_assign__strlit_strlit] = [None, builtins.str, builtins.str, ]
@overload
def can_assign(arg0: builtins.str, arg1: builtins.str) -> builtins.bool:
    pass

def rl_m_can_assign__strlit_strlit_r_bool(arg0: builtins.str, arg1: builtins.str) -> builtins.bool:
    var62 = lib.rl_m_can_assign__strlit_strlit_r_bool
    var63 = c_char_p(arg0.encode("utf-8"))
    var64 = c_char_p(arg1.encode("utf-8"))
    var65 = (c_bool)()
    var62(byref(var65), byref(var63), byref(var64), )
    return var65

wrappers["can_assign"].append(rl_m_can_assign__strlit_strlit_r_bool)
signatures[rl_m_can_assign__strlit_strlit_r_bool] = [builtins.bool, builtins.str, builtins.str, ]
@overload
def assign(arg0: String, arg1: String) -> None:
    pass

def rl_m_assign__String_String(arg0: String, arg1: String) -> None:
    var66 = lib.rl_m_assign__String_String
    var66(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__String_String)
signatures[rl_m_assign__String_String] = [None, String, String, ]
@overload
def can_assign(arg0: String, arg1: String) -> builtins.bool:
    pass

def rl_m_can_assign__String_String_r_bool(arg0: String, arg1: String) -> builtins.bool:
    var67 = lib.rl_m_can_assign__String_String_r_bool
    var68 = (c_bool)()
    var67(byref(var68), byref(arg0), byref(arg1), )
    return var68

wrappers["can_assign"].append(rl_m_can_assign__String_String_r_bool)
signatures[rl_m_can_assign__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def assign(arg0: GameMarkOr, arg1: GameMark) -> None:
    pass

def rl_m_assign__alt_GameMark_GameMark(arg0: GameMarkOr, arg1: GameMark) -> None:
    var69 = lib.rl_m_assign__alt_GameMark_GameMark
    var69(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__alt_GameMark_GameMark)
signatures[rl_m_assign__alt_GameMark_GameMark] = [None, GameMarkOr, GameMark, ]
@overload
def can_assign(arg0: GameMarkOr, arg1: GameMark) -> builtins.bool:
    pass

def rl_m_can_assign__alt_GameMark_GameMark_r_bool(arg0: GameMarkOr, arg1: GameMark) -> builtins.bool:
    var70 = lib.rl_m_can_assign__alt_GameMark_GameMark_r_bool
    var71 = (c_bool)()
    var70(byref(var71), byref(arg0), byref(arg1), )
    return var71

wrappers["can_assign"].append(rl_m_can_assign__alt_GameMark_GameMark_r_bool)
signatures[rl_m_can_assign__alt_GameMark_GameMark_r_bool] = [builtins.bool, GameMarkOr, GameMark, ]
@overload
def assign(arg0: GameMarkOr, arg1: GameMarkOr) -> None:
    pass

def rl_m_assign__alt_GameMark_alt_GameMark(arg0: GameMarkOr, arg1: GameMarkOr) -> None:
    var72 = lib.rl_m_assign__alt_GameMark_alt_GameMark
    var72(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__alt_GameMark_alt_GameMark)
signatures[rl_m_assign__alt_GameMark_alt_GameMark] = [None, GameMarkOr, GameMarkOr, ]
@overload
def can_assign(arg0: GameMarkOr, arg1: GameMarkOr) -> builtins.bool:
    pass

def rl_m_can_assign__alt_GameMark_alt_GameMark_r_bool(arg0: GameMarkOr, arg1: GameMarkOr) -> builtins.bool:
    var73 = lib.rl_m_can_assign__alt_GameMark_alt_GameMark_r_bool
    var74 = (c_bool)()
    var73(byref(var74), byref(arg0), byref(arg1), )
    return var74

wrappers["can_assign"].append(rl_m_can_assign__alt_GameMark_alt_GameMark_r_bool)
signatures[rl_m_can_assign__alt_GameMark_alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, GameMarkOr, ]
@overload
def assign(arg0: GameMark, arg1: GameMark) -> None:
    pass

def rl_m_assign__GameMark_GameMark(arg0: GameMark, arg1: GameMark) -> None:
    var75 = lib.rl_m_assign__GameMark_GameMark
    var75(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__GameMark_GameMark)
signatures[rl_m_assign__GameMark_GameMark] = [None, GameMark, GameMark, ]
@overload
def can_assign(arg0: GameMark, arg1: GameMark) -> builtins.bool:
    pass

def rl_m_can_assign__GameMark_GameMark_r_bool(arg0: GameMark, arg1: GameMark) -> builtins.bool:
    var76 = lib.rl_m_can_assign__GameMark_GameMark_r_bool
    var77 = (c_bool)()
    var76(byref(var77), byref(arg0), byref(arg1), )
    return var77

wrappers["can_assign"].append(rl_m_can_assign__GameMark_GameMark_r_bool)
signatures[rl_m_can_assign__GameMark_GameMark_r_bool] = [builtins.bool, GameMark, GameMark, ]
@overload
def assign(arg0: BIntT0T3T, arg1: BIntT0T3T) -> None:
    pass

def rl_m_assign__BIntT0T3T_BIntT0T3T(arg0: BIntT0T3T, arg1: BIntT0T3T) -> None:
    var78 = lib.rl_m_assign__BIntT0T3T_BIntT0T3T
    var78(byref(arg0), byref(arg1), )
    return

wrappers["assign"].append(rl_m_assign__BIntT0T3T_BIntT0T3T)
signatures[rl_m_assign__BIntT0T3T_BIntT0T3T] = [None, BIntT0T3T, BIntT0T3T, ]
@overload
def can_assign(arg0: BIntT0T3T, arg1: BIntT0T3T) -> builtins.bool:
    pass

def rl_m_can_assign__BIntT0T3T_BIntT0T3T_r_bool(arg0: BIntT0T3T, arg1: BIntT0T3T) -> builtins.bool:
    var79 = lib.rl_m_can_assign__BIntT0T3T_BIntT0T3T_r_bool
    var80 = (c_bool)()
    var79(byref(var80), byref(arg0), byref(arg1), )
    return var80

wrappers["can_assign"].append(rl_m_can_assign__BIntT0T3T_BIntT0T3T_r_bool)
signatures[rl_m_can_assign__BIntT0T3T_BIntT0T3T_r_bool] = [builtins.bool, BIntT0T3T, BIntT0T3T, ]
@overload
def drop(to_drop: String):
    pass

def rl_m_drop__String(to_drop: String):
    var81 = lib.rl_m_drop__String
    var81(byref(to_drop), )
    return

wrappers["drop"].append(rl_m_drop__String)
signatures[rl_m_drop__String] = [None, String, ]
@overload
def can_drop(to_drop: String) -> builtins.bool:
    pass

def rl_m_can_drop__String_r_bool(to_drop: String) -> builtins.bool:
    var82 = lib.rl_m_can_drop__String_r_bool
    var83 = (c_bool)()
    var82(byref(var83), byref(to_drop), )
    return var83

wrappers["can_drop"].append(rl_m_can_drop__String_r_bool)
signatures[rl_m_can_drop__String_r_bool] = [builtins.bool, String, ]
@overload
def print_string(s: String) -> None:
    pass

def rl_print_string__String(s: String) -> None:
    var84 = lib.rl_print_string__String
    var84(byref(s), )
    return

wrappers["print_string"].append(rl_print_string__String)
signatures[rl_print_string__String] = [None, String, ]
@overload
def can_print_string(s: String) -> builtins.bool:
    pass

def rl_can_print_string__String_r_bool(s: String) -> builtins.bool:
    var85 = lib.rl_can_print_string__String_r_bool
    var86 = (c_bool)()
    var85(byref(var86), byref(s), )
    return var86

wrappers["can_print_string"].append(rl_can_print_string__String_r_bool)
signatures[rl_can_print_string__String_r_bool] = [builtins.bool, String, ]
@overload
def print_string_lit(s: builtins.str) -> None:
    pass

def rl_print_string_lit__strlit(s: builtins.str) -> None:
    var87 = lib.rl_print_string_lit__strlit
    var88 = c_char_p(s.encode("utf-8"))
    var87(byref(var88), )
    return

wrappers["print_string_lit"].append(rl_print_string_lit__strlit)
signatures[rl_print_string_lit__strlit] = [None, builtins.str, ]
@overload
def can_print_string_lit(s: builtins.str) -> builtins.bool:
    pass

def rl_can_print_string_lit__strlit_r_bool(s: builtins.str) -> builtins.bool:
    var89 = lib.rl_can_print_string_lit__strlit_r_bool
    var90 = c_char_p(s.encode("utf-8"))
    var91 = (c_bool)()
    var89(byref(var91), byref(var90), )
    return var91

wrappers["can_print_string_lit"].append(rl_can_print_string_lit__strlit_r_bool)
signatures[rl_can_print_string_lit__strlit_r_bool] = [builtins.bool, builtins.str, ]
@overload
def print(to_print: String) -> None:
    pass

def rl_print__String(to_print: String) -> None:
    var92 = lib.rl_print__String
    var92(byref(to_print), )
    return

wrappers["print"].append(rl_print__String)
signatures[rl_print__String] = [None, String, ]
@overload
def can_print(to_print: String) -> builtins.bool:
    pass

def rl_can_print__String_r_bool(to_print: String) -> builtins.bool:
    var93 = lib.rl_can_print__String_r_bool
    var94 = (c_bool)()
    var93(byref(var94), byref(to_print), )
    return var94

wrappers["can_print"].append(rl_can_print__String_r_bool)
signatures[rl_can_print__String_r_bool] = [builtins.bool, String, ]
@overload
def print(to_print: builtins.bool) -> None:
    pass

def rl_print__bool(to_print: builtins.bool) -> None:
    var95 = lib.rl_print__bool
    var96 = c_bool(to_print)
    var95(byref(var96), )
    return

wrappers["print"].append(rl_print__bool)
signatures[rl_print__bool] = [None, builtins.bool, ]
@overload
def can_print(to_print: builtins.bool) -> builtins.bool:
    pass

def rl_can_print__bool_r_bool(to_print: builtins.bool) -> builtins.bool:
    var97 = lib.rl_can_print__bool_r_bool
    var98 = c_bool(to_print)
    var99 = (c_bool)()
    var97(byref(var99), byref(var98), )
    return var99

wrappers["can_print"].append(rl_can_print__bool_r_bool)
signatures[rl_can_print__bool_r_bool] = [builtins.bool, builtins.bool, ]
@overload
def print(to_print: Game) -> None:
    pass

def rl_print__Game(to_print: Game) -> None:
    var100 = lib.rl_print__Game
    var100(byref(to_print), )
    return

wrappers["print"].append(rl_print__Game)
signatures[rl_print__Game] = [None, Game, ]
@overload
def can_print(to_print: Game) -> builtins.bool:
    pass

def rl_can_print__Game_r_bool(to_print: Game) -> builtins.bool:
    var101 = lib.rl_can_print__Game_r_bool
    var102 = (c_bool)()
    var101(byref(var102), byref(to_print), )
    return var102

wrappers["can_print"].append(rl_can_print__Game_r_bool)
signatures[rl_can_print__Game_r_bool] = [builtins.bool, Game, ]
@overload
def print(to_print: GameMarkOr) -> None:
    pass

def rl_print__alt_GameMark(to_print: GameMarkOr) -> None:
    var103 = lib.rl_print__alt_GameMark
    var103(byref(to_print), )
    return

wrappers["print"].append(rl_print__alt_GameMark)
signatures[rl_print__alt_GameMark] = [None, GameMarkOr, ]
@overload
def can_print(to_print: GameMarkOr) -> builtins.bool:
    pass

def rl_can_print__alt_GameMark_r_bool(to_print: GameMarkOr) -> builtins.bool:
    var104 = lib.rl_can_print__alt_GameMark_r_bool
    var105 = (c_bool)()
    var104(byref(var105), byref(to_print), )
    return var105

wrappers["can_print"].append(rl_can_print__alt_GameMark_r_bool)
signatures[rl_can_print__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def append_to_vector(to_add: builtins.int, output: VectorTint8_tT) -> None:
    pass

def rl_append_to_vector__int64_t_VectorTint8_tT(to_add: builtins.int, output: VectorTint8_tT) -> None:
    var106 = lib.rl_append_to_vector__int64_t_VectorTint8_tT
    var107 = c_longlong(to_add)
    var106(byref(var107), byref(output), )
    return

wrappers["append_to_vector"].append(rl_append_to_vector__int64_t_VectorTint8_tT)
signatures[rl_append_to_vector__int64_t_VectorTint8_tT] = [None, builtins.int, VectorTint8_tT, ]
@overload
def can_append_to_vector(to_add: builtins.int, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_append_to_vector__int64_t_VectorTint8_tT_r_bool(to_add: builtins.int, output: VectorTint8_tT) -> builtins.bool:
    var108 = lib.rl_can_append_to_vector__int64_t_VectorTint8_tT_r_bool
    var109 = c_longlong(to_add)
    var110 = (c_bool)()
    var108(byref(var110), byref(var109), byref(output), )
    return var110

wrappers["can_append_to_vector"].append(rl_can_append_to_vector__int64_t_VectorTint8_tT_r_bool)
signatures[rl_can_append_to_vector__int64_t_VectorTint8_tT_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, ]
@overload
def append_to_vector(to_add: builtins.float, output: VectorTint8_tT) -> None:
    pass

def rl_append_to_vector__double_VectorTint8_tT(to_add: builtins.float, output: VectorTint8_tT) -> None:
    var111 = lib.rl_append_to_vector__double_VectorTint8_tT
    var112 = c_double(to_add)
    var111(byref(var112), byref(output), )
    return

wrappers["append_to_vector"].append(rl_append_to_vector__double_VectorTint8_tT)
signatures[rl_append_to_vector__double_VectorTint8_tT] = [None, builtins.float, VectorTint8_tT, ]
@overload
def can_append_to_vector(to_add: builtins.float, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_append_to_vector__double_VectorTint8_tT_r_bool(to_add: builtins.float, output: VectorTint8_tT) -> builtins.bool:
    var113 = lib.rl_can_append_to_vector__double_VectorTint8_tT_r_bool
    var114 = c_double(to_add)
    var115 = (c_bool)()
    var113(byref(var115), byref(var114), byref(output), )
    return var115

wrappers["can_append_to_vector"].append(rl_can_append_to_vector__double_VectorTint8_tT_r_bool)
signatures[rl_can_append_to_vector__double_VectorTint8_tT_r_bool] = [builtins.bool, builtins.float, VectorTint8_tT, ]
@overload
def append_to_vector(to_add: builtins.bool, output: VectorTint8_tT) -> None:
    pass

def rl_append_to_vector__bool_VectorTint8_tT(to_add: builtins.bool, output: VectorTint8_tT) -> None:
    var116 = lib.rl_append_to_vector__bool_VectorTint8_tT
    var117 = c_bool(to_add)
    var116(byref(var117), byref(output), )
    return

wrappers["append_to_vector"].append(rl_append_to_vector__bool_VectorTint8_tT)
signatures[rl_append_to_vector__bool_VectorTint8_tT] = [None, builtins.bool, VectorTint8_tT, ]
@overload
def can_append_to_vector(to_add: builtins.bool, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_append_to_vector__bool_VectorTint8_tT_r_bool(to_add: builtins.bool, output: VectorTint8_tT) -> builtins.bool:
    var118 = lib.rl_can_append_to_vector__bool_VectorTint8_tT_r_bool
    var119 = c_bool(to_add)
    var120 = (c_bool)()
    var118(byref(var120), byref(var119), byref(output), )
    return var120

wrappers["can_append_to_vector"].append(rl_can_append_to_vector__bool_VectorTint8_tT_r_bool)
signatures[rl_can_append_to_vector__bool_VectorTint8_tT_r_bool] = [builtins.bool, builtins.bool, VectorTint8_tT, ]
@overload
def append_to_vector(to_add: builtins.int, output: VectorTint8_tT) -> None:
    pass

def rl_append_to_vector__int8_t_VectorTint8_tT(to_add: builtins.int, output: VectorTint8_tT) -> None:
    var121 = lib.rl_append_to_vector__int8_t_VectorTint8_tT
    var122 = c_byte(to_add)
    var121(byref(var122), byref(output), )
    return

wrappers["append_to_vector"].append(rl_append_to_vector__int8_t_VectorTint8_tT)
signatures[rl_append_to_vector__int8_t_VectorTint8_tT] = [None, builtins.int, VectorTint8_tT, ]
@overload
def can_append_to_vector(to_add: builtins.int, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_append_to_vector__int8_t_VectorTint8_tT_r_bool(to_add: builtins.int, output: VectorTint8_tT) -> builtins.bool:
    var123 = lib.rl_can_append_to_vector__int8_t_VectorTint8_tT_r_bool
    var124 = c_byte(to_add)
    var125 = (c_bool)()
    var123(byref(var125), byref(var124), byref(output), )
    return var125

wrappers["can_append_to_vector"].append(rl_can_append_to_vector__int8_t_VectorTint8_tT_r_bool)
signatures[rl_can_append_to_vector__int8_t_VectorTint8_tT_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, ]
@overload
def append_to_vector(to_add:  list , output: VectorTint8_tT) -> None:
    pass

def rl_append_to_vector__BIntT0T3T_9_VectorTint8_tT(to_add:  list , output: VectorTint8_tT) -> None:
    var126 = lib.rl_append_to_vector__BIntT0T3T_9_VectorTint8_tT
    var126(byref(to_add), byref(output), )
    return

wrappers["append_to_vector"].append(rl_append_to_vector__BIntT0T3T_9_VectorTint8_tT)
signatures[rl_append_to_vector__BIntT0T3T_9_VectorTint8_tT] = [None,  list , VectorTint8_tT, ]
@overload
def can_append_to_vector(to_add:  list , output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_append_to_vector__BIntT0T3T_9_VectorTint8_tT_r_bool(to_add:  list , output: VectorTint8_tT) -> builtins.bool:
    var127 = lib.rl_can_append_to_vector__BIntT0T3T_9_VectorTint8_tT_r_bool
    var128 = (c_bool)()
    var127(byref(var128), byref(to_add), byref(output), )
    return var128

wrappers["can_append_to_vector"].append(rl_can_append_to_vector__BIntT0T3T_9_VectorTint8_tT_r_bool)
signatures[rl_can_append_to_vector__BIntT0T3T_9_VectorTint8_tT_r_bool] = [builtins.bool,  list , VectorTint8_tT, ]
@overload
def _to_vector_impl(to_add: builtins.int, output: VectorTint8_tT) -> None:
    pass

def rl__to_vector_impl__int64_t_VectorTint8_tT(to_add: builtins.int, output: VectorTint8_tT) -> None:
    var129 = lib.rl__to_vector_impl__int64_t_VectorTint8_tT
    var130 = c_longlong(to_add)
    var129(byref(var130), byref(output), )
    return

wrappers["_to_vector_impl"].append(rl__to_vector_impl__int64_t_VectorTint8_tT)
signatures[rl__to_vector_impl__int64_t_VectorTint8_tT] = [None, builtins.int, VectorTint8_tT, ]
@overload
def can__to_vector_impl(to_add: builtins.int, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can__to_vector_impl__int64_t_VectorTint8_tT_r_bool(to_add: builtins.int, output: VectorTint8_tT) -> builtins.bool:
    var131 = lib.rl_can__to_vector_impl__int64_t_VectorTint8_tT_r_bool
    var132 = c_longlong(to_add)
    var133 = (c_bool)()
    var131(byref(var133), byref(var132), byref(output), )
    return var133

wrappers["can__to_vector_impl"].append(rl_can__to_vector_impl__int64_t_VectorTint8_tT_r_bool)
signatures[rl_can__to_vector_impl__int64_t_VectorTint8_tT_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, ]
@overload
def _to_vector_impl(to_add: Game, output: VectorTint8_tT) -> None:
    pass

def rl__to_vector_impl__Game_VectorTint8_tT(to_add: Game, output: VectorTint8_tT) -> None:
    var134 = lib.rl__to_vector_impl__Game_VectorTint8_tT
    var134(byref(to_add), byref(output), )
    return

wrappers["_to_vector_impl"].append(rl__to_vector_impl__Game_VectorTint8_tT)
signatures[rl__to_vector_impl__Game_VectorTint8_tT] = [None, Game, VectorTint8_tT, ]
@overload
def can__to_vector_impl(to_add: Game, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can__to_vector_impl__Game_VectorTint8_tT_r_bool(to_add: Game, output: VectorTint8_tT) -> builtins.bool:
    var135 = lib.rl_can__to_vector_impl__Game_VectorTint8_tT_r_bool
    var136 = (c_bool)()
    var135(byref(var136), byref(to_add), byref(output), )
    return var136

wrappers["can__to_vector_impl"].append(rl_can__to_vector_impl__Game_VectorTint8_tT_r_bool)
signatures[rl_can__to_vector_impl__Game_VectorTint8_tT_r_bool] = [builtins.bool, Game, VectorTint8_tT, ]
@overload
def _to_vector_impl(to_add: Board, output: VectorTint8_tT) -> None:
    pass

def rl__to_vector_impl__Board_VectorTint8_tT(to_add: Board, output: VectorTint8_tT) -> None:
    var137 = lib.rl__to_vector_impl__Board_VectorTint8_tT
    var137(byref(to_add), byref(output), )
    return

wrappers["_to_vector_impl"].append(rl__to_vector_impl__Board_VectorTint8_tT)
signatures[rl__to_vector_impl__Board_VectorTint8_tT] = [None, Board, VectorTint8_tT, ]
@overload
def can__to_vector_impl(to_add: Board, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can__to_vector_impl__Board_VectorTint8_tT_r_bool(to_add: Board, output: VectorTint8_tT) -> builtins.bool:
    var138 = lib.rl_can__to_vector_impl__Board_VectorTint8_tT_r_bool
    var139 = (c_bool)()
    var138(byref(var139), byref(to_add), byref(output), )
    return var139

wrappers["can__to_vector_impl"].append(rl_can__to_vector_impl__Board_VectorTint8_tT_r_bool)
signatures[rl_can__to_vector_impl__Board_VectorTint8_tT_r_bool] = [builtins.bool, Board, VectorTint8_tT, ]
@overload
def _to_vector_impl(to_add:  list , output: VectorTint8_tT) -> None:
    pass

def rl__to_vector_impl__BIntT0T3T_9_VectorTint8_tT(to_add:  list , output: VectorTint8_tT) -> None:
    var140 = lib.rl__to_vector_impl__BIntT0T3T_9_VectorTint8_tT
    var140(byref(to_add), byref(output), )
    return

wrappers["_to_vector_impl"].append(rl__to_vector_impl__BIntT0T3T_9_VectorTint8_tT)
signatures[rl__to_vector_impl__BIntT0T3T_9_VectorTint8_tT] = [None,  list , VectorTint8_tT, ]
@overload
def can__to_vector_impl(to_add:  list , output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can__to_vector_impl__BIntT0T3T_9_VectorTint8_tT_r_bool(to_add:  list , output: VectorTint8_tT) -> builtins.bool:
    var141 = lib.rl_can__to_vector_impl__BIntT0T3T_9_VectorTint8_tT_r_bool
    var142 = (c_bool)()
    var141(byref(var142), byref(to_add), byref(output), )
    return var142

wrappers["can__to_vector_impl"].append(rl_can__to_vector_impl__BIntT0T3T_9_VectorTint8_tT_r_bool)
signatures[rl_can__to_vector_impl__BIntT0T3T_9_VectorTint8_tT_r_bool] = [builtins.bool,  list , VectorTint8_tT, ]
@overload
def _to_vector_impl(to_add: builtins.bool, output: VectorTint8_tT) -> None:
    pass

def rl__to_vector_impl__bool_VectorTint8_tT(to_add: builtins.bool, output: VectorTint8_tT) -> None:
    var143 = lib.rl__to_vector_impl__bool_VectorTint8_tT
    var144 = c_bool(to_add)
    var143(byref(var144), byref(output), )
    return

wrappers["_to_vector_impl"].append(rl__to_vector_impl__bool_VectorTint8_tT)
signatures[rl__to_vector_impl__bool_VectorTint8_tT] = [None, builtins.bool, VectorTint8_tT, ]
@overload
def can__to_vector_impl(to_add: builtins.bool, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can__to_vector_impl__bool_VectorTint8_tT_r_bool(to_add: builtins.bool, output: VectorTint8_tT) -> builtins.bool:
    var145 = lib.rl_can__to_vector_impl__bool_VectorTint8_tT_r_bool
    var146 = c_bool(to_add)
    var147 = (c_bool)()
    var145(byref(var147), byref(var146), byref(output), )
    return var147

wrappers["can__to_vector_impl"].append(rl_can__to_vector_impl__bool_VectorTint8_tT_r_bool)
signatures[rl_can__to_vector_impl__bool_VectorTint8_tT_r_bool] = [builtins.bool, builtins.bool, VectorTint8_tT, ]
@overload
def _to_vector_impl(to_add: BIntT0T3T, output: VectorTint8_tT) -> None:
    pass

def rl__to_vector_impl__BIntT0T3T_VectorTint8_tT(to_add: BIntT0T3T, output: VectorTint8_tT) -> None:
    var148 = lib.rl__to_vector_impl__BIntT0T3T_VectorTint8_tT
    var148(byref(to_add), byref(output), )
    return

wrappers["_to_vector_impl"].append(rl__to_vector_impl__BIntT0T3T_VectorTint8_tT)
signatures[rl__to_vector_impl__BIntT0T3T_VectorTint8_tT] = [None, BIntT0T3T, VectorTint8_tT, ]
@overload
def can__to_vector_impl(to_add: BIntT0T3T, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can__to_vector_impl__BIntT0T3T_VectorTint8_tT_r_bool(to_add: BIntT0T3T, output: VectorTint8_tT) -> builtins.bool:
    var149 = lib.rl_can__to_vector_impl__BIntT0T3T_VectorTint8_tT_r_bool
    var150 = (c_bool)()
    var149(byref(var150), byref(to_add), byref(output), )
    return var150

wrappers["can__to_vector_impl"].append(rl_can__to_vector_impl__BIntT0T3T_VectorTint8_tT_r_bool)
signatures[rl_can__to_vector_impl__BIntT0T3T_VectorTint8_tT_r_bool] = [builtins.bool, BIntT0T3T, VectorTint8_tT, ]
@overload
def as_byte_vector(to_convert: Game) -> VectorTint8_tT:
    pass

def rl_as_byte_vector__Game_r_VectorTint8_tT(to_convert: Game) -> VectorTint8_tT:
    var151 = lib.rl_as_byte_vector__Game_r_VectorTint8_tT
    var152 = (VectorTint8_tT)()
    var151(byref(var152), byref(to_convert), )
    return var152

wrappers["as_byte_vector"].append(rl_as_byte_vector__Game_r_VectorTint8_tT)
signatures[rl_as_byte_vector__Game_r_VectorTint8_tT] = [VectorTint8_tT, Game, ]
@overload
def can_as_byte_vector(to_convert: Game) -> builtins.bool:
    pass

def rl_can_as_byte_vector__Game_r_bool(to_convert: Game) -> builtins.bool:
    var153 = lib.rl_can_as_byte_vector__Game_r_bool
    var154 = (c_bool)()
    var153(byref(var154), byref(to_convert), )
    return var154

wrappers["can_as_byte_vector"].append(rl_can_as_byte_vector__Game_r_bool)
signatures[rl_can_as_byte_vector__Game_r_bool] = [builtins.bool, Game, ]
@overload
def parse_from_vector(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var155 = lib.rl_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool
    var156 = c_longlong(result)
    var157 = c_longlong(index)
    var158 = (c_bool)()
    var155(byref(var158), byref(var156), byref(input), byref(var157), )
    return var158

wrappers["parse_from_vector"].append(rl_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_from_vector(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var159 = lib.rl_can_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool
    var160 = c_longlong(result)
    var161 = c_longlong(index)
    var162 = (c_bool)()
    var159(byref(var162), byref(var160), byref(input), byref(var161), )
    return var162

wrappers["can_parse_from_vector"].append(rl_can_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def parse_from_vector(result: builtins.float, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool(result: builtins.float, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var163 = lib.rl_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool
    var164 = c_double(result)
    var165 = c_longlong(index)
    var166 = (c_bool)()
    var163(byref(var166), byref(var164), byref(input), byref(var165), )
    return var166

wrappers["parse_from_vector"].append(rl_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.float, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_from_vector(result: builtins.float, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool(result: builtins.float, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var167 = lib.rl_can_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool
    var168 = c_double(result)
    var169 = c_longlong(index)
    var170 = (c_bool)()
    var167(byref(var170), byref(var168), byref(input), byref(var169), )
    return var170

wrappers["can_parse_from_vector"].append(rl_can_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.float, VectorTint8_tT, builtins.int, ]
@overload
def parse_from_vector(result: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool(result: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var171 = lib.rl_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool
    var172 = c_bool(result)
    var173 = c_longlong(index)
    var174 = (c_bool)()
    var171(byref(var174), byref(var172), byref(input), byref(var173), )
    return var174

wrappers["parse_from_vector"].append(rl_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_from_vector(result: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool(result: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var175 = lib.rl_can_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool
    var176 = c_bool(result)
    var177 = c_longlong(index)
    var178 = (c_bool)()
    var175(byref(var178), byref(var176), byref(input), byref(var177), )
    return var178

wrappers["can_parse_from_vector"].append(rl_can_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def parse_from_vector(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var179 = lib.rl_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool
    var180 = c_byte(result)
    var181 = c_longlong(index)
    var182 = (c_bool)()
    var179(byref(var182), byref(var180), byref(input), byref(var181), )
    return var182

wrappers["parse_from_vector"].append(rl_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_from_vector(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool(result: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var183 = lib.rl_can_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool
    var184 = c_byte(result)
    var185 = c_longlong(index)
    var186 = (c_bool)()
    var183(byref(var186), byref(var184), byref(input), byref(var185), )
    return var186

wrappers["can_parse_from_vector"].append(rl_can_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def parse_from_vector(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var187 = lib.rl_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool
    var188 = c_longlong(index)
    var189 = (c_bool)()
    var187(byref(var189), byref(to_add), byref(input), byref(var188), )
    return var189

wrappers["parse_from_vector"].append(rl_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool] = [builtins.bool,  list , VectorTint8_tT, builtins.int, ]
@overload
def can_parse_from_vector(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var190 = lib.rl_can_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool
    var191 = c_longlong(index)
    var192 = (c_bool)()
    var190(byref(var192), byref(to_add), byref(input), byref(var191), )
    return var192

wrappers["can_parse_from_vector"].append(rl_can_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool] = [builtins.bool,  list , VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var193 = lib.rl__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool
    var194 = c_longlong(to_add)
    var195 = c_longlong(index)
    var196 = (c_bool)()
    var193(byref(var196), byref(var194), byref(input), byref(var195), )
    return var196

wrappers["_from_vector_impl"].append(rl__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var197 = lib.rl_can__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool
    var198 = c_longlong(to_add)
    var199 = c_longlong(index)
    var200 = (c_bool)()
    var197(byref(var200), byref(var198), byref(input), byref(var199), )
    return var200

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var201 = lib.rl__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool
    var202 = c_byte(to_add)
    var203 = c_longlong(index)
    var204 = (c_bool)()
    var201(byref(var204), byref(var202), byref(input), byref(var203), )
    return var204

wrappers["_from_vector_impl"].append(rl__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool(to_add: builtins.int, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var205 = lib.rl_can__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool
    var206 = c_byte(to_add)
    var207 = c_longlong(index)
    var208 = (c_bool)()
    var205(byref(var208), byref(var206), byref(input), byref(var207), )
    return var208

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: Game, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool(to_add: Game, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var209 = lib.rl__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool
    var210 = c_longlong(index)
    var211 = (c_bool)()
    var209(byref(var211), byref(to_add), byref(input), byref(var210), )
    return var211

wrappers["_from_vector_impl"].append(rl__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, Game, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: Game, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool(to_add: Game, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var212 = lib.rl_can__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool
    var213 = c_longlong(index)
    var214 = (c_bool)()
    var212(byref(var214), byref(to_add), byref(input), byref(var213), )
    return var214

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, Game, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: GameMarkOr, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool(to_add: GameMarkOr, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var215 = lib.rl__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var216 = c_longlong(index)
    var217 = (c_bool)()
    var215(byref(var217), byref(to_add), byref(input), byref(var216), )
    return var217

wrappers["_from_vector_impl"].append(rl__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: GameMarkOr, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool(to_add: GameMarkOr, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var218 = lib.rl_can__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var219 = c_longlong(index)
    var220 = (c_bool)()
    var218(byref(var220), byref(to_add), byref(input), byref(var219), )
    return var220

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: Board, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool(to_add: Board, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var221 = lib.rl__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool
    var222 = c_longlong(index)
    var223 = (c_bool)()
    var221(byref(var223), byref(to_add), byref(input), byref(var222), )
    return var223

wrappers["_from_vector_impl"].append(rl__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, Board, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: Board, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool(to_add: Board, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var224 = lib.rl_can__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool
    var225 = c_longlong(index)
    var226 = (c_bool)()
    var224(byref(var226), byref(to_add), byref(input), byref(var225), )
    return var226

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, Board, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: GameMark, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool(to_add: GameMark, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var227 = lib.rl__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool
    var228 = c_longlong(index)
    var229 = (c_bool)()
    var227(byref(var229), byref(to_add), byref(input), byref(var228), )
    return var229

wrappers["_from_vector_impl"].append(rl__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMark, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: GameMark, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool(to_add: GameMark, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var230 = lib.rl_can__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool
    var231 = c_longlong(index)
    var232 = (c_bool)()
    var230(byref(var232), byref(to_add), byref(input), byref(var231), )
    return var232

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMark, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var233 = lib.rl__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool
    var234 = c_longlong(index)
    var235 = (c_bool)()
    var233(byref(var235), byref(to_add), byref(input), byref(var234), )
    return var235

wrappers["_from_vector_impl"].append(rl__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool] = [builtins.bool,  list , VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(to_add:  list , input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var236 = lib.rl_can__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool
    var237 = c_longlong(index)
    var238 = (c_bool)()
    var236(byref(var238), byref(to_add), byref(input), byref(var237), )
    return var238

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool] = [builtins.bool,  list , VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool(to_add: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var239 = lib.rl__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool
    var240 = c_bool(to_add)
    var241 = c_longlong(index)
    var242 = (c_bool)()
    var239(byref(var242), byref(var240), byref(input), byref(var241), )
    return var242

wrappers["_from_vector_impl"].append(rl__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool(to_add: builtins.bool, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var243 = lib.rl_can__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool
    var244 = c_bool(to_add)
    var245 = c_longlong(index)
    var246 = (c_bool)()
    var243(byref(var246), byref(var244), byref(input), byref(var245), )
    return var246

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def _from_vector_impl(to_add: BIntT0T3T, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(to_add: BIntT0T3T, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var247 = lib.rl__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool
    var248 = c_longlong(index)
    var249 = (c_bool)()
    var247(byref(var249), byref(to_add), byref(input), byref(var248), )
    return var249

wrappers["_from_vector_impl"].append(rl__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool)
signatures[rl__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, BIntT0T3T, VectorTint8_tT, builtins.int, ]
@overload
def can__from_vector_impl(to_add: BIntT0T3T, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(to_add: BIntT0T3T, input: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var250 = lib.rl_can__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool
    var251 = c_longlong(index)
    var252 = (c_bool)()
    var250(byref(var252), byref(to_add), byref(input), byref(var251), )
    return var252

wrappers["can__from_vector_impl"].append(rl_can__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, BIntT0T3T, VectorTint8_tT, builtins.int, ]
@overload
def from_byte_vector(result: Game, input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_from_byte_vector__Game_VectorTint8_tT_r_bool(result: Game, input: VectorTint8_tT) -> builtins.bool:
    var253 = lib.rl_from_byte_vector__Game_VectorTint8_tT_r_bool
    var254 = (c_bool)()
    var253(byref(var254), byref(result), byref(input), )
    return var254

wrappers["from_byte_vector"].append(rl_from_byte_vector__Game_VectorTint8_tT_r_bool)
signatures[rl_from_byte_vector__Game_VectorTint8_tT_r_bool] = [builtins.bool, Game, VectorTint8_tT, ]
@overload
def can_from_byte_vector(result: Game, input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_from_byte_vector__Game_VectorTint8_tT_r_bool(result: Game, input: VectorTint8_tT) -> builtins.bool:
    var255 = lib.rl_can_from_byte_vector__Game_VectorTint8_tT_r_bool
    var256 = (c_bool)()
    var255(byref(var256), byref(result), byref(input), )
    return var256

wrappers["can_from_byte_vector"].append(rl_can_from_byte_vector__Game_VectorTint8_tT_r_bool)
signatures[rl_can_from_byte_vector__Game_VectorTint8_tT_r_bool] = [builtins.bool, Game, VectorTint8_tT, ]
@overload
def from_byte_vector(result: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool(result: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    var257 = lib.rl_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool
    var258 = (c_bool)()
    var257(byref(var258), byref(result), byref(input), )
    return var258

wrappers["from_byte_vector"].append(rl_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool)
signatures[rl_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, ]
@overload
def can_from_byte_vector(result: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool(result: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    var259 = lib.rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool
    var260 = (c_bool)()
    var259(byref(var260), byref(result), byref(input), )
    return var260

wrappers["can_from_byte_vector"].append(rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool)
signatures[rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, ]
@overload
def from_byte_vector(result: builtins.int, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool(result: builtins.int, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var261 = lib.rl_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool
    var262 = c_byte(result)
    var263 = c_longlong(read_bytes)
    var264 = (c_bool)()
    var261(byref(var264), byref(var262), byref(input), byref(var263), )
    return var264

wrappers["from_byte_vector"].append(rl_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def can_from_byte_vector(result: builtins.int, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_can_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool(result: builtins.int, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var265 = lib.rl_can_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool
    var266 = c_byte(result)
    var267 = c_longlong(read_bytes)
    var268 = (c_bool)()
    var265(byref(var268), byref(var266), byref(input), byref(var267), )
    return var268

wrappers["can_from_byte_vector"].append(rl_can_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, builtins.int, VectorTint8_tT, builtins.int, ]
@overload
def from_byte_vector(result: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool(result: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var269 = lib.rl_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var270 = c_longlong(read_bytes)
    var271 = (c_bool)()
    var269(byref(var271), byref(result), byref(input), byref(var270), )
    return var271

wrappers["from_byte_vector"].append(rl_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def can_from_byte_vector(result: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool(result: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var272 = lib.rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var273 = c_longlong(read_bytes)
    var274 = (c_bool)()
    var272(byref(var274), byref(result), byref(input), byref(var273), )
    return var274

wrappers["can_from_byte_vector"].append(rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def from_byte_vector(result: GameMark, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool(result: GameMark, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var275 = lib.rl_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool
    var276 = c_longlong(read_bytes)
    var277 = (c_bool)()
    var275(byref(var277), byref(result), byref(input), byref(var276), )
    return var277

wrappers["from_byte_vector"].append(rl_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMark, VectorTint8_tT, builtins.int, ]
@overload
def can_from_byte_vector(result: GameMark, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_can_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool(result: GameMark, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var278 = lib.rl_can_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool
    var279 = c_longlong(read_bytes)
    var280 = (c_bool)()
    var278(byref(var280), byref(result), byref(input), byref(var279), )
    return var280

wrappers["can_from_byte_vector"].append(rl_can_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMark, VectorTint8_tT, builtins.int, ]
@overload
def size(self: VectorTint8_tT) -> builtins.int:
    pass

def rl_m_size__VectorTint8_tT_r_int64_t(self: VectorTint8_tT) -> builtins.int:
    var281 = lib.rl_m_size__VectorTint8_tT_r_int64_t
    var282 = (c_longlong)()
    var281(byref(var282), byref(self), )
    var283 = var282.value
    return var283

wrappers["size"].append(rl_m_size__VectorTint8_tT_r_int64_t)
signatures[rl_m_size__VectorTint8_tT_r_int64_t] = [builtins.int, VectorTint8_tT, ]
@overload
def can_size(self: VectorTint8_tT) -> builtins.bool:
    pass

def rl_m_can_size__VectorTint8_tT_r_bool(self: VectorTint8_tT) -> builtins.bool:
    var284 = lib.rl_m_can_size__VectorTint8_tT_r_bool
    var285 = (c_bool)()
    var284(byref(var285), byref(self), )
    return var285

wrappers["can_size"].append(rl_m_can_size__VectorTint8_tT_r_bool)
signatures[rl_m_can_size__VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, ]
@overload
def size(self: VectorTdoubleT) -> builtins.int:
    pass

def rl_m_size__VectorTdoubleT_r_int64_t(self: VectorTdoubleT) -> builtins.int:
    var286 = lib.rl_m_size__VectorTdoubleT_r_int64_t
    var287 = (c_longlong)()
    var286(byref(var287), byref(self), )
    var288 = var287.value
    return var288

wrappers["size"].append(rl_m_size__VectorTdoubleT_r_int64_t)
signatures[rl_m_size__VectorTdoubleT_r_int64_t] = [builtins.int, VectorTdoubleT, ]
@overload
def can_size(self: VectorTdoubleT) -> builtins.bool:
    pass

def rl_m_can_size__VectorTdoubleT_r_bool(self: VectorTdoubleT) -> builtins.bool:
    var289 = lib.rl_m_can_size__VectorTdoubleT_r_bool
    var290 = (c_bool)()
    var289(byref(var290), byref(self), )
    return var290

wrappers["can_size"].append(rl_m_can_size__VectorTdoubleT_r_bool)
signatures[rl_m_can_size__VectorTdoubleT_r_bool] = [builtins.bool, VectorTdoubleT, ]
@overload
def size(self: VectorTStringT) -> builtins.int:
    pass

def rl_m_size__VectorTStringT_r_int64_t(self: VectorTStringT) -> builtins.int:
    var291 = lib.rl_m_size__VectorTStringT_r_int64_t
    var292 = (c_longlong)()
    var291(byref(var292), byref(self), )
    var293 = var292.value
    return var293

wrappers["size"].append(rl_m_size__VectorTStringT_r_int64_t)
signatures[rl_m_size__VectorTStringT_r_int64_t] = [builtins.int, VectorTStringT, ]
@overload
def can_size(self: VectorTStringT) -> builtins.bool:
    pass

def rl_m_can_size__VectorTStringT_r_bool(self: VectorTStringT) -> builtins.bool:
    var294 = lib.rl_m_can_size__VectorTStringT_r_bool
    var295 = (c_bool)()
    var294(byref(var295), byref(self), )
    return var295

wrappers["can_size"].append(rl_m_can_size__VectorTStringT_r_bool)
signatures[rl_m_can_size__VectorTStringT_r_bool] = [builtins.bool, VectorTStringT, ]
@overload
def size(self: VectorTalt_GameMarkT) -> builtins.int:
    pass

def rl_m_size__VectorTalt_GameMarkT_r_int64_t(self: VectorTalt_GameMarkT) -> builtins.int:
    var296 = lib.rl_m_size__VectorTalt_GameMarkT_r_int64_t
    var297 = (c_longlong)()
    var296(byref(var297), byref(self), )
    var298 = var297.value
    return var298

wrappers["size"].append(rl_m_size__VectorTalt_GameMarkT_r_int64_t)
signatures[rl_m_size__VectorTalt_GameMarkT_r_int64_t] = [builtins.int, VectorTalt_GameMarkT, ]
@overload
def can_size(self: VectorTalt_GameMarkT) -> builtins.bool:
    pass

def rl_m_can_size__VectorTalt_GameMarkT_r_bool(self: VectorTalt_GameMarkT) -> builtins.bool:
    var299 = lib.rl_m_can_size__VectorTalt_GameMarkT_r_bool
    var300 = (c_bool)()
    var299(byref(var300), byref(self), )
    return var300

wrappers["can_size"].append(rl_m_can_size__VectorTalt_GameMarkT_r_bool)
signatures[rl_m_can_size__VectorTalt_GameMarkT_r_bool] = [builtins.bool, VectorTalt_GameMarkT, ]
@overload
def size(self: VectorTGameMarkT) -> builtins.int:
    pass

def rl_m_size__VectorTGameMarkT_r_int64_t(self: VectorTGameMarkT) -> builtins.int:
    var301 = lib.rl_m_size__VectorTGameMarkT_r_int64_t
    var302 = (c_longlong)()
    var301(byref(var302), byref(self), )
    var303 = var302.value
    return var303

wrappers["size"].append(rl_m_size__VectorTGameMarkT_r_int64_t)
signatures[rl_m_size__VectorTGameMarkT_r_int64_t] = [builtins.int, VectorTGameMarkT, ]
@overload
def can_size(self: VectorTGameMarkT) -> builtins.bool:
    pass

def rl_m_can_size__VectorTGameMarkT_r_bool(self: VectorTGameMarkT) -> builtins.bool:
    var304 = lib.rl_m_can_size__VectorTGameMarkT_r_bool
    var305 = (c_bool)()
    var304(byref(var305), byref(self), )
    return var305

wrappers["can_size"].append(rl_m_can_size__VectorTGameMarkT_r_bool)
signatures[rl_m_can_size__VectorTGameMarkT_r_bool] = [builtins.bool, VectorTGameMarkT, ]
@overload
def size(self: VectorTBIntT0T3TT) -> builtins.int:
    pass

def rl_m_size__VectorTBIntT0T3TT_r_int64_t(self: VectorTBIntT0T3TT) -> builtins.int:
    var306 = lib.rl_m_size__VectorTBIntT0T3TT_r_int64_t
    var307 = (c_longlong)()
    var306(byref(var307), byref(self), )
    var308 = var307.value
    return var308

wrappers["size"].append(rl_m_size__VectorTBIntT0T3TT_r_int64_t)
signatures[rl_m_size__VectorTBIntT0T3TT_r_int64_t] = [builtins.int, VectorTBIntT0T3TT, ]
@overload
def can_size(self: VectorTBIntT0T3TT) -> builtins.bool:
    pass

def rl_m_can_size__VectorTBIntT0T3TT_r_bool(self: VectorTBIntT0T3TT) -> builtins.bool:
    var309 = lib.rl_m_can_size__VectorTBIntT0T3TT_r_bool
    var310 = (c_bool)()
    var309(byref(var310), byref(self), )
    return var310

wrappers["can_size"].append(rl_m_can_size__VectorTBIntT0T3TT_r_bool)
signatures[rl_m_can_size__VectorTBIntT0T3TT_r_bool] = [builtins.bool, VectorTBIntT0T3TT, ]
@overload
def drop_back(self: VectorTint8_tT, quantity: builtins.int) -> None:
    pass

def rl_m_drop_back__VectorTint8_tT_int64_t(self: VectorTint8_tT, quantity: builtins.int) -> None:
    var311 = lib.rl_m_drop_back__VectorTint8_tT_int64_t
    var312 = c_longlong(quantity)
    var311(byref(self), byref(var312), )
    return

wrappers["drop_back"].append(rl_m_drop_back__VectorTint8_tT_int64_t)
signatures[rl_m_drop_back__VectorTint8_tT_int64_t] = [None, VectorTint8_tT, builtins.int, ]
@overload
def can_drop_back(self: VectorTint8_tT, quantity: builtins.int) -> builtins.bool:
    pass

def rl_m_can_drop_back__VectorTint8_tT_int64_t_r_bool(self: VectorTint8_tT, quantity: builtins.int) -> builtins.bool:
    var313 = lib.rl_m_can_drop_back__VectorTint8_tT_int64_t_r_bool
    var314 = c_longlong(quantity)
    var315 = (c_bool)()
    var313(byref(var315), byref(self), byref(var314), )
    return var315

wrappers["can_drop_back"].append(rl_m_can_drop_back__VectorTint8_tT_int64_t_r_bool)
signatures[rl_m_can_drop_back__VectorTint8_tT_int64_t_r_bool] = [builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def pop(self: VectorTint8_tT) -> builtins.int:
    pass

def rl_m_pop__VectorTint8_tT_r_int8_t(self: VectorTint8_tT) -> builtins.int:
    var316 = lib.rl_m_pop__VectorTint8_tT_r_int8_t
    var317 = (c_byte)()
    var316(byref(var317), byref(self), )
    var318 = var317.value
    return var318

wrappers["pop"].append(rl_m_pop__VectorTint8_tT_r_int8_t)
signatures[rl_m_pop__VectorTint8_tT_r_int8_t] = [builtins.int, VectorTint8_tT, ]
@overload
def can_pop(self: VectorTint8_tT) -> builtins.bool:
    pass

def rl_m_can_pop__VectorTint8_tT_r_bool(self: VectorTint8_tT) -> builtins.bool:
    var319 = lib.rl_m_can_pop__VectorTint8_tT_r_bool
    var320 = (c_bool)()
    var319(byref(var320), byref(self), )
    return var320

wrappers["can_pop"].append(rl_m_can_pop__VectorTint8_tT_r_bool)
signatures[rl_m_can_pop__VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, ]
@overload
def pop(self: VectorTStringT) -> String:
    pass

def rl_m_pop__VectorTStringT_r_String(self: VectorTStringT) -> String:
    var321 = lib.rl_m_pop__VectorTStringT_r_String
    var322 = (String)()
    var321(byref(var322), byref(self), )
    return var322

wrappers["pop"].append(rl_m_pop__VectorTStringT_r_String)
signatures[rl_m_pop__VectorTStringT_r_String] = [String, VectorTStringT, ]
@overload
def can_pop(self: VectorTStringT) -> builtins.bool:
    pass

def rl_m_can_pop__VectorTStringT_r_bool(self: VectorTStringT) -> builtins.bool:
    var323 = lib.rl_m_can_pop__VectorTStringT_r_bool
    var324 = (c_bool)()
    var323(byref(var324), byref(self), )
    return var324

wrappers["can_pop"].append(rl_m_can_pop__VectorTStringT_r_bool)
signatures[rl_m_can_pop__VectorTStringT_r_bool] = [builtins.bool, VectorTStringT, ]
@overload
def pop(self: VectorTdoubleT) -> builtins.float:
    pass

def rl_m_pop__VectorTdoubleT_r_double(self: VectorTdoubleT) -> builtins.float:
    var325 = lib.rl_m_pop__VectorTdoubleT_r_double
    var326 = (c_double)()
    var325(byref(var326), byref(self), )
    return var326

wrappers["pop"].append(rl_m_pop__VectorTdoubleT_r_double)
signatures[rl_m_pop__VectorTdoubleT_r_double] = [builtins.float, VectorTdoubleT, ]
@overload
def can_pop(self: VectorTdoubleT) -> builtins.bool:
    pass

def rl_m_can_pop__VectorTdoubleT_r_bool(self: VectorTdoubleT) -> builtins.bool:
    var327 = lib.rl_m_can_pop__VectorTdoubleT_r_bool
    var328 = (c_bool)()
    var327(byref(var328), byref(self), )
    return var328

wrappers["can_pop"].append(rl_m_can_pop__VectorTdoubleT_r_bool)
signatures[rl_m_can_pop__VectorTdoubleT_r_bool] = [builtins.bool, VectorTdoubleT, ]
@overload
def append(self: VectorTint8_tT, value: builtins.int) -> None:
    pass

def rl_m_append__VectorTint8_tT_int8_t(self: VectorTint8_tT, value: builtins.int) -> None:
    var329 = lib.rl_m_append__VectorTint8_tT_int8_t
    var330 = c_byte(value)
    var329(byref(self), byref(var330), )
    return

wrappers["append"].append(rl_m_append__VectorTint8_tT_int8_t)
signatures[rl_m_append__VectorTint8_tT_int8_t] = [None, VectorTint8_tT, builtins.int, ]
@overload
def can_append(self: VectorTint8_tT, value: builtins.int) -> builtins.bool:
    pass

def rl_m_can_append__VectorTint8_tT_int8_t_r_bool(self: VectorTint8_tT, value: builtins.int) -> builtins.bool:
    var331 = lib.rl_m_can_append__VectorTint8_tT_int8_t_r_bool
    var332 = c_byte(value)
    var333 = (c_bool)()
    var331(byref(var333), byref(self), byref(var332), )
    return var333

wrappers["can_append"].append(rl_m_can_append__VectorTint8_tT_int8_t_r_bool)
signatures[rl_m_can_append__VectorTint8_tT_int8_t_r_bool] = [builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def append(self: VectorTboolT, value: builtins.bool) -> None:
    pass

def rl_m_append__VectorTboolT_bool(self: VectorTboolT, value: builtins.bool) -> None:
    var334 = lib.rl_m_append__VectorTboolT_bool
    var335 = c_bool(value)
    var334(byref(self), byref(var335), )
    return

wrappers["append"].append(rl_m_append__VectorTboolT_bool)
signatures[rl_m_append__VectorTboolT_bool] = [None, VectorTboolT, builtins.bool, ]
@overload
def can_append(self: VectorTboolT, value: builtins.bool) -> builtins.bool:
    pass

def rl_m_can_append__VectorTboolT_bool_r_bool(self: VectorTboolT, value: builtins.bool) -> builtins.bool:
    var336 = lib.rl_m_can_append__VectorTboolT_bool_r_bool
    var337 = c_bool(value)
    var338 = (c_bool)()
    var336(byref(var338), byref(self), byref(var337), )
    return var338

wrappers["can_append"].append(rl_m_can_append__VectorTboolT_bool_r_bool)
signatures[rl_m_can_append__VectorTboolT_bool_r_bool] = [builtins.bool, VectorTboolT, builtins.bool, ]
@overload
def append(self: VectorTStringT, value: String) -> None:
    pass

def rl_m_append__VectorTStringT_String(self: VectorTStringT, value: String) -> None:
    var339 = lib.rl_m_append__VectorTStringT_String
    var339(byref(self), byref(value), )
    return

wrappers["append"].append(rl_m_append__VectorTStringT_String)
signatures[rl_m_append__VectorTStringT_String] = [None, VectorTStringT, String, ]
@overload
def can_append(self: VectorTStringT, value: String) -> builtins.bool:
    pass

def rl_m_can_append__VectorTStringT_String_r_bool(self: VectorTStringT, value: String) -> builtins.bool:
    var340 = lib.rl_m_can_append__VectorTStringT_String_r_bool
    var341 = (c_bool)()
    var340(byref(var341), byref(self), byref(value), )
    return var341

wrappers["can_append"].append(rl_m_can_append__VectorTStringT_String_r_bool)
signatures[rl_m_can_append__VectorTStringT_String_r_bool] = [builtins.bool, VectorTStringT, String, ]
@overload
def append(self: VectorTdoubleT, value: builtins.float) -> None:
    pass

def rl_m_append__VectorTdoubleT_double(self: VectorTdoubleT, value: builtins.float) -> None:
    var342 = lib.rl_m_append__VectorTdoubleT_double
    var343 = c_double(value)
    var342(byref(self), byref(var343), )
    return

wrappers["append"].append(rl_m_append__VectorTdoubleT_double)
signatures[rl_m_append__VectorTdoubleT_double] = [None, VectorTdoubleT, builtins.float, ]
@overload
def can_append(self: VectorTdoubleT, value: builtins.float) -> builtins.bool:
    pass

def rl_m_can_append__VectorTdoubleT_double_r_bool(self: VectorTdoubleT, value: builtins.float) -> builtins.bool:
    var344 = lib.rl_m_can_append__VectorTdoubleT_double_r_bool
    var345 = c_double(value)
    var346 = (c_bool)()
    var344(byref(var346), byref(self), byref(var345), )
    return var346

wrappers["can_append"].append(rl_m_can_append__VectorTdoubleT_double_r_bool)
signatures[rl_m_can_append__VectorTdoubleT_double_r_bool] = [builtins.bool, VectorTdoubleT, builtins.float, ]
@overload
def append(self: VectorTalt_GameMarkT, value: GameMarkOr) -> None:
    pass

def rl_m_append__VectorTalt_GameMarkT_alt_GameMark(self: VectorTalt_GameMarkT, value: GameMarkOr) -> None:
    var347 = lib.rl_m_append__VectorTalt_GameMarkT_alt_GameMark
    var347(byref(self), byref(value), )
    return

wrappers["append"].append(rl_m_append__VectorTalt_GameMarkT_alt_GameMark)
signatures[rl_m_append__VectorTalt_GameMarkT_alt_GameMark] = [None, VectorTalt_GameMarkT, GameMarkOr, ]
@overload
def can_append(self: VectorTalt_GameMarkT, value: GameMarkOr) -> builtins.bool:
    pass

def rl_m_can_append__VectorTalt_GameMarkT_alt_GameMark_r_bool(self: VectorTalt_GameMarkT, value: GameMarkOr) -> builtins.bool:
    var348 = lib.rl_m_can_append__VectorTalt_GameMarkT_alt_GameMark_r_bool
    var349 = (c_bool)()
    var348(byref(var349), byref(self), byref(value), )
    return var349

wrappers["can_append"].append(rl_m_can_append__VectorTalt_GameMarkT_alt_GameMark_r_bool)
signatures[rl_m_can_append__VectorTalt_GameMarkT_alt_GameMark_r_bool] = [builtins.bool, VectorTalt_GameMarkT, GameMarkOr, ]
@overload
def append(self: VectorTGameMarkT, value: GameMark) -> None:
    pass

def rl_m_append__VectorTGameMarkT_GameMark(self: VectorTGameMarkT, value: GameMark) -> None:
    var350 = lib.rl_m_append__VectorTGameMarkT_GameMark
    var350(byref(self), byref(value), )
    return

wrappers["append"].append(rl_m_append__VectorTGameMarkT_GameMark)
signatures[rl_m_append__VectorTGameMarkT_GameMark] = [None, VectorTGameMarkT, GameMark, ]
@overload
def can_append(self: VectorTGameMarkT, value: GameMark) -> builtins.bool:
    pass

def rl_m_can_append__VectorTGameMarkT_GameMark_r_bool(self: VectorTGameMarkT, value: GameMark) -> builtins.bool:
    var351 = lib.rl_m_can_append__VectorTGameMarkT_GameMark_r_bool
    var352 = (c_bool)()
    var351(byref(var352), byref(self), byref(value), )
    return var352

wrappers["can_append"].append(rl_m_can_append__VectorTGameMarkT_GameMark_r_bool)
signatures[rl_m_can_append__VectorTGameMarkT_GameMark_r_bool] = [builtins.bool, VectorTGameMarkT, GameMark, ]
@overload
def append(self: VectorTBIntT0T3TT, value: BIntT0T3T) -> None:
    pass

def rl_m_append__VectorTBIntT0T3TT_BIntT0T3T(self: VectorTBIntT0T3TT, value: BIntT0T3T) -> None:
    var353 = lib.rl_m_append__VectorTBIntT0T3TT_BIntT0T3T
    var353(byref(self), byref(value), )
    return

wrappers["append"].append(rl_m_append__VectorTBIntT0T3TT_BIntT0T3T)
signatures[rl_m_append__VectorTBIntT0T3TT_BIntT0T3T] = [None, VectorTBIntT0T3TT, BIntT0T3T, ]
@overload
def can_append(self: VectorTBIntT0T3TT, value: BIntT0T3T) -> builtins.bool:
    pass

def rl_m_can_append__VectorTBIntT0T3TT_BIntT0T3T_r_bool(self: VectorTBIntT0T3TT, value: BIntT0T3T) -> builtins.bool:
    var354 = lib.rl_m_can_append__VectorTBIntT0T3TT_BIntT0T3T_r_bool
    var355 = (c_bool)()
    var354(byref(var355), byref(self), byref(value), )
    return var355

wrappers["can_append"].append(rl_m_can_append__VectorTBIntT0T3TT_BIntT0T3T_r_bool)
signatures[rl_m_can_append__VectorTBIntT0T3TT_BIntT0T3T_r_bool] = [builtins.bool, VectorTBIntT0T3TT, BIntT0T3T, ]
@overload
def get(self: VectorTint8_tT, index: builtins.int) -> POINTER(c_byte):
    pass

def rl_m_get__VectorTint8_tT_int64_t_r_int8_tRef(self: VectorTint8_tT, index: builtins.int) -> POINTER(c_byte):
    var356 = lib.rl_m_get__VectorTint8_tT_int64_t_r_int8_tRef
    var357 = c_longlong(index)
    var358 = (POINTER(c_byte))()
    var356(byref(var358), byref(self), byref(var357), )
    return var358

wrappers["get"].append(rl_m_get__VectorTint8_tT_int64_t_r_int8_tRef)
signatures[rl_m_get__VectorTint8_tT_int64_t_r_int8_tRef] = [POINTER(c_byte), VectorTint8_tT, builtins.int, ]
@overload
def can_get(self: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTint8_tT_int64_t_r_bool(self: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var359 = lib.rl_m_can_get__VectorTint8_tT_int64_t_r_bool
    var360 = c_longlong(index)
    var361 = (c_bool)()
    var359(byref(var361), byref(self), byref(var360), )
    return var361

wrappers["can_get"].append(rl_m_can_get__VectorTint8_tT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTint8_tT_int64_t_r_bool] = [builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def get(self: VectorTdoubleT, index: builtins.int) -> POINTER(c_double):
    pass

def rl_m_get__VectorTdoubleT_int64_t_r_doubleRef(self: VectorTdoubleT, index: builtins.int) -> POINTER(c_double):
    var362 = lib.rl_m_get__VectorTdoubleT_int64_t_r_doubleRef
    var363 = c_longlong(index)
    var364 = (POINTER(c_double))()
    var362(byref(var364), byref(self), byref(var363), )
    return var364

wrappers["get"].append(rl_m_get__VectorTdoubleT_int64_t_r_doubleRef)
signatures[rl_m_get__VectorTdoubleT_int64_t_r_doubleRef] = [POINTER(c_double), VectorTdoubleT, builtins.int, ]
@overload
def can_get(self: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTdoubleT_int64_t_r_bool(self: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var365 = lib.rl_m_can_get__VectorTdoubleT_int64_t_r_bool
    var366 = c_longlong(index)
    var367 = (c_bool)()
    var365(byref(var367), byref(self), byref(var366), )
    return var367

wrappers["can_get"].append(rl_m_can_get__VectorTdoubleT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTdoubleT_int64_t_r_bool] = [builtins.bool, VectorTdoubleT, builtins.int, ]
@overload
def get(self: VectorTStringT, index: builtins.int) -> POINTER(String):
    pass

def rl_m_get__VectorTStringT_int64_t_r_StringRef(self: VectorTStringT, index: builtins.int) -> POINTER(String):
    var368 = lib.rl_m_get__VectorTStringT_int64_t_r_StringRef
    var369 = c_longlong(index)
    var370 = (POINTER(String))()
    var368(byref(var370), byref(self), byref(var369), )
    return var370

wrappers["get"].append(rl_m_get__VectorTStringT_int64_t_r_StringRef)
signatures[rl_m_get__VectorTStringT_int64_t_r_StringRef] = [POINTER(String), VectorTStringT, builtins.int, ]
@overload
def can_get(self: VectorTStringT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTStringT_int64_t_r_bool(self: VectorTStringT, index: builtins.int) -> builtins.bool:
    var371 = lib.rl_m_can_get__VectorTStringT_int64_t_r_bool
    var372 = c_longlong(index)
    var373 = (c_bool)()
    var371(byref(var373), byref(self), byref(var372), )
    return var373

wrappers["can_get"].append(rl_m_can_get__VectorTStringT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTStringT_int64_t_r_bool] = [builtins.bool, VectorTStringT, builtins.int, ]
@overload
def get(self: VectorTboolT, index: builtins.int) -> POINTER(c_bool):
    pass

def rl_m_get__VectorTboolT_int64_t_r_boolRef(self: VectorTboolT, index: builtins.int) -> POINTER(c_bool):
    var374 = lib.rl_m_get__VectorTboolT_int64_t_r_boolRef
    var375 = c_longlong(index)
    var376 = (POINTER(c_bool))()
    var374(byref(var376), byref(self), byref(var375), )
    return var376

wrappers["get"].append(rl_m_get__VectorTboolT_int64_t_r_boolRef)
signatures[rl_m_get__VectorTboolT_int64_t_r_boolRef] = [POINTER(c_bool), VectorTboolT, builtins.int, ]
@overload
def can_get(self: VectorTboolT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTboolT_int64_t_r_bool(self: VectorTboolT, index: builtins.int) -> builtins.bool:
    var377 = lib.rl_m_can_get__VectorTboolT_int64_t_r_bool
    var378 = c_longlong(index)
    var379 = (c_bool)()
    var377(byref(var379), byref(self), byref(var378), )
    return var379

wrappers["can_get"].append(rl_m_can_get__VectorTboolT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTboolT_int64_t_r_bool] = [builtins.bool, VectorTboolT, builtins.int, ]
@overload
def get(self: VectorTalt_GameMarkT, index: builtins.int) -> POINTER(GameMarkOr):
    pass

def rl_m_get__VectorTalt_GameMarkT_int64_t_r_alt_GameMarkRef(self: VectorTalt_GameMarkT, index: builtins.int) -> POINTER(GameMarkOr):
    var380 = lib.rl_m_get__VectorTalt_GameMarkT_int64_t_r_alt_GameMarkRef
    var381 = c_longlong(index)
    var382 = (POINTER(GameMarkOr))()
    var380(byref(var382), byref(self), byref(var381), )
    return var382

wrappers["get"].append(rl_m_get__VectorTalt_GameMarkT_int64_t_r_alt_GameMarkRef)
signatures[rl_m_get__VectorTalt_GameMarkT_int64_t_r_alt_GameMarkRef] = [POINTER(GameMarkOr), VectorTalt_GameMarkT, builtins.int, ]
@overload
def can_get(self: VectorTalt_GameMarkT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTalt_GameMarkT_int64_t_r_bool(self: VectorTalt_GameMarkT, index: builtins.int) -> builtins.bool:
    var383 = lib.rl_m_can_get__VectorTalt_GameMarkT_int64_t_r_bool
    var384 = c_longlong(index)
    var385 = (c_bool)()
    var383(byref(var385), byref(self), byref(var384), )
    return var385

wrappers["can_get"].append(rl_m_can_get__VectorTalt_GameMarkT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTalt_GameMarkT_int64_t_r_bool] = [builtins.bool, VectorTalt_GameMarkT, builtins.int, ]
@overload
def get(self: VectorTGameMarkT, index: builtins.int) -> POINTER(GameMark):
    pass

def rl_m_get__VectorTGameMarkT_int64_t_r_GameMarkRef(self: VectorTGameMarkT, index: builtins.int) -> POINTER(GameMark):
    var386 = lib.rl_m_get__VectorTGameMarkT_int64_t_r_GameMarkRef
    var387 = c_longlong(index)
    var388 = (POINTER(GameMark))()
    var386(byref(var388), byref(self), byref(var387), )
    return var388

wrappers["get"].append(rl_m_get__VectorTGameMarkT_int64_t_r_GameMarkRef)
signatures[rl_m_get__VectorTGameMarkT_int64_t_r_GameMarkRef] = [POINTER(GameMark), VectorTGameMarkT, builtins.int, ]
@overload
def can_get(self: VectorTGameMarkT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTGameMarkT_int64_t_r_bool(self: VectorTGameMarkT, index: builtins.int) -> builtins.bool:
    var389 = lib.rl_m_can_get__VectorTGameMarkT_int64_t_r_bool
    var390 = c_longlong(index)
    var391 = (c_bool)()
    var389(byref(var391), byref(self), byref(var390), )
    return var391

wrappers["can_get"].append(rl_m_can_get__VectorTGameMarkT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTGameMarkT_int64_t_r_bool] = [builtins.bool, VectorTGameMarkT, builtins.int, ]
@overload
def get(self: VectorTBIntT0T3TT, index: builtins.int) -> POINTER(BIntT0T3T):
    pass

def rl_m_get__VectorTBIntT0T3TT_int64_t_r_BIntT0T3TRef(self: VectorTBIntT0T3TT, index: builtins.int) -> POINTER(BIntT0T3T):
    var392 = lib.rl_m_get__VectorTBIntT0T3TT_int64_t_r_BIntT0T3TRef
    var393 = c_longlong(index)
    var394 = (POINTER(BIntT0T3T))()
    var392(byref(var394), byref(self), byref(var393), )
    return var394

wrappers["get"].append(rl_m_get__VectorTBIntT0T3TT_int64_t_r_BIntT0T3TRef)
signatures[rl_m_get__VectorTBIntT0T3TT_int64_t_r_BIntT0T3TRef] = [POINTER(BIntT0T3T), VectorTBIntT0T3TT, builtins.int, ]
@overload
def can_get(self: VectorTBIntT0T3TT, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__VectorTBIntT0T3TT_int64_t_r_bool(self: VectorTBIntT0T3TT, index: builtins.int) -> builtins.bool:
    var395 = lib.rl_m_can_get__VectorTBIntT0T3TT_int64_t_r_bool
    var396 = c_longlong(index)
    var397 = (c_bool)()
    var395(byref(var397), byref(self), byref(var396), )
    return var397

wrappers["can_get"].append(rl_m_can_get__VectorTBIntT0T3TT_int64_t_r_bool)
signatures[rl_m_can_get__VectorTBIntT0T3TT_int64_t_r_bool] = [builtins.bool, VectorTBIntT0T3TT, builtins.int, ]
@overload
def back(self: VectorTint8_tT) -> POINTER(c_byte):
    pass

def rl_m_back__VectorTint8_tT_r_int8_tRef(self: VectorTint8_tT) -> POINTER(c_byte):
    var398 = lib.rl_m_back__VectorTint8_tT_r_int8_tRef
    var399 = (POINTER(c_byte))()
    var398(byref(var399), byref(self), )
    return var399

wrappers["back"].append(rl_m_back__VectorTint8_tT_r_int8_tRef)
signatures[rl_m_back__VectorTint8_tT_r_int8_tRef] = [POINTER(c_byte), VectorTint8_tT, ]
@overload
def can_back(self: VectorTint8_tT) -> builtins.bool:
    pass

def rl_m_can_back__VectorTint8_tT_r_bool(self: VectorTint8_tT) -> builtins.bool:
    var400 = lib.rl_m_can_back__VectorTint8_tT_r_bool
    var401 = (c_bool)()
    var400(byref(var401), byref(self), )
    return var401

wrappers["can_back"].append(rl_m_can_back__VectorTint8_tT_r_bool)
signatures[rl_m_can_back__VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, ]
@overload
def resize(self: VectorTdoubleT, new_size: builtins.int) -> None:
    pass

def rl_m_resize__VectorTdoubleT_int64_t(self: VectorTdoubleT, new_size: builtins.int) -> None:
    var402 = lib.rl_m_resize__VectorTdoubleT_int64_t
    var403 = c_longlong(new_size)
    var402(byref(self), byref(var403), )
    return

wrappers["resize"].append(rl_m_resize__VectorTdoubleT_int64_t)
signatures[rl_m_resize__VectorTdoubleT_int64_t] = [None, VectorTdoubleT, builtins.int, ]
@overload
def can_resize(self: VectorTdoubleT, new_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can_resize__VectorTdoubleT_int64_t_r_bool(self: VectorTdoubleT, new_size: builtins.int) -> builtins.bool:
    var404 = lib.rl_m_can_resize__VectorTdoubleT_int64_t_r_bool
    var405 = c_longlong(new_size)
    var406 = (c_bool)()
    var404(byref(var406), byref(self), byref(var405), )
    return var406

wrappers["can_resize"].append(rl_m_can_resize__VectorTdoubleT_int64_t_r_bool)
signatures[rl_m_can_resize__VectorTdoubleT_int64_t_r_bool] = [builtins.bool, VectorTdoubleT, builtins.int, ]
@overload
def assign(self: VectorTint8_tT, other: VectorTint8_tT) -> None:
    pass

def rl_m_assign__VectorTint8_tT_VectorTint8_tT(self: VectorTint8_tT, other: VectorTint8_tT) -> None:
    var407 = lib.rl_m_assign__VectorTint8_tT_VectorTint8_tT
    var407(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTint8_tT_VectorTint8_tT)
signatures[rl_m_assign__VectorTint8_tT_VectorTint8_tT] = [None, VectorTint8_tT, VectorTint8_tT, ]
@overload
def can_assign(self: VectorTint8_tT, other: VectorTint8_tT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTint8_tT_VectorTint8_tT_r_bool(self: VectorTint8_tT, other: VectorTint8_tT) -> builtins.bool:
    var408 = lib.rl_m_can_assign__VectorTint8_tT_VectorTint8_tT_r_bool
    var409 = (c_bool)()
    var408(byref(var409), byref(self), byref(other), )
    return var409

wrappers["can_assign"].append(rl_m_can_assign__VectorTint8_tT_VectorTint8_tT_r_bool)
signatures[rl_m_can_assign__VectorTint8_tT_VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, VectorTint8_tT, ]
@overload
def assign(self: VectorTboolT, other: VectorTboolT) -> None:
    pass

def rl_m_assign__VectorTboolT_VectorTboolT(self: VectorTboolT, other: VectorTboolT) -> None:
    var410 = lib.rl_m_assign__VectorTboolT_VectorTboolT
    var410(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTboolT_VectorTboolT)
signatures[rl_m_assign__VectorTboolT_VectorTboolT] = [None, VectorTboolT, VectorTboolT, ]
@overload
def can_assign(self: VectorTboolT, other: VectorTboolT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTboolT_VectorTboolT_r_bool(self: VectorTboolT, other: VectorTboolT) -> builtins.bool:
    var411 = lib.rl_m_can_assign__VectorTboolT_VectorTboolT_r_bool
    var412 = (c_bool)()
    var411(byref(var412), byref(self), byref(other), )
    return var412

wrappers["can_assign"].append(rl_m_can_assign__VectorTboolT_VectorTboolT_r_bool)
signatures[rl_m_can_assign__VectorTboolT_VectorTboolT_r_bool] = [builtins.bool, VectorTboolT, VectorTboolT, ]
@overload
def assign(self: VectorTdoubleT, other: VectorTdoubleT) -> None:
    pass

def rl_m_assign__VectorTdoubleT_VectorTdoubleT(self: VectorTdoubleT, other: VectorTdoubleT) -> None:
    var413 = lib.rl_m_assign__VectorTdoubleT_VectorTdoubleT
    var413(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTdoubleT_VectorTdoubleT)
signatures[rl_m_assign__VectorTdoubleT_VectorTdoubleT] = [None, VectorTdoubleT, VectorTdoubleT, ]
@overload
def can_assign(self: VectorTdoubleT, other: VectorTdoubleT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTdoubleT_VectorTdoubleT_r_bool(self: VectorTdoubleT, other: VectorTdoubleT) -> builtins.bool:
    var414 = lib.rl_m_can_assign__VectorTdoubleT_VectorTdoubleT_r_bool
    var415 = (c_bool)()
    var414(byref(var415), byref(self), byref(other), )
    return var415

wrappers["can_assign"].append(rl_m_can_assign__VectorTdoubleT_VectorTdoubleT_r_bool)
signatures[rl_m_can_assign__VectorTdoubleT_VectorTdoubleT_r_bool] = [builtins.bool, VectorTdoubleT, VectorTdoubleT, ]
@overload
def assign(self: VectorTStringT, other: VectorTStringT) -> None:
    pass

def rl_m_assign__VectorTStringT_VectorTStringT(self: VectorTStringT, other: VectorTStringT) -> None:
    var416 = lib.rl_m_assign__VectorTStringT_VectorTStringT
    var416(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTStringT_VectorTStringT)
signatures[rl_m_assign__VectorTStringT_VectorTStringT] = [None, VectorTStringT, VectorTStringT, ]
@overload
def can_assign(self: VectorTStringT, other: VectorTStringT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTStringT_VectorTStringT_r_bool(self: VectorTStringT, other: VectorTStringT) -> builtins.bool:
    var417 = lib.rl_m_can_assign__VectorTStringT_VectorTStringT_r_bool
    var418 = (c_bool)()
    var417(byref(var418), byref(self), byref(other), )
    return var418

wrappers["can_assign"].append(rl_m_can_assign__VectorTStringT_VectorTStringT_r_bool)
signatures[rl_m_can_assign__VectorTStringT_VectorTStringT_r_bool] = [builtins.bool, VectorTStringT, VectorTStringT, ]
@overload
def assign(self: VectorTalt_GameMarkT, other: VectorTalt_GameMarkT) -> None:
    pass

def rl_m_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT(self: VectorTalt_GameMarkT, other: VectorTalt_GameMarkT) -> None:
    var419 = lib.rl_m_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT
    var419(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT)
signatures[rl_m_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT] = [None, VectorTalt_GameMarkT, VectorTalt_GameMarkT, ]
@overload
def can_assign(self: VectorTalt_GameMarkT, other: VectorTalt_GameMarkT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT_r_bool(self: VectorTalt_GameMarkT, other: VectorTalt_GameMarkT) -> builtins.bool:
    var420 = lib.rl_m_can_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT_r_bool
    var421 = (c_bool)()
    var420(byref(var421), byref(self), byref(other), )
    return var421

wrappers["can_assign"].append(rl_m_can_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT_r_bool)
signatures[rl_m_can_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT_r_bool] = [builtins.bool, VectorTalt_GameMarkT, VectorTalt_GameMarkT, ]
@overload
def assign(self: VectorTGameMarkT, other: VectorTGameMarkT) -> None:
    pass

def rl_m_assign__VectorTGameMarkT_VectorTGameMarkT(self: VectorTGameMarkT, other: VectorTGameMarkT) -> None:
    var422 = lib.rl_m_assign__VectorTGameMarkT_VectorTGameMarkT
    var422(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTGameMarkT_VectorTGameMarkT)
signatures[rl_m_assign__VectorTGameMarkT_VectorTGameMarkT] = [None, VectorTGameMarkT, VectorTGameMarkT, ]
@overload
def can_assign(self: VectorTGameMarkT, other: VectorTGameMarkT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTGameMarkT_VectorTGameMarkT_r_bool(self: VectorTGameMarkT, other: VectorTGameMarkT) -> builtins.bool:
    var423 = lib.rl_m_can_assign__VectorTGameMarkT_VectorTGameMarkT_r_bool
    var424 = (c_bool)()
    var423(byref(var424), byref(self), byref(other), )
    return var424

wrappers["can_assign"].append(rl_m_can_assign__VectorTGameMarkT_VectorTGameMarkT_r_bool)
signatures[rl_m_can_assign__VectorTGameMarkT_VectorTGameMarkT_r_bool] = [builtins.bool, VectorTGameMarkT, VectorTGameMarkT, ]
@overload
def assign(self: VectorTBIntT0T3TT, other: VectorTBIntT0T3TT) -> None:
    pass

def rl_m_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT(self: VectorTBIntT0T3TT, other: VectorTBIntT0T3TT) -> None:
    var425 = lib.rl_m_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT
    var425(byref(self), byref(other), )
    return

wrappers["assign"].append(rl_m_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT)
signatures[rl_m_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT] = [None, VectorTBIntT0T3TT, VectorTBIntT0T3TT, ]
@overload
def can_assign(self: VectorTBIntT0T3TT, other: VectorTBIntT0T3TT) -> builtins.bool:
    pass

def rl_m_can_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT_r_bool(self: VectorTBIntT0T3TT, other: VectorTBIntT0T3TT) -> builtins.bool:
    var426 = lib.rl_m_can_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT_r_bool
    var427 = (c_bool)()
    var426(byref(var427), byref(self), byref(other), )
    return var427

wrappers["can_assign"].append(rl_m_can_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT_r_bool)
signatures[rl_m_can_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT_r_bool] = [builtins.bool, VectorTBIntT0T3TT, VectorTBIntT0T3TT, ]
@overload
def drop(self: VectorTint8_tT) -> None:
    pass

def rl_m_drop__VectorTint8_tT(self: VectorTint8_tT) -> None:
    var428 = lib.rl_m_drop__VectorTint8_tT
    var428(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTint8_tT)
signatures[rl_m_drop__VectorTint8_tT] = [None, VectorTint8_tT, ]
@overload
def can_drop(self: VectorTint8_tT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTint8_tT_r_bool(self: VectorTint8_tT) -> builtins.bool:
    var429 = lib.rl_m_can_drop__VectorTint8_tT_r_bool
    var430 = (c_bool)()
    var429(byref(var430), byref(self), )
    return var430

wrappers["can_drop"].append(rl_m_can_drop__VectorTint8_tT_r_bool)
signatures[rl_m_can_drop__VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, ]
@overload
def drop(self: VectorTdoubleT) -> None:
    pass

def rl_m_drop__VectorTdoubleT(self: VectorTdoubleT) -> None:
    var431 = lib.rl_m_drop__VectorTdoubleT
    var431(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTdoubleT)
signatures[rl_m_drop__VectorTdoubleT] = [None, VectorTdoubleT, ]
@overload
def can_drop(self: VectorTdoubleT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTdoubleT_r_bool(self: VectorTdoubleT) -> builtins.bool:
    var432 = lib.rl_m_can_drop__VectorTdoubleT_r_bool
    var433 = (c_bool)()
    var432(byref(var433), byref(self), )
    return var433

wrappers["can_drop"].append(rl_m_can_drop__VectorTdoubleT_r_bool)
signatures[rl_m_can_drop__VectorTdoubleT_r_bool] = [builtins.bool, VectorTdoubleT, ]
@overload
def drop(self: VectorTStringT) -> None:
    pass

def rl_m_drop__VectorTStringT(self: VectorTStringT) -> None:
    var434 = lib.rl_m_drop__VectorTStringT
    var434(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTStringT)
signatures[rl_m_drop__VectorTStringT] = [None, VectorTStringT, ]
@overload
def can_drop(self: VectorTStringT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTStringT_r_bool(self: VectorTStringT) -> builtins.bool:
    var435 = lib.rl_m_can_drop__VectorTStringT_r_bool
    var436 = (c_bool)()
    var435(byref(var436), byref(self), )
    return var436

wrappers["can_drop"].append(rl_m_can_drop__VectorTStringT_r_bool)
signatures[rl_m_can_drop__VectorTStringT_r_bool] = [builtins.bool, VectorTStringT, ]
@overload
def drop(self: VectorTboolT) -> None:
    pass

def rl_m_drop__VectorTboolT(self: VectorTboolT) -> None:
    var437 = lib.rl_m_drop__VectorTboolT
    var437(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTboolT)
signatures[rl_m_drop__VectorTboolT] = [None, VectorTboolT, ]
@overload
def can_drop(self: VectorTboolT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTboolT_r_bool(self: VectorTboolT) -> builtins.bool:
    var438 = lib.rl_m_can_drop__VectorTboolT_r_bool
    var439 = (c_bool)()
    var438(byref(var439), byref(self), )
    return var439

wrappers["can_drop"].append(rl_m_can_drop__VectorTboolT_r_bool)
signatures[rl_m_can_drop__VectorTboolT_r_bool] = [builtins.bool, VectorTboolT, ]
@overload
def drop(self: VectorTalt_GameMarkT) -> None:
    pass

def rl_m_drop__VectorTalt_GameMarkT(self: VectorTalt_GameMarkT) -> None:
    var440 = lib.rl_m_drop__VectorTalt_GameMarkT
    var440(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTalt_GameMarkT)
signatures[rl_m_drop__VectorTalt_GameMarkT] = [None, VectorTalt_GameMarkT, ]
@overload
def can_drop(self: VectorTalt_GameMarkT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTalt_GameMarkT_r_bool(self: VectorTalt_GameMarkT) -> builtins.bool:
    var441 = lib.rl_m_can_drop__VectorTalt_GameMarkT_r_bool
    var442 = (c_bool)()
    var441(byref(var442), byref(self), )
    return var442

wrappers["can_drop"].append(rl_m_can_drop__VectorTalt_GameMarkT_r_bool)
signatures[rl_m_can_drop__VectorTalt_GameMarkT_r_bool] = [builtins.bool, VectorTalt_GameMarkT, ]
@overload
def drop(self: VectorTGameMarkT) -> None:
    pass

def rl_m_drop__VectorTGameMarkT(self: VectorTGameMarkT) -> None:
    var443 = lib.rl_m_drop__VectorTGameMarkT
    var443(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTGameMarkT)
signatures[rl_m_drop__VectorTGameMarkT] = [None, VectorTGameMarkT, ]
@overload
def can_drop(self: VectorTGameMarkT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTGameMarkT_r_bool(self: VectorTGameMarkT) -> builtins.bool:
    var444 = lib.rl_m_can_drop__VectorTGameMarkT_r_bool
    var445 = (c_bool)()
    var444(byref(var445), byref(self), )
    return var445

wrappers["can_drop"].append(rl_m_can_drop__VectorTGameMarkT_r_bool)
signatures[rl_m_can_drop__VectorTGameMarkT_r_bool] = [builtins.bool, VectorTGameMarkT, ]
@overload
def drop(self: VectorTBIntT0T3TT) -> None:
    pass

def rl_m_drop__VectorTBIntT0T3TT(self: VectorTBIntT0T3TT) -> None:
    var446 = lib.rl_m_drop__VectorTBIntT0T3TT
    var446(byref(self), )
    return

wrappers["drop"].append(rl_m_drop__VectorTBIntT0T3TT)
signatures[rl_m_drop__VectorTBIntT0T3TT] = [None, VectorTBIntT0T3TT, ]
@overload
def can_drop(self: VectorTBIntT0T3TT) -> builtins.bool:
    pass

def rl_m_can_drop__VectorTBIntT0T3TT_r_bool(self: VectorTBIntT0T3TT) -> builtins.bool:
    var447 = lib.rl_m_can_drop__VectorTBIntT0T3TT_r_bool
    var448 = (c_bool)()
    var447(byref(var448), byref(self), )
    return var448

wrappers["can_drop"].append(rl_m_can_drop__VectorTBIntT0T3TT_r_bool)
signatures[rl_m_can_drop__VectorTBIntT0T3TT_r_bool] = [builtins.bool, VectorTBIntT0T3TT, ]
@overload
def init(self: VectorTint8_tT) -> None:
    pass

def rl_m_init__VectorTint8_tT(self: VectorTint8_tT) -> None:
    var449 = lib.rl_m_init__VectorTint8_tT
    var449(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTint8_tT)
signatures[rl_m_init__VectorTint8_tT] = [None, VectorTint8_tT, ]
@overload
def can_init(self: VectorTint8_tT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTint8_tT_r_bool(self: VectorTint8_tT) -> builtins.bool:
    var450 = lib.rl_m_can_init__VectorTint8_tT_r_bool
    var451 = (c_bool)()
    var450(byref(var451), byref(self), )
    return var451

wrappers["can_init"].append(rl_m_can_init__VectorTint8_tT_r_bool)
signatures[rl_m_can_init__VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, ]
@overload
def init(self: VectorTdoubleT) -> None:
    pass

def rl_m_init__VectorTdoubleT(self: VectorTdoubleT) -> None:
    var452 = lib.rl_m_init__VectorTdoubleT
    var452(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTdoubleT)
signatures[rl_m_init__VectorTdoubleT] = [None, VectorTdoubleT, ]
@overload
def can_init(self: VectorTdoubleT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTdoubleT_r_bool(self: VectorTdoubleT) -> builtins.bool:
    var453 = lib.rl_m_can_init__VectorTdoubleT_r_bool
    var454 = (c_bool)()
    var453(byref(var454), byref(self), )
    return var454

wrappers["can_init"].append(rl_m_can_init__VectorTdoubleT_r_bool)
signatures[rl_m_can_init__VectorTdoubleT_r_bool] = [builtins.bool, VectorTdoubleT, ]
@overload
def init(self: VectorTStringT) -> None:
    pass

def rl_m_init__VectorTStringT(self: VectorTStringT) -> None:
    var455 = lib.rl_m_init__VectorTStringT
    var455(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTStringT)
signatures[rl_m_init__VectorTStringT] = [None, VectorTStringT, ]
@overload
def can_init(self: VectorTStringT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTStringT_r_bool(self: VectorTStringT) -> builtins.bool:
    var456 = lib.rl_m_can_init__VectorTStringT_r_bool
    var457 = (c_bool)()
    var456(byref(var457), byref(self), )
    return var457

wrappers["can_init"].append(rl_m_can_init__VectorTStringT_r_bool)
signatures[rl_m_can_init__VectorTStringT_r_bool] = [builtins.bool, VectorTStringT, ]
@overload
def init(self: VectorTboolT) -> None:
    pass

def rl_m_init__VectorTboolT(self: VectorTboolT) -> None:
    var458 = lib.rl_m_init__VectorTboolT
    var458(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTboolT)
signatures[rl_m_init__VectorTboolT] = [None, VectorTboolT, ]
@overload
def can_init(self: VectorTboolT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTboolT_r_bool(self: VectorTboolT) -> builtins.bool:
    var459 = lib.rl_m_can_init__VectorTboolT_r_bool
    var460 = (c_bool)()
    var459(byref(var460), byref(self), )
    return var460

wrappers["can_init"].append(rl_m_can_init__VectorTboolT_r_bool)
signatures[rl_m_can_init__VectorTboolT_r_bool] = [builtins.bool, VectorTboolT, ]
@overload
def init(self: VectorTalt_GameMarkT) -> None:
    pass

def rl_m_init__VectorTalt_GameMarkT(self: VectorTalt_GameMarkT) -> None:
    var461 = lib.rl_m_init__VectorTalt_GameMarkT
    var461(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTalt_GameMarkT)
signatures[rl_m_init__VectorTalt_GameMarkT] = [None, VectorTalt_GameMarkT, ]
@overload
def can_init(self: VectorTalt_GameMarkT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTalt_GameMarkT_r_bool(self: VectorTalt_GameMarkT) -> builtins.bool:
    var462 = lib.rl_m_can_init__VectorTalt_GameMarkT_r_bool
    var463 = (c_bool)()
    var462(byref(var463), byref(self), )
    return var463

wrappers["can_init"].append(rl_m_can_init__VectorTalt_GameMarkT_r_bool)
signatures[rl_m_can_init__VectorTalt_GameMarkT_r_bool] = [builtins.bool, VectorTalt_GameMarkT, ]
@overload
def init(self: VectorTGameMarkT) -> None:
    pass

def rl_m_init__VectorTGameMarkT(self: VectorTGameMarkT) -> None:
    var464 = lib.rl_m_init__VectorTGameMarkT
    var464(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTGameMarkT)
signatures[rl_m_init__VectorTGameMarkT] = [None, VectorTGameMarkT, ]
@overload
def can_init(self: VectorTGameMarkT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTGameMarkT_r_bool(self: VectorTGameMarkT) -> builtins.bool:
    var465 = lib.rl_m_can_init__VectorTGameMarkT_r_bool
    var466 = (c_bool)()
    var465(byref(var466), byref(self), )
    return var466

wrappers["can_init"].append(rl_m_can_init__VectorTGameMarkT_r_bool)
signatures[rl_m_can_init__VectorTGameMarkT_r_bool] = [builtins.bool, VectorTGameMarkT, ]
@overload
def init(self: VectorTBIntT0T3TT) -> None:
    pass

def rl_m_init__VectorTBIntT0T3TT(self: VectorTBIntT0T3TT) -> None:
    var467 = lib.rl_m_init__VectorTBIntT0T3TT
    var467(byref(self), )
    return

wrappers["init"].append(rl_m_init__VectorTBIntT0T3TT)
signatures[rl_m_init__VectorTBIntT0T3TT] = [None, VectorTBIntT0T3TT, ]
@overload
def can_init(self: VectorTBIntT0T3TT) -> builtins.bool:
    pass

def rl_m_can_init__VectorTBIntT0T3TT_r_bool(self: VectorTBIntT0T3TT) -> builtins.bool:
    var468 = lib.rl_m_can_init__VectorTBIntT0T3TT_r_bool
    var469 = (c_bool)()
    var468(byref(var469), byref(self), )
    return var469

wrappers["can_init"].append(rl_m_can_init__VectorTBIntT0T3TT_r_bool)
signatures[rl_m_can_init__VectorTBIntT0T3TT_r_bool] = [builtins.bool, VectorTBIntT0T3TT, ]
@overload
def _grow(self: VectorTint8_tT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTint8_tT_int64_t(self: VectorTint8_tT, target_size: builtins.int) -> None:
    var470 = lib.rl_m__grow__VectorTint8_tT_int64_t
    var471 = c_longlong(target_size)
    var470(byref(self), byref(var471), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTint8_tT_int64_t)
signatures[rl_m__grow__VectorTint8_tT_int64_t] = [None, VectorTint8_tT, builtins.int, ]
@overload
def can__grow(self: VectorTint8_tT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTint8_tT_int64_t_r_bool(self: VectorTint8_tT, target_size: builtins.int) -> builtins.bool:
    var472 = lib.rl_m_can__grow__VectorTint8_tT_int64_t_r_bool
    var473 = c_longlong(target_size)
    var474 = (c_bool)()
    var472(byref(var474), byref(self), byref(var473), )
    return var474

wrappers["can__grow"].append(rl_m_can__grow__VectorTint8_tT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTint8_tT_int64_t_r_bool] = [builtins.bool, VectorTint8_tT, builtins.int, ]
@overload
def _grow(self: VectorTboolT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTboolT_int64_t(self: VectorTboolT, target_size: builtins.int) -> None:
    var475 = lib.rl_m__grow__VectorTboolT_int64_t
    var476 = c_longlong(target_size)
    var475(byref(self), byref(var476), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTboolT_int64_t)
signatures[rl_m__grow__VectorTboolT_int64_t] = [None, VectorTboolT, builtins.int, ]
@overload
def can__grow(self: VectorTboolT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTboolT_int64_t_r_bool(self: VectorTboolT, target_size: builtins.int) -> builtins.bool:
    var477 = lib.rl_m_can__grow__VectorTboolT_int64_t_r_bool
    var478 = c_longlong(target_size)
    var479 = (c_bool)()
    var477(byref(var479), byref(self), byref(var478), )
    return var479

wrappers["can__grow"].append(rl_m_can__grow__VectorTboolT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTboolT_int64_t_r_bool] = [builtins.bool, VectorTboolT, builtins.int, ]
@overload
def _grow(self: VectorTStringT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTStringT_int64_t(self: VectorTStringT, target_size: builtins.int) -> None:
    var480 = lib.rl_m__grow__VectorTStringT_int64_t
    var481 = c_longlong(target_size)
    var480(byref(self), byref(var481), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTStringT_int64_t)
signatures[rl_m__grow__VectorTStringT_int64_t] = [None, VectorTStringT, builtins.int, ]
@overload
def can__grow(self: VectorTStringT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTStringT_int64_t_r_bool(self: VectorTStringT, target_size: builtins.int) -> builtins.bool:
    var482 = lib.rl_m_can__grow__VectorTStringT_int64_t_r_bool
    var483 = c_longlong(target_size)
    var484 = (c_bool)()
    var482(byref(var484), byref(self), byref(var483), )
    return var484

wrappers["can__grow"].append(rl_m_can__grow__VectorTStringT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTStringT_int64_t_r_bool] = [builtins.bool, VectorTStringT, builtins.int, ]
@overload
def _grow(self: VectorTdoubleT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTdoubleT_int64_t(self: VectorTdoubleT, target_size: builtins.int) -> None:
    var485 = lib.rl_m__grow__VectorTdoubleT_int64_t
    var486 = c_longlong(target_size)
    var485(byref(self), byref(var486), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTdoubleT_int64_t)
signatures[rl_m__grow__VectorTdoubleT_int64_t] = [None, VectorTdoubleT, builtins.int, ]
@overload
def can__grow(self: VectorTdoubleT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTdoubleT_int64_t_r_bool(self: VectorTdoubleT, target_size: builtins.int) -> builtins.bool:
    var487 = lib.rl_m_can__grow__VectorTdoubleT_int64_t_r_bool
    var488 = c_longlong(target_size)
    var489 = (c_bool)()
    var487(byref(var489), byref(self), byref(var488), )
    return var489

wrappers["can__grow"].append(rl_m_can__grow__VectorTdoubleT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTdoubleT_int64_t_r_bool] = [builtins.bool, VectorTdoubleT, builtins.int, ]
@overload
def _grow(self: VectorTalt_GameMarkT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTalt_GameMarkT_int64_t(self: VectorTalt_GameMarkT, target_size: builtins.int) -> None:
    var490 = lib.rl_m__grow__VectorTalt_GameMarkT_int64_t
    var491 = c_longlong(target_size)
    var490(byref(self), byref(var491), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTalt_GameMarkT_int64_t)
signatures[rl_m__grow__VectorTalt_GameMarkT_int64_t] = [None, VectorTalt_GameMarkT, builtins.int, ]
@overload
def can__grow(self: VectorTalt_GameMarkT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTalt_GameMarkT_int64_t_r_bool(self: VectorTalt_GameMarkT, target_size: builtins.int) -> builtins.bool:
    var492 = lib.rl_m_can__grow__VectorTalt_GameMarkT_int64_t_r_bool
    var493 = c_longlong(target_size)
    var494 = (c_bool)()
    var492(byref(var494), byref(self), byref(var493), )
    return var494

wrappers["can__grow"].append(rl_m_can__grow__VectorTalt_GameMarkT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTalt_GameMarkT_int64_t_r_bool] = [builtins.bool, VectorTalt_GameMarkT, builtins.int, ]
@overload
def _grow(self: VectorTGameMarkT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTGameMarkT_int64_t(self: VectorTGameMarkT, target_size: builtins.int) -> None:
    var495 = lib.rl_m__grow__VectorTGameMarkT_int64_t
    var496 = c_longlong(target_size)
    var495(byref(self), byref(var496), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTGameMarkT_int64_t)
signatures[rl_m__grow__VectorTGameMarkT_int64_t] = [None, VectorTGameMarkT, builtins.int, ]
@overload
def can__grow(self: VectorTGameMarkT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTGameMarkT_int64_t_r_bool(self: VectorTGameMarkT, target_size: builtins.int) -> builtins.bool:
    var497 = lib.rl_m_can__grow__VectorTGameMarkT_int64_t_r_bool
    var498 = c_longlong(target_size)
    var499 = (c_bool)()
    var497(byref(var499), byref(self), byref(var498), )
    return var499

wrappers["can__grow"].append(rl_m_can__grow__VectorTGameMarkT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTGameMarkT_int64_t_r_bool] = [builtins.bool, VectorTGameMarkT, builtins.int, ]
@overload
def _grow(self: VectorTBIntT0T3TT, target_size: builtins.int) -> None:
    pass

def rl_m__grow__VectorTBIntT0T3TT_int64_t(self: VectorTBIntT0T3TT, target_size: builtins.int) -> None:
    var500 = lib.rl_m__grow__VectorTBIntT0T3TT_int64_t
    var501 = c_longlong(target_size)
    var500(byref(self), byref(var501), )
    return

wrappers["_grow"].append(rl_m__grow__VectorTBIntT0T3TT_int64_t)
signatures[rl_m__grow__VectorTBIntT0T3TT_int64_t] = [None, VectorTBIntT0T3TT, builtins.int, ]
@overload
def can__grow(self: VectorTBIntT0T3TT, target_size: builtins.int) -> builtins.bool:
    pass

def rl_m_can__grow__VectorTBIntT0T3TT_int64_t_r_bool(self: VectorTBIntT0T3TT, target_size: builtins.int) -> builtins.bool:
    var502 = lib.rl_m_can__grow__VectorTBIntT0T3TT_int64_t_r_bool
    var503 = c_longlong(target_size)
    var504 = (c_bool)()
    var502(byref(var504), byref(self), byref(var503), )
    return var504

wrappers["can__grow"].append(rl_m_can__grow__VectorTBIntT0T3TT_int64_t_r_bool)
signatures[rl_m_can__grow__VectorTBIntT0T3TT_int64_t_r_bool] = [builtins.bool, VectorTBIntT0T3TT, builtins.int, ]
@overload
def to_indented_lines(self: String) -> String:
    pass

def rl_m_to_indented_lines__String_r_String(self: String) -> String:
    var505 = lib.rl_m_to_indented_lines__String_r_String
    var506 = (String)()
    var505(byref(var506), byref(self), )
    return var506

wrappers["to_indented_lines"].append(rl_m_to_indented_lines__String_r_String)
signatures[rl_m_to_indented_lines__String_r_String] = [String, String, ]
@overload
def can_to_indented_lines(self: String) -> builtins.bool:
    pass

def rl_m_can_to_indented_lines__String_r_bool(self: String) -> builtins.bool:
    var507 = lib.rl_m_can_to_indented_lines__String_r_bool
    var508 = (c_bool)()
    var507(byref(var508), byref(self), )
    return var508

wrappers["can_to_indented_lines"].append(rl_m_can_to_indented_lines__String_r_bool)
signatures[rl_m_can_to_indented_lines__String_r_bool] = [builtins.bool, String, ]
@overload
def reverse(self: String) -> None:
    pass

def rl_m_reverse__String(self: String) -> None:
    var509 = lib.rl_m_reverse__String
    var509(byref(self), )
    return

wrappers["reverse"].append(rl_m_reverse__String)
signatures[rl_m_reverse__String] = [None, String, ]
@overload
def can_reverse(self: String) -> builtins.bool:
    pass

def rl_m_can_reverse__String_r_bool(self: String) -> builtins.bool:
    var510 = lib.rl_m_can_reverse__String_r_bool
    var511 = (c_bool)()
    var510(byref(var511), byref(self), )
    return var511

wrappers["can_reverse"].append(rl_m_can_reverse__String_r_bool)
signatures[rl_m_can_reverse__String_r_bool] = [builtins.bool, String, ]
@overload
def back(self: String) -> POINTER(c_byte):
    pass

def rl_m_back__String_r_int8_tRef(self: String) -> POINTER(c_byte):
    var512 = lib.rl_m_back__String_r_int8_tRef
    var513 = (POINTER(c_byte))()
    var512(byref(var513), byref(self), )
    return var513

wrappers["back"].append(rl_m_back__String_r_int8_tRef)
signatures[rl_m_back__String_r_int8_tRef] = [POINTER(c_byte), String, ]
@overload
def can_back(self: String) -> builtins.bool:
    pass

def rl_m_can_back__String_r_bool(self: String) -> builtins.bool:
    var514 = lib.rl_m_can_back__String_r_bool
    var515 = (c_bool)()
    var514(byref(var515), byref(self), )
    return var515

wrappers["can_back"].append(rl_m_can_back__String_r_bool)
signatures[rl_m_can_back__String_r_bool] = [builtins.bool, String, ]
@overload
def drop_back(self: String, quantity: builtins.int) -> None:
    pass

def rl_m_drop_back__String_int64_t(self: String, quantity: builtins.int) -> None:
    var516 = lib.rl_m_drop_back__String_int64_t
    var517 = c_longlong(quantity)
    var516(byref(self), byref(var517), )
    return

wrappers["drop_back"].append(rl_m_drop_back__String_int64_t)
signatures[rl_m_drop_back__String_int64_t] = [None, String, builtins.int, ]
@overload
def can_drop_back(self: String, quantity: builtins.int) -> builtins.bool:
    pass

def rl_m_can_drop_back__String_int64_t_r_bool(self: String, quantity: builtins.int) -> builtins.bool:
    var518 = lib.rl_m_can_drop_back__String_int64_t_r_bool
    var519 = c_longlong(quantity)
    var520 = (c_bool)()
    var518(byref(var520), byref(self), byref(var519), )
    return var520

wrappers["can_drop_back"].append(rl_m_can_drop_back__String_int64_t_r_bool)
signatures[rl_m_can_drop_back__String_int64_t_r_bool] = [builtins.bool, String, builtins.int, ]
@overload
def not_equal(self: String, other: builtins.str) -> builtins.bool:
    pass

def rl_m_not_equal__String_strlit_r_bool(self: String, other: builtins.str) -> builtins.bool:
    var521 = lib.rl_m_not_equal__String_strlit_r_bool
    var522 = c_char_p(other.encode("utf-8"))
    var523 = (c_bool)()
    var521(byref(var523), byref(self), byref(var522), )
    return var523

wrappers["not_equal"].append(rl_m_not_equal__String_strlit_r_bool)
signatures[rl_m_not_equal__String_strlit_r_bool] = [builtins.bool, String, builtins.str, ]
@overload
def can_not_equal(self: String, other: builtins.str) -> builtins.bool:
    pass

def rl_m_can_not_equal__String_strlit_r_bool(self: String, other: builtins.str) -> builtins.bool:
    var524 = lib.rl_m_can_not_equal__String_strlit_r_bool
    var525 = c_char_p(other.encode("utf-8"))
    var526 = (c_bool)()
    var524(byref(var526), byref(self), byref(var525), )
    return var526

wrappers["can_not_equal"].append(rl_m_can_not_equal__String_strlit_r_bool)
signatures[rl_m_can_not_equal__String_strlit_r_bool] = [builtins.bool, String, builtins.str, ]
@overload
def not_equal(self: String, other: String) -> builtins.bool:
    pass

def rl_m_not_equal__String_String_r_bool(self: String, other: String) -> builtins.bool:
    var527 = lib.rl_m_not_equal__String_String_r_bool
    var528 = (c_bool)()
    var527(byref(var528), byref(self), byref(other), )
    return var528

wrappers["not_equal"].append(rl_m_not_equal__String_String_r_bool)
signatures[rl_m_not_equal__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def can_not_equal(self: String, other: String) -> builtins.bool:
    pass

def rl_m_can_not_equal__String_String_r_bool(self: String, other: String) -> builtins.bool:
    var529 = lib.rl_m_can_not_equal__String_String_r_bool
    var530 = (c_bool)()
    var529(byref(var530), byref(self), byref(other), )
    return var530

wrappers["can_not_equal"].append(rl_m_can_not_equal__String_String_r_bool)
signatures[rl_m_can_not_equal__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def equal(self: String, other: String) -> builtins.bool:
    pass

def rl_m_equal__String_String_r_bool(self: String, other: String) -> builtins.bool:
    var531 = lib.rl_m_equal__String_String_r_bool
    var532 = (c_bool)()
    var531(byref(var532), byref(self), byref(other), )
    return var532

wrappers["equal"].append(rl_m_equal__String_String_r_bool)
signatures[rl_m_equal__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def can_equal(self: String, other: String) -> builtins.bool:
    pass

def rl_m_can_equal__String_String_r_bool(self: String, other: String) -> builtins.bool:
    var533 = lib.rl_m_can_equal__String_String_r_bool
    var534 = (c_bool)()
    var533(byref(var534), byref(self), byref(other), )
    return var534

wrappers["can_equal"].append(rl_m_can_equal__String_String_r_bool)
signatures[rl_m_can_equal__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def equal(self: String, other: builtins.str) -> builtins.bool:
    pass

def rl_m_equal__String_strlit_r_bool(self: String, other: builtins.str) -> builtins.bool:
    var535 = lib.rl_m_equal__String_strlit_r_bool
    var536 = c_char_p(other.encode("utf-8"))
    var537 = (c_bool)()
    var535(byref(var537), byref(self), byref(var536), )
    return var537

wrappers["equal"].append(rl_m_equal__String_strlit_r_bool)
signatures[rl_m_equal__String_strlit_r_bool] = [builtins.bool, String, builtins.str, ]
@overload
def can_equal(self: String, other: builtins.str) -> builtins.bool:
    pass

def rl_m_can_equal__String_strlit_r_bool(self: String, other: builtins.str) -> builtins.bool:
    var538 = lib.rl_m_can_equal__String_strlit_r_bool
    var539 = c_char_p(other.encode("utf-8"))
    var540 = (c_bool)()
    var538(byref(var540), byref(self), byref(var539), )
    return var540

wrappers["can_equal"].append(rl_m_can_equal__String_strlit_r_bool)
signatures[rl_m_can_equal__String_strlit_r_bool] = [builtins.bool, String, builtins.str, ]
@overload
def add(self: String, other: String) -> String:
    pass

def rl_m_add__String_String_r_String(self: String, other: String) -> String:
    var541 = lib.rl_m_add__String_String_r_String
    var542 = (String)()
    var541(byref(var542), byref(self), byref(other), )
    return var542

wrappers["add"].append(rl_m_add__String_String_r_String)
signatures[rl_m_add__String_String_r_String] = [String, String, String, ]
@overload
def can_add(self: String, other: String) -> builtins.bool:
    pass

def rl_m_can_add__String_String_r_bool(self: String, other: String) -> builtins.bool:
    var543 = lib.rl_m_can_add__String_String_r_bool
    var544 = (c_bool)()
    var543(byref(var544), byref(self), byref(other), )
    return var544

wrappers["can_add"].append(rl_m_can_add__String_String_r_bool)
signatures[rl_m_can_add__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def append(self: String, str: String) -> None:
    pass

def rl_m_append__String_String(self: String, str: String) -> None:
    var545 = lib.rl_m_append__String_String
    var545(byref(self), byref(str), )
    return

wrappers["append"].append(rl_m_append__String_String)
signatures[rl_m_append__String_String] = [None, String, String, ]
@overload
def can_append(self: String, str: String) -> builtins.bool:
    pass

def rl_m_can_append__String_String_r_bool(self: String, str: String) -> builtins.bool:
    var546 = lib.rl_m_can_append__String_String_r_bool
    var547 = (c_bool)()
    var546(byref(var547), byref(self), byref(str), )
    return var547

wrappers["can_append"].append(rl_m_can_append__String_String_r_bool)
signatures[rl_m_can_append__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def append(self: String, str: builtins.str) -> None:
    pass

def rl_m_append__String_strlit(self: String, str: builtins.str) -> None:
    var548 = lib.rl_m_append__String_strlit
    var549 = c_char_p(str.encode("utf-8"))
    var548(byref(self), byref(var549), )
    return

wrappers["append"].append(rl_m_append__String_strlit)
signatures[rl_m_append__String_strlit] = [None, String, builtins.str, ]
@overload
def can_append(self: String, str: builtins.str) -> builtins.bool:
    pass

def rl_m_can_append__String_strlit_r_bool(self: String, str: builtins.str) -> builtins.bool:
    var550 = lib.rl_m_can_append__String_strlit_r_bool
    var551 = c_char_p(str.encode("utf-8"))
    var552 = (c_bool)()
    var550(byref(var552), byref(self), byref(var551), )
    return var552

wrappers["can_append"].append(rl_m_can_append__String_strlit_r_bool)
signatures[rl_m_can_append__String_strlit_r_bool] = [builtins.bool, String, builtins.str, ]
@overload
def count(self: String, b: builtins.int) -> builtins.int:
    pass

def rl_m_count__String_int8_t_r_int64_t(self: String, b: builtins.int) -> builtins.int:
    var553 = lib.rl_m_count__String_int8_t_r_int64_t
    var554 = c_byte(b)
    var555 = (c_longlong)()
    var553(byref(var555), byref(self), byref(var554), )
    var556 = var555.value
    return var556

wrappers["count"].append(rl_m_count__String_int8_t_r_int64_t)
signatures[rl_m_count__String_int8_t_r_int64_t] = [builtins.int, String, builtins.int, ]
@overload
def can_count(self: String, b: builtins.int) -> builtins.bool:
    pass

def rl_m_can_count__String_int8_t_r_bool(self: String, b: builtins.int) -> builtins.bool:
    var557 = lib.rl_m_can_count__String_int8_t_r_bool
    var558 = c_byte(b)
    var559 = (c_bool)()
    var557(byref(var559), byref(self), byref(var558), )
    return var559

wrappers["can_count"].append(rl_m_can_count__String_int8_t_r_bool)
signatures[rl_m_can_count__String_int8_t_r_bool] = [builtins.bool, String, builtins.int, ]
@overload
def size(self: String) -> builtins.int:
    pass

def rl_m_size__String_r_int64_t(self: String) -> builtins.int:
    var560 = lib.rl_m_size__String_r_int64_t
    var561 = (c_longlong)()
    var560(byref(var561), byref(self), )
    var562 = var561.value
    return var562

wrappers["size"].append(rl_m_size__String_r_int64_t)
signatures[rl_m_size__String_r_int64_t] = [builtins.int, String, ]
@overload
def can_size(self: String) -> builtins.bool:
    pass

def rl_m_can_size__String_r_bool(self: String) -> builtins.bool:
    var563 = lib.rl_m_can_size__String_r_bool
    var564 = (c_bool)()
    var563(byref(var564), byref(self), )
    return var564

wrappers["can_size"].append(rl_m_can_size__String_r_bool)
signatures[rl_m_can_size__String_r_bool] = [builtins.bool, String, ]
@overload
def substring_matches(self: String, lit: builtins.str, pos: builtins.int) -> builtins.bool:
    pass

def rl_m_substring_matches__String_strlit_int64_t_r_bool(self: String, lit: builtins.str, pos: builtins.int) -> builtins.bool:
    var565 = lib.rl_m_substring_matches__String_strlit_int64_t_r_bool
    var566 = c_char_p(lit.encode("utf-8"))
    var567 = c_longlong(pos)
    var568 = (c_bool)()
    var565(byref(var568), byref(self), byref(var566), byref(var567), )
    return var568

wrappers["substring_matches"].append(rl_m_substring_matches__String_strlit_int64_t_r_bool)
signatures[rl_m_substring_matches__String_strlit_int64_t_r_bool] = [builtins.bool, String, builtins.str, builtins.int, ]
@overload
def can_substring_matches(self: String, lit: builtins.str, pos: builtins.int) -> builtins.bool:
    pass

def rl_m_can_substring_matches__String_strlit_int64_t_r_bool(self: String, lit: builtins.str, pos: builtins.int) -> builtins.bool:
    var569 = lib.rl_m_can_substring_matches__String_strlit_int64_t_r_bool
    var570 = c_char_p(lit.encode("utf-8"))
    var571 = c_longlong(pos)
    var572 = (c_bool)()
    var569(byref(var572), byref(self), byref(var570), byref(var571), )
    return var572

wrappers["can_substring_matches"].append(rl_m_can_substring_matches__String_strlit_int64_t_r_bool)
signatures[rl_m_can_substring_matches__String_strlit_int64_t_r_bool] = [builtins.bool, String, builtins.str, builtins.int, ]
@overload
def get(self: String, index: builtins.int) -> POINTER(c_byte):
    pass

def rl_m_get__String_int64_t_r_int8_tRef(self: String, index: builtins.int) -> POINTER(c_byte):
    var573 = lib.rl_m_get__String_int64_t_r_int8_tRef
    var574 = c_longlong(index)
    var575 = (POINTER(c_byte))()
    var573(byref(var575), byref(self), byref(var574), )
    return var575

wrappers["get"].append(rl_m_get__String_int64_t_r_int8_tRef)
signatures[rl_m_get__String_int64_t_r_int8_tRef] = [POINTER(c_byte), String, builtins.int, ]
@overload
def can_get(self: String, index: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__String_int64_t_r_bool(self: String, index: builtins.int) -> builtins.bool:
    var576 = lib.rl_m_can_get__String_int64_t_r_bool
    var577 = c_longlong(index)
    var578 = (c_bool)()
    var576(byref(var578), byref(self), byref(var577), )
    return var578

wrappers["can_get"].append(rl_m_can_get__String_int64_t_r_bool)
signatures[rl_m_can_get__String_int64_t_r_bool] = [builtins.bool, String, builtins.int, ]
@overload
def append(self: String, b: builtins.int) -> None:
    pass

def rl_m_append__String_int8_t(self: String, b: builtins.int) -> None:
    var579 = lib.rl_m_append__String_int8_t
    var580 = c_byte(b)
    var579(byref(self), byref(var580), )
    return

wrappers["append"].append(rl_m_append__String_int8_t)
signatures[rl_m_append__String_int8_t] = [None, String, builtins.int, ]
@overload
def can_append(self: String, b: builtins.int) -> builtins.bool:
    pass

def rl_m_can_append__String_int8_t_r_bool(self: String, b: builtins.int) -> builtins.bool:
    var581 = lib.rl_m_can_append__String_int8_t_r_bool
    var582 = c_byte(b)
    var583 = (c_bool)()
    var581(byref(var583), byref(self), byref(var582), )
    return var583

wrappers["can_append"].append(rl_m_can_append__String_int8_t_r_bool)
signatures[rl_m_can_append__String_int8_t_r_bool] = [builtins.bool, String, builtins.int, ]
@overload
def init(self: String) -> None:
    pass

def rl_m_init__String(self: String) -> None:
    var584 = lib.rl_m_init__String
    var584(byref(self), )
    return

wrappers["init"].append(rl_m_init__String)
signatures[rl_m_init__String] = [None, String, ]
@overload
def can_init(self: String) -> builtins.bool:
    pass

def rl_m_can_init__String_r_bool(self: String) -> builtins.bool:
    var585 = lib.rl_m_can_init__String_r_bool
    var586 = (c_bool)()
    var585(byref(var586), byref(self), )
    return var586

wrappers["can_init"].append(rl_m_can_init__String_r_bool)
signatures[rl_m_can_init__String_r_bool] = [builtins.bool, String, ]
@overload
def _indent_string(output: String, count: builtins.int) -> None:
    pass

def rl__indent_string__String_int64_t(output: String, count: builtins.int) -> None:
    var587 = lib.rl__indent_string__String_int64_t
    var588 = c_longlong(count)
    var587(byref(output), byref(var588), )
    return

wrappers["_indent_string"].append(rl__indent_string__String_int64_t)
signatures[rl__indent_string__String_int64_t] = [None, String, builtins.int, ]
@overload
def can__indent_string(output: String, count: builtins.int) -> builtins.bool:
    pass

def rl_can__indent_string__String_int64_t_r_bool(output: String, count: builtins.int) -> builtins.bool:
    var589 = lib.rl_can__indent_string__String_int64_t_r_bool
    var590 = c_longlong(count)
    var591 = (c_bool)()
    var589(byref(var591), byref(output), byref(var590), )
    return var591

wrappers["can__indent_string"].append(rl_can__indent_string__String_int64_t_r_bool)
signatures[rl_can__indent_string__String_int64_t_r_bool] = [builtins.bool, String, builtins.int, ]
@overload
def s(literal: builtins.str) -> String:
    pass

def rl_s__strlit_r_String(literal: builtins.str) -> String:
    var592 = lib.rl_s__strlit_r_String
    var593 = c_char_p(literal.encode("utf-8"))
    var594 = (String)()
    var592(byref(var594), byref(var593), )
    return var594

wrappers["s"].append(rl_s__strlit_r_String)
signatures[rl_s__strlit_r_String] = [String, builtins.str, ]
@overload
def can_s(literal: builtins.str) -> builtins.bool:
    pass

def rl_can_s__strlit_r_bool(literal: builtins.str) -> builtins.bool:
    var595 = lib.rl_can_s__strlit_r_bool
    var596 = c_char_p(literal.encode("utf-8"))
    var597 = (c_bool)()
    var595(byref(var597), byref(var596), )
    return var597

wrappers["can_s"].append(rl_can_s__strlit_r_bool)
signatures[rl_can_s__strlit_r_bool] = [builtins.bool, builtins.str, ]
@overload
def append_to_string(x: builtins.str, output: String) -> None:
    pass

def rl_append_to_string__strlit_String(x: builtins.str, output: String) -> None:
    var598 = lib.rl_append_to_string__strlit_String
    var599 = c_char_p(x.encode("utf-8"))
    var598(byref(var599), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__strlit_String)
signatures[rl_append_to_string__strlit_String] = [None, builtins.str, String, ]
@overload
def can_append_to_string(x: builtins.str, output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__strlit_String_r_bool(x: builtins.str, output: String) -> builtins.bool:
    var600 = lib.rl_can_append_to_string__strlit_String_r_bool
    var601 = c_char_p(x.encode("utf-8"))
    var602 = (c_bool)()
    var600(byref(var602), byref(var601), byref(output), )
    return var602

wrappers["can_append_to_string"].append(rl_can_append_to_string__strlit_String_r_bool)
signatures[rl_can_append_to_string__strlit_String_r_bool] = [builtins.bool, builtins.str, String, ]
@overload
def load_file(file_name: String, out: String) -> builtins.bool:
    pass

def rl_load_file__String_String_r_bool(file_name: String, out: String) -> builtins.bool:
    var603 = lib.rl_load_file__String_String_r_bool
    var604 = (c_bool)()
    var603(byref(var604), byref(file_name), byref(out), )
    return var604

wrappers["load_file"].append(rl_load_file__String_String_r_bool)
signatures[rl_load_file__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def can_load_file(file_name: String, out: String) -> builtins.bool:
    pass

def rl_can_load_file__String_String_r_bool(file_name: String, out: String) -> builtins.bool:
    var605 = lib.rl_can_load_file__String_String_r_bool
    var606 = (c_bool)()
    var605(byref(var606), byref(file_name), byref(out), )
    return var606

wrappers["can_load_file"].append(rl_can_load_file__String_String_r_bool)
signatures[rl_can_load_file__String_String_r_bool] = [builtins.bool, String, String, ]
@overload
def append_to_string(x: builtins.int, output: String) -> None:
    pass

def rl_append_to_string__int64_t_String(x: builtins.int, output: String) -> None:
    var607 = lib.rl_append_to_string__int64_t_String
    var608 = c_longlong(x)
    var607(byref(var608), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__int64_t_String)
signatures[rl_append_to_string__int64_t_String] = [None, builtins.int, String, ]
@overload
def can_append_to_string(x: builtins.int, output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__int64_t_String_r_bool(x: builtins.int, output: String) -> builtins.bool:
    var609 = lib.rl_can_append_to_string__int64_t_String_r_bool
    var610 = c_longlong(x)
    var611 = (c_bool)()
    var609(byref(var611), byref(var610), byref(output), )
    return var611

wrappers["can_append_to_string"].append(rl_can_append_to_string__int64_t_String_r_bool)
signatures[rl_can_append_to_string__int64_t_String_r_bool] = [builtins.bool, builtins.int, String, ]
@overload
def append_to_string(x: builtins.int, output: String) -> None:
    pass

def rl_append_to_string__int8_t_String(x: builtins.int, output: String) -> None:
    var612 = lib.rl_append_to_string__int8_t_String
    var613 = c_byte(x)
    var612(byref(var613), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__int8_t_String)
signatures[rl_append_to_string__int8_t_String] = [None, builtins.int, String, ]
@overload
def can_append_to_string(x: builtins.int, output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__int8_t_String_r_bool(x: builtins.int, output: String) -> builtins.bool:
    var614 = lib.rl_can_append_to_string__int8_t_String_r_bool
    var615 = c_byte(x)
    var616 = (c_bool)()
    var614(byref(var616), byref(var615), byref(output), )
    return var616

wrappers["can_append_to_string"].append(rl_can_append_to_string__int8_t_String_r_bool)
signatures[rl_can_append_to_string__int8_t_String_r_bool] = [builtins.bool, builtins.int, String, ]
@overload
def append_to_string(x: builtins.float, output: String) -> None:
    pass

def rl_append_to_string__double_String(x: builtins.float, output: String) -> None:
    var617 = lib.rl_append_to_string__double_String
    var618 = c_double(x)
    var617(byref(var618), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__double_String)
signatures[rl_append_to_string__double_String] = [None, builtins.float, String, ]
@overload
def can_append_to_string(x: builtins.float, output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__double_String_r_bool(x: builtins.float, output: String) -> builtins.bool:
    var619 = lib.rl_can_append_to_string__double_String_r_bool
    var620 = c_double(x)
    var621 = (c_bool)()
    var619(byref(var621), byref(var620), byref(output), )
    return var621

wrappers["can_append_to_string"].append(rl_can_append_to_string__double_String_r_bool)
signatures[rl_can_append_to_string__double_String_r_bool] = [builtins.bool, builtins.float, String, ]
@overload
def append_to_string(x: builtins.bool, output: String) -> None:
    pass

def rl_append_to_string__bool_String(x: builtins.bool, output: String) -> None:
    var622 = lib.rl_append_to_string__bool_String
    var623 = c_bool(x)
    var622(byref(var623), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__bool_String)
signatures[rl_append_to_string__bool_String] = [None, builtins.bool, String, ]
@overload
def can_append_to_string(x: builtins.bool, output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__bool_String_r_bool(x: builtins.bool, output: String) -> builtins.bool:
    var624 = lib.rl_can_append_to_string__bool_String_r_bool
    var625 = c_bool(x)
    var626 = (c_bool)()
    var624(byref(var626), byref(var625), byref(output), )
    return var626

wrappers["can_append_to_string"].append(rl_can_append_to_string__bool_String_r_bool)
signatures[rl_can_append_to_string__bool_String_r_bool] = [builtins.bool, builtins.bool, String, ]
@overload
def append_to_string(to_add:  list , output: String) -> None:
    pass

def rl_append_to_string__BIntT0T3T_9_String(to_add:  list , output: String) -> None:
    var627 = lib.rl_append_to_string__BIntT0T3T_9_String
    var627(byref(to_add), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__BIntT0T3T_9_String)
signatures[rl_append_to_string__BIntT0T3T_9_String] = [None,  list , String, ]
@overload
def can_append_to_string(to_add:  list , output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__BIntT0T3T_9_String_r_bool(to_add:  list , output: String) -> builtins.bool:
    var628 = lib.rl_can_append_to_string__BIntT0T3T_9_String_r_bool
    var629 = (c_bool)()
    var628(byref(var629), byref(to_add), byref(output), )
    return var629

wrappers["can_append_to_string"].append(rl_can_append_to_string__BIntT0T3T_9_String_r_bool)
signatures[rl_can_append_to_string__BIntT0T3T_9_String_r_bool] = [builtins.bool,  list , String, ]
@overload
def _print_type(to_add: GameMark, default_type_name: builtins.str, output: String) -> None:
    pass

def rl__print_type__GameMark_strlit_String(to_add: GameMark, default_type_name: builtins.str, output: String) -> None:
    var630 = lib.rl__print_type__GameMark_strlit_String
    var631 = c_char_p(default_type_name.encode("utf-8"))
    var630(byref(to_add), byref(var631), byref(output), )
    return

wrappers["_print_type"].append(rl__print_type__GameMark_strlit_String)
signatures[rl__print_type__GameMark_strlit_String] = [None, GameMark, builtins.str, String, ]
@overload
def can__print_type(to_add: GameMark, default_type_name: builtins.str, output: String) -> builtins.bool:
    pass

def rl_can__print_type__GameMark_strlit_String_r_bool(to_add: GameMark, default_type_name: builtins.str, output: String) -> builtins.bool:
    var632 = lib.rl_can__print_type__GameMark_strlit_String_r_bool
    var633 = c_char_p(default_type_name.encode("utf-8"))
    var634 = (c_bool)()
    var632(byref(var634), byref(to_add), byref(var633), byref(output), )
    return var634

wrappers["can__print_type"].append(rl_can__print_type__GameMark_strlit_String_r_bool)
signatures[rl_can__print_type__GameMark_strlit_String_r_bool] = [builtins.bool, GameMark, builtins.str, String, ]
@overload
def _to_string_impl(to_add: builtins.str, output: String) -> None:
    pass

def rl__to_string_impl__strlit_String(to_add: builtins.str, output: String) -> None:
    var635 = lib.rl__to_string_impl__strlit_String
    var636 = c_char_p(to_add.encode("utf-8"))
    var635(byref(var636), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__strlit_String)
signatures[rl__to_string_impl__strlit_String] = [None, builtins.str, String, ]
@overload
def can__to_string_impl(to_add: builtins.str, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__strlit_String_r_bool(to_add: builtins.str, output: String) -> builtins.bool:
    var637 = lib.rl_can__to_string_impl__strlit_String_r_bool
    var638 = c_char_p(to_add.encode("utf-8"))
    var639 = (c_bool)()
    var637(byref(var639), byref(var638), byref(output), )
    return var639

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__strlit_String_r_bool)
signatures[rl_can__to_string_impl__strlit_String_r_bool] = [builtins.bool, builtins.str, String, ]
@overload
def _to_string_impl(to_add: builtins.int, output: String) -> None:
    pass

def rl__to_string_impl__int64_t_String(to_add: builtins.int, output: String) -> None:
    var640 = lib.rl__to_string_impl__int64_t_String
    var641 = c_longlong(to_add)
    var640(byref(var641), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__int64_t_String)
signatures[rl__to_string_impl__int64_t_String] = [None, builtins.int, String, ]
@overload
def can__to_string_impl(to_add: builtins.int, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__int64_t_String_r_bool(to_add: builtins.int, output: String) -> builtins.bool:
    var642 = lib.rl_can__to_string_impl__int64_t_String_r_bool
    var643 = c_longlong(to_add)
    var644 = (c_bool)()
    var642(byref(var644), byref(var643), byref(output), )
    return var644

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__int64_t_String_r_bool)
signatures[rl_can__to_string_impl__int64_t_String_r_bool] = [builtins.bool, builtins.int, String, ]
@overload
def _to_string_impl(to_add: builtins.bool, output: String) -> None:
    pass

def rl__to_string_impl__bool_String(to_add: builtins.bool, output: String) -> None:
    var645 = lib.rl__to_string_impl__bool_String
    var646 = c_bool(to_add)
    var645(byref(var646), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__bool_String)
signatures[rl__to_string_impl__bool_String] = [None, builtins.bool, String, ]
@overload
def can__to_string_impl(to_add: builtins.bool, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__bool_String_r_bool(to_add: builtins.bool, output: String) -> builtins.bool:
    var647 = lib.rl_can__to_string_impl__bool_String_r_bool
    var648 = c_bool(to_add)
    var649 = (c_bool)()
    var647(byref(var649), byref(var648), byref(output), )
    return var649

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__bool_String_r_bool)
signatures[rl_can__to_string_impl__bool_String_r_bool] = [builtins.bool, builtins.bool, String, ]
@overload
def _to_string_impl(to_add: Game, output: String) -> None:
    pass

def rl__to_string_impl__Game_String(to_add: Game, output: String) -> None:
    var650 = lib.rl__to_string_impl__Game_String
    var650(byref(to_add), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__Game_String)
signatures[rl__to_string_impl__Game_String] = [None, Game, String, ]
@overload
def can__to_string_impl(to_add: Game, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__Game_String_r_bool(to_add: Game, output: String) -> builtins.bool:
    var651 = lib.rl_can__to_string_impl__Game_String_r_bool
    var652 = (c_bool)()
    var651(byref(var652), byref(to_add), byref(output), )
    return var652

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__Game_String_r_bool)
signatures[rl_can__to_string_impl__Game_String_r_bool] = [builtins.bool, Game, String, ]
@overload
def _to_string_impl(to_add: GameMarkOr, output: String) -> None:
    pass

def rl__to_string_impl__alt_GameMark_String(to_add: GameMarkOr, output: String) -> None:
    var653 = lib.rl__to_string_impl__alt_GameMark_String
    var653(byref(to_add), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__alt_GameMark_String)
signatures[rl__to_string_impl__alt_GameMark_String] = [None, GameMarkOr, String, ]
@overload
def can__to_string_impl(to_add: GameMarkOr, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__alt_GameMark_String_r_bool(to_add: GameMarkOr, output: String) -> builtins.bool:
    var654 = lib.rl_can__to_string_impl__alt_GameMark_String_r_bool
    var655 = (c_bool)()
    var654(byref(var655), byref(to_add), byref(output), )
    return var655

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__alt_GameMark_String_r_bool)
signatures[rl_can__to_string_impl__alt_GameMark_String_r_bool] = [builtins.bool, GameMarkOr, String, ]
@overload
def _to_string_impl(to_add: Board, output: String) -> None:
    pass

def rl__to_string_impl__Board_String(to_add: Board, output: String) -> None:
    var656 = lib.rl__to_string_impl__Board_String
    var656(byref(to_add), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__Board_String)
signatures[rl__to_string_impl__Board_String] = [None, Board, String, ]
@overload
def can__to_string_impl(to_add: Board, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__Board_String_r_bool(to_add: Board, output: String) -> builtins.bool:
    var657 = lib.rl_can__to_string_impl__Board_String_r_bool
    var658 = (c_bool)()
    var657(byref(var658), byref(to_add), byref(output), )
    return var658

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__Board_String_r_bool)
signatures[rl_can__to_string_impl__Board_String_r_bool] = [builtins.bool, Board, String, ]
@overload
def _to_string_impl(to_add: GameMark, output: String) -> None:
    pass

def rl__to_string_impl__GameMark_String(to_add: GameMark, output: String) -> None:
    var659 = lib.rl__to_string_impl__GameMark_String
    var659(byref(to_add), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__GameMark_String)
signatures[rl__to_string_impl__GameMark_String] = [None, GameMark, String, ]
@overload
def can__to_string_impl(to_add: GameMark, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__GameMark_String_r_bool(to_add: GameMark, output: String) -> builtins.bool:
    var660 = lib.rl_can__to_string_impl__GameMark_String_r_bool
    var661 = (c_bool)()
    var660(byref(var661), byref(to_add), byref(output), )
    return var661

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__GameMark_String_r_bool)
signatures[rl_can__to_string_impl__GameMark_String_r_bool] = [builtins.bool, GameMark, String, ]
@overload
def _to_string_impl(to_add:  list , output: String) -> None:
    pass

def rl__to_string_impl__BIntT0T3T_9_String(to_add:  list , output: String) -> None:
    var662 = lib.rl__to_string_impl__BIntT0T3T_9_String
    var662(byref(to_add), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__BIntT0T3T_9_String)
signatures[rl__to_string_impl__BIntT0T3T_9_String] = [None,  list , String, ]
@overload
def can__to_string_impl(to_add:  list , output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__BIntT0T3T_9_String_r_bool(to_add:  list , output: String) -> builtins.bool:
    var663 = lib.rl_can__to_string_impl__BIntT0T3T_9_String_r_bool
    var664 = (c_bool)()
    var663(byref(var664), byref(to_add), byref(output), )
    return var664

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__BIntT0T3T_9_String_r_bool)
signatures[rl_can__to_string_impl__BIntT0T3T_9_String_r_bool] = [builtins.bool,  list , String, ]
@overload
def _to_string_impl(to_add: BIntT0T3T, output: String) -> None:
    pass

def rl__to_string_impl__BIntT0T3T_String(to_add: BIntT0T3T, output: String) -> None:
    var665 = lib.rl__to_string_impl__BIntT0T3T_String
    var665(byref(to_add), byref(output), )
    return

wrappers["_to_string_impl"].append(rl__to_string_impl__BIntT0T3T_String)
signatures[rl__to_string_impl__BIntT0T3T_String] = [None, BIntT0T3T, String, ]
@overload
def can__to_string_impl(to_add: BIntT0T3T, output: String) -> builtins.bool:
    pass

def rl_can__to_string_impl__BIntT0T3T_String_r_bool(to_add: BIntT0T3T, output: String) -> builtins.bool:
    var666 = lib.rl_can__to_string_impl__BIntT0T3T_String_r_bool
    var667 = (c_bool)()
    var666(byref(var667), byref(to_add), byref(output), )
    return var667

wrappers["can__to_string_impl"].append(rl_can__to_string_impl__BIntT0T3T_String_r_bool)
signatures[rl_can__to_string_impl__BIntT0T3T_String_r_bool] = [builtins.bool, BIntT0T3T, String, ]
@overload
def to_string(to_stringyfi: builtins.int) -> String:
    pass

def rl_to_string__int64_t_r_String(to_stringyfi: builtins.int) -> String:
    var668 = lib.rl_to_string__int64_t_r_String
    var669 = c_longlong(to_stringyfi)
    var670 = (String)()
    var668(byref(var670), byref(var669), )
    return var670

wrappers["to_string"].append(rl_to_string__int64_t_r_String)
signatures[rl_to_string__int64_t_r_String] = [String, builtins.int, ]
@overload
def can_to_string(to_stringyfi: builtins.int) -> builtins.bool:
    pass

def rl_can_to_string__int64_t_r_bool(to_stringyfi: builtins.int) -> builtins.bool:
    var671 = lib.rl_can_to_string__int64_t_r_bool
    var672 = c_longlong(to_stringyfi)
    var673 = (c_bool)()
    var671(byref(var673), byref(var672), )
    return var673

wrappers["can_to_string"].append(rl_can_to_string__int64_t_r_bool)
signatures[rl_can_to_string__int64_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def to_string(to_stringyfi: builtins.bool) -> String:
    pass

def rl_to_string__bool_r_String(to_stringyfi: builtins.bool) -> String:
    var674 = lib.rl_to_string__bool_r_String
    var675 = c_bool(to_stringyfi)
    var676 = (String)()
    var674(byref(var676), byref(var675), )
    return var676

wrappers["to_string"].append(rl_to_string__bool_r_String)
signatures[rl_to_string__bool_r_String] = [String, builtins.bool, ]
@overload
def can_to_string(to_stringyfi: builtins.bool) -> builtins.bool:
    pass

def rl_can_to_string__bool_r_bool(to_stringyfi: builtins.bool) -> builtins.bool:
    var677 = lib.rl_can_to_string__bool_r_bool
    var678 = c_bool(to_stringyfi)
    var679 = (c_bool)()
    var677(byref(var679), byref(var678), )
    return var679

wrappers["can_to_string"].append(rl_can_to_string__bool_r_bool)
signatures[rl_can_to_string__bool_r_bool] = [builtins.bool, builtins.bool, ]
@overload
def to_string(to_stringyfi: Game) -> String:
    pass

def rl_to_string__Game_r_String(to_stringyfi: Game) -> String:
    var680 = lib.rl_to_string__Game_r_String
    var681 = (String)()
    var680(byref(var681), byref(to_stringyfi), )
    return var681

wrappers["to_string"].append(rl_to_string__Game_r_String)
signatures[rl_to_string__Game_r_String] = [String, Game, ]
@overload
def can_to_string(to_stringyfi: Game) -> builtins.bool:
    pass

def rl_can_to_string__Game_r_bool(to_stringyfi: Game) -> builtins.bool:
    var682 = lib.rl_can_to_string__Game_r_bool
    var683 = (c_bool)()
    var682(byref(var683), byref(to_stringyfi), )
    return var683

wrappers["can_to_string"].append(rl_can_to_string__Game_r_bool)
signatures[rl_can_to_string__Game_r_bool] = [builtins.bool, Game, ]
@overload
def to_string(to_stringyfi: GameMarkOr) -> String:
    pass

def rl_to_string__alt_GameMark_r_String(to_stringyfi: GameMarkOr) -> String:
    var684 = lib.rl_to_string__alt_GameMark_r_String
    var685 = (String)()
    var684(byref(var685), byref(to_stringyfi), )
    return var685

wrappers["to_string"].append(rl_to_string__alt_GameMark_r_String)
signatures[rl_to_string__alt_GameMark_r_String] = [String, GameMarkOr, ]
@overload
def can_to_string(to_stringyfi: GameMarkOr) -> builtins.bool:
    pass

def rl_can_to_string__alt_GameMark_r_bool(to_stringyfi: GameMarkOr) -> builtins.bool:
    var686 = lib.rl_can_to_string__alt_GameMark_r_bool
    var687 = (c_bool)()
    var686(byref(var687), byref(to_stringyfi), )
    return var687

wrappers["can_to_string"].append(rl_can_to_string__alt_GameMark_r_bool)
signatures[rl_can_to_string__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def is_space(b: builtins.int) -> builtins.bool:
    pass

def rl_is_space__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var688 = lib.rl_is_space__int8_t_r_bool
    var689 = c_byte(b)
    var690 = (c_bool)()
    var688(byref(var690), byref(var689), )
    return var690

wrappers["is_space"].append(rl_is_space__int8_t_r_bool)
signatures[rl_is_space__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def can_is_space(b: builtins.int) -> builtins.bool:
    pass

def rl_can_is_space__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var691 = lib.rl_can_is_space__int8_t_r_bool
    var692 = c_byte(b)
    var693 = (c_bool)()
    var691(byref(var693), byref(var692), )
    return var693

wrappers["can_is_space"].append(rl_can_is_space__int8_t_r_bool)
signatures[rl_can_is_space__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def is_alphanumeric(b: builtins.int) -> builtins.bool:
    pass

def rl_is_alphanumeric__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var694 = lib.rl_is_alphanumeric__int8_t_r_bool
    var695 = c_byte(b)
    var696 = (c_bool)()
    var694(byref(var696), byref(var695), )
    return var696

wrappers["is_alphanumeric"].append(rl_is_alphanumeric__int8_t_r_bool)
signatures[rl_is_alphanumeric__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def can_is_alphanumeric(b: builtins.int) -> builtins.bool:
    pass

def rl_can_is_alphanumeric__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var697 = lib.rl_can_is_alphanumeric__int8_t_r_bool
    var698 = c_byte(b)
    var699 = (c_bool)()
    var697(byref(var699), byref(var698), )
    return var699

wrappers["can_is_alphanumeric"].append(rl_can_is_alphanumeric__int8_t_r_bool)
signatures[rl_can_is_alphanumeric__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def is_open_paren(b: builtins.int) -> builtins.bool:
    pass

def rl_is_open_paren__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var700 = lib.rl_is_open_paren__int8_t_r_bool
    var701 = c_byte(b)
    var702 = (c_bool)()
    var700(byref(var702), byref(var701), )
    return var702

wrappers["is_open_paren"].append(rl_is_open_paren__int8_t_r_bool)
signatures[rl_is_open_paren__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def can_is_open_paren(b: builtins.int) -> builtins.bool:
    pass

def rl_can_is_open_paren__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var703 = lib.rl_can_is_open_paren__int8_t_r_bool
    var704 = c_byte(b)
    var705 = (c_bool)()
    var703(byref(var705), byref(var704), )
    return var705

wrappers["can_is_open_paren"].append(rl_can_is_open_paren__int8_t_r_bool)
signatures[rl_can_is_open_paren__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def is_close_paren(b: builtins.int) -> builtins.bool:
    pass

def rl_is_close_paren__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var706 = lib.rl_is_close_paren__int8_t_r_bool
    var707 = c_byte(b)
    var708 = (c_bool)()
    var706(byref(var708), byref(var707), )
    return var708

wrappers["is_close_paren"].append(rl_is_close_paren__int8_t_r_bool)
signatures[rl_is_close_paren__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def can_is_close_paren(b: builtins.int) -> builtins.bool:
    pass

def rl_can_is_close_paren__int8_t_r_bool(b: builtins.int) -> builtins.bool:
    var709 = lib.rl_can_is_close_paren__int8_t_r_bool
    var710 = c_byte(b)
    var711 = (c_bool)()
    var709(byref(var711), byref(var710), )
    return var711

wrappers["can_is_close_paren"].append(rl_can_is_close_paren__int8_t_r_bool)
signatures[rl_can_is_close_paren__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def parse_string(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_string__int64_t_String_int64_t_r_bool(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    var712 = lib.rl_parse_string__int64_t_String_int64_t_r_bool
    var713 = c_longlong(result)
    var714 = c_longlong(index)
    var715 = (c_bool)()
    var712(byref(var715), byref(var713), byref(buffer), byref(var714), )
    return var715

wrappers["parse_string"].append(rl_parse_string__int64_t_String_int64_t_r_bool)
signatures[rl_parse_string__int64_t_String_int64_t_r_bool] = [builtins.bool, builtins.int, String, builtins.int, ]
@overload
def can_parse_string(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_string__int64_t_String_int64_t_r_bool(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    var716 = lib.rl_can_parse_string__int64_t_String_int64_t_r_bool
    var717 = c_longlong(result)
    var718 = c_longlong(index)
    var719 = (c_bool)()
    var716(byref(var719), byref(var717), byref(buffer), byref(var718), )
    return var719

wrappers["can_parse_string"].append(rl_can_parse_string__int64_t_String_int64_t_r_bool)
signatures[rl_can_parse_string__int64_t_String_int64_t_r_bool] = [builtins.bool, builtins.int, String, builtins.int, ]
@overload
def parse_string(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_string__int8_t_String_int64_t_r_bool(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    var720 = lib.rl_parse_string__int8_t_String_int64_t_r_bool
    var721 = c_byte(result)
    var722 = c_longlong(index)
    var723 = (c_bool)()
    var720(byref(var723), byref(var721), byref(buffer), byref(var722), )
    return var723

wrappers["parse_string"].append(rl_parse_string__int8_t_String_int64_t_r_bool)
signatures[rl_parse_string__int8_t_String_int64_t_r_bool] = [builtins.bool, builtins.int, String, builtins.int, ]
@overload
def can_parse_string(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_string__int8_t_String_int64_t_r_bool(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    var724 = lib.rl_can_parse_string__int8_t_String_int64_t_r_bool
    var725 = c_byte(result)
    var726 = c_longlong(index)
    var727 = (c_bool)()
    var724(byref(var727), byref(var725), byref(buffer), byref(var726), )
    return var727

wrappers["can_parse_string"].append(rl_can_parse_string__int8_t_String_int64_t_r_bool)
signatures[rl_can_parse_string__int8_t_String_int64_t_r_bool] = [builtins.bool, builtins.int, String, builtins.int, ]
@overload
def parse_string(result: builtins.float, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_string__double_String_int64_t_r_bool(result: builtins.float, buffer: String, index: builtins.int) -> builtins.bool:
    var728 = lib.rl_parse_string__double_String_int64_t_r_bool
    var729 = c_double(result)
    var730 = c_longlong(index)
    var731 = (c_bool)()
    var728(byref(var731), byref(var729), byref(buffer), byref(var730), )
    return var731

wrappers["parse_string"].append(rl_parse_string__double_String_int64_t_r_bool)
signatures[rl_parse_string__double_String_int64_t_r_bool] = [builtins.bool, builtins.float, String, builtins.int, ]
@overload
def can_parse_string(result: builtins.float, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_string__double_String_int64_t_r_bool(result: builtins.float, buffer: String, index: builtins.int) -> builtins.bool:
    var732 = lib.rl_can_parse_string__double_String_int64_t_r_bool
    var733 = c_double(result)
    var734 = c_longlong(index)
    var735 = (c_bool)()
    var732(byref(var735), byref(var733), byref(buffer), byref(var734), )
    return var735

wrappers["can_parse_string"].append(rl_can_parse_string__double_String_int64_t_r_bool)
signatures[rl_can_parse_string__double_String_int64_t_r_bool] = [builtins.bool, builtins.float, String, builtins.int, ]
@overload
def _consume_space(buffer: String, index: builtins.int) -> None:
    pass

def rl__consume_space__String_int64_t(buffer: String, index: builtins.int) -> None:
    var736 = lib.rl__consume_space__String_int64_t
    var737 = c_longlong(index)
    var736(byref(buffer), byref(var737), )
    return

wrappers["_consume_space"].append(rl__consume_space__String_int64_t)
signatures[rl__consume_space__String_int64_t] = [None, String, builtins.int, ]
@overload
def can__consume_space(buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__consume_space__String_int64_t_r_bool(buffer: String, index: builtins.int) -> builtins.bool:
    var738 = lib.rl_can__consume_space__String_int64_t_r_bool
    var739 = c_longlong(index)
    var740 = (c_bool)()
    var738(byref(var740), byref(buffer), byref(var739), )
    return var740

wrappers["can__consume_space"].append(rl_can__consume_space__String_int64_t_r_bool)
signatures[rl_can__consume_space__String_int64_t_r_bool] = [builtins.bool, String, builtins.int, ]
@overload
def length(literal: builtins.str) -> builtins.int:
    pass

def rl_length__strlit_r_int64_t(literal: builtins.str) -> builtins.int:
    var741 = lib.rl_length__strlit_r_int64_t
    var742 = c_char_p(literal.encode("utf-8"))
    var743 = (c_longlong)()
    var741(byref(var743), byref(var742), )
    var744 = var743.value
    return var744

wrappers["length"].append(rl_length__strlit_r_int64_t)
signatures[rl_length__strlit_r_int64_t] = [builtins.int, builtins.str, ]
@overload
def can_length(literal: builtins.str) -> builtins.bool:
    pass

def rl_can_length__strlit_r_bool(literal: builtins.str) -> builtins.bool:
    var745 = lib.rl_can_length__strlit_r_bool
    var746 = c_char_p(literal.encode("utf-8"))
    var747 = (c_bool)()
    var745(byref(var747), byref(var746), )
    return var747

wrappers["can_length"].append(rl_can_length__strlit_r_bool)
signatures[rl_can_length__strlit_r_bool] = [builtins.bool, builtins.str, ]
@overload
def _consume_literal(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    pass

def rl__consume_literal__String_strlit_int64_t_r_bool(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    var748 = lib.rl__consume_literal__String_strlit_int64_t_r_bool
    var749 = c_char_p(literal.encode("utf-8"))
    var750 = c_longlong(index)
    var751 = (c_bool)()
    var748(byref(var751), byref(buffer), byref(var749), byref(var750), )
    return var751

wrappers["_consume_literal"].append(rl__consume_literal__String_strlit_int64_t_r_bool)
signatures[rl__consume_literal__String_strlit_int64_t_r_bool] = [builtins.bool, String, builtins.str, builtins.int, ]
@overload
def can__consume_literal(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    pass

def rl_can__consume_literal__String_strlit_int64_t_r_bool(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    var752 = lib.rl_can__consume_literal__String_strlit_int64_t_r_bool
    var753 = c_char_p(literal.encode("utf-8"))
    var754 = c_longlong(index)
    var755 = (c_bool)()
    var752(byref(var755), byref(buffer), byref(var753), byref(var754), )
    return var755

wrappers["can__consume_literal"].append(rl_can__consume_literal__String_strlit_int64_t_r_bool)
signatures[rl_can__consume_literal__String_strlit_int64_t_r_bool] = [builtins.bool, String, builtins.str, builtins.int, ]
@overload
def _consume_literal_token(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    pass

def rl__consume_literal_token__String_strlit_int64_t_r_bool(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    var756 = lib.rl__consume_literal_token__String_strlit_int64_t_r_bool
    var757 = c_char_p(literal.encode("utf-8"))
    var758 = c_longlong(index)
    var759 = (c_bool)()
    var756(byref(var759), byref(buffer), byref(var757), byref(var758), )
    return var759

wrappers["_consume_literal_token"].append(rl__consume_literal_token__String_strlit_int64_t_r_bool)
signatures[rl__consume_literal_token__String_strlit_int64_t_r_bool] = [builtins.bool, String, builtins.str, builtins.int, ]
@overload
def can__consume_literal_token(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    pass

def rl_can__consume_literal_token__String_strlit_int64_t_r_bool(buffer: String, literal: builtins.str, index: builtins.int) -> builtins.bool:
    var760 = lib.rl_can__consume_literal_token__String_strlit_int64_t_r_bool
    var761 = c_char_p(literal.encode("utf-8"))
    var762 = c_longlong(index)
    var763 = (c_bool)()
    var760(byref(var763), byref(buffer), byref(var761), byref(var762), )
    return var763

wrappers["can__consume_literal_token"].append(rl_can__consume_literal_token__String_strlit_int64_t_r_bool)
signatures[rl_can__consume_literal_token__String_strlit_int64_t_r_bool] = [builtins.bool, String, builtins.str, builtins.int, ]
@overload
def parse_string(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_string__bool_String_int64_t_r_bool(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    var764 = lib.rl_parse_string__bool_String_int64_t_r_bool
    var765 = c_bool(result)
    var766 = c_longlong(index)
    var767 = (c_bool)()
    var764(byref(var767), byref(var765), byref(buffer), byref(var766), )
    return var767

wrappers["parse_string"].append(rl_parse_string__bool_String_int64_t_r_bool)
signatures[rl_parse_string__bool_String_int64_t_r_bool] = [builtins.bool, builtins.bool, String, builtins.int, ]
@overload
def can_parse_string(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_string__bool_String_int64_t_r_bool(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    var768 = lib.rl_can_parse_string__bool_String_int64_t_r_bool
    var769 = c_bool(result)
    var770 = c_longlong(index)
    var771 = (c_bool)()
    var768(byref(var771), byref(var769), byref(buffer), byref(var770), )
    return var771

wrappers["can_parse_string"].append(rl_can_parse_string__bool_String_int64_t_r_bool)
signatures[rl_can_parse_string__bool_String_int64_t_r_bool] = [builtins.bool, builtins.bool, String, builtins.int, ]
@overload
def parse_string(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_string__BIntT0T3T_9_String_int64_t_r_bool(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    var772 = lib.rl_parse_string__BIntT0T3T_9_String_int64_t_r_bool
    var773 = c_longlong(index)
    var774 = (c_bool)()
    var772(byref(var774), byref(result), byref(buffer), byref(var773), )
    return var774

wrappers["parse_string"].append(rl_parse_string__BIntT0T3T_9_String_int64_t_r_bool)
signatures[rl_parse_string__BIntT0T3T_9_String_int64_t_r_bool] = [builtins.bool,  list , String, builtins.int, ]
@overload
def can_parse_string(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_string__BIntT0T3T_9_String_int64_t_r_bool(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    var775 = lib.rl_can_parse_string__BIntT0T3T_9_String_int64_t_r_bool
    var776 = c_longlong(index)
    var777 = (c_bool)()
    var775(byref(var777), byref(result), byref(buffer), byref(var776), )
    return var777

wrappers["can_parse_string"].append(rl_can_parse_string__BIntT0T3T_9_String_int64_t_r_bool)
signatures[rl_can_parse_string__BIntT0T3T_9_String_int64_t_r_bool] = [builtins.bool,  list , String, builtins.int, ]
@overload
def _parse_type(to_parse: GameMark, buffer: String, type_name: builtins.str, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_type__GameMark_String_strlit_int64_t_r_bool(to_parse: GameMark, buffer: String, type_name: builtins.str, index: builtins.int) -> builtins.bool:
    var778 = lib.rl__parse_type__GameMark_String_strlit_int64_t_r_bool
    var779 = c_char_p(type_name.encode("utf-8"))
    var780 = c_longlong(index)
    var781 = (c_bool)()
    var778(byref(var781), byref(to_parse), byref(buffer), byref(var779), byref(var780), )
    return var781

wrappers["_parse_type"].append(rl__parse_type__GameMark_String_strlit_int64_t_r_bool)
signatures[rl__parse_type__GameMark_String_strlit_int64_t_r_bool] = [builtins.bool, GameMark, String, builtins.str, builtins.int, ]
@overload
def can__parse_type(to_parse: GameMark, buffer: String, type_name: builtins.str, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_type__GameMark_String_strlit_int64_t_r_bool(to_parse: GameMark, buffer: String, type_name: builtins.str, index: builtins.int) -> builtins.bool:
    var782 = lib.rl_can__parse_type__GameMark_String_strlit_int64_t_r_bool
    var783 = c_char_p(type_name.encode("utf-8"))
    var784 = c_longlong(index)
    var785 = (c_bool)()
    var782(byref(var785), byref(to_parse), byref(buffer), byref(var783), byref(var784), )
    return var785

wrappers["can__parse_type"].append(rl_can__parse_type__GameMark_String_strlit_int64_t_r_bool)
signatures[rl_can__parse_type__GameMark_String_strlit_int64_t_r_bool] = [builtins.bool, GameMark, String, builtins.str, builtins.int, ]
@overload
def _parse_string_impl(result: Game, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__Game_String_int64_t_r_bool(result: Game, buffer: String, index: builtins.int) -> builtins.bool:
    var786 = lib.rl__parse_string_impl__Game_String_int64_t_r_bool
    var787 = c_longlong(index)
    var788 = (c_bool)()
    var786(byref(var788), byref(result), byref(buffer), byref(var787), )
    return var788

wrappers["_parse_string_impl"].append(rl__parse_string_impl__Game_String_int64_t_r_bool)
signatures[rl__parse_string_impl__Game_String_int64_t_r_bool] = [builtins.bool, Game, String, builtins.int, ]
@overload
def can__parse_string_impl(result: Game, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__Game_String_int64_t_r_bool(result: Game, buffer: String, index: builtins.int) -> builtins.bool:
    var789 = lib.rl_can__parse_string_impl__Game_String_int64_t_r_bool
    var790 = c_longlong(index)
    var791 = (c_bool)()
    var789(byref(var791), byref(result), byref(buffer), byref(var790), )
    return var791

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__Game_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__Game_String_int64_t_r_bool] = [builtins.bool, Game, String, builtins.int, ]
@overload
def _parse_string_impl(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__int64_t_String_int64_t_r_bool(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    var792 = lib.rl__parse_string_impl__int64_t_String_int64_t_r_bool
    var793 = c_longlong(result)
    var794 = c_longlong(index)
    var795 = (c_bool)()
    var792(byref(var795), byref(var793), byref(buffer), byref(var794), )
    return var795

wrappers["_parse_string_impl"].append(rl__parse_string_impl__int64_t_String_int64_t_r_bool)
signatures[rl__parse_string_impl__int64_t_String_int64_t_r_bool] = [builtins.bool, builtins.int, String, builtins.int, ]
@overload
def can__parse_string_impl(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__int64_t_String_int64_t_r_bool(result: builtins.int, buffer: String, index: builtins.int) -> builtins.bool:
    var796 = lib.rl_can__parse_string_impl__int64_t_String_int64_t_r_bool
    var797 = c_longlong(result)
    var798 = c_longlong(index)
    var799 = (c_bool)()
    var796(byref(var799), byref(var797), byref(buffer), byref(var798), )
    return var799

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__int64_t_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__int64_t_String_int64_t_r_bool] = [builtins.bool, builtins.int, String, builtins.int, ]
@overload
def _parse_string_impl(result: Board, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__Board_String_int64_t_r_bool(result: Board, buffer: String, index: builtins.int) -> builtins.bool:
    var800 = lib.rl__parse_string_impl__Board_String_int64_t_r_bool
    var801 = c_longlong(index)
    var802 = (c_bool)()
    var800(byref(var802), byref(result), byref(buffer), byref(var801), )
    return var802

wrappers["_parse_string_impl"].append(rl__parse_string_impl__Board_String_int64_t_r_bool)
signatures[rl__parse_string_impl__Board_String_int64_t_r_bool] = [builtins.bool, Board, String, builtins.int, ]
@overload
def can__parse_string_impl(result: Board, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__Board_String_int64_t_r_bool(result: Board, buffer: String, index: builtins.int) -> builtins.bool:
    var803 = lib.rl_can__parse_string_impl__Board_String_int64_t_r_bool
    var804 = c_longlong(index)
    var805 = (c_bool)()
    var803(byref(var805), byref(result), byref(buffer), byref(var804), )
    return var805

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__Board_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__Board_String_int64_t_r_bool] = [builtins.bool, Board, String, builtins.int, ]
@overload
def _parse_string_impl(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__alt_GameMark_String_int64_t_r_bool(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    var806 = lib.rl__parse_string_impl__alt_GameMark_String_int64_t_r_bool
    var807 = c_longlong(index)
    var808 = (c_bool)()
    var806(byref(var808), byref(result), byref(buffer), byref(var807), )
    return var808

wrappers["_parse_string_impl"].append(rl__parse_string_impl__alt_GameMark_String_int64_t_r_bool)
signatures[rl__parse_string_impl__alt_GameMark_String_int64_t_r_bool] = [builtins.bool, GameMarkOr, String, builtins.int, ]
@overload
def can__parse_string_impl(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__alt_GameMark_String_int64_t_r_bool(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    var809 = lib.rl_can__parse_string_impl__alt_GameMark_String_int64_t_r_bool
    var810 = c_longlong(index)
    var811 = (c_bool)()
    var809(byref(var811), byref(result), byref(buffer), byref(var810), )
    return var811

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__alt_GameMark_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__alt_GameMark_String_int64_t_r_bool] = [builtins.bool, GameMarkOr, String, builtins.int, ]
@overload
def _parse_string_impl(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    var812 = lib.rl__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool
    var813 = c_longlong(index)
    var814 = (c_bool)()
    var812(byref(var814), byref(result), byref(buffer), byref(var813), )
    return var814

wrappers["_parse_string_impl"].append(rl__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool)
signatures[rl__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool] = [builtins.bool,  list , String, builtins.int, ]
@overload
def can__parse_string_impl(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool(result:  list , buffer: String, index: builtins.int) -> builtins.bool:
    var815 = lib.rl_can__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool
    var816 = c_longlong(index)
    var817 = (c_bool)()
    var815(byref(var817), byref(result), byref(buffer), byref(var816), )
    return var817

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool] = [builtins.bool,  list , String, builtins.int, ]
@overload
def _parse_string_impl(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__bool_String_int64_t_r_bool(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    var818 = lib.rl__parse_string_impl__bool_String_int64_t_r_bool
    var819 = c_bool(result)
    var820 = c_longlong(index)
    var821 = (c_bool)()
    var818(byref(var821), byref(var819), byref(buffer), byref(var820), )
    return var821

wrappers["_parse_string_impl"].append(rl__parse_string_impl__bool_String_int64_t_r_bool)
signatures[rl__parse_string_impl__bool_String_int64_t_r_bool] = [builtins.bool, builtins.bool, String, builtins.int, ]
@overload
def can__parse_string_impl(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__bool_String_int64_t_r_bool(result: builtins.bool, buffer: String, index: builtins.int) -> builtins.bool:
    var822 = lib.rl_can__parse_string_impl__bool_String_int64_t_r_bool
    var823 = c_bool(result)
    var824 = c_longlong(index)
    var825 = (c_bool)()
    var822(byref(var825), byref(var823), byref(buffer), byref(var824), )
    return var825

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__bool_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__bool_String_int64_t_r_bool] = [builtins.bool, builtins.bool, String, builtins.int, ]
@overload
def _parse_string_impl(result: GameMark, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__GameMark_String_int64_t_r_bool(result: GameMark, buffer: String, index: builtins.int) -> builtins.bool:
    var826 = lib.rl__parse_string_impl__GameMark_String_int64_t_r_bool
    var827 = c_longlong(index)
    var828 = (c_bool)()
    var826(byref(var828), byref(result), byref(buffer), byref(var827), )
    return var828

wrappers["_parse_string_impl"].append(rl__parse_string_impl__GameMark_String_int64_t_r_bool)
signatures[rl__parse_string_impl__GameMark_String_int64_t_r_bool] = [builtins.bool, GameMark, String, builtins.int, ]
@overload
def can__parse_string_impl(result: GameMark, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__GameMark_String_int64_t_r_bool(result: GameMark, buffer: String, index: builtins.int) -> builtins.bool:
    var829 = lib.rl_can__parse_string_impl__GameMark_String_int64_t_r_bool
    var830 = c_longlong(index)
    var831 = (c_bool)()
    var829(byref(var831), byref(result), byref(buffer), byref(var830), )
    return var831

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__GameMark_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__GameMark_String_int64_t_r_bool] = [builtins.bool, GameMark, String, builtins.int, ]
@overload
def _parse_string_impl(result: BIntT0T3T, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl__parse_string_impl__BIntT0T3T_String_int64_t_r_bool(result: BIntT0T3T, buffer: String, index: builtins.int) -> builtins.bool:
    var832 = lib.rl__parse_string_impl__BIntT0T3T_String_int64_t_r_bool
    var833 = c_longlong(index)
    var834 = (c_bool)()
    var832(byref(var834), byref(result), byref(buffer), byref(var833), )
    return var834

wrappers["_parse_string_impl"].append(rl__parse_string_impl__BIntT0T3T_String_int64_t_r_bool)
signatures[rl__parse_string_impl__BIntT0T3T_String_int64_t_r_bool] = [builtins.bool, BIntT0T3T, String, builtins.int, ]
@overload
def can__parse_string_impl(result: BIntT0T3T, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can__parse_string_impl__BIntT0T3T_String_int64_t_r_bool(result: BIntT0T3T, buffer: String, index: builtins.int) -> builtins.bool:
    var835 = lib.rl_can__parse_string_impl__BIntT0T3T_String_int64_t_r_bool
    var836 = c_longlong(index)
    var837 = (c_bool)()
    var835(byref(var837), byref(result), byref(buffer), byref(var836), )
    return var837

wrappers["can__parse_string_impl"].append(rl_can__parse_string_impl__BIntT0T3T_String_int64_t_r_bool)
signatures[rl_can__parse_string_impl__BIntT0T3T_String_int64_t_r_bool] = [builtins.bool, BIntT0T3T, String, builtins.int, ]
@overload
def from_string(result: Game, buffer: String) -> builtins.bool:
    pass

def rl_from_string__Game_String_r_bool(result: Game, buffer: String) -> builtins.bool:
    var838 = lib.rl_from_string__Game_String_r_bool
    var839 = (c_bool)()
    var838(byref(var839), byref(result), byref(buffer), )
    return var839

wrappers["from_string"].append(rl_from_string__Game_String_r_bool)
signatures[rl_from_string__Game_String_r_bool] = [builtins.bool, Game, String, ]
@overload
def can_from_string(result: Game, buffer: String) -> builtins.bool:
    pass

def rl_can_from_string__Game_String_r_bool(result: Game, buffer: String) -> builtins.bool:
    var840 = lib.rl_can_from_string__Game_String_r_bool
    var841 = (c_bool)()
    var840(byref(var841), byref(result), byref(buffer), )
    return var841

wrappers["can_from_string"].append(rl_can_from_string__Game_String_r_bool)
signatures[rl_can_from_string__Game_String_r_bool] = [builtins.bool, Game, String, ]
@overload
def from_string(result: GameMarkOr, buffer: String) -> builtins.bool:
    pass

def rl_from_string__alt_GameMark_String_r_bool(result: GameMarkOr, buffer: String) -> builtins.bool:
    var842 = lib.rl_from_string__alt_GameMark_String_r_bool
    var843 = (c_bool)()
    var842(byref(var843), byref(result), byref(buffer), )
    return var843

wrappers["from_string"].append(rl_from_string__alt_GameMark_String_r_bool)
signatures[rl_from_string__alt_GameMark_String_r_bool] = [builtins.bool, GameMarkOr, String, ]
@overload
def can_from_string(result: GameMarkOr, buffer: String) -> builtins.bool:
    pass

def rl_can_from_string__alt_GameMark_String_r_bool(result: GameMarkOr, buffer: String) -> builtins.bool:
    var844 = lib.rl_can_from_string__alt_GameMark_String_r_bool
    var845 = (c_bool)()
    var844(byref(var845), byref(result), byref(buffer), )
    return var845

wrappers["can_from_string"].append(rl_can_from_string__alt_GameMark_String_r_bool)
signatures[rl_can_from_string__alt_GameMark_String_r_bool] = [builtins.bool, GameMarkOr, String, ]
@overload
def from_string(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_from_string__alt_GameMark_String_int64_t_r_bool(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    var846 = lib.rl_from_string__alt_GameMark_String_int64_t_r_bool
    var847 = c_longlong(index)
    var848 = (c_bool)()
    var846(byref(var848), byref(result), byref(buffer), byref(var847), )
    return var848

wrappers["from_string"].append(rl_from_string__alt_GameMark_String_int64_t_r_bool)
signatures[rl_from_string__alt_GameMark_String_int64_t_r_bool] = [builtins.bool, GameMarkOr, String, builtins.int, ]
@overload
def can_from_string(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_from_string__alt_GameMark_String_int64_t_r_bool(result: GameMarkOr, buffer: String, index: builtins.int) -> builtins.bool:
    var849 = lib.rl_can_from_string__alt_GameMark_String_int64_t_r_bool
    var850 = c_longlong(index)
    var851 = (c_bool)()
    var849(byref(var851), byref(result), byref(buffer), byref(var850), )
    return var851

wrappers["can_from_string"].append(rl_can_from_string__alt_GameMark_String_int64_t_r_bool)
signatures[rl_can_from_string__alt_GameMark_String_int64_t_r_bool] = [builtins.bool, GameMarkOr, String, builtins.int, ]
@overload
def append_to_vector(to_add: BIntT0T3T, output: VectorTint8_tT) -> None:
    pass

def rl_append_to_vector__BIntT0T3T_VectorTint8_tT(to_add: BIntT0T3T, output: VectorTint8_tT) -> None:
    var852 = lib.rl_append_to_vector__BIntT0T3T_VectorTint8_tT
    var852(byref(to_add), byref(output), )
    return

wrappers["append_to_vector"].append(rl_append_to_vector__BIntT0T3T_VectorTint8_tT)
signatures[rl_append_to_vector__BIntT0T3T_VectorTint8_tT] = [None, BIntT0T3T, VectorTint8_tT, ]
@overload
def can_append_to_vector(to_add: BIntT0T3T, output: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_append_to_vector__BIntT0T3T_VectorTint8_tT_r_bool(to_add: BIntT0T3T, output: VectorTint8_tT) -> builtins.bool:
    var853 = lib.rl_can_append_to_vector__BIntT0T3T_VectorTint8_tT_r_bool
    var854 = (c_bool)()
    var853(byref(var854), byref(to_add), byref(output), )
    return var854

wrappers["can_append_to_vector"].append(rl_can_append_to_vector__BIntT0T3T_VectorTint8_tT_r_bool)
signatures[rl_can_append_to_vector__BIntT0T3T_VectorTint8_tT_r_bool] = [builtins.bool, BIntT0T3T, VectorTint8_tT, ]
@overload
def parse_from_vector(to_add: BIntT0T3T, output: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(to_add: BIntT0T3T, output: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var855 = lib.rl_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool
    var856 = c_longlong(index)
    var857 = (c_bool)()
    var855(byref(var857), byref(to_add), byref(output), byref(var856), )
    return var857

wrappers["parse_from_vector"].append(rl_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, BIntT0T3T, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_from_vector(to_add: BIntT0T3T, output: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(to_add: BIntT0T3T, output: VectorTint8_tT, index: builtins.int) -> builtins.bool:
    var858 = lib.rl_can_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool
    var859 = c_longlong(index)
    var860 = (c_bool)()
    var858(byref(var860), byref(to_add), byref(output), byref(var859), )
    return var860

wrappers["can_parse_from_vector"].append(rl_can_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, BIntT0T3T, VectorTint8_tT, builtins.int, ]
@overload
def append_to_string(to_add: BIntT0T3T, output: String) -> None:
    pass

def rl_append_to_string__BIntT0T3T_String(to_add: BIntT0T3T, output: String) -> None:
    var861 = lib.rl_append_to_string__BIntT0T3T_String
    var861(byref(to_add), byref(output), )
    return

wrappers["append_to_string"].append(rl_append_to_string__BIntT0T3T_String)
signatures[rl_append_to_string__BIntT0T3T_String] = [None, BIntT0T3T, String, ]
@overload
def can_append_to_string(to_add: BIntT0T3T, output: String) -> builtins.bool:
    pass

def rl_can_append_to_string__BIntT0T3T_String_r_bool(to_add: BIntT0T3T, output: String) -> builtins.bool:
    var862 = lib.rl_can_append_to_string__BIntT0T3T_String_r_bool
    var863 = (c_bool)()
    var862(byref(var863), byref(to_add), byref(output), )
    return var863

wrappers["can_append_to_string"].append(rl_can_append_to_string__BIntT0T3T_String_r_bool)
signatures[rl_can_append_to_string__BIntT0T3T_String_r_bool] = [builtins.bool, BIntT0T3T, String, ]
@overload
def parse_string(to_add: BIntT0T3T, input: String, index: builtins.int) -> builtins.bool:
    pass

def rl_parse_string__BIntT0T3T_String_int64_t_r_bool(to_add: BIntT0T3T, input: String, index: builtins.int) -> builtins.bool:
    var864 = lib.rl_parse_string__BIntT0T3T_String_int64_t_r_bool
    var865 = c_longlong(index)
    var866 = (c_bool)()
    var864(byref(var866), byref(to_add), byref(input), byref(var865), )
    return var866

wrappers["parse_string"].append(rl_parse_string__BIntT0T3T_String_int64_t_r_bool)
signatures[rl_parse_string__BIntT0T3T_String_int64_t_r_bool] = [builtins.bool, BIntT0T3T, String, builtins.int, ]
@overload
def can_parse_string(to_add: BIntT0T3T, input: String, index: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_string__BIntT0T3T_String_int64_t_r_bool(to_add: BIntT0T3T, input: String, index: builtins.int) -> builtins.bool:
    var867 = lib.rl_can_parse_string__BIntT0T3T_String_int64_t_r_bool
    var868 = c_longlong(index)
    var869 = (c_bool)()
    var867(byref(var869), byref(to_add), byref(input), byref(var868), )
    return var869

wrappers["can_parse_string"].append(rl_can_parse_string__BIntT0T3T_String_int64_t_r_bool)
signatures[rl_can_parse_string__BIntT0T3T_String_int64_t_r_bool] = [builtins.bool, BIntT0T3T, String, builtins.int, ]
@overload
def enumerate(to_add: BIntT0T3T, output: VectorTBIntT0T3TT) -> None:
    pass

def rl_enumerate__BIntT0T3T_VectorTBIntT0T3TT(to_add: BIntT0T3T, output: VectorTBIntT0T3TT) -> None:
    var870 = lib.rl_enumerate__BIntT0T3T_VectorTBIntT0T3TT
    var870(byref(to_add), byref(output), )
    return

wrappers["enumerate"].append(rl_enumerate__BIntT0T3T_VectorTBIntT0T3TT)
signatures[rl_enumerate__BIntT0T3T_VectorTBIntT0T3TT] = [None, BIntT0T3T, VectorTBIntT0T3TT, ]
@overload
def can_enumerate(to_add: BIntT0T3T, output: VectorTBIntT0T3TT) -> builtins.bool:
    pass

def rl_can_enumerate__BIntT0T3T_VectorTBIntT0T3TT_r_bool(to_add: BIntT0T3T, output: VectorTBIntT0T3TT) -> builtins.bool:
    var871 = lib.rl_can_enumerate__BIntT0T3T_VectorTBIntT0T3TT_r_bool
    var872 = (c_bool)()
    var871(byref(var872), byref(to_add), byref(output), )
    return var872

wrappers["can_enumerate"].append(rl_can_enumerate__BIntT0T3T_VectorTBIntT0T3TT_r_bool)
signatures[rl_can_enumerate__BIntT0T3T_VectorTBIntT0T3TT_r_bool] = [builtins.bool, BIntT0T3T, VectorTBIntT0T3TT, ]
@overload
def max(a: builtins.int, b: builtins.int) -> builtins.int:
    pass

def rl_max__int64_t_int64_t_r_int64_t(a: builtins.int, b: builtins.int) -> builtins.int:
    var873 = lib.rl_max__int64_t_int64_t_r_int64_t
    var874 = c_longlong(a)
    var875 = c_longlong(b)
    var876 = (c_longlong)()
    var873(byref(var876), byref(var874), byref(var875), )
    var877 = var876.value
    return var877

wrappers["max"].append(rl_max__int64_t_int64_t_r_int64_t)
signatures[rl_max__int64_t_int64_t_r_int64_t] = [builtins.int, builtins.int, builtins.int, ]
@overload
def can_max(a: builtins.int, b: builtins.int) -> builtins.bool:
    pass

def rl_can_max__int64_t_int64_t_r_bool(a: builtins.int, b: builtins.int) -> builtins.bool:
    var878 = lib.rl_can_max__int64_t_int64_t_r_bool
    var879 = c_longlong(a)
    var880 = c_longlong(b)
    var881 = (c_bool)()
    var878(byref(var881), byref(var879), byref(var880), )
    return var881

wrappers["can_max"].append(rl_can_max__int64_t_int64_t_r_bool)
signatures[rl_can_max__int64_t_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def min(a: builtins.int, b: builtins.int) -> builtins.int:
    pass

def rl_min__int64_t_int64_t_r_int64_t(a: builtins.int, b: builtins.int) -> builtins.int:
    var882 = lib.rl_min__int64_t_int64_t_r_int64_t
    var883 = c_longlong(a)
    var884 = c_longlong(b)
    var885 = (c_longlong)()
    var882(byref(var885), byref(var883), byref(var884), )
    var886 = var885.value
    return var886

wrappers["min"].append(rl_min__int64_t_int64_t_r_int64_t)
signatures[rl_min__int64_t_int64_t_r_int64_t] = [builtins.int, builtins.int, builtins.int, ]
@overload
def can_min(a: builtins.int, b: builtins.int) -> builtins.bool:
    pass

def rl_can_min__int64_t_int64_t_r_bool(a: builtins.int, b: builtins.int) -> builtins.bool:
    var887 = lib.rl_can_min__int64_t_int64_t_r_bool
    var888 = c_longlong(a)
    var889 = c_longlong(b)
    var890 = (c_bool)()
    var887(byref(var890), byref(var888), byref(var889), )
    return var890

wrappers["can_min"].append(rl_can_min__int64_t_int64_t_r_bool)
signatures[rl_can_min__int64_t_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def sqrt(f: builtins.float) -> builtins.float:
    pass

def rl_sqrt__double_r_double(f: builtins.float) -> builtins.float:
    var891 = lib.rl_sqrt__double_r_double
    var892 = c_double(f)
    var893 = (c_double)()
    var891(byref(var893), byref(var892), )
    return var893

wrappers["sqrt"].append(rl_sqrt__double_r_double)
signatures[rl_sqrt__double_r_double] = [builtins.float, builtins.float, ]
@overload
def can_sqrt(f: builtins.float) -> builtins.bool:
    pass

def rl_can_sqrt__double_r_bool(f: builtins.float) -> builtins.bool:
    var894 = lib.rl_can_sqrt__double_r_bool
    var895 = c_double(f)
    var896 = (c_bool)()
    var894(byref(var896), byref(var895), )
    return var896

wrappers["can_sqrt"].append(rl_can_sqrt__double_r_bool)
signatures[rl_can_sqrt__double_r_bool] = [builtins.bool, builtins.float, ]
@overload
def abs(a: builtins.int) -> builtins.int:
    pass

def rl_abs__int64_t_r_int64_t(a: builtins.int) -> builtins.int:
    var897 = lib.rl_abs__int64_t_r_int64_t
    var898 = c_longlong(a)
    var899 = (c_longlong)()
    var897(byref(var899), byref(var898), )
    var900 = var899.value
    return var900

wrappers["abs"].append(rl_abs__int64_t_r_int64_t)
signatures[rl_abs__int64_t_r_int64_t] = [builtins.int, builtins.int, ]
@overload
def can_abs(a: builtins.int) -> builtins.bool:
    pass

def rl_can_abs__int64_t_r_bool(a: builtins.int) -> builtins.bool:
    var901 = lib.rl_can_abs__int64_t_r_bool
    var902 = c_longlong(a)
    var903 = (c_bool)()
    var901(byref(var903), byref(var902), )
    return var903

wrappers["can_abs"].append(rl_can_abs__int64_t_r_bool)
signatures[rl_can_abs__int64_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def custom_equal(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    pass

def rl_custom_equal__int64_t_int64_t_r_bool(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    var904 = lib.rl_custom_equal__int64_t_int64_t_r_bool
    var905 = c_longlong(lhs)
    var906 = c_longlong(rhs)
    var907 = (c_bool)()
    var904(byref(var907), byref(var905), byref(var906), )
    return var907

wrappers["custom_equal"].append(rl_custom_equal__int64_t_int64_t_r_bool)
signatures[rl_custom_equal__int64_t_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def can_custom_equal(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    pass

def rl_can_custom_equal__int64_t_int64_t_r_bool(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    var908 = lib.rl_can_custom_equal__int64_t_int64_t_r_bool
    var909 = c_longlong(lhs)
    var910 = c_longlong(rhs)
    var911 = (c_bool)()
    var908(byref(var911), byref(var909), byref(var910), )
    return var911

wrappers["can_custom_equal"].append(rl_can_custom_equal__int64_t_int64_t_r_bool)
signatures[rl_can_custom_equal__int64_t_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def custom_equal(lhs: builtins.bool, rhs: builtins.bool) -> builtins.bool:
    pass

def rl_custom_equal__bool_bool_r_bool(lhs: builtins.bool, rhs: builtins.bool) -> builtins.bool:
    var912 = lib.rl_custom_equal__bool_bool_r_bool
    var913 = c_bool(lhs)
    var914 = c_bool(rhs)
    var915 = (c_bool)()
    var912(byref(var915), byref(var913), byref(var914), )
    return var915

wrappers["custom_equal"].append(rl_custom_equal__bool_bool_r_bool)
signatures[rl_custom_equal__bool_bool_r_bool] = [builtins.bool, builtins.bool, builtins.bool, ]
@overload
def can_custom_equal(lhs: builtins.bool, rhs: builtins.bool) -> builtins.bool:
    pass

def rl_can_custom_equal__bool_bool_r_bool(lhs: builtins.bool, rhs: builtins.bool) -> builtins.bool:
    var916 = lib.rl_can_custom_equal__bool_bool_r_bool
    var917 = c_bool(lhs)
    var918 = c_bool(rhs)
    var919 = (c_bool)()
    var916(byref(var919), byref(var917), byref(var918), )
    return var919

wrappers["can_custom_equal"].append(rl_can_custom_equal__bool_bool_r_bool)
signatures[rl_can_custom_equal__bool_bool_r_bool] = [builtins.bool, builtins.bool, builtins.bool, ]
@overload
def custom_equal(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    pass

def rl_custom_equal__int8_t_int8_t_r_bool(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    var920 = lib.rl_custom_equal__int8_t_int8_t_r_bool
    var921 = c_byte(lhs)
    var922 = c_byte(rhs)
    var923 = (c_bool)()
    var920(byref(var923), byref(var921), byref(var922), )
    return var923

wrappers["custom_equal"].append(rl_custom_equal__int8_t_int8_t_r_bool)
signatures[rl_custom_equal__int8_t_int8_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def can_custom_equal(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    pass

def rl_can_custom_equal__int8_t_int8_t_r_bool(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    var924 = lib.rl_can_custom_equal__int8_t_int8_t_r_bool
    var925 = c_byte(lhs)
    var926 = c_byte(rhs)
    var927 = (c_bool)()
    var924(byref(var927), byref(var925), byref(var926), )
    return var927

wrappers["can_custom_equal"].append(rl_can_custom_equal__int8_t_int8_t_r_bool)
signatures[rl_can_custom_equal__int8_t_int8_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def custom_equal(lhs: builtins.float, rhs: builtins.float) -> builtins.bool:
    pass

def rl_custom_equal__double_double_r_bool(lhs: builtins.float, rhs: builtins.float) -> builtins.bool:
    var928 = lib.rl_custom_equal__double_double_r_bool
    var929 = c_double(lhs)
    var930 = c_double(rhs)
    var931 = (c_bool)()
    var928(byref(var931), byref(var929), byref(var930), )
    return var931

wrappers["custom_equal"].append(rl_custom_equal__double_double_r_bool)
signatures[rl_custom_equal__double_double_r_bool] = [builtins.bool, builtins.float, builtins.float, ]
@overload
def can_custom_equal(lhs: builtins.float, rhs: builtins.float) -> builtins.bool:
    pass

def rl_can_custom_equal__double_double_r_bool(lhs: builtins.float, rhs: builtins.float) -> builtins.bool:
    var932 = lib.rl_can_custom_equal__double_double_r_bool
    var933 = c_double(lhs)
    var934 = c_double(rhs)
    var935 = (c_bool)()
    var932(byref(var935), byref(var933), byref(var934), )
    return var935

wrappers["can_custom_equal"].append(rl_can_custom_equal__double_double_r_bool)
signatures[rl_can_custom_equal__double_double_r_bool] = [builtins.bool, builtins.float, builtins.float, ]
@overload
def equal(lhs: GameMarkOr, rhs: GameMarkOr) -> builtins.bool:
    pass

def rl_equal__alt_GameMark_alt_GameMark_r_bool(lhs: GameMarkOr, rhs: GameMarkOr) -> builtins.bool:
    var936 = lib.rl_equal__alt_GameMark_alt_GameMark_r_bool
    var937 = (c_bool)()
    var936(byref(var937), byref(lhs), byref(rhs), )
    return var937

wrappers["equal"].append(rl_equal__alt_GameMark_alt_GameMark_r_bool)
signatures[rl_equal__alt_GameMark_alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, GameMarkOr, ]
@overload
def can_equal(lhs: GameMarkOr, rhs: GameMarkOr) -> builtins.bool:
    pass

def rl_can_equal__alt_GameMark_alt_GameMark_r_bool(lhs: GameMarkOr, rhs: GameMarkOr) -> builtins.bool:
    var938 = lib.rl_can_equal__alt_GameMark_alt_GameMark_r_bool
    var939 = (c_bool)()
    var938(byref(var939), byref(lhs), byref(rhs), )
    return var939

wrappers["can_equal"].append(rl_can_equal__alt_GameMark_alt_GameMark_r_bool)
signatures[rl_can_equal__alt_GameMark_alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, GameMarkOr, ]
@overload
def equal(lhs: GameMark, rhs: GameMark) -> builtins.bool:
    pass

def rl_equal__GameMark_GameMark_r_bool(lhs: GameMark, rhs: GameMark) -> builtins.bool:
    var940 = lib.rl_equal__GameMark_GameMark_r_bool
    var941 = (c_bool)()
    var940(byref(var941), byref(lhs), byref(rhs), )
    return var941

wrappers["equal"].append(rl_equal__GameMark_GameMark_r_bool)
signatures[rl_equal__GameMark_GameMark_r_bool] = [builtins.bool, GameMark, GameMark, ]
@overload
def can_equal(lhs: GameMark, rhs: GameMark) -> builtins.bool:
    pass

def rl_can_equal__GameMark_GameMark_r_bool(lhs: GameMark, rhs: GameMark) -> builtins.bool:
    var942 = lib.rl_can_equal__GameMark_GameMark_r_bool
    var943 = (c_bool)()
    var942(byref(var943), byref(lhs), byref(rhs), )
    return var943

wrappers["can_equal"].append(rl_can_equal__GameMark_GameMark_r_bool)
signatures[rl_can_equal__GameMark_GameMark_r_bool] = [builtins.bool, GameMark, GameMark, ]
@overload
def equal(lhs: BIntT0T3T, rhs: BIntT0T3T) -> builtins.bool:
    pass

def rl_equal__BIntT0T3T_BIntT0T3T_r_bool(lhs: BIntT0T3T, rhs: BIntT0T3T) -> builtins.bool:
    var944 = lib.rl_equal__BIntT0T3T_BIntT0T3T_r_bool
    var945 = (c_bool)()
    var944(byref(var945), byref(lhs), byref(rhs), )
    return var945

wrappers["equal"].append(rl_equal__BIntT0T3T_BIntT0T3T_r_bool)
signatures[rl_equal__BIntT0T3T_BIntT0T3T_r_bool] = [builtins.bool, BIntT0T3T, BIntT0T3T, ]
@overload
def can_equal(lhs: BIntT0T3T, rhs: BIntT0T3T) -> builtins.bool:
    pass

def rl_can_equal__BIntT0T3T_BIntT0T3T_r_bool(lhs: BIntT0T3T, rhs: BIntT0T3T) -> builtins.bool:
    var946 = lib.rl_can_equal__BIntT0T3T_BIntT0T3T_r_bool
    var947 = (c_bool)()
    var946(byref(var947), byref(lhs), byref(rhs), )
    return var947

wrappers["can_equal"].append(rl_can_equal__BIntT0T3T_BIntT0T3T_r_bool)
signatures[rl_can_equal__BIntT0T3T_BIntT0T3T_r_bool] = [builtins.bool, BIntT0T3T, BIntT0T3T, ]
@overload
def equal(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    pass

def rl_equal__int64_t_int64_t_r_bool(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    var948 = lib.rl_equal__int64_t_int64_t_r_bool
    var949 = c_longlong(lhs)
    var950 = c_longlong(rhs)
    var951 = (c_bool)()
    var948(byref(var951), byref(var949), byref(var950), )
    return var951

wrappers["equal"].append(rl_equal__int64_t_int64_t_r_bool)
signatures[rl_equal__int64_t_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def can_equal(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    pass

def rl_can_equal__int64_t_int64_t_r_bool(lhs: builtins.int, rhs: builtins.int) -> builtins.bool:
    var952 = lib.rl_can_equal__int64_t_int64_t_r_bool
    var953 = c_longlong(lhs)
    var954 = c_longlong(rhs)
    var955 = (c_bool)()
    var952(byref(var955), byref(var953), byref(var954), )
    return var955

wrappers["can_equal"].append(rl_can_equal__int64_t_int64_t_r_bool)
signatures[rl_can_equal__int64_t_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, ]
@overload
def can_apply_impl(action: GameMarkOr, frame: Game) -> builtins.bool:
    pass

def rl_can_apply_impl__alt_GameMark_Game_r_bool(action: GameMarkOr, frame: Game) -> builtins.bool:
    var956 = lib.rl_can_apply_impl__alt_GameMark_Game_r_bool
    var957 = (c_bool)()
    var956(byref(var957), byref(action), byref(frame), )
    return var957

wrappers["can_apply_impl"].append(rl_can_apply_impl__alt_GameMark_Game_r_bool)
signatures[rl_can_apply_impl__alt_GameMark_Game_r_bool] = [builtins.bool, GameMarkOr, Game, ]
@overload
def can_can_apply_impl(action: GameMarkOr, frame: Game) -> builtins.bool:
    pass

def rl_can_can_apply_impl__alt_GameMark_Game_r_bool(action: GameMarkOr, frame: Game) -> builtins.bool:
    var958 = lib.rl_can_can_apply_impl__alt_GameMark_Game_r_bool
    var959 = (c_bool)()
    var958(byref(var959), byref(action), byref(frame), )
    return var959

wrappers["can_can_apply_impl"].append(rl_can_can_apply_impl__alt_GameMark_Game_r_bool)
signatures[rl_can_can_apply_impl__alt_GameMark_Game_r_bool] = [builtins.bool, GameMarkOr, Game, ]
@overload
def apply(action: GameMarkOr, frame: Game) -> None:
    pass

def rl_apply__alt_GameMark_Game(action: GameMarkOr, frame: Game) -> None:
    var960 = lib.rl_apply__alt_GameMark_Game
    var960(byref(action), byref(frame), )
    return

wrappers["apply"].append(rl_apply__alt_GameMark_Game)
signatures[rl_apply__alt_GameMark_Game] = [None, GameMarkOr, Game, ]
@overload
def can_apply(action: GameMarkOr, frame: Game) -> builtins.bool:
    pass

def rl_can_apply__alt_GameMark_Game_r_bool(action: GameMarkOr, frame: Game) -> builtins.bool:
    var961 = lib.rl_can_apply__alt_GameMark_Game_r_bool
    var962 = (c_bool)()
    var961(byref(var962), byref(action), byref(frame), )
    return var962

wrappers["can_apply"].append(rl_can_apply__alt_GameMark_Game_r_bool)
signatures[rl_can_apply__alt_GameMark_Game_r_bool] = [builtins.bool, GameMarkOr, Game, ]
@overload
def apply(action: VectorTalt_GameMarkT, frame: Game) -> builtins.bool:
    pass

def rl_apply__VectorTalt_GameMarkT_Game_r_bool(action: VectorTalt_GameMarkT, frame: Game) -> builtins.bool:
    var963 = lib.rl_apply__VectorTalt_GameMarkT_Game_r_bool
    var964 = (c_bool)()
    var963(byref(var964), byref(action), byref(frame), )
    return var964

wrappers["apply"].append(rl_apply__VectorTalt_GameMarkT_Game_r_bool)
signatures[rl_apply__VectorTalt_GameMarkT_Game_r_bool] = [builtins.bool, VectorTalt_GameMarkT, Game, ]
@overload
def can_apply(action: VectorTalt_GameMarkT, frame: Game) -> builtins.bool:
    pass

def rl_can_apply__VectorTalt_GameMarkT_Game_r_bool(action: VectorTalt_GameMarkT, frame: Game) -> builtins.bool:
    var965 = lib.rl_can_apply__VectorTalt_GameMarkT_Game_r_bool
    var966 = (c_bool)()
    var965(byref(var966), byref(action), byref(frame), )
    return var966

wrappers["can_apply"].append(rl_can_apply__VectorTalt_GameMarkT_Game_r_bool)
signatures[rl_can_apply__VectorTalt_GameMarkT_Game_r_bool] = [builtins.bool, VectorTalt_GameMarkT, Game, ]
@overload
def parse_and_execute(state: Game, variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> None:
    pass

def rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t(state: Game, variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> None:
    var967 = lib.rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t
    var968 = c_longlong(read_bytes)
    var967(byref(state), byref(variant), byref(input), byref(var968), )
    return

wrappers["parse_and_execute"].append(rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t)
signatures[rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t] = [None, Game, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_and_execute(state: Game, variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t_r_bool(state: Game, variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var969 = lib.rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var970 = c_longlong(read_bytes)
    var971 = (c_bool)()
    var969(byref(var971), byref(state), byref(variant), byref(input), byref(var970), )
    return var971

wrappers["can_parse_and_execute"].append(rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, Game, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def parse_actions(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> VectorTalt_GameMarkT:
    pass

def rl_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_VectorTalt_GameMarkT(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> VectorTalt_GameMarkT:
    var972 = lib.rl_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_VectorTalt_GameMarkT
    var973 = c_longlong(read_bytes)
    var974 = (VectorTalt_GameMarkT)()
    var972(byref(var974), byref(variant), byref(input), byref(var973), )
    return var974

wrappers["parse_actions"].append(rl_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_VectorTalt_GameMarkT)
signatures[rl_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_VectorTalt_GameMarkT] = [VectorTalt_GameMarkT, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_actions(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_bool(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var975 = lib.rl_can_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var976 = c_longlong(read_bytes)
    var977 = (c_bool)()
    var975(byref(var977), byref(variant), byref(input), byref(var976), )
    return var977

wrappers["can_parse_actions"].append(rl_can_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def parse_actions(variant: GameMarkOr, input: String) -> VectorTalt_GameMarkT:
    pass

def rl_parse_actions__alt_GameMark_String_r_VectorTalt_GameMarkT(variant: GameMarkOr, input: String) -> VectorTalt_GameMarkT:
    var978 = lib.rl_parse_actions__alt_GameMark_String_r_VectorTalt_GameMarkT
    var979 = (VectorTalt_GameMarkT)()
    var978(byref(var979), byref(variant), byref(input), )
    return var979

wrappers["parse_actions"].append(rl_parse_actions__alt_GameMark_String_r_VectorTalt_GameMarkT)
signatures[rl_parse_actions__alt_GameMark_String_r_VectorTalt_GameMarkT] = [VectorTalt_GameMarkT, GameMarkOr, String, ]
@overload
def can_parse_actions(variant: GameMarkOr, input: String) -> builtins.bool:
    pass

def rl_can_parse_actions__alt_GameMark_String_r_bool(variant: GameMarkOr, input: String) -> builtins.bool:
    var980 = lib.rl_can_parse_actions__alt_GameMark_String_r_bool
    var981 = (c_bool)()
    var980(byref(var981), byref(variant), byref(input), )
    return var981

wrappers["can_parse_actions"].append(rl_can_parse_actions__alt_GameMark_String_r_bool)
signatures[rl_can_parse_actions__alt_GameMark_String_r_bool] = [builtins.bool, GameMarkOr, String, ]
@overload
def parse_action_optimized(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var982 = lib.rl_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var983 = c_longlong(read_bytes)
    var984 = (c_bool)()
    var982(byref(var984), byref(variant), byref(input), byref(var983), )
    return var984

wrappers["parse_action_optimized"].append(rl_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def can_parse_action_optimized(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    pass

def rl_can_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool(variant: GameMarkOr, input: VectorTint8_tT, read_bytes: builtins.int) -> builtins.bool:
    var985 = lib.rl_can_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool
    var986 = c_longlong(read_bytes)
    var987 = (c_bool)()
    var985(byref(var987), byref(variant), byref(input), byref(var986), )
    return var987

wrappers["can_parse_action_optimized"].append(rl_can_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool)
signatures[rl_can_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, builtins.int, ]
@overload
def parse_actions(variant: GameMarkOr, input: VectorTint8_tT) -> VectorTalt_GameMarkT:
    pass

def rl_parse_actions__alt_GameMark_VectorTint8_tT_r_VectorTalt_GameMarkT(variant: GameMarkOr, input: VectorTint8_tT) -> VectorTalt_GameMarkT:
    var988 = lib.rl_parse_actions__alt_GameMark_VectorTint8_tT_r_VectorTalt_GameMarkT
    var989 = (VectorTalt_GameMarkT)()
    var988(byref(var989), byref(variant), byref(input), )
    return var989

wrappers["parse_actions"].append(rl_parse_actions__alt_GameMark_VectorTint8_tT_r_VectorTalt_GameMarkT)
signatures[rl_parse_actions__alt_GameMark_VectorTint8_tT_r_VectorTalt_GameMarkT] = [VectorTalt_GameMarkT, GameMarkOr, VectorTint8_tT, ]
@overload
def can_parse_actions(variant: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_parse_actions__alt_GameMark_VectorTint8_tT_r_bool(variant: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    var990 = lib.rl_can_parse_actions__alt_GameMark_VectorTint8_tT_r_bool
    var991 = (c_bool)()
    var990(byref(var991), byref(variant), byref(input), )
    return var991

wrappers["can_parse_actions"].append(rl_can_parse_actions__alt_GameMark_VectorTint8_tT_r_bool)
signatures[rl_can_parse_actions__alt_GameMark_VectorTint8_tT_r_bool] = [builtins.bool, GameMarkOr, VectorTint8_tT, ]
@overload
def parse_and_execute(state: Game, variant: GameMarkOr, input: VectorTint8_tT) -> None:
    pass

def rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT(state: Game, variant: GameMarkOr, input: VectorTint8_tT) -> None:
    var992 = lib.rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT
    var992(byref(state), byref(variant), byref(input), )
    return

wrappers["parse_and_execute"].append(rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT)
signatures[rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT] = [None, Game, GameMarkOr, VectorTint8_tT, ]
@overload
def can_parse_and_execute(state: Game, variant: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_r_bool(state: Game, variant: GameMarkOr, input: VectorTint8_tT) -> builtins.bool:
    var993 = lib.rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_r_bool
    var994 = (c_bool)()
    var993(byref(var994), byref(state), byref(variant), byref(input), )
    return var994

wrappers["can_parse_and_execute"].append(rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_r_bool)
signatures[rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_r_bool] = [builtins.bool, Game, GameMarkOr, VectorTint8_tT, ]
@overload
def gen_python_methods(state: Game, variant: GameMarkOr) -> None:
    pass

def rl_gen_python_methods__Game_alt_GameMark(state: Game, variant: GameMarkOr) -> None:
    var995 = lib.rl_gen_python_methods__Game_alt_GameMark
    var995(byref(state), byref(variant), )
    return

wrappers["gen_python_methods"].append(rl_gen_python_methods__Game_alt_GameMark)
signatures[rl_gen_python_methods__Game_alt_GameMark] = [None, Game, GameMarkOr, ]
@overload
def can_gen_python_methods(state: Game, variant: GameMarkOr) -> builtins.bool:
    pass

def rl_can_gen_python_methods__Game_alt_GameMark_r_bool(state: Game, variant: GameMarkOr) -> builtins.bool:
    var996 = lib.rl_can_gen_python_methods__Game_alt_GameMark_r_bool
    var997 = (c_bool)()
    var996(byref(var997), byref(state), byref(variant), )
    return var997

wrappers["can_gen_python_methods"].append(rl_can_gen_python_methods__Game_alt_GameMark_r_bool)
signatures[rl_can_gen_python_methods__Game_alt_GameMark_r_bool] = [builtins.bool, Game, GameMarkOr, ]
@overload
def load_action_vector_file(file_name: String, out: VectorTalt_GameMarkT) -> builtins.bool:
    pass

def rl_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool(file_name: String, out: VectorTalt_GameMarkT) -> builtins.bool:
    var998 = lib.rl_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool
    var999 = (c_bool)()
    var998(byref(var999), byref(file_name), byref(out), )
    return var999

wrappers["load_action_vector_file"].append(rl_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool)
signatures[rl_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool] = [builtins.bool, String, VectorTalt_GameMarkT, ]
@overload
def can_load_action_vector_file(file_name: String, out: VectorTalt_GameMarkT) -> builtins.bool:
    pass

def rl_can_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool(file_name: String, out: VectorTalt_GameMarkT) -> builtins.bool:
    var1000 = lib.rl_can_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool
    var1001 = (c_bool)()
    var1000(byref(var1001), byref(file_name), byref(out), )
    return var1001

wrappers["can_load_action_vector_file"].append(rl_can_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool)
signatures[rl_can_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool] = [builtins.bool, String, VectorTalt_GameMarkT, ]
@overload
def enumerate(b: builtins.bool, output: VectorTboolT) -> None:
    pass

def rl_enumerate__bool_VectorTboolT(b: builtins.bool, output: VectorTboolT) -> None:
    var1002 = lib.rl_enumerate__bool_VectorTboolT
    var1003 = c_bool(b)
    var1002(byref(var1003), byref(output), )
    return

wrappers["enumerate"].append(rl_enumerate__bool_VectorTboolT)
signatures[rl_enumerate__bool_VectorTboolT] = [None, builtins.bool, VectorTboolT, ]
@overload
def can_enumerate(b: builtins.bool, output: VectorTboolT) -> builtins.bool:
    pass

def rl_can_enumerate__bool_VectorTboolT_r_bool(b: builtins.bool, output: VectorTboolT) -> builtins.bool:
    var1004 = lib.rl_can_enumerate__bool_VectorTboolT_r_bool
    var1005 = c_bool(b)
    var1006 = (c_bool)()
    var1004(byref(var1006), byref(var1005), byref(output), )
    return var1006

wrappers["can_enumerate"].append(rl_can_enumerate__bool_VectorTboolT_r_bool)
signatures[rl_can_enumerate__bool_VectorTboolT_r_bool] = [builtins.bool, builtins.bool, VectorTboolT, ]
@overload
def _enumerate_impl(obj: GameMark, current_argument: builtins.int, out: VectorTGameMarkT, num_args: builtins.int) -> None:
    pass

def rl__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t(obj: GameMark, current_argument: builtins.int, out: VectorTGameMarkT, num_args: builtins.int) -> None:
    var1007 = lib.rl__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t
    var1008 = c_longlong(current_argument)
    var1009 = c_longlong(num_args)
    var1007(byref(obj), byref(var1008), byref(out), byref(var1009), )
    return

wrappers["_enumerate_impl"].append(rl__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t)
signatures[rl__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t] = [None, GameMark, builtins.int, VectorTGameMarkT, builtins.int, ]
@overload
def can__enumerate_impl(obj: GameMark, current_argument: builtins.int, out: VectorTGameMarkT, num_args: builtins.int) -> builtins.bool:
    pass

def rl_can__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t_r_bool(obj: GameMark, current_argument: builtins.int, out: VectorTGameMarkT, num_args: builtins.int) -> builtins.bool:
    var1010 = lib.rl_can__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t_r_bool
    var1011 = c_longlong(current_argument)
    var1012 = c_longlong(num_args)
    var1013 = (c_bool)()
    var1010(byref(var1013), byref(obj), byref(var1011), byref(out), byref(var1012), )
    return var1013

wrappers["can__enumerate_impl"].append(rl_can__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t_r_bool)
signatures[rl_can__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t_r_bool] = [builtins.bool, GameMark, builtins.int, VectorTGameMarkT, builtins.int, ]
@overload
def enumeration_error(x: builtins.int, out: String, context: VectorTStringT) -> None:
    pass

def rl_enumeration_error__int64_t_String_VectorTStringT(x: builtins.int, out: String, context: VectorTStringT) -> None:
    var1014 = lib.rl_enumeration_error__int64_t_String_VectorTStringT
    var1015 = c_longlong(x)
    var1014(byref(var1015), byref(out), byref(context), )
    return

wrappers["enumeration_error"].append(rl_enumeration_error__int64_t_String_VectorTStringT)
signatures[rl_enumeration_error__int64_t_String_VectorTStringT] = [None, builtins.int, String, VectorTStringT, ]
@overload
def can_enumeration_error(x: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_enumeration_error__int64_t_String_VectorTStringT_r_bool(x: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    var1016 = lib.rl_can_enumeration_error__int64_t_String_VectorTStringT_r_bool
    var1017 = c_longlong(x)
    var1018 = (c_bool)()
    var1016(byref(var1018), byref(var1017), byref(out), byref(context), )
    return var1018

wrappers["can_enumeration_error"].append(rl_can_enumeration_error__int64_t_String_VectorTStringT_r_bool)
signatures[rl_can_enumeration_error__int64_t_String_VectorTStringT_r_bool] = [builtins.bool, builtins.int, String, VectorTStringT, ]
@overload
def enumeration_error(x: builtins.float, out: String, context: VectorTStringT) -> None:
    pass

def rl_enumeration_error__double_String_VectorTStringT(x: builtins.float, out: String, context: VectorTStringT) -> None:
    var1019 = lib.rl_enumeration_error__double_String_VectorTStringT
    var1020 = c_double(x)
    var1019(byref(var1020), byref(out), byref(context), )
    return

wrappers["enumeration_error"].append(rl_enumeration_error__double_String_VectorTStringT)
signatures[rl_enumeration_error__double_String_VectorTStringT] = [None, builtins.float, String, VectorTStringT, ]
@overload
def can_enumeration_error(x: builtins.float, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_enumeration_error__double_String_VectorTStringT_r_bool(x: builtins.float, out: String, context: VectorTStringT) -> builtins.bool:
    var1021 = lib.rl_can_enumeration_error__double_String_VectorTStringT_r_bool
    var1022 = c_double(x)
    var1023 = (c_bool)()
    var1021(byref(var1023), byref(var1022), byref(out), byref(context), )
    return var1023

wrappers["can_enumeration_error"].append(rl_can_enumeration_error__double_String_VectorTStringT_r_bool)
signatures[rl_can_enumeration_error__double_String_VectorTStringT_r_bool] = [builtins.bool, builtins.float, String, VectorTStringT, ]
@overload
def get_enumeration_errors_impl(obj: GameMarkOr, out: String, context: VectorTStringT) -> None:
    pass

def rl_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT(obj: GameMarkOr, out: String, context: VectorTStringT) -> None:
    var1024 = lib.rl_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT
    var1024(byref(obj), byref(out), byref(context), )
    return

wrappers["get_enumeration_errors_impl"].append(rl_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT)
signatures[rl_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT] = [None, GameMarkOr, String, VectorTStringT, ]
@overload
def can_get_enumeration_errors_impl(obj: GameMarkOr, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT_r_bool(obj: GameMarkOr, out: String, context: VectorTStringT) -> builtins.bool:
    var1025 = lib.rl_can_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT_r_bool
    var1026 = (c_bool)()
    var1025(byref(var1026), byref(obj), byref(out), byref(context), )
    return var1026

wrappers["can_get_enumeration_errors_impl"].append(rl_can_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT_r_bool)
signatures[rl_can_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT_r_bool] = [builtins.bool, GameMarkOr, String, VectorTStringT, ]
@overload
def get_enumeration_errors_impl(obj: GameMark, out: String, context: VectorTStringT) -> None:
    pass

def rl_get_enumeration_errors_impl__GameMark_String_VectorTStringT(obj: GameMark, out: String, context: VectorTStringT) -> None:
    var1027 = lib.rl_get_enumeration_errors_impl__GameMark_String_VectorTStringT
    var1027(byref(obj), byref(out), byref(context), )
    return

wrappers["get_enumeration_errors_impl"].append(rl_get_enumeration_errors_impl__GameMark_String_VectorTStringT)
signatures[rl_get_enumeration_errors_impl__GameMark_String_VectorTStringT] = [None, GameMark, String, VectorTStringT, ]
@overload
def can_get_enumeration_errors_impl(obj: GameMark, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_get_enumeration_errors_impl__GameMark_String_VectorTStringT_r_bool(obj: GameMark, out: String, context: VectorTStringT) -> builtins.bool:
    var1028 = lib.rl_can_get_enumeration_errors_impl__GameMark_String_VectorTStringT_r_bool
    var1029 = (c_bool)()
    var1028(byref(var1029), byref(obj), byref(out), byref(context), )
    return var1029

wrappers["can_get_enumeration_errors_impl"].append(rl_can_get_enumeration_errors_impl__GameMark_String_VectorTStringT_r_bool)
signatures[rl_can_get_enumeration_errors_impl__GameMark_String_VectorTStringT_r_bool] = [builtins.bool, GameMark, String, VectorTStringT, ]
@overload
def get_enumeration_errors_impl(obj: BIntT0T3T, out: String, context: VectorTStringT) -> None:
    pass

def rl_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT(obj: BIntT0T3T, out: String, context: VectorTStringT) -> None:
    var1030 = lib.rl_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT
    var1030(byref(obj), byref(out), byref(context), )
    return

wrappers["get_enumeration_errors_impl"].append(rl_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT)
signatures[rl_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT] = [None, BIntT0T3T, String, VectorTStringT, ]
@overload
def can_get_enumeration_errors_impl(obj: BIntT0T3T, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT_r_bool(obj: BIntT0T3T, out: String, context: VectorTStringT) -> builtins.bool:
    var1031 = lib.rl_can_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT_r_bool
    var1032 = (c_bool)()
    var1031(byref(var1032), byref(obj), byref(out), byref(context), )
    return var1032

wrappers["can_get_enumeration_errors_impl"].append(rl_can_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT_r_bool)
signatures[rl_can_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT_r_bool] = [builtins.bool, BIntT0T3T, String, VectorTStringT, ]
@overload
def get_enumeration_errors_impl(obj: builtins.int, out: String, context: VectorTStringT) -> None:
    pass

def rl_get_enumeration_errors_impl__int64_t_String_VectorTStringT(obj: builtins.int, out: String, context: VectorTStringT) -> None:
    var1033 = lib.rl_get_enumeration_errors_impl__int64_t_String_VectorTStringT
    var1034 = c_longlong(obj)
    var1033(byref(var1034), byref(out), byref(context), )
    return

wrappers["get_enumeration_errors_impl"].append(rl_get_enumeration_errors_impl__int64_t_String_VectorTStringT)
signatures[rl_get_enumeration_errors_impl__int64_t_String_VectorTStringT] = [None, builtins.int, String, VectorTStringT, ]
@overload
def can_get_enumeration_errors_impl(obj: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_get_enumeration_errors_impl__int64_t_String_VectorTStringT_r_bool(obj: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    var1035 = lib.rl_can_get_enumeration_errors_impl__int64_t_String_VectorTStringT_r_bool
    var1036 = c_longlong(obj)
    var1037 = (c_bool)()
    var1035(byref(var1037), byref(var1036), byref(out), byref(context), )
    return var1037

wrappers["can_get_enumeration_errors_impl"].append(rl_can_get_enumeration_errors_impl__int64_t_String_VectorTStringT_r_bool)
signatures[rl_can_get_enumeration_errors_impl__int64_t_String_VectorTStringT_r_bool] = [builtins.bool, builtins.int, String, VectorTStringT, ]
@overload
def get_enumeration_errors(obj: GameMarkOr) -> String:
    pass

def rl_get_enumeration_errors__alt_GameMark_r_String(obj: GameMarkOr) -> String:
    var1038 = lib.rl_get_enumeration_errors__alt_GameMark_r_String
    var1039 = (String)()
    var1038(byref(var1039), byref(obj), )
    return var1039

wrappers["get_enumeration_errors"].append(rl_get_enumeration_errors__alt_GameMark_r_String)
signatures[rl_get_enumeration_errors__alt_GameMark_r_String] = [String, GameMarkOr, ]
@overload
def can_get_enumeration_errors(obj: GameMarkOr) -> builtins.bool:
    pass

def rl_can_get_enumeration_errors__alt_GameMark_r_bool(obj: GameMarkOr) -> builtins.bool:
    var1040 = lib.rl_can_get_enumeration_errors__alt_GameMark_r_bool
    var1041 = (c_bool)()
    var1040(byref(var1041), byref(obj), )
    return var1041

wrappers["can_get_enumeration_errors"].append(rl_can_get_enumeration_errors__alt_GameMark_r_bool)
signatures[rl_can_get_enumeration_errors__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def print_enumeration_errors(obj: GameMarkOr) -> builtins.bool:
    pass

def rl_print_enumeration_errors__alt_GameMark_r_bool(obj: GameMarkOr) -> builtins.bool:
    var1042 = lib.rl_print_enumeration_errors__alt_GameMark_r_bool
    var1043 = (c_bool)()
    var1042(byref(var1043), byref(obj), )
    return var1043

wrappers["print_enumeration_errors"].append(rl_print_enumeration_errors__alt_GameMark_r_bool)
signatures[rl_print_enumeration_errors__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def can_print_enumeration_errors(obj: GameMarkOr) -> builtins.bool:
    pass

def rl_can_print_enumeration_errors__alt_GameMark_r_bool(obj: GameMarkOr) -> builtins.bool:
    var1044 = lib.rl_can_print_enumeration_errors__alt_GameMark_r_bool
    var1045 = (c_bool)()
    var1044(byref(var1045), byref(obj), )
    return var1045

wrappers["can_print_enumeration_errors"].append(rl_can_print_enumeration_errors__alt_GameMark_r_bool)
signatures[rl_can_print_enumeration_errors__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def enumerate(obj: GameMarkOr) -> VectorTalt_GameMarkT:
    pass

def rl_enumerate__alt_GameMark_r_VectorTalt_GameMarkT(obj: GameMarkOr) -> VectorTalt_GameMarkT:
    var1046 = lib.rl_enumerate__alt_GameMark_r_VectorTalt_GameMarkT
    var1047 = (VectorTalt_GameMarkT)()
    var1046(byref(var1047), byref(obj), )
    return var1047

wrappers["enumerate"].append(rl_enumerate__alt_GameMark_r_VectorTalt_GameMarkT)
signatures[rl_enumerate__alt_GameMark_r_VectorTalt_GameMarkT] = [VectorTalt_GameMarkT, GameMarkOr, ]
@overload
def can_enumerate(obj: GameMarkOr) -> builtins.bool:
    pass

def rl_can_enumerate__alt_GameMark_r_bool(obj: GameMarkOr) -> builtins.bool:
    var1048 = lib.rl_can_enumerate__alt_GameMark_r_bool
    var1049 = (c_bool)()
    var1048(byref(var1049), byref(obj), )
    return var1049

wrappers["can_enumerate"].append(rl_can_enumerate__alt_GameMark_r_bool)
signatures[rl_can_enumerate__alt_GameMark_r_bool] = [builtins.bool, GameMarkOr, ]
@overload
def enumerate(obj: GameMark) -> VectorTGameMarkT:
    pass

def rl_enumerate__GameMark_r_VectorTGameMarkT(obj: GameMark) -> VectorTGameMarkT:
    var1050 = lib.rl_enumerate__GameMark_r_VectorTGameMarkT
    var1051 = (VectorTGameMarkT)()
    var1050(byref(var1051), byref(obj), )
    return var1051

wrappers["enumerate"].append(rl_enumerate__GameMark_r_VectorTGameMarkT)
signatures[rl_enumerate__GameMark_r_VectorTGameMarkT] = [VectorTGameMarkT, GameMark, ]
@overload
def can_enumerate(obj: GameMark) -> builtins.bool:
    pass

def rl_can_enumerate__GameMark_r_bool(obj: GameMark) -> builtins.bool:
    var1052 = lib.rl_can_enumerate__GameMark_r_bool
    var1053 = (c_bool)()
    var1052(byref(var1053), byref(obj), )
    return var1053

wrappers["can_enumerate"].append(rl_can_enumerate__GameMark_r_bool)
signatures[rl_can_enumerate__GameMark_r_bool] = [builtins.bool, GameMark, ]
@overload
def write_in_observation_tensor(value: builtins.int, min: builtins.int, max: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t(value: builtins.int, min: builtins.int, max: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1054 = lib.rl_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t
    var1055 = c_longlong(value)
    var1056 = c_longlong(min)
    var1057 = c_longlong(max)
    var1058 = c_longlong(index)
    var1054(byref(var1055), byref(var1056), byref(var1057), byref(output), byref(var1058), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t] = [None, builtins.int, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(value: builtins.int, min: builtins.int, max: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t_r_bool(value: builtins.int, min: builtins.int, max: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1059 = lib.rl_can_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t_r_bool
    var1060 = c_longlong(value)
    var1061 = c_longlong(min)
    var1062 = c_longlong(max)
    var1063 = c_longlong(index)
    var1064 = (c_bool)()
    var1059(byref(var1064), byref(var1060), byref(var1061), byref(var1062), byref(output), byref(var1063), )
    return var1064

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def write_in_observation_tensor(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1065 = lib.rl_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t
    var1066 = c_longlong(obj)
    var1067 = c_longlong(observer_id)
    var1068 = c_longlong(index)
    var1065(byref(var1066), byref(var1067), byref(output), byref(var1068), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t] = [None, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1069 = lib.rl_can_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool
    var1070 = c_longlong(obj)
    var1071 = c_longlong(observer_id)
    var1072 = c_longlong(index)
    var1073 = (c_bool)()
    var1069(byref(var1073), byref(var1070), byref(var1071), byref(output), byref(var1072), )
    return var1073

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def size_as_observation_tensor(obj: builtins.int) -> builtins.int:
    pass

def rl_size_as_observation_tensor__int64_t_r_int64_t(obj: builtins.int) -> builtins.int:
    var1074 = lib.rl_size_as_observation_tensor__int64_t_r_int64_t
    var1075 = c_longlong(obj)
    var1076 = (c_longlong)()
    var1074(byref(var1076), byref(var1075), )
    var1077 = var1076.value
    return var1077

wrappers["size_as_observation_tensor"].append(rl_size_as_observation_tensor__int64_t_r_int64_t)
signatures[rl_size_as_observation_tensor__int64_t_r_int64_t] = [builtins.int, builtins.int, ]
@overload
def can_size_as_observation_tensor(obj: builtins.int) -> builtins.bool:
    pass

def rl_can_size_as_observation_tensor__int64_t_r_bool(obj: builtins.int) -> builtins.bool:
    var1078 = lib.rl_can_size_as_observation_tensor__int64_t_r_bool
    var1079 = c_longlong(obj)
    var1080 = (c_bool)()
    var1078(byref(var1080), byref(var1079), )
    return var1080

wrappers["can_size_as_observation_tensor"].append(rl_can_size_as_observation_tensor__int64_t_r_bool)
signatures[rl_can_size_as_observation_tensor__int64_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def write_in_observation_tensor(obj: builtins.float, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t(obj: builtins.float, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1081 = lib.rl_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t
    var1082 = c_double(obj)
    var1083 = c_longlong(observer_id)
    var1084 = c_longlong(index)
    var1081(byref(var1082), byref(var1083), byref(output), byref(var1084), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t] = [None, builtins.float, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(obj: builtins.float, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t_r_bool(obj: builtins.float, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1085 = lib.rl_can_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t_r_bool
    var1086 = c_double(obj)
    var1087 = c_longlong(observer_id)
    var1088 = c_longlong(index)
    var1089 = (c_bool)()
    var1085(byref(var1089), byref(var1086), byref(var1087), byref(output), byref(var1088), )
    return var1089

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.float, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def size_as_observation_tensor(obj: builtins.float) -> builtins.int:
    pass

def rl_size_as_observation_tensor__double_r_int64_t(obj: builtins.float) -> builtins.int:
    var1090 = lib.rl_size_as_observation_tensor__double_r_int64_t
    var1091 = c_double(obj)
    var1092 = (c_longlong)()
    var1090(byref(var1092), byref(var1091), )
    var1093 = var1092.value
    return var1093

wrappers["size_as_observation_tensor"].append(rl_size_as_observation_tensor__double_r_int64_t)
signatures[rl_size_as_observation_tensor__double_r_int64_t] = [builtins.int, builtins.float, ]
@overload
def can_size_as_observation_tensor(obj: builtins.float) -> builtins.bool:
    pass

def rl_can_size_as_observation_tensor__double_r_bool(obj: builtins.float) -> builtins.bool:
    var1094 = lib.rl_can_size_as_observation_tensor__double_r_bool
    var1095 = c_double(obj)
    var1096 = (c_bool)()
    var1094(byref(var1096), byref(var1095), )
    return var1096

wrappers["can_size_as_observation_tensor"].append(rl_can_size_as_observation_tensor__double_r_bool)
signatures[rl_can_size_as_observation_tensor__double_r_bool] = [builtins.bool, builtins.float, ]
@overload
def write_in_observation_tensor(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1097 = lib.rl_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t
    var1098 = c_bool(obj)
    var1099 = c_longlong(observer_id)
    var1100 = c_longlong(index)
    var1097(byref(var1098), byref(var1099), byref(output), byref(var1100), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t] = [None, builtins.bool, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1101 = lib.rl_can_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool
    var1102 = c_bool(obj)
    var1103 = c_longlong(observer_id)
    var1104 = c_longlong(index)
    var1105 = (c_bool)()
    var1101(byref(var1105), byref(var1102), byref(var1103), byref(output), byref(var1104), )
    return var1105

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.bool, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def size_as_observation_tensor(obj: builtins.bool) -> builtins.int:
    pass

def rl_size_as_observation_tensor__bool_r_int64_t(obj: builtins.bool) -> builtins.int:
    var1106 = lib.rl_size_as_observation_tensor__bool_r_int64_t
    var1107 = c_bool(obj)
    var1108 = (c_longlong)()
    var1106(byref(var1108), byref(var1107), )
    var1109 = var1108.value
    return var1109

wrappers["size_as_observation_tensor"].append(rl_size_as_observation_tensor__bool_r_int64_t)
signatures[rl_size_as_observation_tensor__bool_r_int64_t] = [builtins.int, builtins.bool, ]
@overload
def can_size_as_observation_tensor(obj: builtins.bool) -> builtins.bool:
    pass

def rl_can_size_as_observation_tensor__bool_r_bool(obj: builtins.bool) -> builtins.bool:
    var1110 = lib.rl_can_size_as_observation_tensor__bool_r_bool
    var1111 = c_bool(obj)
    var1112 = (c_bool)()
    var1110(byref(var1112), byref(var1111), )
    return var1112

wrappers["can_size_as_observation_tensor"].append(rl_can_size_as_observation_tensor__bool_r_bool)
signatures[rl_can_size_as_observation_tensor__bool_r_bool] = [builtins.bool, builtins.bool, ]
@overload
def write_in_observation_tensor(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1113 = lib.rl_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t
    var1114 = c_byte(obj)
    var1115 = c_longlong(observer_id)
    var1116 = c_longlong(index)
    var1113(byref(var1114), byref(var1115), byref(output), byref(var1116), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t] = [None, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t_r_bool(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1117 = lib.rl_can_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t_r_bool
    var1118 = c_byte(obj)
    var1119 = c_longlong(observer_id)
    var1120 = c_longlong(index)
    var1121 = (c_bool)()
    var1117(byref(var1121), byref(var1118), byref(var1119), byref(output), byref(var1120), )
    return var1121

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def size_as_observation_tensor(obj: builtins.int) -> builtins.int:
    pass

def rl_size_as_observation_tensor__int8_t_r_int64_t(obj: builtins.int) -> builtins.int:
    var1122 = lib.rl_size_as_observation_tensor__int8_t_r_int64_t
    var1123 = c_byte(obj)
    var1124 = (c_longlong)()
    var1122(byref(var1124), byref(var1123), )
    var1125 = var1124.value
    return var1125

wrappers["size_as_observation_tensor"].append(rl_size_as_observation_tensor__int8_t_r_int64_t)
signatures[rl_size_as_observation_tensor__int8_t_r_int64_t] = [builtins.int, builtins.int, ]
@overload
def can_size_as_observation_tensor(obj: builtins.int) -> builtins.bool:
    pass

def rl_can_size_as_observation_tensor__int8_t_r_bool(obj: builtins.int) -> builtins.bool:
    var1126 = lib.rl_can_size_as_observation_tensor__int8_t_r_bool
    var1127 = c_byte(obj)
    var1128 = (c_bool)()
    var1126(byref(var1128), byref(var1127), )
    return var1128

wrappers["can_size_as_observation_tensor"].append(rl_can_size_as_observation_tensor__int8_t_r_bool)
signatures[rl_can_size_as_observation_tensor__int8_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def write_in_observation_tensor(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1129 = lib.rl_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t
    var1130 = c_longlong(observer_id)
    var1131 = c_longlong(index)
    var1129(byref(obj), byref(var1130), byref(output), byref(var1131), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t] = [None,  list , builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1132 = lib.rl_can_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool
    var1133 = c_longlong(observer_id)
    var1134 = c_longlong(index)
    var1135 = (c_bool)()
    var1132(byref(var1135), byref(obj), byref(var1133), byref(output), byref(var1134), )
    return var1135

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool,  list , builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def size_as_observation_tensor(obj:  list ) -> builtins.int:
    pass

def rl_size_as_observation_tensor__BIntT0T3T_9_r_int64_t(obj:  list ) -> builtins.int:
    var1136 = lib.rl_size_as_observation_tensor__BIntT0T3T_9_r_int64_t
    var1137 = (c_longlong)()
    var1136(byref(var1137), byref(obj), )
    var1138 = var1137.value
    return var1138

wrappers["size_as_observation_tensor"].append(rl_size_as_observation_tensor__BIntT0T3T_9_r_int64_t)
signatures[rl_size_as_observation_tensor__BIntT0T3T_9_r_int64_t] = [builtins.int,  list , ]
@overload
def can_size_as_observation_tensor(obj:  list ) -> builtins.bool:
    pass

def rl_can_size_as_observation_tensor__BIntT0T3T_9_r_bool(obj:  list ) -> builtins.bool:
    var1139 = lib.rl_can_size_as_observation_tensor__BIntT0T3T_9_r_bool
    var1140 = (c_bool)()
    var1139(byref(var1140), byref(obj), )
    return var1140

wrappers["can_size_as_observation_tensor"].append(rl_can_size_as_observation_tensor__BIntT0T3T_9_r_bool)
signatures[rl_can_size_as_observation_tensor__BIntT0T3T_9_r_bool] = [builtins.bool,  list , ]
@overload
def write_in_observation_tensor(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1141 = lib.rl_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t
    var1142 = c_longlong(observer_id)
    var1143 = c_longlong(index)
    var1141(byref(obj), byref(var1142), byref(output), byref(var1143), )
    return

wrappers["write_in_observation_tensor"].append(rl_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t)
signatures[rl_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t] = [None, BIntT0T3T, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can_write_in_observation_tensor(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1144 = lib.rl_can_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool
    var1145 = c_longlong(observer_id)
    var1146 = c_longlong(index)
    var1147 = (c_bool)()
    var1144(byref(var1147), byref(obj), byref(var1145), byref(output), byref(var1146), )
    return var1147

wrappers["can_write_in_observation_tensor"].append(rl_can_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, BIntT0T3T, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def size_as_observation_tensor(obj: BIntT0T3T) -> builtins.int:
    pass

def rl_size_as_observation_tensor__BIntT0T3T_r_int64_t(obj: BIntT0T3T) -> builtins.int:
    var1148 = lib.rl_size_as_observation_tensor__BIntT0T3T_r_int64_t
    var1149 = (c_longlong)()
    var1148(byref(var1149), byref(obj), )
    var1150 = var1149.value
    return var1150

wrappers["size_as_observation_tensor"].append(rl_size_as_observation_tensor__BIntT0T3T_r_int64_t)
signatures[rl_size_as_observation_tensor__BIntT0T3T_r_int64_t] = [builtins.int, BIntT0T3T, ]
@overload
def can_size_as_observation_tensor(obj: BIntT0T3T) -> builtins.bool:
    pass

def rl_can_size_as_observation_tensor__BIntT0T3T_r_bool(obj: BIntT0T3T) -> builtins.bool:
    var1151 = lib.rl_can_size_as_observation_tensor__BIntT0T3T_r_bool
    var1152 = (c_bool)()
    var1151(byref(var1152), byref(obj), )
    return var1152

wrappers["can_size_as_observation_tensor"].append(rl_can_size_as_observation_tensor__BIntT0T3T_r_bool)
signatures[rl_can_size_as_observation_tensor__BIntT0T3T_r_bool] = [builtins.bool, BIntT0T3T, ]
@overload
def _size_as_observation_tensor_impl(obj: Game) -> builtins.int:
    pass

def rl__size_as_observation_tensor_impl__Game_r_int64_t(obj: Game) -> builtins.int:
    var1153 = lib.rl__size_as_observation_tensor_impl__Game_r_int64_t
    var1154 = (c_longlong)()
    var1153(byref(var1154), byref(obj), )
    var1155 = var1154.value
    return var1155

wrappers["_size_as_observation_tensor_impl"].append(rl__size_as_observation_tensor_impl__Game_r_int64_t)
signatures[rl__size_as_observation_tensor_impl__Game_r_int64_t] = [builtins.int, Game, ]
@overload
def can__size_as_observation_tensor_impl(obj: Game) -> builtins.bool:
    pass

def rl_can__size_as_observation_tensor_impl__Game_r_bool(obj: Game) -> builtins.bool:
    var1156 = lib.rl_can__size_as_observation_tensor_impl__Game_r_bool
    var1157 = (c_bool)()
    var1156(byref(var1157), byref(obj), )
    return var1157

wrappers["can__size_as_observation_tensor_impl"].append(rl_can__size_as_observation_tensor_impl__Game_r_bool)
signatures[rl_can__size_as_observation_tensor_impl__Game_r_bool] = [builtins.bool, Game, ]
@overload
def _size_as_observation_tensor_impl(obj: builtins.int) -> builtins.int:
    pass

def rl__size_as_observation_tensor_impl__int64_t_r_int64_t(obj: builtins.int) -> builtins.int:
    var1158 = lib.rl__size_as_observation_tensor_impl__int64_t_r_int64_t
    var1159 = c_longlong(obj)
    var1160 = (c_longlong)()
    var1158(byref(var1160), byref(var1159), )
    var1161 = var1160.value
    return var1161

wrappers["_size_as_observation_tensor_impl"].append(rl__size_as_observation_tensor_impl__int64_t_r_int64_t)
signatures[rl__size_as_observation_tensor_impl__int64_t_r_int64_t] = [builtins.int, builtins.int, ]
@overload
def can__size_as_observation_tensor_impl(obj: builtins.int) -> builtins.bool:
    pass

def rl_can__size_as_observation_tensor_impl__int64_t_r_bool(obj: builtins.int) -> builtins.bool:
    var1162 = lib.rl_can__size_as_observation_tensor_impl__int64_t_r_bool
    var1163 = c_longlong(obj)
    var1164 = (c_bool)()
    var1162(byref(var1164), byref(var1163), )
    return var1164

wrappers["can__size_as_observation_tensor_impl"].append(rl_can__size_as_observation_tensor_impl__int64_t_r_bool)
signatures[rl_can__size_as_observation_tensor_impl__int64_t_r_bool] = [builtins.bool, builtins.int, ]
@overload
def _size_as_observation_tensor_impl(obj: Board) -> builtins.int:
    pass

def rl__size_as_observation_tensor_impl__Board_r_int64_t(obj: Board) -> builtins.int:
    var1165 = lib.rl__size_as_observation_tensor_impl__Board_r_int64_t
    var1166 = (c_longlong)()
    var1165(byref(var1166), byref(obj), )
    var1167 = var1166.value
    return var1167

wrappers["_size_as_observation_tensor_impl"].append(rl__size_as_observation_tensor_impl__Board_r_int64_t)
signatures[rl__size_as_observation_tensor_impl__Board_r_int64_t] = [builtins.int, Board, ]
@overload
def can__size_as_observation_tensor_impl(obj: Board) -> builtins.bool:
    pass

def rl_can__size_as_observation_tensor_impl__Board_r_bool(obj: Board) -> builtins.bool:
    var1168 = lib.rl_can__size_as_observation_tensor_impl__Board_r_bool
    var1169 = (c_bool)()
    var1168(byref(var1169), byref(obj), )
    return var1169

wrappers["can__size_as_observation_tensor_impl"].append(rl_can__size_as_observation_tensor_impl__Board_r_bool)
signatures[rl_can__size_as_observation_tensor_impl__Board_r_bool] = [builtins.bool, Board, ]
@overload
def _size_as_observation_tensor_impl(obj:  list ) -> builtins.int:
    pass

def rl__size_as_observation_tensor_impl__BIntT0T3T_9_r_int64_t(obj:  list ) -> builtins.int:
    var1170 = lib.rl__size_as_observation_tensor_impl__BIntT0T3T_9_r_int64_t
    var1171 = (c_longlong)()
    var1170(byref(var1171), byref(obj), )
    var1172 = var1171.value
    return var1172

wrappers["_size_as_observation_tensor_impl"].append(rl__size_as_observation_tensor_impl__BIntT0T3T_9_r_int64_t)
signatures[rl__size_as_observation_tensor_impl__BIntT0T3T_9_r_int64_t] = [builtins.int,  list , ]
@overload
def can__size_as_observation_tensor_impl(obj:  list ) -> builtins.bool:
    pass

def rl_can__size_as_observation_tensor_impl__BIntT0T3T_9_r_bool(obj:  list ) -> builtins.bool:
    var1173 = lib.rl_can__size_as_observation_tensor_impl__BIntT0T3T_9_r_bool
    var1174 = (c_bool)()
    var1173(byref(var1174), byref(obj), )
    return var1174

wrappers["can__size_as_observation_tensor_impl"].append(rl_can__size_as_observation_tensor_impl__BIntT0T3T_9_r_bool)
signatures[rl_can__size_as_observation_tensor_impl__BIntT0T3T_9_r_bool] = [builtins.bool,  list , ]
@overload
def _size_as_observation_tensor_impl(obj: builtins.bool) -> builtins.int:
    pass

def rl__size_as_observation_tensor_impl__bool_r_int64_t(obj: builtins.bool) -> builtins.int:
    var1175 = lib.rl__size_as_observation_tensor_impl__bool_r_int64_t
    var1176 = c_bool(obj)
    var1177 = (c_longlong)()
    var1175(byref(var1177), byref(var1176), )
    var1178 = var1177.value
    return var1178

wrappers["_size_as_observation_tensor_impl"].append(rl__size_as_observation_tensor_impl__bool_r_int64_t)
signatures[rl__size_as_observation_tensor_impl__bool_r_int64_t] = [builtins.int, builtins.bool, ]
@overload
def can__size_as_observation_tensor_impl(obj: builtins.bool) -> builtins.bool:
    pass

def rl_can__size_as_observation_tensor_impl__bool_r_bool(obj: builtins.bool) -> builtins.bool:
    var1179 = lib.rl_can__size_as_observation_tensor_impl__bool_r_bool
    var1180 = c_bool(obj)
    var1181 = (c_bool)()
    var1179(byref(var1181), byref(var1180), )
    return var1181

wrappers["can__size_as_observation_tensor_impl"].append(rl_can__size_as_observation_tensor_impl__bool_r_bool)
signatures[rl_can__size_as_observation_tensor_impl__bool_r_bool] = [builtins.bool, builtins.bool, ]
@overload
def _size_as_observation_tensor_impl(obj: BIntT0T3T) -> builtins.int:
    pass

def rl__size_as_observation_tensor_impl__BIntT0T3T_r_int64_t(obj: BIntT0T3T) -> builtins.int:
    var1182 = lib.rl__size_as_observation_tensor_impl__BIntT0T3T_r_int64_t
    var1183 = (c_longlong)()
    var1182(byref(var1183), byref(obj), )
    var1184 = var1183.value
    return var1184

wrappers["_size_as_observation_tensor_impl"].append(rl__size_as_observation_tensor_impl__BIntT0T3T_r_int64_t)
signatures[rl__size_as_observation_tensor_impl__BIntT0T3T_r_int64_t] = [builtins.int, BIntT0T3T, ]
@overload
def can__size_as_observation_tensor_impl(obj: BIntT0T3T) -> builtins.bool:
    pass

def rl_can__size_as_observation_tensor_impl__BIntT0T3T_r_bool(obj: BIntT0T3T) -> builtins.bool:
    var1185 = lib.rl_can__size_as_observation_tensor_impl__BIntT0T3T_r_bool
    var1186 = (c_bool)()
    var1185(byref(var1186), byref(obj), )
    return var1186

wrappers["can__size_as_observation_tensor_impl"].append(rl_can__size_as_observation_tensor_impl__BIntT0T3T_r_bool)
signatures[rl_can__size_as_observation_tensor_impl__BIntT0T3T_r_bool] = [builtins.bool, BIntT0T3T, ]
@overload
def _to_observation_tensor(obj: Game, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t(obj: Game, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1187 = lib.rl__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t
    var1188 = c_longlong(observer_id)
    var1189 = c_longlong(index)
    var1187(byref(obj), byref(var1188), byref(output), byref(var1189), )
    return

wrappers["_to_observation_tensor"].append(rl__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t)
signatures[rl__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t] = [None, Game, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can__to_observation_tensor(obj: Game, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t_r_bool(obj: Game, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1190 = lib.rl_can__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t_r_bool
    var1191 = c_longlong(observer_id)
    var1192 = c_longlong(index)
    var1193 = (c_bool)()
    var1190(byref(var1193), byref(obj), byref(var1191), byref(output), byref(var1192), )
    return var1193

wrappers["can__to_observation_tensor"].append(rl_can__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, Game, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def _to_observation_tensor(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1194 = lib.rl__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t
    var1195 = c_longlong(obj)
    var1196 = c_longlong(observer_id)
    var1197 = c_longlong(index)
    var1194(byref(var1195), byref(var1196), byref(output), byref(var1197), )
    return

wrappers["_to_observation_tensor"].append(rl__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t)
signatures[rl__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t] = [None, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can__to_observation_tensor(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool(obj: builtins.int, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1198 = lib.rl_can__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool
    var1199 = c_longlong(obj)
    var1200 = c_longlong(observer_id)
    var1201 = c_longlong(index)
    var1202 = (c_bool)()
    var1198(byref(var1202), byref(var1199), byref(var1200), byref(output), byref(var1201), )
    return var1202

wrappers["can__to_observation_tensor"].append(rl_can__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.int, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def _to_observation_tensor(obj: Board, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t(obj: Board, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1203 = lib.rl__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t
    var1204 = c_longlong(observer_id)
    var1205 = c_longlong(index)
    var1203(byref(obj), byref(var1204), byref(output), byref(var1205), )
    return

wrappers["_to_observation_tensor"].append(rl__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t)
signatures[rl__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t] = [None, Board, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can__to_observation_tensor(obj: Board, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t_r_bool(obj: Board, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1206 = lib.rl_can__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t_r_bool
    var1207 = c_longlong(observer_id)
    var1208 = c_longlong(index)
    var1209 = (c_bool)()
    var1206(byref(var1209), byref(obj), byref(var1207), byref(output), byref(var1208), )
    return var1209

wrappers["can__to_observation_tensor"].append(rl_can__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, Board, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def _to_observation_tensor(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1210 = lib.rl__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t
    var1211 = c_longlong(observer_id)
    var1212 = c_longlong(index)
    var1210(byref(obj), byref(var1211), byref(output), byref(var1212), )
    return

wrappers["_to_observation_tensor"].append(rl__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t)
signatures[rl__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t] = [None,  list , builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can__to_observation_tensor(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool(obj:  list , observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1213 = lib.rl_can__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool
    var1214 = c_longlong(observer_id)
    var1215 = c_longlong(index)
    var1216 = (c_bool)()
    var1213(byref(var1216), byref(obj), byref(var1214), byref(output), byref(var1215), )
    return var1216

wrappers["can__to_observation_tensor"].append(rl_can__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool,  list , builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def _to_observation_tensor(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1217 = lib.rl__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t
    var1218 = c_bool(obj)
    var1219 = c_longlong(observer_id)
    var1220 = c_longlong(index)
    var1217(byref(var1218), byref(var1219), byref(output), byref(var1220), )
    return

wrappers["_to_observation_tensor"].append(rl__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t)
signatures[rl__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t] = [None, builtins.bool, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can__to_observation_tensor(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool(obj: builtins.bool, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1221 = lib.rl_can__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool
    var1222 = c_bool(obj)
    var1223 = c_longlong(observer_id)
    var1224 = c_longlong(index)
    var1225 = (c_bool)()
    var1221(byref(var1225), byref(var1222), byref(var1223), byref(output), byref(var1224), )
    return var1225

wrappers["can__to_observation_tensor"].append(rl_can__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, builtins.bool, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def _to_observation_tensor(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    pass

def rl__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> None:
    var1226 = lib.rl__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t
    var1227 = c_longlong(observer_id)
    var1228 = c_longlong(index)
    var1226(byref(obj), byref(var1227), byref(output), byref(var1228), )
    return

wrappers["_to_observation_tensor"].append(rl__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t)
signatures[rl__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t] = [None, BIntT0T3T, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def can__to_observation_tensor(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    pass

def rl_can__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool(obj: BIntT0T3T, observer_id: builtins.int, output: VectorTdoubleT, index: builtins.int) -> builtins.bool:
    var1229 = lib.rl_can__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool
    var1230 = c_longlong(observer_id)
    var1231 = c_longlong(index)
    var1232 = (c_bool)()
    var1229(byref(var1232), byref(obj), byref(var1230), byref(output), byref(var1231), )
    return var1232

wrappers["can__to_observation_tensor"].append(rl_can__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool)
signatures[rl_can__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool] = [builtins.bool, BIntT0T3T, builtins.int, VectorTdoubleT, builtins.int, ]
@overload
def to_observation_tensor(obj: Game, observer_id: builtins.int, output: VectorTdoubleT) -> None:
    pass

def rl_to_observation_tensor__Game_int64_t_VectorTdoubleT(obj: Game, observer_id: builtins.int, output: VectorTdoubleT) -> None:
    var1233 = lib.rl_to_observation_tensor__Game_int64_t_VectorTdoubleT
    var1234 = c_longlong(observer_id)
    var1233(byref(obj), byref(var1234), byref(output), )
    return

wrappers["to_observation_tensor"].append(rl_to_observation_tensor__Game_int64_t_VectorTdoubleT)
signatures[rl_to_observation_tensor__Game_int64_t_VectorTdoubleT] = [None, Game, builtins.int, VectorTdoubleT, ]
@overload
def can_to_observation_tensor(obj: Game, observer_id: builtins.int, output: VectorTdoubleT) -> builtins.bool:
    pass

def rl_can_to_observation_tensor__Game_int64_t_VectorTdoubleT_r_bool(obj: Game, observer_id: builtins.int, output: VectorTdoubleT) -> builtins.bool:
    var1235 = lib.rl_can_to_observation_tensor__Game_int64_t_VectorTdoubleT_r_bool
    var1236 = c_longlong(observer_id)
    var1237 = (c_bool)()
    var1235(byref(var1237), byref(obj), byref(var1236), byref(output), )
    return var1237

wrappers["can_to_observation_tensor"].append(rl_can_to_observation_tensor__Game_int64_t_VectorTdoubleT_r_bool)
signatures[rl_can_to_observation_tensor__Game_int64_t_VectorTdoubleT_r_bool] = [builtins.bool, Game, builtins.int, VectorTdoubleT, ]
@overload
def observation_tensor_size(obj: Game) -> builtins.int:
    pass

def rl_observation_tensor_size__Game_r_int64_t(obj: Game) -> builtins.int:
    var1238 = lib.rl_observation_tensor_size__Game_r_int64_t
    var1239 = (c_longlong)()
    var1238(byref(var1239), byref(obj), )
    var1240 = var1239.value
    return var1240

wrappers["observation_tensor_size"].append(rl_observation_tensor_size__Game_r_int64_t)
signatures[rl_observation_tensor_size__Game_r_int64_t] = [builtins.int, Game, ]
@overload
def can_observation_tensor_size(obj: Game) -> builtins.bool:
    pass

def rl_can_observation_tensor_size__Game_r_bool(obj: Game) -> builtins.bool:
    var1241 = lib.rl_can_observation_tensor_size__Game_r_bool
    var1242 = (c_bool)()
    var1241(byref(var1242), byref(obj), )
    return var1242

wrappers["can_observation_tensor_size"].append(rl_can_observation_tensor_size__Game_r_bool)
signatures[rl_can_observation_tensor_size__Game_r_bool] = [builtins.bool, Game, ]
@overload
def write_tensor_warning_context(out: String, context: VectorTStringT) -> None:
    pass

def rl_write_tensor_warning_context__String_VectorTStringT(out: String, context: VectorTStringT) -> None:
    var1243 = lib.rl_write_tensor_warning_context__String_VectorTStringT
    var1243(byref(out), byref(context), )
    return

wrappers["write_tensor_warning_context"].append(rl_write_tensor_warning_context__String_VectorTStringT)
signatures[rl_write_tensor_warning_context__String_VectorTStringT] = [None, String, VectorTStringT, ]
@overload
def can_write_tensor_warning_context(out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_write_tensor_warning_context__String_VectorTStringT_r_bool(out: String, context: VectorTStringT) -> builtins.bool:
    var1244 = lib.rl_can_write_tensor_warning_context__String_VectorTStringT_r_bool
    var1245 = (c_bool)()
    var1244(byref(var1245), byref(out), byref(context), )
    return var1245

wrappers["can_write_tensor_warning_context"].append(rl_can_write_tensor_warning_context__String_VectorTStringT_r_bool)
signatures[rl_can_write_tensor_warning_context__String_VectorTStringT_r_bool] = [builtins.bool, String, VectorTStringT, ]
@overload
def tensorable_warning(x: builtins.int, out: String, context: VectorTStringT) -> None:
    pass

def rl_tensorable_warning__int64_t_String_VectorTStringT(x: builtins.int, out: String, context: VectorTStringT) -> None:
    var1246 = lib.rl_tensorable_warning__int64_t_String_VectorTStringT
    var1247 = c_longlong(x)
    var1246(byref(var1247), byref(out), byref(context), )
    return

wrappers["tensorable_warning"].append(rl_tensorable_warning__int64_t_String_VectorTStringT)
signatures[rl_tensorable_warning__int64_t_String_VectorTStringT] = [None, builtins.int, String, VectorTStringT, ]
@overload
def can_tensorable_warning(x: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_tensorable_warning__int64_t_String_VectorTStringT_r_bool(x: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    var1248 = lib.rl_can_tensorable_warning__int64_t_String_VectorTStringT_r_bool
    var1249 = c_longlong(x)
    var1250 = (c_bool)()
    var1248(byref(var1250), byref(var1249), byref(out), byref(context), )
    return var1250

wrappers["can_tensorable_warning"].append(rl_can_tensorable_warning__int64_t_String_VectorTStringT_r_bool)
signatures[rl_can_tensorable_warning__int64_t_String_VectorTStringT_r_bool] = [builtins.bool, builtins.int, String, VectorTStringT, ]
@overload
def tensorable_warning(x: builtins.float, out: String, context: VectorTStringT) -> None:
    pass

def rl_tensorable_warning__double_String_VectorTStringT(x: builtins.float, out: String, context: VectorTStringT) -> None:
    var1251 = lib.rl_tensorable_warning__double_String_VectorTStringT
    var1252 = c_double(x)
    var1251(byref(var1252), byref(out), byref(context), )
    return

wrappers["tensorable_warning"].append(rl_tensorable_warning__double_String_VectorTStringT)
signatures[rl_tensorable_warning__double_String_VectorTStringT] = [None, builtins.float, String, VectorTStringT, ]
@overload
def can_tensorable_warning(x: builtins.float, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_tensorable_warning__double_String_VectorTStringT_r_bool(x: builtins.float, out: String, context: VectorTStringT) -> builtins.bool:
    var1253 = lib.rl_can_tensorable_warning__double_String_VectorTStringT_r_bool
    var1254 = c_double(x)
    var1255 = (c_bool)()
    var1253(byref(var1255), byref(var1254), byref(out), byref(context), )
    return var1255

wrappers["can_tensorable_warning"].append(rl_can_tensorable_warning__double_String_VectorTStringT_r_bool)
signatures[rl_can_tensorable_warning__double_String_VectorTStringT_r_bool] = [builtins.bool, builtins.float, String, VectorTStringT, ]
@overload
def tensorable_warning(x:  list , out: String, context: VectorTStringT) -> None:
    pass

def rl_tensorable_warning__BIntT0T3T_9_String_VectorTStringT(x:  list , out: String, context: VectorTStringT) -> None:
    var1256 = lib.rl_tensorable_warning__BIntT0T3T_9_String_VectorTStringT
    var1256(byref(x), byref(out), byref(context), )
    return

wrappers["tensorable_warning"].append(rl_tensorable_warning__BIntT0T3T_9_String_VectorTStringT)
signatures[rl_tensorable_warning__BIntT0T3T_9_String_VectorTStringT] = [None,  list , String, VectorTStringT, ]
@overload
def can_tensorable_warning(x:  list , out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can_tensorable_warning__BIntT0T3T_9_String_VectorTStringT_r_bool(x:  list , out: String, context: VectorTStringT) -> builtins.bool:
    var1257 = lib.rl_can_tensorable_warning__BIntT0T3T_9_String_VectorTStringT_r_bool
    var1258 = (c_bool)()
    var1257(byref(var1258), byref(x), byref(out), byref(context), )
    return var1258

wrappers["can_tensorable_warning"].append(rl_can_tensorable_warning__BIntT0T3T_9_String_VectorTStringT_r_bool)
signatures[rl_can_tensorable_warning__BIntT0T3T_9_String_VectorTStringT_r_bool] = [builtins.bool,  list , String, VectorTStringT, ]
@overload
def _observation_tensor_warnings(obj: Game, out: String, context: VectorTStringT) -> None:
    pass

def rl__observation_tensor_warnings__Game_String_VectorTStringT(obj: Game, out: String, context: VectorTStringT) -> None:
    var1259 = lib.rl__observation_tensor_warnings__Game_String_VectorTStringT
    var1259(byref(obj), byref(out), byref(context), )
    return

wrappers["_observation_tensor_warnings"].append(rl__observation_tensor_warnings__Game_String_VectorTStringT)
signatures[rl__observation_tensor_warnings__Game_String_VectorTStringT] = [None, Game, String, VectorTStringT, ]
@overload
def can__observation_tensor_warnings(obj: Game, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can__observation_tensor_warnings__Game_String_VectorTStringT_r_bool(obj: Game, out: String, context: VectorTStringT) -> builtins.bool:
    var1260 = lib.rl_can__observation_tensor_warnings__Game_String_VectorTStringT_r_bool
    var1261 = (c_bool)()
    var1260(byref(var1261), byref(obj), byref(out), byref(context), )
    return var1261

wrappers["can__observation_tensor_warnings"].append(rl_can__observation_tensor_warnings__Game_String_VectorTStringT_r_bool)
signatures[rl_can__observation_tensor_warnings__Game_String_VectorTStringT_r_bool] = [builtins.bool, Game, String, VectorTStringT, ]
@overload
def _observation_tensor_warnings(obj: builtins.int, out: String, context: VectorTStringT) -> None:
    pass

def rl__observation_tensor_warnings__int64_t_String_VectorTStringT(obj: builtins.int, out: String, context: VectorTStringT) -> None:
    var1262 = lib.rl__observation_tensor_warnings__int64_t_String_VectorTStringT
    var1263 = c_longlong(obj)
    var1262(byref(var1263), byref(out), byref(context), )
    return

wrappers["_observation_tensor_warnings"].append(rl__observation_tensor_warnings__int64_t_String_VectorTStringT)
signatures[rl__observation_tensor_warnings__int64_t_String_VectorTStringT] = [None, builtins.int, String, VectorTStringT, ]
@overload
def can__observation_tensor_warnings(obj: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can__observation_tensor_warnings__int64_t_String_VectorTStringT_r_bool(obj: builtins.int, out: String, context: VectorTStringT) -> builtins.bool:
    var1264 = lib.rl_can__observation_tensor_warnings__int64_t_String_VectorTStringT_r_bool
    var1265 = c_longlong(obj)
    var1266 = (c_bool)()
    var1264(byref(var1266), byref(var1265), byref(out), byref(context), )
    return var1266

wrappers["can__observation_tensor_warnings"].append(rl_can__observation_tensor_warnings__int64_t_String_VectorTStringT_r_bool)
signatures[rl_can__observation_tensor_warnings__int64_t_String_VectorTStringT_r_bool] = [builtins.bool, builtins.int, String, VectorTStringT, ]
@overload
def _observation_tensor_warnings(obj: Board, out: String, context: VectorTStringT) -> None:
    pass

def rl__observation_tensor_warnings__Board_String_VectorTStringT(obj: Board, out: String, context: VectorTStringT) -> None:
    var1267 = lib.rl__observation_tensor_warnings__Board_String_VectorTStringT
    var1267(byref(obj), byref(out), byref(context), )
    return

wrappers["_observation_tensor_warnings"].append(rl__observation_tensor_warnings__Board_String_VectorTStringT)
signatures[rl__observation_tensor_warnings__Board_String_VectorTStringT] = [None, Board, String, VectorTStringT, ]
@overload
def can__observation_tensor_warnings(obj: Board, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can__observation_tensor_warnings__Board_String_VectorTStringT_r_bool(obj: Board, out: String, context: VectorTStringT) -> builtins.bool:
    var1268 = lib.rl_can__observation_tensor_warnings__Board_String_VectorTStringT_r_bool
    var1269 = (c_bool)()
    var1268(byref(var1269), byref(obj), byref(out), byref(context), )
    return var1269

wrappers["can__observation_tensor_warnings"].append(rl_can__observation_tensor_warnings__Board_String_VectorTStringT_r_bool)
signatures[rl_can__observation_tensor_warnings__Board_String_VectorTStringT_r_bool] = [builtins.bool, Board, String, VectorTStringT, ]
@overload
def _observation_tensor_warnings(obj:  list , out: String, context: VectorTStringT) -> None:
    pass

def rl__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT(obj:  list , out: String, context: VectorTStringT) -> None:
    var1270 = lib.rl__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT
    var1270(byref(obj), byref(out), byref(context), )
    return

wrappers["_observation_tensor_warnings"].append(rl__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT)
signatures[rl__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT] = [None,  list , String, VectorTStringT, ]
@overload
def can__observation_tensor_warnings(obj:  list , out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT_r_bool(obj:  list , out: String, context: VectorTStringT) -> builtins.bool:
    var1271 = lib.rl_can__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT_r_bool
    var1272 = (c_bool)()
    var1271(byref(var1272), byref(obj), byref(out), byref(context), )
    return var1272

wrappers["can__observation_tensor_warnings"].append(rl_can__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT_r_bool)
signatures[rl_can__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT_r_bool] = [builtins.bool,  list , String, VectorTStringT, ]
@overload
def _observation_tensor_warnings(obj: builtins.bool, out: String, context: VectorTStringT) -> None:
    pass

def rl__observation_tensor_warnings__bool_String_VectorTStringT(obj: builtins.bool, out: String, context: VectorTStringT) -> None:
    var1273 = lib.rl__observation_tensor_warnings__bool_String_VectorTStringT
    var1274 = c_bool(obj)
    var1273(byref(var1274), byref(out), byref(context), )
    return

wrappers["_observation_tensor_warnings"].append(rl__observation_tensor_warnings__bool_String_VectorTStringT)
signatures[rl__observation_tensor_warnings__bool_String_VectorTStringT] = [None, builtins.bool, String, VectorTStringT, ]
@overload
def can__observation_tensor_warnings(obj: builtins.bool, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can__observation_tensor_warnings__bool_String_VectorTStringT_r_bool(obj: builtins.bool, out: String, context: VectorTStringT) -> builtins.bool:
    var1275 = lib.rl_can__observation_tensor_warnings__bool_String_VectorTStringT_r_bool
    var1276 = c_bool(obj)
    var1277 = (c_bool)()
    var1275(byref(var1277), byref(var1276), byref(out), byref(context), )
    return var1277

wrappers["can__observation_tensor_warnings"].append(rl_can__observation_tensor_warnings__bool_String_VectorTStringT_r_bool)
signatures[rl_can__observation_tensor_warnings__bool_String_VectorTStringT_r_bool] = [builtins.bool, builtins.bool, String, VectorTStringT, ]
@overload
def _observation_tensor_warnings(obj: BIntT0T3T, out: String, context: VectorTStringT) -> None:
    pass

def rl__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT(obj: BIntT0T3T, out: String, context: VectorTStringT) -> None:
    var1278 = lib.rl__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT
    var1278(byref(obj), byref(out), byref(context), )
    return

wrappers["_observation_tensor_warnings"].append(rl__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT)
signatures[rl__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT] = [None, BIntT0T3T, String, VectorTStringT, ]
@overload
def can__observation_tensor_warnings(obj: BIntT0T3T, out: String, context: VectorTStringT) -> builtins.bool:
    pass

def rl_can__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT_r_bool(obj: BIntT0T3T, out: String, context: VectorTStringT) -> builtins.bool:
    var1279 = lib.rl_can__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT_r_bool
    var1280 = (c_bool)()
    var1279(byref(var1280), byref(obj), byref(out), byref(context), )
    return var1280

wrappers["can__observation_tensor_warnings"].append(rl_can__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT_r_bool)
signatures[rl_can__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT_r_bool] = [builtins.bool, BIntT0T3T, String, VectorTStringT, ]
@overload
def to_observation_tensor_warnings(obj: Game) -> String:
    pass

def rl_to_observation_tensor_warnings__Game_r_String(obj: Game) -> String:
    var1281 = lib.rl_to_observation_tensor_warnings__Game_r_String
    var1282 = (String)()
    var1281(byref(var1282), byref(obj), )
    return var1282

wrappers["to_observation_tensor_warnings"].append(rl_to_observation_tensor_warnings__Game_r_String)
signatures[rl_to_observation_tensor_warnings__Game_r_String] = [String, Game, ]
@overload
def can_to_observation_tensor_warnings(obj: Game) -> builtins.bool:
    pass

def rl_can_to_observation_tensor_warnings__Game_r_bool(obj: Game) -> builtins.bool:
    var1283 = lib.rl_can_to_observation_tensor_warnings__Game_r_bool
    var1284 = (c_bool)()
    var1283(byref(var1284), byref(obj), )
    return var1284

wrappers["can_to_observation_tensor_warnings"].append(rl_can_to_observation_tensor_warnings__Game_r_bool)
signatures[rl_can_to_observation_tensor_warnings__Game_r_bool] = [builtins.bool, Game, ]
@overload
def emit_observation_tensor_warnings(obj: Game) -> None:
    pass

def rl_emit_observation_tensor_warnings__Game(obj: Game) -> None:
    var1285 = lib.rl_emit_observation_tensor_warnings__Game
    var1285(byref(obj), )
    return

wrappers["emit_observation_tensor_warnings"].append(rl_emit_observation_tensor_warnings__Game)
signatures[rl_emit_observation_tensor_warnings__Game] = [None, Game, ]
@overload
def can_emit_observation_tensor_warnings(obj: Game) -> builtins.bool:
    pass

def rl_can_emit_observation_tensor_warnings__Game_r_bool(obj: Game) -> builtins.bool:
    var1286 = lib.rl_can_emit_observation_tensor_warnings__Game_r_bool
    var1287 = (c_bool)()
    var1286(byref(var1287), byref(obj), )
    return var1287

wrappers["can_emit_observation_tensor_warnings"].append(rl_can_emit_observation_tensor_warnings__Game_r_bool)
signatures[rl_can_emit_observation_tensor_warnings__Game_r_bool] = [builtins.bool, Game, ]
@overload
def gen_printer_parser() -> None:
    pass

def rl_gen_printer_parser_() -> None:
    var1288 = lib.rl_gen_printer_parser_
    var1288()
    return

wrappers["gen_printer_parser"].append(rl_gen_printer_parser_)
signatures[rl_gen_printer_parser_] = [None, ]
@overload
def can_gen_printer_parser() -> builtins.bool:
    pass

def rl_can_gen_printer_parser__r_bool() -> builtins.bool:
    var1289 = lib.rl_can_gen_printer_parser__r_bool
    var1290 = (c_bool)()
    var1289(byref(var1290), )
    return var1290

wrappers["can_gen_printer_parser"].append(rl_can_gen_printer_parser__r_bool)
signatures[rl_can_gen_printer_parser__r_bool] = [builtins.bool, ]
@overload
def next_turn(self: Board) -> None:
    pass

def rl_m_next_turn__Board(self: Board) -> None:
    var1291 = lib.rl_m_next_turn__Board
    var1291(byref(self), )
    return

wrappers["next_turn"].append(rl_m_next_turn__Board)
signatures[rl_m_next_turn__Board] = [None, Board, ]
@overload
def can_next_turn(self: Board) -> builtins.bool:
    pass

def rl_m_can_next_turn__Board_r_bool(self: Board) -> builtins.bool:
    var1292 = lib.rl_m_can_next_turn__Board_r_bool
    var1293 = (c_bool)()
    var1292(byref(var1293), byref(self), )
    return var1293

wrappers["can_next_turn"].append(rl_m_can_next_turn__Board_r_bool)
signatures[rl_m_can_next_turn__Board_r_bool] = [builtins.bool, Board, ]
@overload
def current_player(self: Board) -> builtins.int:
    pass

def rl_m_current_player__Board_r_int64_t(self: Board) -> builtins.int:
    var1294 = lib.rl_m_current_player__Board_r_int64_t
    var1295 = (c_longlong)()
    var1294(byref(var1295), byref(self), )
    var1296 = var1295.value
    return var1296

wrappers["current_player"].append(rl_m_current_player__Board_r_int64_t)
signatures[rl_m_current_player__Board_r_int64_t] = [builtins.int, Board, ]
@overload
def can_current_player(self: Board) -> builtins.bool:
    pass

def rl_m_can_current_player__Board_r_bool(self: Board) -> builtins.bool:
    var1297 = lib.rl_m_can_current_player__Board_r_bool
    var1298 = (c_bool)()
    var1297(byref(var1298), byref(self), )
    return var1298

wrappers["can_current_player"].append(rl_m_can_current_player__Board_r_bool)
signatures[rl_m_can_current_player__Board_r_bool] = [builtins.bool, Board, ]
@overload
def three_in_a_line_player(self: Board, player_id: builtins.int) -> builtins.bool:
    pass

def rl_m_three_in_a_line_player__Board_int64_t_r_bool(self: Board, player_id: builtins.int) -> builtins.bool:
    var1299 = lib.rl_m_three_in_a_line_player__Board_int64_t_r_bool
    var1300 = c_longlong(player_id)
    var1301 = (c_bool)()
    var1299(byref(var1301), byref(self), byref(var1300), )
    return var1301

wrappers["three_in_a_line_player"].append(rl_m_three_in_a_line_player__Board_int64_t_r_bool)
signatures[rl_m_three_in_a_line_player__Board_int64_t_r_bool] = [builtins.bool, Board, builtins.int, ]
@overload
def can_three_in_a_line_player(self: Board, player_id: builtins.int) -> builtins.bool:
    pass

def rl_m_can_three_in_a_line_player__Board_int64_t_r_bool(self: Board, player_id: builtins.int) -> builtins.bool:
    var1302 = lib.rl_m_can_three_in_a_line_player__Board_int64_t_r_bool
    var1303 = c_longlong(player_id)
    var1304 = (c_bool)()
    var1302(byref(var1304), byref(self), byref(var1303), )
    return var1304

wrappers["can_three_in_a_line_player"].append(rl_m_can_three_in_a_line_player__Board_int64_t_r_bool)
signatures[rl_m_can_three_in_a_line_player__Board_int64_t_r_bool] = [builtins.bool, Board, builtins.int, ]
@overload
def three_in_a_line_player_row(self: Board, player_id: builtins.int, row: builtins.int) -> builtins.bool:
    pass

def rl_m_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool(self: Board, player_id: builtins.int, row: builtins.int) -> builtins.bool:
    var1305 = lib.rl_m_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool
    var1306 = c_longlong(player_id)
    var1307 = c_longlong(row)
    var1308 = (c_bool)()
    var1305(byref(var1308), byref(self), byref(var1306), byref(var1307), )
    return var1308

wrappers["three_in_a_line_player_row"].append(rl_m_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool)
signatures[rl_m_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool] = [builtins.bool, Board, builtins.int, builtins.int, ]
@overload
def can_three_in_a_line_player_row(self: Board, player_id: builtins.int, row: builtins.int) -> builtins.bool:
    pass

def rl_m_can_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool(self: Board, player_id: builtins.int, row: builtins.int) -> builtins.bool:
    var1309 = lib.rl_m_can_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool
    var1310 = c_longlong(player_id)
    var1311 = c_longlong(row)
    var1312 = (c_bool)()
    var1309(byref(var1312), byref(self), byref(var1310), byref(var1311), )
    return var1312

wrappers["can_three_in_a_line_player_row"].append(rl_m_can_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool)
signatures[rl_m_can_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool] = [builtins.bool, Board, builtins.int, builtins.int, ]
@overload
def full(self: Board) -> builtins.bool:
    pass

def rl_m_full__Board_r_bool(self: Board) -> builtins.bool:
    var1313 = lib.rl_m_full__Board_r_bool
    var1314 = (c_bool)()
    var1313(byref(var1314), byref(self), )
    return var1314

wrappers["full"].append(rl_m_full__Board_r_bool)
signatures[rl_m_full__Board_r_bool] = [builtins.bool, Board, ]
@overload
def can_full(self: Board) -> builtins.bool:
    pass

def rl_m_can_full__Board_r_bool(self: Board) -> builtins.bool:
    var1315 = lib.rl_m_can_full__Board_r_bool
    var1316 = (c_bool)()
    var1315(byref(var1316), byref(self), )
    return var1316

wrappers["can_full"].append(rl_m_can_full__Board_r_bool)
signatures[rl_m_can_full__Board_r_bool] = [builtins.bool, Board, ]
@overload
def set(self: Board, x: builtins.int, y: builtins.int, val: builtins.int) -> None:
    pass

def rl_m_set__Board_int64_t_int64_t_int64_t(self: Board, x: builtins.int, y: builtins.int, val: builtins.int) -> None:
    var1317 = lib.rl_m_set__Board_int64_t_int64_t_int64_t
    var1318 = c_longlong(x)
    var1319 = c_longlong(y)
    var1320 = c_longlong(val)
    var1317(byref(self), byref(var1318), byref(var1319), byref(var1320), )
    return

wrappers["set"].append(rl_m_set__Board_int64_t_int64_t_int64_t)
signatures[rl_m_set__Board_int64_t_int64_t_int64_t] = [None, Board, builtins.int, builtins.int, builtins.int, ]
@overload
def can_set(self: Board, x: builtins.int, y: builtins.int, val: builtins.int) -> builtins.bool:
    pass

def rl_m_can_set__Board_int64_t_int64_t_int64_t_r_bool(self: Board, x: builtins.int, y: builtins.int, val: builtins.int) -> builtins.bool:
    var1321 = lib.rl_m_can_set__Board_int64_t_int64_t_int64_t_r_bool
    var1322 = c_longlong(x)
    var1323 = c_longlong(y)
    var1324 = c_longlong(val)
    var1325 = (c_bool)()
    var1321(byref(var1325), byref(self), byref(var1322), byref(var1323), byref(var1324), )
    return var1325

wrappers["can_set"].append(rl_m_can_set__Board_int64_t_int64_t_int64_t_r_bool)
signatures[rl_m_can_set__Board_int64_t_int64_t_int64_t_r_bool] = [builtins.bool, Board, builtins.int, builtins.int, builtins.int, ]
@overload
def get(self: Board, x: builtins.int, y: builtins.int) -> builtins.int:
    pass

def rl_m_get__Board_int64_t_int64_t_r_int64_t(self: Board, x: builtins.int, y: builtins.int) -> builtins.int:
    var1326 = lib.rl_m_get__Board_int64_t_int64_t_r_int64_t
    var1327 = c_longlong(x)
    var1328 = c_longlong(y)
    var1329 = (c_longlong)()
    var1326(byref(var1329), byref(self), byref(var1327), byref(var1328), )
    var1330 = var1329.value
    return var1330

wrappers["get"].append(rl_m_get__Board_int64_t_int64_t_r_int64_t)
signatures[rl_m_get__Board_int64_t_int64_t_r_int64_t] = [builtins.int, Board, builtins.int, builtins.int, ]
@overload
def can_get(self: Board, x: builtins.int, y: builtins.int) -> builtins.bool:
    pass

def rl_m_can_get__Board_int64_t_int64_t_r_bool(self: Board, x: builtins.int, y: builtins.int) -> builtins.bool:
    var1331 = lib.rl_m_can_get__Board_int64_t_int64_t_r_bool
    var1332 = c_longlong(x)
    var1333 = c_longlong(y)
    var1334 = (c_bool)()
    var1331(byref(var1334), byref(self), byref(var1332), byref(var1333), )
    return var1334

wrappers["can_get"].append(rl_m_can_get__Board_int64_t_int64_t_r_bool)
signatures[rl_m_can_get__Board_int64_t_int64_t_r_bool] = [builtins.bool, Board, builtins.int, builtins.int, ]
@overload
def apply(self: GameMark, frame: Game):
    pass

def rl_apply__GameMark_Game(self: GameMark, frame: Game):
    var1335 = lib.rl_apply__GameMark_Game
    var1335(byref(self), byref(frame), )
    return

wrappers["apply"].append(rl_apply__GameMark_Game)
signatures[rl_apply__GameMark_Game] = [None, GameMark, Game, ]
@overload
def can_apply(self: GameMark, frame: Game) -> builtins.bool:
    pass

def rl_can_apply__GameMark_Game_r_bool(self: GameMark, frame: Game) -> builtins.bool:
    var1336 = lib.rl_can_apply__GameMark_Game_r_bool
    var1337 = (c_bool)()
    var1336(byref(var1337), byref(self), byref(frame), )
    return var1337

wrappers["can_apply"].append(rl_can_apply__GameMark_Game_r_bool)
signatures[rl_can_apply__GameMark_Game_r_bool] = [builtins.bool, GameMark, Game, ]
@overload
def get_type_name(self: GameMark) -> builtins.str:
    pass

def rl_get_type_name__GameMark_r_strlit(self: GameMark) -> builtins.str:
    var1338 = lib.rl_get_type_name__GameMark_r_strlit
    var1339 = (builtins.str)()
    var1338(byref(var1339), byref(self), )
    var1340 = var1339.value
    return var1340

wrappers["get_type_name"].append(rl_get_type_name__GameMark_r_strlit)
signatures[rl_get_type_name__GameMark_r_strlit] = [builtins.str, GameMark, ]
@overload
def can_get_type_name(self: GameMark) -> builtins.bool:
    pass

def rl_can_get_type_name__GameMark_r_bool(self: GameMark) -> builtins.bool:
    var1341 = lib.rl_can_get_type_name__GameMark_r_bool
    var1342 = (c_bool)()
    var1341(byref(var1342), byref(self), )
    return var1342

wrappers["can_get_type_name"].append(rl_can_get_type_name__GameMark_r_bool)
signatures[rl_can_get_type_name__GameMark_r_bool] = [builtins.bool, GameMark, ]
actionToAnyFunctionType["play"] = AnyGameAction

@overload
def play() -> Game:
    pass

def rl_play__r_Game() -> Game:
    var1343 = lib.rl_play__r_Game
    var1344 = (Game)()
    var1343(byref(var1344), )
    return var1344

wrappers["play"].append(rl_play__r_Game)
signatures[rl_play__r_Game] = [Game, ]
actions["play"].append(rl_play__r_Game)
args_info[rl_play__r_Game] = []

@overload
def mark(frame: Game, x: BIntT0T3T, y: BIntT0T3T):
    pass

def rl_m_mark__Game_BIntT0T3T_BIntT0T3T(frame: Game, x: BIntT0T3T, y: BIntT0T3T):
    var1345 = lib.rl_m_mark__Game_BIntT0T3T_BIntT0T3T
    var1345(byref(frame), byref(x), byref(y), )
    return

wrappers["mark"].append(rl_m_mark__Game_BIntT0T3T_BIntT0T3T)
signatures[rl_m_mark__Game_BIntT0T3T_BIntT0T3T] = [None, Game, BIntT0T3T, BIntT0T3T, ]
actions["mark"].append(rl_m_mark__Game_BIntT0T3T_BIntT0T3T)
args_info[rl_m_mark__Game_BIntT0T3T_BIntT0T3T] = [None, (-9223372036854775808, 9223372036854775807), (-9223372036854775808, 9223372036854775807), ]

@overload
def can_mark(frame: Game, x: BIntT0T3T, y: BIntT0T3T) -> builtins.bool:
    pass

def rl_m_can_mark__Game_BIntT0T3T_BIntT0T3T_r_bool(frame: Game, x: BIntT0T3T, y: BIntT0T3T) -> builtins.bool:
    var1346 = lib.rl_m_can_mark__Game_BIntT0T3T_BIntT0T3T_r_bool
    var1347 = (c_bool)()
    var1346(byref(var1347), byref(frame), byref(x), byref(y), )
    return var1347

wrappers["can_mark"].append(rl_m_can_mark__Game_BIntT0T3T_BIntT0T3T_r_bool)
signatures[rl_m_can_mark__Game_BIntT0T3T_BIntT0T3T_r_bool] = [builtins.bool, Game, BIntT0T3T, BIntT0T3T, ]
@overload
def get_current_player(g: Game) -> builtins.int:
    pass

def rl_get_current_player__Game_r_int64_t(g: Game) -> builtins.int:
    var1348 = lib.rl_get_current_player__Game_r_int64_t
    var1349 = (c_longlong)()
    var1348(byref(var1349), byref(g), )
    var1350 = var1349.value
    return var1350

wrappers["get_current_player"].append(rl_get_current_player__Game_r_int64_t)
signatures[rl_get_current_player__Game_r_int64_t] = [builtins.int, Game, ]
@overload
def can_get_current_player(g: Game) -> builtins.bool:
    pass

def rl_can_get_current_player__Game_r_bool(g: Game) -> builtins.bool:
    var1351 = lib.rl_can_get_current_player__Game_r_bool
    var1352 = (c_bool)()
    var1351(byref(var1352), byref(g), )
    return var1352

wrappers["can_get_current_player"].append(rl_can_get_current_player__Game_r_bool)
signatures[rl_can_get_current_player__Game_r_bool] = [builtins.bool, Game, ]
@overload
def score(g: Game, player_id: builtins.int) -> builtins.float:
    pass

def rl_score__Game_int64_t_r_double(g: Game, player_id: builtins.int) -> builtins.float:
    var1353 = lib.rl_score__Game_int64_t_r_double
    var1354 = c_longlong(player_id)
    var1355 = (c_double)()
    var1353(byref(var1355), byref(g), byref(var1354), )
    return var1355

wrappers["score"].append(rl_score__Game_int64_t_r_double)
signatures[rl_score__Game_int64_t_r_double] = [builtins.float, Game, builtins.int, ]
@overload
def can_score(g: Game, player_id: builtins.int) -> builtins.bool:
    pass

def rl_can_score__Game_int64_t_r_bool(g: Game, player_id: builtins.int) -> builtins.bool:
    var1356 = lib.rl_can_score__Game_int64_t_r_bool
    var1357 = c_longlong(player_id)
    var1358 = (c_bool)()
    var1356(byref(var1358), byref(g), byref(var1357), )
    return var1358

wrappers["can_score"].append(rl_can_score__Game_int64_t_r_bool)
signatures[rl_can_score__Game_int64_t_r_bool] = [builtins.bool, Game, builtins.int, ]
@overload
def get_num_players() -> builtins.int:
    pass

def rl_get_num_players__r_int64_t() -> builtins.int:
    var1359 = lib.rl_get_num_players__r_int64_t
    var1360 = (c_longlong)()
    var1359(byref(var1360), )
    var1361 = var1360.value
    return var1361

wrappers["get_num_players"].append(rl_get_num_players__r_int64_t)
signatures[rl_get_num_players__r_int64_t] = [builtins.int, ]
@overload
def can_get_num_players() -> builtins.bool:
    pass

def rl_can_get_num_players__r_bool() -> builtins.bool:
    var1362 = lib.rl_can_get_num_players__r_bool
    var1363 = (c_bool)()
    var1362(byref(var1363), )
    return var1363

wrappers["can_get_num_players"].append(rl_can_get_num_players__r_bool)
signatures[rl_can_get_num_players__r_bool] = [builtins.bool, ]
@overload
def fuzz(input: VectorTint8_tT) -> None:
    pass

def rl_fuzz__VectorTint8_tT(input: VectorTint8_tT) -> None:
    var1364 = lib.rl_fuzz__VectorTint8_tT
    var1364(byref(input), )
    return

wrappers["fuzz"].append(rl_fuzz__VectorTint8_tT)
signatures[rl_fuzz__VectorTint8_tT] = [None, VectorTint8_tT, ]
@overload
def can_fuzz(input: VectorTint8_tT) -> builtins.bool:
    pass

def rl_can_fuzz__VectorTint8_tT_r_bool(input: VectorTint8_tT) -> builtins.bool:
    var1365 = lib.rl_can_fuzz__VectorTint8_tT_r_bool
    var1366 = (c_bool)()
    var1365(byref(var1366), byref(input), )
    return var1366

wrappers["can_fuzz"].append(rl_can_fuzz__VectorTint8_tT_r_bool)
signatures[rl_can_fuzz__VectorTint8_tT_r_bool] = [builtins.bool, VectorTint8_tT, ]
@overload
def main() -> builtins.int:
    pass

def rl_main__r_int64_t() -> builtins.int:
    var1367 = lib.rl_main__r_int64_t
    var1368 = (c_longlong)()
    var1367(byref(var1368), )
    var1369 = var1368.value
    return var1369

wrappers["main"].append(rl_main__r_int64_t)
signatures[rl_main__r_int64_t] = [builtins.int, ]
@overload
def can_main() -> builtins.bool:
    pass

def rl_can_main__r_bool() -> builtins.bool:
    var1370 = lib.rl_can_main__r_bool
    var1371 = (c_bool)()
    var1370(byref(var1371), )
    return var1371

wrappers["can_main"].append(rl_can_main__r_bool)
signatures[rl_can_main__r_bool] = [builtins.bool, ]
@overload
def pretty_print(g: Game) -> None:
    pass

def rl_pretty_print__Game(g: Game) -> None:
    var1372 = lib.rl_pretty_print__Game
    var1372(byref(g), )
    return

wrappers["pretty_print"].append(rl_pretty_print__Game)
signatures[rl_pretty_print__Game] = [None, Game, ]
@overload
def can_pretty_print(g: Game) -> builtins.bool:
    pass

def rl_can_pretty_print__Game_r_bool(g: Game) -> builtins.bool:
    var1373 = lib.rl_can_pretty_print__Game_r_bool
    var1374 = (c_bool)()
    var1373(byref(var1374), byref(g), )
    return var1374

wrappers["can_pretty_print"].append(rl_can_pretty_print__Game_r_bool)
signatures[rl_can_pretty_print__Game_r_bool] = [builtins.bool, Game, ]
class functions:
    def can__parse_type(*args):
        if len(args) == 4 and isinstance(args[0], GameMark) and isinstance(args[1], String) and isinstance(args[2], builtins.str) and isinstance(args[3], builtins.int):
            return rl_can__parse_type__GameMark_String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__parse_type"

    def fuzz(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_fuzz__VectorTint8_tT(*args)


        assert False, "no correct overload to invoke fuzz"

    def _consume_space(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl__consume_space__String_int64_t(*args)


        assert False, "no correct overload to invoke _consume_space"

    def can_print(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_can_print__String_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_can_print__bool_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_print__Game_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_can_print__alt_GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_print"

    def _indent_string(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl__indent_string__String_int64_t(*args)


        assert False, "no correct overload to invoke _indent_string"

    def _from_vector_impl(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke _from_vector_impl"

    def current_player(*args):
        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_current_player__Board_r_int64_t(*args)


        assert False, "no correct overload to invoke current_player"

    def get_type_name(*args):
        if len(args) == 1 and isinstance(args[0], GameMark):
            return rl_get_type_name__GameMark_r_strlit(*args)


        assert False, "no correct overload to invoke get_type_name"

    def get_enumeration_errors(*args):
        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_get_enumeration_errors__alt_GameMark_r_String(*args)


        assert False, "no correct overload to invoke get_enumeration_errors"

    def custom_equal(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_custom_equal__int64_t_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], builtins.bool):
            return rl_custom_equal__bool_bool_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_custom_equal__int8_t_int8_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.float) and isinstance(args[1], builtins.float):
            return rl_custom_equal__double_double_r_bool(*args)


        assert False, "no correct overload to invoke custom_equal"

    def three_in_a_line_player_row(*args):
        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int):
            return rl_m_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke three_in_a_line_player_row"

    def can_as_byte_vector(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_as_byte_vector__Game_r_bool(*args)


        assert False, "no correct overload to invoke can_as_byte_vector"

    def s(*args):
        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_s__strlit_r_String(*args)


        assert False, "no correct overload to invoke s"

    def can__size_as_observation_tensor_impl(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can__size_as_observation_tensor_impl__Game_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can__size_as_observation_tensor_impl__int64_t_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], Board):
            return rl_can__size_as_observation_tensor_impl__Board_r_bool(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_can__size_as_observation_tensor_impl__BIntT0T3T_9_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_can__size_as_observation_tensor_impl__bool_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], BIntT0T3T):
            return rl_can__size_as_observation_tensor_impl__BIntT0T3T_r_bool(*args)


        assert False, "no correct overload to invoke can__size_as_observation_tensor_impl"

    def print_enumeration_errors(*args):
        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_print_enumeration_errors__alt_GameMark_r_bool(*args)


        assert False, "no correct overload to invoke print_enumeration_errors"

    def can_write_tensor_warning_context(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], VectorTStringT):
            return rl_can_write_tensor_warning_context__String_VectorTStringT_r_bool(*args)


        assert False, "no correct overload to invoke can_write_tensor_warning_context"

    def can__parse_string_impl(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__Game_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__int64_t_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__Board_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__alt_GameMark_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__bool_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__GameMark_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can__parse_string_impl__BIntT0T3T_String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__parse_string_impl"

    def can_print_string_lit(*args):
        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_can_print_string_lit__strlit_r_bool(*args)


        assert False, "no correct overload to invoke can_print_string_lit"

    def gen_printer_parser(*args):
        if len(args) == 0:
            return rl_gen_printer_parser_(*args)


        assert False, "no correct overload to invoke gen_printer_parser"

    def to_indented_lines(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_to_indented_lines__String_r_String(*args)


        assert False, "no correct overload to invoke to_indented_lines"

    def get_current_player(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_get_current_player__Game_r_int64_t(*args)


        assert False, "no correct overload to invoke get_current_player"

    def mark(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], BIntT0T3T) and isinstance(args[2], BIntT0T3T):
            return rl_m_mark__Game_BIntT0T3T_BIntT0T3T(*args)


        assert False, "no correct overload to invoke mark"

    def can_to_observation_tensor_warnings(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_to_observation_tensor_warnings__Game_r_bool(*args)


        assert False, "no correct overload to invoke can_to_observation_tensor_warnings"

    def set(*args):
        if len(args) == 4 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int) and isinstance(args[3], builtins.int):
            return rl_m_set__Board_int64_t_int64_t_int64_t(*args)


        assert False, "no correct overload to invoke set"

    def can_resize(*args):
        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.int):
            return rl_m_can_resize__VectorTdoubleT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_resize"

    def can_three_in_a_line_player(*args):
        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], builtins.int):
            return rl_m_can_three_in_a_line_player__Board_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_three_in_a_line_player"

    def can__print_type(*args):
        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], builtins.str) and isinstance(args[2], String):
            return rl_can__print_type__GameMark_strlit_String_r_bool(*args)


        assert False, "no correct overload to invoke can__print_type"

    def is_open_paren(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_is_open_paren__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke is_open_paren"

    def pop(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_pop__VectorTint8_tT_r_int8_t(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_pop__VectorTStringT_r_String(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_pop__VectorTdoubleT_r_double(*args).value


        assert False, "no correct overload to invoke pop"

    def can_parse_string(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_parse_string__int64_t_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_parse_string__int8_t_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_parse_string__double_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_parse_string__bool_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_parse_string__BIntT0T3T_9_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_parse_string__BIntT0T3T_String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_parse_string"

    def max(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_max__int64_t_int64_t_r_int64_t(*args)


        assert False, "no correct overload to invoke max"

    def can_print_enumeration_errors(*args):
        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_can_print_enumeration_errors__alt_GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_print_enumeration_errors"

    def can_not_equal(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.str):
            return rl_m_can_not_equal__String_strlit_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_can_not_equal__String_String_r_bool(*args)


        assert False, "no correct overload to invoke can_not_equal"

    def can_is_open_paren(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_is_open_paren__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke can_is_open_paren"

    def is_close_paren(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_is_close_paren__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke is_close_paren"

    def can_parse_actions(*args):
        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String):
            return rl_can_parse_actions__alt_GameMark_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT):
            return rl_can_parse_actions__alt_GameMark_VectorTint8_tT_r_bool(*args)


        assert False, "no correct overload to invoke can_parse_actions"

    def can_equal(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_can_equal__String_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.str):
            return rl_m_can_equal__String_strlit_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], GameMarkOr):
            return rl_can_equal__alt_GameMark_alt_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], GameMark):
            return rl_can_equal__GameMark_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], BIntT0T3T):
            return rl_can_equal__BIntT0T3T_BIntT0T3T_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_can_equal__int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_equal"

    def can_count(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_can_count__String_int8_t_r_bool(*args)


        assert False, "no correct overload to invoke can_count"

    def get_num_players(*args):
        if len(args) == 0:
            return rl_get_num_players__r_int64_t(*args)


        assert False, "no correct overload to invoke get_num_players"

    def can_append_to_vector(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT):
            return rl_can_append_to_vector__int64_t_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.float) and isinstance(args[1], VectorTint8_tT):
            return rl_can_append_to_vector__double_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT):
            return rl_can_append_to_vector__bool_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT):
            return rl_can_append_to_vector__int8_t_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT):
            return rl_can_append_to_vector__BIntT0T3T_9_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT):
            return rl_can_append_to_vector__BIntT0T3T_VectorTint8_tT_r_bool(*args)


        assert False, "no correct overload to invoke can_append_to_vector"

    def can__indent_string(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_can__indent_string__String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__indent_string"

    def can_write_in_observation_tensor(*args):
        if len(args) == 5 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int) and isinstance(args[3], VectorTdoubleT) and isinstance(args[4], builtins.int):
            return rl_can_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], builtins.float) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], builtins.bool) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0],  list ) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_write_in_observation_tensor"

    def back(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_back__VectorTint8_tT_r_int8_tRef(*args)


        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_back__String_r_int8_tRef(*args)


        assert False, "no correct overload to invoke back"

    def resize(*args):
        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.int):
            return rl_m_resize__VectorTdoubleT_int64_t(*args)


        assert False, "no correct overload to invoke resize"

    def can_score(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], builtins.int):
            return rl_can_score__Game_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_score"

    def can_init(*args):
        if len(args) == 1 and isinstance(args[0], POINTER(BIntT0T3T)):
            return rl_m_can_init__BIntT0T3TPtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(GameMark)):
            return rl_m_can_init__GameMarkPtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(GameMarkOr)):
            return rl_m_can_init__alt_GameMarkPtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(c_bool)):
            return rl_m_can_init__boolPtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(c_double)):
            return rl_m_can_init__doublePtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(String)):
            return rl_m_can_init__StringPtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(c_byte)):
            return rl_m_can_init__int8_tPtr_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_m_can_init__alt_GameMark_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], Game):
            return rl_m_can_init__Game_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_can_init__Board_r_bool(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_m_can_init__BIntT0T3T_9_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_m_can_init__strlit_r_bool(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_m_can_init__int8_t_1_r_bool(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_m_can_init__int8_t_8_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], GameMark):
            return rl_m_can_init__GameMark_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], BIntT0T3T):
            return rl_m_can_init__BIntT0T3T_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_can_init__VectorTint8_tT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_can_init__VectorTdoubleT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_can_init__VectorTStringT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTboolT):
            return rl_m_can_init__VectorTboolT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTalt_GameMarkT):
            return rl_m_can_init__VectorTalt_GameMarkT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTGameMarkT):
            return rl_m_can_init__VectorTGameMarkT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTBIntT0T3TT):
            return rl_m_can_init__VectorTBIntT0T3TT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_can_init__String_r_bool(*args)


        assert False, "no correct overload to invoke can_init"

    def size_as_observation_tensor(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_size_as_observation_tensor__int64_t_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], builtins.float):
            return rl_size_as_observation_tensor__double_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_size_as_observation_tensor__bool_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_size_as_observation_tensor__int8_t_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_size_as_observation_tensor__BIntT0T3T_9_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], BIntT0T3T):
            return rl_size_as_observation_tensor__BIntT0T3T_r_int64_t(*args)


        assert False, "no correct overload to invoke size_as_observation_tensor"

    def can_get_num_players(*args):
        if len(args) == 0:
            return rl_can_get_num_players__r_bool(*args)


        assert False, "no correct overload to invoke can_get_num_players"

    def can_load_file(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_can_load_file__String_String_r_bool(*args)


        assert False, "no correct overload to invoke can_load_file"

    def can_parse_and_execute(*args):
        if len(args) == 4 and isinstance(args[0], Game) and isinstance(args[1], GameMarkOr) and isinstance(args[2], VectorTint8_tT) and isinstance(args[3], builtins.int):
            return rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], GameMarkOr) and isinstance(args[2], VectorTint8_tT):
            return rl_can_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_r_bool(*args)


        assert False, "no correct overload to invoke can_parse_and_execute"

    def equal(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_equal__String_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.str):
            return rl_m_equal__String_strlit_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], GameMarkOr):
            return rl_equal__alt_GameMark_alt_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], GameMark):
            return rl_equal__GameMark_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], BIntT0T3T):
            return rl_equal__BIntT0T3T_BIntT0T3T_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_equal__int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke equal"

    def can__to_string_impl(*args):
        if len(args) == 2 and isinstance(args[0], builtins.str) and isinstance(args[1], String):
            return rl_can__to_string_impl__strlit_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], String):
            return rl_can__to_string_impl__int64_t_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], String):
            return rl_can__to_string_impl__bool_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], String):
            return rl_can__to_string_impl__Game_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String):
            return rl_can__to_string_impl__alt_GameMark_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], String):
            return rl_can__to_string_impl__Board_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], String):
            return rl_can__to_string_impl__GameMark_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], String):
            return rl_can__to_string_impl__BIntT0T3T_9_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String):
            return rl_can__to_string_impl__BIntT0T3T_String_r_bool(*args)


        assert False, "no correct overload to invoke can__to_string_impl"

    def parse_and_execute(*args):
        if len(args) == 4 and isinstance(args[0], Game) and isinstance(args[1], GameMarkOr) and isinstance(args[2], VectorTint8_tT) and isinstance(args[3], builtins.int):
            return rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT_int64_t(*args)


        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], GameMarkOr) and isinstance(args[2], VectorTint8_tT):
            return rl_parse_and_execute__Game_alt_GameMark_VectorTint8_tT(*args)


        assert False, "no correct overload to invoke parse_and_execute"

    def is_space(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_is_space__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke is_space"

    def write_in_observation_tensor(*args):
        if len(args) == 5 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int) and isinstance(args[3], VectorTdoubleT) and isinstance(args[4], builtins.int):
            return rl_write_in_observation_tensor__int64_t_int64_t_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_write_in_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], builtins.float) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_write_in_observation_tensor__double_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], builtins.bool) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_write_in_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_write_in_observation_tensor__int8_t_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0],  list ) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_write_in_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_write_in_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t(*args)


        assert False, "no correct overload to invoke write_in_observation_tensor"

    def can__to_vector_impl(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT):
            return rl_can__to_vector_impl__int64_t_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], VectorTint8_tT):
            return rl_can__to_vector_impl__Game_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], VectorTint8_tT):
            return rl_can__to_vector_impl__Board_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT):
            return rl_can__to_vector_impl__BIntT0T3T_9_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT):
            return rl_can__to_vector_impl__bool_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT):
            return rl_can__to_vector_impl__BIntT0T3T_VectorTint8_tT_r_bool(*args)


        assert False, "no correct overload to invoke can__to_vector_impl"

    def parse_actions(*args):
        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_actions__alt_GameMark_VectorTint8_tT_int64_t_r_VectorTalt_GameMarkT(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String):
            return rl_parse_actions__alt_GameMark_String_r_VectorTalt_GameMarkT(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT):
            return rl_parse_actions__alt_GameMark_VectorTint8_tT_r_VectorTalt_GameMarkT(*args)


        assert False, "no correct overload to invoke parse_actions"

    def to_observation_tensor(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT):
            return rl_to_observation_tensor__Game_int64_t_VectorTdoubleT(*args)


        assert False, "no correct overload to invoke to_observation_tensor"

    def parse_action_optimized(*args):
        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke parse_action_optimized"

    def init(*args):
        if len(args) == 1 and isinstance(args[0], POINTER(BIntT0T3T)):
            return rl_m_init__BIntT0T3TPtr(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(GameMark)):
            return rl_m_init__GameMarkPtr(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(GameMarkOr)):
            return rl_m_init__alt_GameMarkPtr(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(c_bool)):
            return rl_m_init__boolPtr(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(c_double)):
            return rl_m_init__doublePtr(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(String)):
            return rl_m_init__StringPtr(*args)


        if len(args) == 1 and isinstance(args[0], POINTER(c_byte)):
            return rl_m_init__int8_tPtr(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_m_init__alt_GameMark(*args)


        if len(args) == 1 and isinstance(args[0], Game):
            return rl_m_init__Game(*args)


        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_init__Board(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_m_init__BIntT0T3T_9(*args)


        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_m_init__strlit(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_m_init__int8_t_1(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_m_init__int8_t_8(*args)


        if len(args) == 1 and isinstance(args[0], GameMark):
            return rl_m_init__GameMark(*args)


        if len(args) == 1 and isinstance(args[0], BIntT0T3T):
            return rl_m_init__BIntT0T3T(*args)


        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_init__VectorTint8_tT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_init__VectorTdoubleT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_init__VectorTStringT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTboolT):
            return rl_m_init__VectorTboolT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTalt_GameMarkT):
            return rl_m_init__VectorTalt_GameMarkT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTGameMarkT):
            return rl_m_init__VectorTGameMarkT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTBIntT0T3TT):
            return rl_m_init__VectorTBIntT0T3TT(*args)


        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_init__String(*args)


        assert False, "no correct overload to invoke init"

    def write_tensor_warning_context(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], VectorTStringT):
            return rl_write_tensor_warning_context__String_VectorTStringT(*args)


        assert False, "no correct overload to invoke write_tensor_warning_context"

    def can_main(*args):
        if len(args) == 0:
            return rl_can_main__r_bool(*args)


        assert False, "no correct overload to invoke can_main"

    def drop(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_drop__String(*args)


        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_drop__VectorTint8_tT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_drop__VectorTdoubleT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_drop__VectorTStringT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTboolT):
            return rl_m_drop__VectorTboolT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTalt_GameMarkT):
            return rl_m_drop__VectorTalt_GameMarkT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTGameMarkT):
            return rl_m_drop__VectorTGameMarkT(*args)


        if len(args) == 1 and isinstance(args[0], VectorTBIntT0T3TT):
            return rl_m_drop__VectorTBIntT0T3TT(*args)


        assert False, "no correct overload to invoke drop"

    def parse_string(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_parse_string__int64_t_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_parse_string__int8_t_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_parse_string__double_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_parse_string__bool_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_parse_string__BIntT0T3T_9_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_parse_string__BIntT0T3T_String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke parse_string"

    def length(*args):
        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_length__strlit_r_int64_t(*args)


        assert False, "no correct overload to invoke length"

    def can_reverse(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_can_reverse__String_r_bool(*args)


        assert False, "no correct overload to invoke can_reverse"

    def can_s(*args):
        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_can_s__strlit_r_bool(*args)


        assert False, "no correct overload to invoke can_s"

    def append_to_vector(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT):
            return rl_append_to_vector__int64_t_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], builtins.float) and isinstance(args[1], VectorTint8_tT):
            return rl_append_to_vector__double_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT):
            return rl_append_to_vector__bool_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT):
            return rl_append_to_vector__int8_t_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT):
            return rl_append_to_vector__BIntT0T3T_9_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT):
            return rl_append_to_vector__BIntT0T3T_VectorTint8_tT(*args)


        assert False, "no correct overload to invoke append_to_vector"

    def can_get_type_name(*args):
        if len(args) == 1 and isinstance(args[0], GameMark):
            return rl_can_get_type_name__GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_get_type_name"

    def can_drop_back(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_can_drop_back__VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_can_drop_back__String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_drop_back"

    def can_from_byte_vector(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], VectorTint8_tT):
            return rl_can_from_byte_vector__Game_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT):
            return rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_from_byte_vector"

    def sqrt(*args):
        if len(args) == 1 and isinstance(args[0], builtins.float):
            return rl_sqrt__double_r_double(*args).value


        assert False, "no correct overload to invoke sqrt"

    def size(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_size__VectorTint8_tT_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_size__VectorTdoubleT_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_size__VectorTStringT_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], VectorTalt_GameMarkT):
            return rl_m_size__VectorTalt_GameMarkT_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], VectorTGameMarkT):
            return rl_m_size__VectorTGameMarkT_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], VectorTBIntT0T3TT):
            return rl_m_size__VectorTBIntT0T3TT_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_size__String_r_int64_t(*args)


        assert False, "no correct overload to invoke size"

    def print(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_print__String(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_print__bool(*args)


        if len(args) == 1 and isinstance(args[0], Game):
            return rl_print__Game(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_print__alt_GameMark(*args)


        assert False, "no correct overload to invoke print"

    def can_to_string(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_to_string__int64_t_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_can_to_string__bool_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_to_string__Game_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_can_to_string__alt_GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_to_string"

    def load_action_vector_file(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], VectorTalt_GameMarkT):
            return rl_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool(*args)


        assert False, "no correct overload to invoke load_action_vector_file"

    def can_drop(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_can_drop__String_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_can_drop__VectorTint8_tT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_can_drop__VectorTdoubleT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_can_drop__VectorTStringT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTboolT):
            return rl_m_can_drop__VectorTboolT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTalt_GameMarkT):
            return rl_m_can_drop__VectorTalt_GameMarkT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTGameMarkT):
            return rl_m_can_drop__VectorTGameMarkT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTBIntT0T3TT):
            return rl_m_can_drop__VectorTBIntT0T3TT_r_bool(*args)


        assert False, "no correct overload to invoke can_drop"

    def from_byte_vector(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], VectorTint8_tT):
            return rl_from_byte_vector__Game_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT):
            return rl_from_byte_vector__alt_GameMark_VectorTint8_tT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_from_byte_vector__int8_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_from_byte_vector__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_from_byte_vector__GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke from_byte_vector"

    def append_to_string(*args):
        if len(args) == 2 and isinstance(args[0], builtins.str) and isinstance(args[1], String):
            return rl_append_to_string__strlit_String(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], String):
            return rl_append_to_string__int64_t_String(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], String):
            return rl_append_to_string__int8_t_String(*args)


        if len(args) == 2 and isinstance(args[0], builtins.float) and isinstance(args[1], String):
            return rl_append_to_string__double_String(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], String):
            return rl_append_to_string__bool_String(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], String):
            return rl_append_to_string__BIntT0T3T_9_String(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String):
            return rl_append_to_string__BIntT0T3T_String(*args)


        assert False, "no correct overload to invoke append_to_string"

    def can_print_string(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_can_print_string__String_r_bool(*args)


        assert False, "no correct overload to invoke can_print_string"

    def parse_from_vector(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke parse_from_vector"

    def not_equal(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.str):
            return rl_m_not_equal__String_strlit_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_not_equal__String_String_r_bool(*args)


        assert False, "no correct overload to invoke not_equal"

    def can_add(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_can_add__String_String_r_bool(*args)


        assert False, "no correct overload to invoke can_add"

    def _parse_type(*args):
        if len(args) == 4 and isinstance(args[0], GameMark) and isinstance(args[1], String) and isinstance(args[2], builtins.str) and isinstance(args[3], builtins.int):
            return rl__parse_type__GameMark_String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke _parse_type"

    def to_string(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_to_string__int64_t_r_String(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_to_string__bool_r_String(*args)


        if len(args) == 1 and isinstance(args[0], Game):
            return rl_to_string__Game_r_String(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_to_string__alt_GameMark_r_String(*args)


        assert False, "no correct overload to invoke to_string"

    def can_apply(*args):
        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], Game):
            return rl_can_apply__alt_GameMark_Game_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], Game):
            return rl_can_apply__VectorTalt_GameMarkT_Game_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], Game):
            return rl_can_apply__GameMark_Game_r_bool(*args)


        assert False, "no correct overload to invoke can_apply"

    def can_custom_equal(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_can_custom_equal__int64_t_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], builtins.bool):
            return rl_can_custom_equal__bool_bool_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_can_custom_equal__int8_t_int8_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.float) and isinstance(args[1], builtins.float):
            return rl_can_custom_equal__double_double_r_bool(*args)


        assert False, "no correct overload to invoke can_custom_equal"

    def can_append_to_string(*args):
        if len(args) == 2 and isinstance(args[0], builtins.str) and isinstance(args[1], String):
            return rl_can_append_to_string__strlit_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], String):
            return rl_can_append_to_string__int64_t_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], String):
            return rl_can_append_to_string__int8_t_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.float) and isinstance(args[1], String):
            return rl_can_append_to_string__double_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], String):
            return rl_can_append_to_string__bool_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], String):
            return rl_can_append_to_string__BIntT0T3T_9_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String):
            return rl_can_append_to_string__BIntT0T3T_String_r_bool(*args)


        assert False, "no correct overload to invoke can_append_to_string"

    def can_from_string(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], String):
            return rl_can_from_string__Game_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String):
            return rl_can_from_string__alt_GameMark_String_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_can_from_string__alt_GameMark_String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_from_string"

    def can_get_enumeration_errors(*args):
        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_can_get_enumeration_errors__alt_GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_get_enumeration_errors"

    def can_can_apply_impl(*args):
        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], Game):
            return rl_can_can_apply_impl__alt_GameMark_Game_r_bool(*args)


        assert False, "no correct overload to invoke can_can_apply_impl"

    def can__consume_literal_token(*args):
        if len(args) == 3 and isinstance(args[0], String) and isinstance(args[1], builtins.str) and isinstance(args[2], builtins.int):
            return rl_can__consume_literal_token__String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__consume_literal_token"

    def add(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_add__String_String_r_String(*args)


        assert False, "no correct overload to invoke add"

    def pretty_print(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_pretty_print__Game(*args)


        assert False, "no correct overload to invoke pretty_print"

    def can_set(*args):
        if len(args) == 4 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int) and isinstance(args[3], builtins.int):
            return rl_m_can_set__Board_int64_t_int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_set"

    def can_load_action_vector_file(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], VectorTalt_GameMarkT):
            return rl_can_load_action_vector_file__String_VectorTalt_GameMarkT_r_bool(*args)


        assert False, "no correct overload to invoke can_load_action_vector_file"

    def can_sqrt(*args):
        if len(args) == 1 and isinstance(args[0], builtins.float):
            return rl_can_sqrt__double_r_bool(*args)


        assert False, "no correct overload to invoke can_sqrt"

    def can_substring_matches(*args):
        if len(args) == 3 and isinstance(args[0], String) and isinstance(args[1], builtins.str) and isinstance(args[2], builtins.int):
            return rl_m_can_substring_matches__String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_substring_matches"

    def can_abs(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_abs__int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_abs"

    def can_get_enumeration_errors_impl(*args):
        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_get_enumeration_errors_impl__GameMark_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_get_enumeration_errors_impl__int64_t_String_VectorTStringT_r_bool(*args)


        assert False, "no correct overload to invoke can_get_enumeration_errors_impl"

    def can_is_close_paren(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_is_close_paren__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke can_is_close_paren"

    def can_max(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_can_max__int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_max"

    def can_is_alphanumeric(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_is_alphanumeric__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke can_is_alphanumeric"

    def can_parse_action_optimized(*args):
        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_action_optimized__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_parse_action_optimized"

    def can_enumeration_error(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_enumeration_error__int64_t_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_enumeration_error__double_String_VectorTStringT_r_bool(*args)


        assert False, "no correct overload to invoke can_enumeration_error"

    def can_emit_observation_tensor_warnings(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_emit_observation_tensor_warnings__Game_r_bool(*args)


        assert False, "no correct overload to invoke can_emit_observation_tensor_warnings"

    def can_min(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_can_min__int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_min"

    def _grow(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTint8_tT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTboolT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTStringT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTdoubleT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTalt_GameMarkT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTGameMarkT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], builtins.int):
            return rl_m__grow__VectorTBIntT0T3TT_int64_t(*args)


        assert False, "no correct overload to invoke _grow"

    def abs(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_abs__int64_t_r_int64_t(*args)


        assert False, "no correct overload to invoke abs"

    def can_next_turn(*args):
        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_can_next_turn__Board_r_bool(*args)


        assert False, "no correct overload to invoke can_next_turn"

    def can_full(*args):
        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_can_full__Board_r_bool(*args)


        assert False, "no correct overload to invoke can_full"

    def can_mark(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], BIntT0T3T) and isinstance(args[2], BIntT0T3T):
            return rl_m_can_mark__Game_BIntT0T3T_BIntT0T3T_r_bool(*args)


        assert False, "no correct overload to invoke can_mark"

    def from_string(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], String):
            return rl_from_string__Game_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String):
            return rl_from_string__alt_GameMark_String_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl_from_string__alt_GameMark_String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke from_string"

    def can__grow(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTboolT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTStringT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTalt_GameMarkT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTGameMarkT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], builtins.int):
            return rl_m_can__grow__VectorTBIntT0T3TT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__grow"

    def play(*args):
        if len(args) == 0:
            return rl_play__r_Game(*args)


        assert False, "no correct overload to invoke play"

    def can__consume_space(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_can__consume_space__String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__consume_space"

    def next_turn(*args):
        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_next_turn__Board(*args)


        assert False, "no correct overload to invoke next_turn"

    def _enumerate_impl(*args):
        if len(args) == 4 and isinstance(args[0], GameMark) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTGameMarkT) and isinstance(args[3], builtins.int):
            return rl__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t(*args)


        assert False, "no correct overload to invoke _enumerate_impl"

    def is_alphanumeric(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_is_alphanumeric__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke is_alphanumeric"

    def score(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], builtins.int):
            return rl_score__Game_int64_t_r_double(*args).value


        assert False, "no correct overload to invoke score"

    def assign(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], Game):
            return rl_m_assign__Game_Game(*args)


        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], Board):
            return rl_m_assign__Board_Board(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1],  list ):
            return rl_m_assign__BIntT0T3T_9_BIntT0T3T_9(*args)


        if len(args) == 2 and isinstance(args[0], builtins.str) and isinstance(args[1], builtins.str):
            return rl_m_assign__strlit_strlit(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_assign__String_String(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], GameMark):
            return rl_m_assign__alt_GameMark_GameMark(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], GameMarkOr):
            return rl_m_assign__alt_GameMark_alt_GameMark(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], GameMark):
            return rl_m_assign__GameMark_GameMark(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], BIntT0T3T):
            return rl_m_assign__BIntT0T3T_BIntT0T3T(*args)


        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], VectorTint8_tT):
            return rl_m_assign__VectorTint8_tT_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], VectorTboolT):
            return rl_m_assign__VectorTboolT_VectorTboolT(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], VectorTdoubleT):
            return rl_m_assign__VectorTdoubleT_VectorTdoubleT(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], VectorTStringT):
            return rl_m_assign__VectorTStringT_VectorTStringT(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], VectorTalt_GameMarkT):
            return rl_m_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], VectorTGameMarkT):
            return rl_m_assign__VectorTGameMarkT_VectorTGameMarkT(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], VectorTBIntT0T3TT):
            return rl_m_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT(*args)


        assert False, "no correct overload to invoke assign"

    def can_length(*args):
        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_can_length__strlit_r_bool(*args)


        assert False, "no correct overload to invoke can_length"

    def reverse(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_reverse__String(*args)


        assert False, "no correct overload to invoke reverse"

    def can_tensorable_warning(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_tensorable_warning__int64_t_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_tensorable_warning__double_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can_tensorable_warning__BIntT0T3T_9_String_VectorTStringT_r_bool(*args)


        assert False, "no correct overload to invoke can_tensorable_warning"

    def enumerate(*args):
        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTBIntT0T3TT):
            return rl_enumerate__BIntT0T3T_VectorTBIntT0T3TT(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTboolT):
            return rl_enumerate__bool_VectorTboolT(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_enumerate__alt_GameMark_r_VectorTalt_GameMarkT(*args)


        if len(args) == 1 and isinstance(args[0], GameMark):
            return rl_enumerate__GameMark_r_VectorTGameMarkT(*args)


        assert False, "no correct overload to invoke enumerate"

    def get(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTint8_tT_int64_t_r_int8_tRef(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTdoubleT_int64_t_r_doubleRef(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTStringT_int64_t_r_StringRef(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTboolT_int64_t_r_boolRef(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTalt_GameMarkT_int64_t_r_alt_GameMarkRef(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTGameMarkT_int64_t_r_GameMarkRef(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], builtins.int):
            return rl_m_get__VectorTBIntT0T3TT_int64_t_r_BIntT0T3TRef(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_get__String_int64_t_r_int8_tRef(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int):
            return rl_m_get__Board_int64_t_int64_t_r_int64_t(*args)


        assert False, "no correct overload to invoke get"

    def can_is_space(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_is_space__int8_t_r_bool(*args)


        assert False, "no correct overload to invoke can_is_space"

    def apply(*args):
        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], Game):
            return rl_apply__alt_GameMark_Game(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], Game):
            return rl_apply__VectorTalt_GameMarkT_Game_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], Game):
            return rl_apply__GameMark_Game(*args)


        assert False, "no correct overload to invoke apply"

    def can_append(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_can_append__VectorTint8_tT_int8_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], builtins.bool):
            return rl_m_can_append__VectorTboolT_bool_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], String):
            return rl_m_can_append__VectorTStringT_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.float):
            return rl_m_can_append__VectorTdoubleT_double_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], GameMarkOr):
            return rl_m_can_append__VectorTalt_GameMarkT_alt_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], GameMark):
            return rl_m_can_append__VectorTGameMarkT_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], BIntT0T3T):
            return rl_m_can_append__VectorTBIntT0T3TT_BIntT0T3T_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_can_append__String_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.str):
            return rl_m_can_append__String_strlit_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_can_append__String_int8_t_r_bool(*args)


        assert False, "no correct overload to invoke can_append"

    def _to_observation_tensor(*args):
        if len(args) == 4 and isinstance(args[0], Game) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0],  list ) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], builtins.bool) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t(*args)


        if len(args) == 4 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t(*args)


        assert False, "no correct overload to invoke _to_observation_tensor"

    def can__enumerate_impl(*args):
        if len(args) == 4 and isinstance(args[0], GameMark) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTGameMarkT) and isinstance(args[3], builtins.int):
            return rl_can__enumerate_impl__GameMark_int64_t_VectorTGameMarkT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__enumerate_impl"

    def _to_vector_impl(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT):
            return rl__to_vector_impl__int64_t_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], VectorTint8_tT):
            return rl__to_vector_impl__Game_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], VectorTint8_tT):
            return rl__to_vector_impl__Board_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT):
            return rl__to_vector_impl__BIntT0T3T_9_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT):
            return rl__to_vector_impl__bool_VectorTint8_tT(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT):
            return rl__to_vector_impl__BIntT0T3T_VectorTint8_tT(*args)


        assert False, "no correct overload to invoke _to_vector_impl"

    def can_parse_from_vector(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_from_vector__int64_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_from_vector__double_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_from_vector__bool_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_from_vector__int8_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_from_vector__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can_parse_from_vector__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_parse_from_vector"

    def append(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_append__VectorTint8_tT_int8_t(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], builtins.bool):
            return rl_m_append__VectorTboolT_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], String):
            return rl_m_append__VectorTStringT_String(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.float):
            return rl_m_append__VectorTdoubleT_double(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], GameMarkOr):
            return rl_m_append__VectorTalt_GameMarkT_alt_GameMark(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], GameMark):
            return rl_m_append__VectorTGameMarkT_GameMark(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], BIntT0T3T):
            return rl_m_append__VectorTBIntT0T3TT_BIntT0T3T(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_append__String_String(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.str):
            return rl_m_append__String_strlit(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_append__String_int8_t(*args)


        assert False, "no correct overload to invoke append"

    def load_file(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_load_file__String_String_r_bool(*args)


        assert False, "no correct overload to invoke load_file"

    def tensorable_warning(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_tensorable_warning__int64_t_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_tensorable_warning__double_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_tensorable_warning__BIntT0T3T_9_String_VectorTStringT(*args)


        assert False, "no correct overload to invoke tensorable_warning"

    def can__from_vector_impl(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__int64_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__int8_t_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__Game_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__alt_GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__Board_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__GameMark_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__BIntT0T3T_9_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__bool_VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTint8_tT) and isinstance(args[2], builtins.int):
            return rl_can__from_vector_impl__BIntT0T3T_VectorTint8_tT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__from_vector_impl"

    def _size_as_observation_tensor_impl(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl__size_as_observation_tensor_impl__Game_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl__size_as_observation_tensor_impl__int64_t_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], Board):
            return rl__size_as_observation_tensor_impl__Board_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl__size_as_observation_tensor_impl__BIntT0T3T_9_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl__size_as_observation_tensor_impl__bool_r_int64_t(*args)


        if len(args) == 1 and isinstance(args[0], BIntT0T3T):
            return rl__size_as_observation_tensor_impl__BIntT0T3T_r_int64_t(*args)


        assert False, "no correct overload to invoke _size_as_observation_tensor_impl"

    def _print_type(*args):
        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], builtins.str) and isinstance(args[2], String):
            return rl__print_type__GameMark_strlit_String(*args)


        assert False, "no correct overload to invoke _print_type"

    def observation_tensor_size(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_observation_tensor_size__Game_r_int64_t(*args)


        assert False, "no correct overload to invoke observation_tensor_size"

    def can_fuzz(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_can_fuzz__VectorTint8_tT_r_bool(*args)


        assert False, "no correct overload to invoke can_fuzz"

    def can__consume_literal(*args):
        if len(args) == 3 and isinstance(args[0], String) and isinstance(args[1], builtins.str) and isinstance(args[2], builtins.int):
            return rl_can__consume_literal__String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__consume_literal"

    def min(*args):
        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int):
            return rl_min__int64_t_int64_t_r_int64_t(*args)


        assert False, "no correct overload to invoke min"

    def emit_observation_tensor_warnings(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_emit_observation_tensor_warnings__Game(*args)


        assert False, "no correct overload to invoke emit_observation_tensor_warnings"

    def can_back(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_can_back__VectorTint8_tT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_can_back__String_r_bool(*args)


        assert False, "no correct overload to invoke can_back"

    def can_to_indented_lines(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_can_to_indented_lines__String_r_bool(*args)


        assert False, "no correct overload to invoke can_to_indented_lines"

    def can_to_observation_tensor(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT):
            return rl_can_to_observation_tensor__Game_int64_t_VectorTdoubleT_r_bool(*args)


        assert False, "no correct overload to invoke can_to_observation_tensor"

    def _parse_string_impl(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__Game_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__int64_t_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__Board_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__alt_GameMark_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__BIntT0T3T_9_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__bool_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__GameMark_String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], builtins.int):
            return rl__parse_string_impl__BIntT0T3T_String_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke _parse_string_impl"

    def _observation_tensor_warnings(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl__observation_tensor_warnings__Game_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl__observation_tensor_warnings__int64_t_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl__observation_tensor_warnings__Board_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl__observation_tensor_warnings__bool_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT(*args)


        assert False, "no correct overload to invoke _observation_tensor_warnings"

    def three_in_a_line_player(*args):
        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], builtins.int):
            return rl_m_three_in_a_line_player__Board_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke three_in_a_line_player"

    def can_assign(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], Game):
            return rl_m_can_assign__Game_Game_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], Board):
            return rl_m_can_assign__Board_Board_r_bool(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1],  list ):
            return rl_m_can_assign__BIntT0T3T_9_BIntT0T3T_9_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.str) and isinstance(args[1], builtins.str):
            return rl_m_can_assign__strlit_strlit_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], String):
            return rl_m_can_assign__String_String_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], GameMark):
            return rl_m_can_assign__alt_GameMark_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], GameMarkOr):
            return rl_m_can_assign__alt_GameMark_alt_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], GameMark):
            return rl_m_can_assign__GameMark_GameMark_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], BIntT0T3T):
            return rl_m_can_assign__BIntT0T3T_BIntT0T3T_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], VectorTint8_tT):
            return rl_m_can_assign__VectorTint8_tT_VectorTint8_tT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], VectorTboolT):
            return rl_m_can_assign__VectorTboolT_VectorTboolT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], VectorTdoubleT):
            return rl_m_can_assign__VectorTdoubleT_VectorTdoubleT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], VectorTStringT):
            return rl_m_can_assign__VectorTStringT_VectorTStringT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], VectorTalt_GameMarkT):
            return rl_m_can_assign__VectorTalt_GameMarkT_VectorTalt_GameMarkT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], VectorTGameMarkT):
            return rl_m_can_assign__VectorTGameMarkT_VectorTGameMarkT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], VectorTBIntT0T3TT):
            return rl_m_can_assign__VectorTBIntT0T3TT_VectorTBIntT0T3TT_r_bool(*args)


        assert False, "no correct overload to invoke can_assign"

    def can_three_in_a_line_player_row(*args):
        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int):
            return rl_m_can_three_in_a_line_player_row__Board_int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_three_in_a_line_player_row"

    def print_string(*args):
        if len(args) == 1 and isinstance(args[0], String):
            return rl_print_string__String(*args)


        assert False, "no correct overload to invoke print_string"

    def can_pop(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_can_pop__VectorTint8_tT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_can_pop__VectorTStringT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_can_pop__VectorTdoubleT_r_bool(*args)


        assert False, "no correct overload to invoke can_pop"

    def print_string_lit(*args):
        if len(args) == 1 and isinstance(args[0], builtins.str):
            return rl_print_string_lit__strlit(*args)


        assert False, "no correct overload to invoke print_string_lit"

    def _consume_literal(*args):
        if len(args) == 3 and isinstance(args[0], String) and isinstance(args[1], builtins.str) and isinstance(args[2], builtins.int):
            return rl__consume_literal__String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke _consume_literal"

    def as_byte_vector(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_as_byte_vector__Game_r_VectorTint8_tT(*args)


        assert False, "no correct overload to invoke as_byte_vector"

    def can_apply_impl(*args):
        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], Game):
            return rl_can_apply_impl__alt_GameMark_Game_r_bool(*args)


        assert False, "no correct overload to invoke can_apply_impl"

    def can_size_as_observation_tensor(*args):
        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_size_as_observation_tensor__int64_t_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.float):
            return rl_can_size_as_observation_tensor__double_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.bool):
            return rl_can_size_as_observation_tensor__bool_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], builtins.int):
            return rl_can_size_as_observation_tensor__int8_t_r_bool(*args)


        if len(args) == 1 and isinstance(args[0],  list ):
            return rl_can_size_as_observation_tensor__BIntT0T3T_9_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], BIntT0T3T):
            return rl_can_size_as_observation_tensor__BIntT0T3T_r_bool(*args)


        assert False, "no correct overload to invoke can_size_as_observation_tensor"

    def can_gen_printer_parser(*args):
        if len(args) == 0:
            return rl_can_gen_printer_parser__r_bool(*args)


        assert False, "no correct overload to invoke can_gen_printer_parser"

    def to_observation_tensor_warnings(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_to_observation_tensor_warnings__Game_r_String(*args)


        assert False, "no correct overload to invoke to_observation_tensor_warnings"

    def can_get(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTint8_tT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTdoubleT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTStringT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTStringT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTboolT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTboolT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTalt_GameMarkT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTalt_GameMarkT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTGameMarkT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTGameMarkT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], VectorTBIntT0T3TT) and isinstance(args[1], builtins.int):
            return rl_m_can_get__VectorTBIntT0T3TT_int64_t_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_can_get__String_int64_t_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], builtins.int):
            return rl_m_can_get__Board_int64_t_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can_get"

    def _to_string_impl(*args):
        if len(args) == 2 and isinstance(args[0], builtins.str) and isinstance(args[1], String):
            return rl__to_string_impl__strlit_String(*args)


        if len(args) == 2 and isinstance(args[0], builtins.int) and isinstance(args[1], String):
            return rl__to_string_impl__int64_t_String(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], String):
            return rl__to_string_impl__bool_String(*args)


        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], String):
            return rl__to_string_impl__Game_String(*args)


        if len(args) == 2 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String):
            return rl__to_string_impl__alt_GameMark_String(*args)


        if len(args) == 2 and isinstance(args[0], Board) and isinstance(args[1], String):
            return rl__to_string_impl__Board_String(*args)


        if len(args) == 2 and isinstance(args[0], GameMark) and isinstance(args[1], String):
            return rl__to_string_impl__GameMark_String(*args)


        if len(args) == 2 and isinstance(args[0],  list ) and isinstance(args[1], String):
            return rl__to_string_impl__BIntT0T3T_9_String(*args)


        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String):
            return rl__to_string_impl__BIntT0T3T_String(*args)


        assert False, "no correct overload to invoke _to_string_impl"

    def main(*args):
        if len(args) == 0:
            return rl_main__r_int64_t(*args)


        assert False, "no correct overload to invoke main"

    def can_size(*args):
        if len(args) == 1 and isinstance(args[0], VectorTint8_tT):
            return rl_m_can_size__VectorTint8_tT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTdoubleT):
            return rl_m_can_size__VectorTdoubleT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTStringT):
            return rl_m_can_size__VectorTStringT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTalt_GameMarkT):
            return rl_m_can_size__VectorTalt_GameMarkT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTGameMarkT):
            return rl_m_can_size__VectorTGameMarkT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], VectorTBIntT0T3TT):
            return rl_m_can_size__VectorTBIntT0T3TT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], String):
            return rl_m_can_size__String_r_bool(*args)


        assert False, "no correct overload to invoke can_size"

    def can__to_observation_tensor(*args):
        if len(args) == 4 and isinstance(args[0], Game) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can__to_observation_tensor__Game_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], builtins.int) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can__to_observation_tensor__int64_t_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], Board) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can__to_observation_tensor__Board_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0],  list ) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can__to_observation_tensor__BIntT0T3T_9_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], builtins.bool) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can__to_observation_tensor__bool_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        if len(args) == 4 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], builtins.int) and isinstance(args[2], VectorTdoubleT) and isinstance(args[3], builtins.int):
            return rl_can__to_observation_tensor__BIntT0T3T_int64_t_VectorTdoubleT_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke can__to_observation_tensor"

    def _consume_literal_token(*args):
        if len(args) == 3 and isinstance(args[0], String) and isinstance(args[1], builtins.str) and isinstance(args[2], builtins.int):
            return rl__consume_literal_token__String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke _consume_literal_token"

    def can_enumerate(*args):
        if len(args) == 2 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], VectorTBIntT0T3TT):
            return rl_can_enumerate__BIntT0T3T_VectorTBIntT0T3TT_r_bool(*args)


        if len(args) == 2 and isinstance(args[0], builtins.bool) and isinstance(args[1], VectorTboolT):
            return rl_can_enumerate__bool_VectorTboolT_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], GameMarkOr):
            return rl_can_enumerate__alt_GameMark_r_bool(*args)


        if len(args) == 1 and isinstance(args[0], GameMark):
            return rl_can_enumerate__GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_enumerate"

    def can_pretty_print(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_pretty_print__Game_r_bool(*args)


        assert False, "no correct overload to invoke can_pretty_print"

    def substring_matches(*args):
        if len(args) == 3 and isinstance(args[0], String) and isinstance(args[1], builtins.str) and isinstance(args[2], builtins.int):
            return rl_m_substring_matches__String_strlit_int64_t_r_bool(*args)


        assert False, "no correct overload to invoke substring_matches"

    def can__observation_tensor_warnings(*args):
        if len(args) == 3 and isinstance(args[0], Game) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can__observation_tensor_warnings__Game_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can__observation_tensor_warnings__int64_t_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], Board) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can__observation_tensor_warnings__Board_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0],  list ) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can__observation_tensor_warnings__BIntT0T3T_9_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], builtins.bool) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can__observation_tensor_warnings__bool_String_VectorTStringT_r_bool(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_can__observation_tensor_warnings__BIntT0T3T_String_VectorTStringT_r_bool(*args)


        assert False, "no correct overload to invoke can__observation_tensor_warnings"

    def can_current_player(*args):
        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_can_current_player__Board_r_bool(*args)


        assert False, "no correct overload to invoke can_current_player"

    def count(*args):
        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_count__String_int8_t_r_int64_t(*args)


        assert False, "no correct overload to invoke count"

    def get_enumeration_errors_impl(*args):
        if len(args) == 3 and isinstance(args[0], GameMarkOr) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_get_enumeration_errors_impl__alt_GameMark_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], GameMark) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_get_enumeration_errors_impl__GameMark_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], BIntT0T3T) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_get_enumeration_errors_impl__BIntT0T3T_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_get_enumeration_errors_impl__int64_t_String_VectorTStringT(*args)


        assert False, "no correct overload to invoke get_enumeration_errors_impl"

    def can_observation_tensor_size(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_observation_tensor_size__Game_r_bool(*args)


        assert False, "no correct overload to invoke can_observation_tensor_size"

    def gen_python_methods(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], GameMarkOr):
            return rl_gen_python_methods__Game_alt_GameMark(*args)


        assert False, "no correct overload to invoke gen_python_methods"

    def full(*args):
        if len(args) == 1 and isinstance(args[0], Board):
            return rl_m_full__Board_r_bool(*args)


        assert False, "no correct overload to invoke full"

    def enumeration_error(*args):
        if len(args) == 3 and isinstance(args[0], builtins.int) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_enumeration_error__int64_t_String_VectorTStringT(*args)


        if len(args) == 3 and isinstance(args[0], builtins.float) and isinstance(args[1], String) and isinstance(args[2], VectorTStringT):
            return rl_enumeration_error__double_String_VectorTStringT(*args)


        assert False, "no correct overload to invoke enumeration_error"

    def drop_back(*args):
        if len(args) == 2 and isinstance(args[0], VectorTint8_tT) and isinstance(args[1], builtins.int):
            return rl_m_drop_back__VectorTint8_tT_int64_t(*args)


        if len(args) == 2 and isinstance(args[0], String) and isinstance(args[1], builtins.int):
            return rl_m_drop_back__String_int64_t(*args)


        assert False, "no correct overload to invoke drop_back"

    def can_gen_python_methods(*args):
        if len(args) == 2 and isinstance(args[0], Game) and isinstance(args[1], GameMarkOr):
            return rl_can_gen_python_methods__Game_alt_GameMark_r_bool(*args)


        assert False, "no correct overload to invoke can_gen_python_methods"

    def can_get_current_player(*args):
        if len(args) == 1 and isinstance(args[0], Game):
            return rl_can_get_current_player__Game_r_bool(*args)


        assert False, "no correct overload to invoke can_get_current_player"

