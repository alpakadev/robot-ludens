from OutsideBlockManager import OutsideBlockManager


class OutsideBlockFacade:
    def __init__(self):
        self.block_manager = OutsideBlockManager()

    def take_block(self):
        return self.block_manager.take_block()

    def get_block_count(self):
        return self.block_manager.block_count
