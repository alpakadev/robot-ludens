import random
from .Enums.Outside import Outside


class OutsideBlockManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.block_count = 5
            cls._instance.outside_blocks = list(Outside)

        return cls._instance

    def take_block(self) -> Outside | None:
        if self.block_count > 0:
            block_to_take = random.choice(self.outside_blocks)
            self.outside_blocks.remove(block_to_take)
            self.block_count -= 1
            return block_to_take

        return None

    def reset(self) -> None:
        self._instance = 5
