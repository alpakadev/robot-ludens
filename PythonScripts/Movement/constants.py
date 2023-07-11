HOST_ADDRESS = '192.168.1.94'

ORIGIN_COORDINATES = [0.15, -0.31, -0.38]

GRIP_FORCE_HOLDING = 60
GRIP_FORCE_HOLDING_THRESHOLD = 100

# The distance to position hand in front of object
DELTA_FRONT = 0.07
# The distance above the object to move the arm back
DELTA_HEIGHT = 0.22
#Distance about all cylinders on the field
DELTA_SAFE_HEIGHT = 0.03
# The distance from the middle of the hand to non-moving part
DELTA_HAND_WIDTH = 0.02
# The distance form the middle to tip of the hand
DELTA_HAND_TIP = 0.01

POS_ARM_AT_RIGHT_ANGLE = [0.36, -0.20, -0.28]
POS_SAVE_COORDINATES = [0.36, -0.2, 0]
POS_ARM_SIDE = [0, -0.45, -0.2]

HEAD_LOOK_FRONT = [0.5, 0, 0]
HEAD_LOOK_DOWN = [0.05, 0, -0.05]

GRIPPER_OPEN_FULL = -40
GRIPPER_CLOSED = 5

STEAL_PLACE = [0.3, 0.44, 0.08]

L_GRIPPER_CLOSE = 0
L_GRIPPER_OPEN = 50

ARM_SPEED_FACTOR = 1.6

#sounds

ANGRY_SOUND = ["PythonScripts/Movement/Sounds/angry/angr1.wav", "PythonScripts/Movement/Sounds/angry/angry2.wav"] 

CHANCE_WIN_HUMAN = ["PythonScripts/Movement/Sounds/chance_human/chance_hm1.wav", "PythonScripts/Movement/Sounds/chance_human/chance_hm2.wav"]

CHANCE_WIN_REACHY = ["PythonScripts/Movement/Sounds/chance_reachy/chance_rh1.wav", "PythonScripts/Movement/Sounds/chance_reachy/chance_rh2.wav", "PythonScripts/Movement/Sounds/chance_reachy/chance_rh3.wav"]

DETECT_TIE = ["PythonScripts/Movement/Sounds/detect_tie/detect_tie1.wav", "PythonScripts/Movement/Sounds/detect_tie/detect_tie2.wav",
               "PythonScripts/Movement/Sounds/detect_tie/detect_tie3.wav", "PythonScripts/Movement/Sounds/detect_tie/detect_tie4.wav", "PythonScripts/Movement/Sounds/detect_tie/detect_tie5.wav"]

START_HUMAN = ["PythonScripts/Movement/Sounds/game_start_human/start_hm1.wav", "PythonScripts/Movement/Sounds/game_start_human/start_hm2.wav", "PythonScripts/Movement/Sounds/game_start_human/start_hm3.wav", "PythonScripts/Movement/Sounds/game_start_human/start_hm4.wav", "PythonScripts/Movement/Sounds/game_start_human/start_hm5.wav"]

START_REACHY = ["PythonScripts/Movement/Sounds/game_start_reachy/start_rh1.wav", " PythonScripts/Movement/Sounds/game_start_reachy/start_rh2.wav", "PythonScripts/Movement/Sounds/game_start_reachy/start_rh3.wav", "PythonScripts/Movement/Sounds/game_start_reachy/start_rh4.wav", "PythonScripts/Movement/Sounds/game_start_reachy/start_rh5.wav"]

ILLEGALMOVE_REACHY = ["PythonScripts/Movement/Sounds/illegalmove_human/illegalmove_hm1.wav", "PythonScripts/Movement/Sounds/illegalmove_human/illegalmove_hm2.wav", "PythonScripts/Movement/Sounds/illegalmove_human/illegalmove_hm3.wav", "PythonScripts/Movement/Sounds/illegalmove_human/illegalmove_hm4.wav"]

ILLEGALMOVE_HUMAN = ["PythonScripts/Movement/Sounds/illegalmove_reachy/illegalmove_rh1.wav", "PythonScripts/Movement/Sounds/illegalmove_reachy/regelkonform.wav", "PythonScripts/Movement/Sounds/illegalmove_reachy/total_richtig.wav", "PythonScripts/Movement/Sounds/illegalmove_reachy/völlig_legal.wav"]

JOKE = ["PythonScripts/Movement/Sounds/joke/joke.wav"]

LEVEL_DECREASE = ["PythonScripts/Movement/Sounds/level_decrease/du_kannst_gewinnen.wav", "PythonScripts/Movement/Sounds/level_decrease/ohne_mühe.wav", "PythonScripts/Movement/Sounds/level_decrease/streng_dich_an.wav", "PythonScripts/Movement/Sounds/level_decrease/zurücklegen.wav"]

LEVEL_INCREASE = ["PythonScripts/Movement/Sounds/level_increase/viel_mühe.wav", "PythonScripts/Movement/Sounds/level_increase/mehr_anstrengen.wav", "PythonScripts/Movement/Sounds/level_increase/jz_strenge_mehr_an.wav"]

