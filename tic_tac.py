value = True
all_pos = []

# Players
X_player = [0, 0, 0, 0, 0, 0, 0, 0, 0]
O_player = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1


def board(x, o):
    zero = f"{'X' if x[0] == 1 else ('O' if o[0] == 1 else 0)}"
    one = f"{'X' if x[1] == 1 else ('O' if o[1] == 1 else 1)}"
    two = f"{'X' if x[2] == 1 else ('O' if o[2] == 1 else 2)}"
    three = f"{'X' if x[3] == 1 else ('O' if o[3] == 1 else 3)}"
    four = f"{'X' if x[4] == 1 else ('O' if o[4] == 1 else 4)}"
    five = f"{'X' if x[5] == 1 else ('O' if o[5] == 1 else 5)}"
    six = f"{'X' if x[6] == 1 else ('O' if o[6] == 1 else 6)}"
    seven = f"{'X' if x[7] == 1 else ('O' if o[7] == 1 else 7)}"
    eight = f"{'X' if x[8] == 1 else ('O' if o[8] == 1 else 8)}"

    global all_pos
    all_pos = [zero, one, two, three, four, five, six, seven, eight]

    print(f" {zero} | {one} | {two}")
    print("---|---|---")
    print(f" {three} | {four} | {five}")
    print("---|---|---")
    print(f" {six} | {seven} | {eight}")


def check_win(x, o):
    is_num = None
    for nums in all_pos:
        try:
            nums = int(nums)
        except ValueError:
            pass
        if isinstance(nums, int):
            is_num = True
        else:
            pass
    if not is_num:
        global value
        value = False
        print("Match is Draw!!")
    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in winning:
        if x[win[0]] + x[win[1]] + x[win[2]] == 3:
            print("Player X won!!")
            return "x"
        elif o[win[0]] + o[win[1]] + o[win[2]] == 3:
            print("Player O won!!")
            return "o"


board(X_player, O_player)

while value:
    if turn == 1:
        pos = int(input("X's turn to play: "))
        X_player[pos] = 1
        board(X_player, O_player)
    else:
        pos = int(input("O's turn to play: "))
        O_player[pos] = 1
        board(X_player, O_player)

    win = check_win(X_player, O_player)
    if win == "x" or win == "o":
        print("Match Over")
        break
    turn = 1 - turn
