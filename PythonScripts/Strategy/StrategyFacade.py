from .Game import Game

class StrategyFacade:
    def __init__(self):
        self.game = Game()


    def set_dependencies(self,  move, perc):
        self.game.set_dependency(move,perc)

    def start_game(self):
        return self.game.arcadeModus()

#if __name__ == "__main__":
#    game = StrategyFacade()