LOSING = ["PythonScripts/Movement/Sounds/losing/der_sieg_ist_dein.wav", "PythonScripts/Movement/Sounds/losing/du_hast_gewonnen.wav", "PythonScripts/Movement/Sounds/losing/glückwunsch.wav", "PythonScripts/Movement/Sounds/losing/gut_gespielt.wav", "PythonScripts/Movement/Sounds/losing/starke_leistung.wav"]

NEXT_MOVE_HUMAN = ["PythonScripts/Movement/Sounds/next_move_human/dein_zug.wav", "PythonScripts/Movement/Sounds/next_move_human/du_bist_dran.wav", "PythonScripts/Movement/Sounds/next_move_human/jetzt_du.wav"]

NEXT_MOVE_REACHY = ["PythonScripts/Movement/Sounds/next_move_reachy/hier_komme_ich.wav", "PythonScripts/Movement/Sounds/next_move_reachy/jetzt_bin_ich_dran.wav", "PythonScripts/Movement/Sounds/next_move_reachy/lass_mich_zeigen.wav", "PythonScripts/Movement/Sounds/next_move_reachy/mit_diesem_zug.wav", "PythonScripts/Movement/Sounds/next_move_reachy/pläne_durchkreuzen.wav", "PythonScripts/Movement/Sounds/next_move_reachy/überraschen.wav"]

THINKING = ["PythonScripts/Movement/Sounds/thinking/was_ist_nächster_zug.wav", "PythonScripts/Movement/Sounds/thinking/was_mache_ich_jz.wav", "PythonScripts/Movement/Sounds/before_thinking/before_thinking1.wav", "PythonScripts/Movement/Sounds/before_thinking/before_thinking2.wav"]

TIE = ["PythonScripts/Movement/Sounds/tie/auf_augenhöhe.wav", "PythonScripts/Movement/Sounds/tie/bestes_gegeben.wav", "PythonScripts/Movement/Sounds/tie/es_ist_unentschieden.wav", "PythonScripts/Movement/Sounds/tie/würdiger_gegner.wav"]

TRAP_DONE = ["PythonScripts/Movement/Sounds/trap_done_by_reachy/du_sitzt_in_der_falle.wav", "PythonScripts/Movement/Sounds/trap_done_by_reachy/jz_hab_ich_dich.wav", "PythonScripts/Movement/Sounds/trap_done_by_reachy/kein_entkommen.wav", "PythonScripts/Movement/Sounds/trap_done_by_reachy/keinen_ausweg.wav", "PythonScripts/Movement/Sounds/trap_done_by_reachy/nicht_fertig_gewinnen.wav"]

TRAP_RECOGNIZE = ["PythonScripts/Movement/Sounds/trap_recognize/das_funktioniert_bei_mir_nicht.wav", "PythonScripts/Movement/Sounds/trap_recognize/ich_durchschau_dich.wav", "PythonScripts/Movement/Sounds/trap_recognize/ich_durchschaue_deine_strategie.wav", "PythonScripts/Movement/Sounds/trap_recognize/ich_sehe_deine_strategie.wav", "PythonScripts/Movement/Sounds/trap_recognize/ich_sehe_was_du_versuchst.wav"]

WIN_PREVENT = ["PythonScripts/Movement/Sounds/win_prevent/keine_chance.wav", "PythonScripts/Movement/Sounds/win_prevent/ich_werde_dich_aufhalten.wav", "PythonScripts/Movement/Sounds/win_prevent/muss_ich_verhindern.wav","PythonScripts/Movement/Sounds/win_prevent/nicht_mit_mir.wav", "PythonScripts/Movement/Sounds/win_prevent/siegchance.wav"]

WIN_PREVENT_FAILED = ["PythonScripts/Movement/Sounds/win_prevent_failed/das_kann_nicht.wav", "PythonScripts/Movement/Sounds/win_prevent_failed/ich_wollte_gewinnen.wav", "PythonScripts/Movement/Sounds/win_prevent_failed/nicht_aufgepasst.wav", "PythonScripts/Movement/Sounds/win_prevent_failed/von_dir_lernen.wav", "PythonScripts/Movement/Sounds/win_prevent_failed/wie_hast_du_gemacht.wav"]

WINNING = ["PythonScripts/Movement/Sounds/winning/du_hast_verloren.wav", "PythonScripts/Movement/Sounds/winning/ich_bin_ein_gewinner.wav", "PythonScripts/Movement/Sounds/winning/ich_bin_unschlagbar.wav", "PythonScripts/Movement/Sounds/winning/ich_habe_gewonnen.wav", "PythonScripts/Movement/Sounds/winning/kollision.wav", "PythonScripts/Movement/Sounds/winning/sieg_an_mich.wav"]

WAITING =  ["PythonScripts/Movement/Sounds/waiting/bedenke_deine_schritte.wav", "PythonScripts/Movement/Sounds/waiting/denk_gut_nach.wav", "PythonScripts/Movement/Sounds/waiting/ich_warte.wav", "PythonScripts/Movement/Sounds/waiting/na_los.wav", "PythonScripts/Movement/Sounds/waiting/spannung_steigt.wav", "PythonScripts/Movement/Sounds/waiting/wer_gewinnen.wav", "PythonScripts/Movement/Sounds/waiting/whistling.wav", "PythonScripts/Movement/Sounds/waiting/zeit_zum_nachdenken.wav"]