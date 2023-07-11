from .OutsideBlockManager import OutsideBlockManager


class OutsideBlockFacade:
    def __init__(self):
        """
        Initialisiert die OutsideBlockFacade-Klasse und erstellt eine Instanz des OutsideBlockManagers.
        """
        self.block_manager = OutsideBlockManager()

    def take_block(self):
        """
        Nimmt einen verfügbaren Block von außerhalb, sofern verfügbare Blöcke nicht null sind. Andernfalls wird nichts getan.

        Returns:
            object | None: Der genommene Block oder None, wenn keine Blöcke verfügbar sind.
        """
        return self.block_manager.take_block()

    def get_block_count(self):
        """
        Gibt die Anzahl der aktuellen verfügbaren Blöcke von außerhalb zurück.

        Returns:
            int: Die Anzahl der verfügbaren Blöcke.
        """
        return self.block_manager.block_count

    def reset_block_count(self):
        """
        Setzt die aktuelle Blockanzahl auf den ursprünglichen Wert von 5 zurück.

        Returns:
            None
        """
        self.block_manager.reset()
