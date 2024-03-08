from matplotlib import pyplot as plt


def main():
    directions = read_file("input02.txt")
    print(move(directions))


def read_file(file_name):
    with open(file_name) as infile:
        directions = infile.read().splitlines()
    return directions


def move(directions):
    knots_pos = [(0, 0) for _ in range(n_knots)]
    knots_last_pos = [(0, 0) for _ in range(n_knots)]
    visited_positions = {(0, 0)}

    def update_position(dx, dy):
        nonlocal knots_pos
        nonlocal knots_last_pos
        nonlocal visited_positions
        for _ in range(steps):
            for i in range(n_knots - 1):
                if i == 0:
                    knots_last_pos[i] = knots_pos[i]
                    knots_pos[i] = (knots_pos[i][0] + dx, knots_pos[i][1] + dy)
                    if (abs(knots_pos[i][0] - knots_pos[i + 1][0]) > 1 or
                            abs(knots_pos[i][1] - knots_pos[i + 1][1]) > 1):
                        knots_last_pos[i + 1] = knots_pos[i + 1]
                        knots_pos[i + 1] = knots_last_pos[i]
                # left, down
                elif ((((knots_pos[i][0] - knots_pos[i + 1][0]) < -1 and
                        (knots_pos[i][1] - knots_pos[i + 1][1]) < 0)) or
                      (((knots_pos[i][0] - knots_pos[i + 1][0]) < 0 and
                        (knots_pos[i][1] - knots_pos[i + 1][1]) < -1))):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] - 1, knots_pos[i + 1][1] - 1)
                # left, up
                elif (((knots_pos[i][0] - knots_pos[i + 1][0]) < -1 and
                       (knots_pos[i][1] - knots_pos[i + 1][1]) > 0)):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] - 1, knots_pos[i + 1][1] + 1)
                # up, left
                elif (((knots_pos[i][0] - knots_pos[i + 1][0]) < -1 and
                       (knots_pos[i][1] - knots_pos[i + 1][1]) > 0) or
                      ((knots_pos[i][0] - knots_pos[i + 1][0]) < 0 and
                       (knots_pos[i][1] - knots_pos[i + 1][1]) > 1)):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] - 1, knots_pos[i + 1][1] + 1)
                # up, right
                elif ((knots_pos[i][0] - knots_pos[i + 1][0]) > 1 and
                      (knots_pos[i][1] - knots_pos[i + 1][1]) > 0):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] + 1, knots_pos[i + 1][1] + 1)
                # right, up
                elif (((knots_pos[i][0] - knots_pos[i + 1][0]) > 1 and
                       (knots_pos[i][1] - knots_pos[i + 1][1]) > 0) or
                      (((knots_pos[i][0] - knots_pos[i + 1][0]) > 0 and
                        (knots_pos[i][1] - knots_pos[i + 1][1]) > 1))):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] + 1, knots_pos[i + 1][1] + 1)
                # right, down
                elif (((knots_pos[i][0] - knots_pos[i + 1][0]) > 1 and
                       (knots_pos[i][1] - knots_pos[i + 1][1]) < 0) or
                      ((knots_pos[i][0] - knots_pos[i + 1][0]) > 0 and
                       (knots_pos[i][1] - knots_pos[i + 1][1]) < -1)):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] + 1, knots_pos[i + 1][1] - 1)
                # down, left
                elif ((knots_pos[i][0] - knots_pos[i + 1][0]) < -1 and
                      (knots_pos[i][1] - knots_pos[i + 1][1]) < 0):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] - 1, knots_pos[i + 1][1] - 1)
                # down, right
                elif ((knots_pos[i][0] - knots_pos[i + 1][0]) > 1 and
                      (knots_pos[i][1] - knots_pos[i + 1][1]) < 0):
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] + 1, knots_pos[i + 1][1] - 1)
                # right
                elif knots_pos[i][0] - knots_pos[i + 1][0] > 1:
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] + 1, knots_pos[i + 1][1])
                # left
                elif knots_pos[i][0] - knots_pos[i + 1][0] < -1:
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0] - 1, knots_pos[i + 1][1])
                # up
                elif knots_pos[i][1] - knots_pos[i + 1][1] > 1:
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0], knots_pos[i + 1][1] + 1)
                # down
                elif knots_pos[i][1] - knots_pos[i + 1][1] < -1:
                    knots_last_pos[i + 1] = knots_pos[i + 1]
                    knots_pos[i + 1] = (knots_pos[i + 1][0], knots_pos[i + 1][1] - 1)
            visited_positions.add(knots_pos[-1])

    for line in directions:
        direction, steps = line.split()
        steps = int(steps)
        match direction:
            case 'R':
                update_position(1, 0)
            case 'L':
                update_position(-1, 0)
            case 'U':
                update_position(0, 1)
            case 'D':
                update_position(0, -1)
    plt.scatter(*zip(*visited_positions))
    plt.show()
    return len(visited_positions)


n_knots = 10
main()
