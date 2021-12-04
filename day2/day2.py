depth, pos = 0, 0
with open("input.dat", "r") as infile:
    for line in infile:
        command, distance = line.split()
        distance = int(distance)
        if command == "forward":
            pos += distance
        elif command == "down":
            depth += distance
        elif command == "up":
            depth -= distance
        else:
            raise ValueError("Unknown command")
print(depth, pos, depth*pos)

depth, pos, aim = 0, 0, 0
with open("input.dat", "r") as infile:
    for line in infile:
        command, distance = line.split()
        distance = int(distance)
        if command == "forward":
            pos += distance
            depth += distance*aim
        elif command == "down":
            aim += distance
        elif command == "up":
            aim -= distance
        else:
            raise ValueError("Unknown command")
print(depth, pos, depth*pos)
