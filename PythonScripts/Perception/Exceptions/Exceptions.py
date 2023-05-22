# Exception die gefangen und geworfen werden kann, wenn kein klares Bild des Spielfeldes zustande gekommen ist
class ViewCloudedError(Exception):
    """raised when view of board not clear"""

