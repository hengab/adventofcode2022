import typing as typ

opponent_rock: typ.Literal["A"] = "A"
opponent_paper: typ.Literal["B"] = "B"
opponent_scissors: typ.Literal["C"] = "C"
me_rock: typ.Literal["X"] = "X"
me_paper: typ.Literal["Y"] = "Y"
me_scissors: typ.Literal["Z"] = "Z"
loss: typ.Literal["X"] = "X"
draw: typ.Literal["Y"] = "Y"
win: typ.Literal["Z"] = "Z"

hand_sign_score: typ.Dict[str, int] = {me_rock: 1, me_paper: 2, me_scissors: 3}
rock_score: typ.Literal[1] = 1
paper_score: typ.Literal[1] = 2
scissors_score: typ.Literal[1] = 3
loss_score: typ.Literal[0] = 0
draw_score: typ.Literal[3] = 3
win_score: typ.Literal[6] = 6
part_1_round_score: typ.Dict[typ.Tuple[str, str], int] = {
    (opponent_rock, me_rock): draw_score,
    (opponent_rock, me_paper): win_score,
    (opponent_rock, me_scissors): loss_score,
    (opponent_paper, me_rock): loss_score,
    (opponent_paper, me_paper): draw_score,
    (opponent_paper, me_scissors): win_score,
    (opponent_scissors, me_rock): win_score,
    (opponent_scissors, me_paper): loss_score,
    (opponent_scissors, me_scissors): draw_score,
}

part_2_round_score: typ.Dict[str, int] = {
    loss: loss_score,
    draw: draw_score,
    win: win_score,
}
my_hand_sign_score: typ.Dict[typ.Tuple[str, str], int] = {
    (opponent_rock, loss): scissors_score,
    (opponent_rock, draw): rock_score,
    (opponent_rock, win): paper_score,
    (opponent_paper, loss): rock_score,
    (opponent_paper, draw): paper_score,
    (opponent_paper, win): scissors_score,
    (opponent_scissors, loss): paper_score,
    (opponent_scissors, draw): scissors_score,
    (opponent_scissors, win): rock_score,
}

part_1_score = 0
part_2_score = 0
with open("input.txt") as input_file:
    for line in input_file.readlines():
        if line.strip() != "":
            round_input = (line[0], line[2])
            part_1_score = (
                part_1_score
                + hand_sign_score[round_input[1]]
                + part_1_round_score[round_input]
            )
            part_2_score = (
                part_2_score
                + my_hand_sign_score[round_input]
                + part_2_round_score[round_input[1]]
            )

print(f"Part 1 Score: {part_1_score}")
print(f"Part 2 Score: {part_2_score}")
