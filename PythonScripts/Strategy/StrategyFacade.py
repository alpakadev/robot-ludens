from Game import Game

class StrategyFacade:
    def __init__(self):
        self.game = Game()


    def set_dependencies(self,  move, perc):
        self.perc = perc
        self.move = move


#if __name__ == "__main__":
#    game = StrategyFacade()

