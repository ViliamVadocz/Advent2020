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
            colours[colour] = [(int(words[0]), "".join(words[1:3])) for words in statements]


def rec(colour):
    return sum(amount * rec(c) for amount, c in colours[colour]) + 1

print(rec("shinygold") - 1)
