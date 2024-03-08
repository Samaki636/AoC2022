def main():
    infile = read_file("input02.txt")
    print(start_p1(infile))
    for line in start_p2(infile):
        print(line)


def read_file(file_name):
    with open(file_name) as infile:
        return infile.read().splitlines()


def start_p1(infile):
    cycle_n = 1
    x = 1
    result = 0

    def check_strength():
        nonlocal cycle_n
        nonlocal x
        nonlocal result
        if (cycle_n - 20) % 40 == 0:
            result += cycle_n * x
            print(result)

    for line in infile:
        cycle_n += 1
        check_strength()
        if line != 'noop':
            x += int(line.split()[1])
            cycle_n += 1
            check_strength()
    return result


def start_p2(infile):
    crt = [['0' for _ in range(width)] for _ in range(height)]
    draw_x = 0
    draw_y = 0
    sprite_x = 1

    def draw_sprite():
        nonlocal crt
        nonlocal draw_x
        nonlocal draw_y
        nonlocal sprite_x
        if sprite_x - 1 <= draw_x <= sprite_x + 1:
            crt[draw_y][draw_x] = '#'
        else:
            crt[draw_y][draw_x] = '.'
        draw_x = (draw_x + 1) % width
        if draw_x == 0:
            draw_y += 1

    for line in infile:
        draw_sprite()
        if line != 'noop':
            sprite_x += int(line.split()[1])
            draw_sprite()
    return crt


width = 40
height = 6
main()
