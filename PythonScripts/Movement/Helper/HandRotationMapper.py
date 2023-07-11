from ..Enums.Board import Board


class HandRotationMapper:
    """
    Die HandRotationMapper-Klasse bildet die Zielpositionen auf Rotationswinkel ab,
    die von der Hand des Reachy-Roboters verwendet werden.

    Attributes:
        rotations (dict): Ein Wörterbuch, das die Zielpositionen auf die entsprechenden Rotationswinkel abbildet.
    """

    def __init__(self):
        self.rotations = {
            'TOP_LEFT': 45,
            'TOP_CENTER': 45,
            'TOP_RIGHT': 0,
            'CENTER_LEFT': 45,
            'CENTER': 45,
            'CENTER_RIGHT': 0,
            'BOTTOM_LEFT': 90,
            'BOTTOM_CENTER': 90,
            'BOTTOM_RIGHT': 45,
        }

    def _map(self, pos_to: str):
        """
        Internes Mapping der Positionen auf Rotationswinkel.

        Args:
            pos_to (str): Die Zielposition als String.

        Returns:
            int: Der zugeordnete Rotationswinkel.
        """
        return self.rotations[pos_to]

    def get_hand_rotation(self, pos_to: Board):
        """
        Gibt den Rotationswinkel für die angegebene Zielposition zurück.

        Args:
            pos_to (Board): Die Zielposition als Board-Enum.

        Returns:
            int: Der zugeordnete Rotationswinkel.
        """
        return self._map(pos_to.name)
