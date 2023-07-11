import random

from .Enums.Outside import Outside


class OutsideBlockManager:
    """
    Diese Klasse verwaltet Außenblöcke und stellt Methoden zum Nehmen und Zurücksetzen von Blöcken bereit.
    Es wird ein Singleton-Muster verwendet, um sicherzustellen, dass nur eine Instanz der Klasse erstellt wird.
    """

    _instance = None

    def __new__(cls):
        """
        Erstellt eine Instanz der Klasse, falls noch keine existiert, und initialisiert die Attribute.
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.block_count = 5
            cls._instance.outside_blocks = list(Outside)

        return cls._instance

    def take_block(self) -> Outside | None:
        """
        Nimmt einen Außenblock, falls verfügbar, und aktualisiert den Status der verfügbaren Blöcke.
        Gibt den genommenen Block zurück oder None, wenn keine Blöcke verfügbar sind.
        """

        if self.block_count > 0:
            block_to_take = random.choice(self.outside_blocks)
            self.outside_blocks.remove(block_to_take)
            self.block_count -= 1
            return block_to_take

        return None

    def reset(self) -> None:
        """
        Setzt die Anzahl der verfügbaren Blöcke zurück.
        """

        self._instance = 5
