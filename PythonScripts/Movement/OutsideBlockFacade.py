from OutsideBlockManager import OutsideBlockManager


class OutsideBlockFacade:
    def __init__(self):
        self.block_manager = OutsideBlockManager()

    def take_block(self):
        """
        Takes an available block from the outside if available blocks is not null else does nothing
        :rtype: object | None
        """
        return self.block_manager.take_block()

    def get_block_count(self):
        """
        Returns the current outside available blocks
        :rtype: int
        """
        return self.block_manager.block_count

    def reset_block_count(self):
        """
        Resets the current block count to the initial state of 5
        :rtype: None
        """
        self.block_manager.reset()
