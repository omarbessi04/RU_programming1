piece_value = int(input())
if piece_value == 1:
    print("Pawn")
elif piece_value == 3:
    print("Bishop or Knight")
elif piece_value == 5:
    print("Rook")
elif piece_value == 9:
    print("Queen")
else:
    print("No piece")