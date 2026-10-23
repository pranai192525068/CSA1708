
rooms = {"A": "Dirty", "B": "Dirty"}
current = "A"

while True:
    if rooms[current] == "Dirty":
        print("Clean room", current)
        rooms[current] = "Clean"
    else:
        print("Room", current, "is already clean")

    if current == "A":
        current = "B"
    else:
        if all(status == "Clean" for status in rooms.values()):
            break
        current = "A"

print("All rooms are clean")
