def print_move(start, end):
    print(start, '-->', end)


def move(n, start, end):
    # Base case
    if n == 1:
        print_move(start, end)

    else:
        other = 6 - (start + end)
        move(n-1, start, other)
        print_move(start, end)
        move(n-1, other, end)

start_tower = 1
end_tower = 3
num_rings = 3
move(num_rings, start_tower, end_tower)
