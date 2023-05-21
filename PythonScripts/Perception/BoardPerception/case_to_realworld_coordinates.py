def case_to_realworld_coordinates(feldname):
    match feldname:
        case "TOP_LEFT_CORNER":
            return (28.4, 17.9)
        case "TOP_MIDDLE":
            return (28.4, 11.2)
        case "TOP_RIGHT_CORNER":
            return (28.4, 4.7)
        case "LEFT_MIDDLE":
            return (16.65, 17.9)
        case "CENTER":
            return (16.65, 11.2)
        case "RIGHT_MIDDLE":
            return (16.65, 4.7)
        case "BOTTOM_LEFT_CORNER":
            return (6.3, 17.9)
        case "BOTTOM_MIDDLE":
            return (6.3, 11.2)
        case "BOTTOM_RIGHT_CORNER":
            return (6.3, 4.7)
        case _:
            return "invalid input string"