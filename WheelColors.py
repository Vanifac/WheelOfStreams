
color_dict = {
    "White": "#FFFFFF",
    "Silver": "#C0C0C0",
    "Gray": "#808080",
    "Black": "#000000",
    "Red": "#FF0000",
    "Maroon": "#800000",
    "Yellow": "#FFFF00",
    "Olive": "#808000",
    "Lime": "#00FF00",
    "Green": "#008000",
    "Aqua": "#00FFFF",
    "Teal": "#008080",
    "Blue": "#0000FF",
    "Navy": "#000080",
    "Fuchsia": "#FF00FF",
    "Purple": "#800080"}


def get_color(color: str):
    if color.title() in color_dict:
        return color_dict[color.title()]
    return None


def validate_color(color: str):
    new_color = None
    # Check Color HEX
    if color[0] == "#" and len(color) == 7:
        try:
            int(color[1:], 16)
            new_color = color
        except ValueError:
            pass
    else:
        new_color = get_color(color)
    return new_color
