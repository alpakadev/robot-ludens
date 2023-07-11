from enum import Enum


class Sentence(Enum):
    LEVEL_INC = "level_inc",
    LEVEL_DEC = "level_dec",
    CHANCE_HM = "chance_human",
    CHANCE_RH = "chance_reachy",
    DETECT_TIE = "detect_tie",
    ILLEGALMOVE_HM = "illegalmove_hm",
    ILLEGALMOVE_RH = "illegalmove_rh",
    JOKE= "joke",
    NEXT_MOVE_HM = "next_move_hm",
    NEXT_MOVE_RH = "next_move_rh",
    TRAP_DONE_RH= "trap_done_rh",
    TRAP_RECOGNIZE= "trap_recognize",
    WAITING= "waiting",
    WIN_PREVENT= "win_prevent",
    WIN_PREVENT_FAILED= "win_prevent_failed",


