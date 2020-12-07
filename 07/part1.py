with open("input.txt", "r") as file:
    colours = {}
    for line in file.readlines():
        colour, rest = line.split("bags contain")
        colour = colour.replace(" ", "")
        if "no other" in rest:
            colours[colour] = []
        else:
            statements = rest.split(",")
            statements = [bag_type.split() for bag_type in statements]
            colours[colour] = ["".join(words[1:3]) for words in statements]


on_outside = {colour: False for colour in colours.keys()}
on_outside["shinygold"] = True

def rec(colour, origin):
    global on_outside
    return colour != origin and (
        on_outside[colour] or any(rec(c, origin) for c in colours[colour])
    )

for colour in on_outside.keys():
    on_outside[colour] |= any(rec(c, colour) for c in colours[colour])
    # print(colour, on_outside[colour])

on_outside["shinygold"] = False
print(sum(1 for v in on_outside.values() if v))
