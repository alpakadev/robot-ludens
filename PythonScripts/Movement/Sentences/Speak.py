from ..Enums.Sentence import Sentence
from ..Sentences.Level_dec import sentence_level_dec
from ..Sentences.Level_inc import sentence_level_inc
from ..Sentences.chance_hm import sentence_chance_hm
from ..Sentences.chance_rh import sentence_chance_rh
from ..Sentences.detect_tie import sentence_detect_tie
from ..Sentences.illegalmove_hm import sentence_illegalmove_hm
from ..Sentences.illegalmove_rh import sentence_illegalmove_rh
from ..Sentences.joke import sentence_joke
from ..Sentences.next_move_hm import sentence_nextmove_hm
from ..Sentences.next_move_rh import sentence_nextmove_rh
from ..Sentences.trap_done_rh import sentence_trap_done
from ..Sentences.trap_recognize import sentence_trap_recognize
from ..Sentences.win_prevent import sentence_win_prevent
from ..Sentences.win_prevent_failed import sentence_win_prevent_failed
from ..Sentences.waiting import sentence_waiting

def sentence_line(sentence_type: Sentence):
        match sentence_type:
            case Sentence.LEVEL_DEC:
                sentence_level_dec()
            case Sentence.LEVEL_INC:
                sentence_level_inc()
            case Sentence.CHANCE_HM:
                  sentence_chance_hm()
            case Sentence.CHANCE_RH:
                sentence_chance_rh()
            case Sentence.DETECT_TIE:
                sentence_detect_tie()
            case Sentence.ILLEGALMOVE_HM:
                sentence_illegalmove_hm()
            case Sentence.ILLEGALMOVE_RH:
                sentence_illegalmove_rh()
            case Sentence.JOKE:
                sentence_joke()
            case Sentence.NEXT_MOVE_HM:
                sentence_nextmove_hm()
            case Sentence.NEXT_MOVE_RH:
                sentence_nextmove_rh()
            case Sentence.TRAP_DONE_RH:
                sentence_trap_done()
            case Sentence.TRAP_RECOGNIZE:
                sentence_trap_recognize()
            case Sentence.WAITING:
                sentence_waiting()
            case Sentence.WIN_PREVENT:
                sentence_win_prevent()
            case Sentence.WIN_PREVENT_FAILED:
                sentence_win_prevent_failed()
    
                