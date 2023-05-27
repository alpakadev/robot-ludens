from enum import Enum

# Für unsere Config zu DEBUG Zwecken genutzt
class Stage(Enum):
    SIMULATION="simulation"
    LAB="lab"
    TESTING="testing"