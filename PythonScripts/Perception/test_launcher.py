from PerceptionFacade import PerceptionFacade
from reachy_sdk import ReachySDK
from Enums.stage import Stage
import yaml
config = yaml.safe_load(open("PythonScripts/Perception/config.yml"))

def getHost():
    if config["stage"] == Stage.SIMULATION.value:
        return "localhost"
    elif config["stage"] == Stage.LAB.value:
        #Add Reachys Lab IP here
        return "Reachys Lab IP"
    else:
        return "localhost"
    
reachy = ReachySDK(getHost())

perc = PerceptionFacade()
perc.set_dependencies(reachy, None, None)

# TESTING OF ALL FUNCTIONS
game_state = perc.get_game_state()
print(game_state)
coordinates = perc.get_coordinates_of_square("TOP_LEFT_CORNER")
print(coordinates)
valid = perc.check_game_state_validity([[-1, -1, 0], [1, -1, 0], [-1, 1, -1]])
print(valid)