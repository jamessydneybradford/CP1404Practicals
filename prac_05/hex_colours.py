"""
Hex Colours
"""
COlOUR_TO_HEX = {"ABSOLUTE ZERO": "#b0bf1a", "ACID GREEN": "#b0bf1a",
                "ALICEBLUE": "#f0f8ff", "ALIZARIN CRIMSON": "#e32636",
                 "AMARANTH ": "#e52b50", "AMBER": "#ffbf00",
                 "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7",
                 "ANTIQUEWHITE1": "#ffefdb", "ANTIQUEWHITE2": "#eedfcc"}

# print(COlOUR_TO_HEX)
print()
print()
print(f"{'Colour':21} {'Hex'}")
for colour, hex in COlOUR_TO_HEX.items():
    print(f"{colour:20}  {hex}")
print()
colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    try:
        print(colour_name, "has hex value", COlOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid cour name")
    print()
    colour_name = input("Enter colour name: ").upper()

