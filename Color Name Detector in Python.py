import webcolors

# for hex_code, name in webcolors.CSS3_HEX_TO_NAMES.items():
#     print(f"{hex_code}: {name}")

def closest(rgb):
    diff={}

    for hex_code, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(hex_code)
        diff[sum([(r - rgb[0]) ** 2, (g - rgb[1]) ** 2, (b - rgb[2]) ** 2])] = name

    return diff[min(diff.keys())]

color=(255,0,0)

try:
    color_name=webcolors.rgb_to_name(color)
    print(f"Color is exactly :{color_name}")
except ValueError:
    color_name=closest(color)
    print(f"Color is closest to : {color_name}")






