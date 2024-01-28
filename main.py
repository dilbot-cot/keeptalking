def get_boolean_input(prompt):
    return input(prompt).lower() == 'y'

def get_wire_color():
    color = input("What is the wire color (Enter 'stripe' for red and blue): ").lower()
    return color

def should_cut_wire(wire, serial, parallel, batteries, light, star):
    if wire == "white":
        return not light or (light and star and batteries)
    elif wire == "red":
        return (not light and star) or (not light and not star and serial) or (light and batteries)
    elif wire == "blue":
        return (not light and not star and serial) or (light and parallel)
    elif wire == "stripe":
        return (not star and serial) or (not light and star and parallel)
    return False

def get_input():
    serial = get_boolean_input("Is last digit of serial number even (y/n): ")
    parallel = get_boolean_input("Does bomb have parallel port (y/n): ")
    batteries = get_boolean_input("Does bomb have two or more batteries (y/n): ")

    while True:
        if not get_boolean_input("Is there more wires? (y/n): "):
            break

        light = get_boolean_input("Does wire have LED on (y/n): ")
        star = get_boolean_input("Does wire have star (y/n): ")
        wire = get_wire_color()

        if should_cut_wire(wire, serial, parallel, batteries, light, star):
            print("Cut")
        else:
            print("Leave")

get_input()