start_half = input().strip()
N = int(input())
cards = list(map(int, input().split()))

top_ptr = 0
bottom_ptr = N // 2

shuffled_cards = []

if start_half == "top":
    while len(shuffled_cards) < N:
        shuffled_cards.append(cards[top_ptr])
        top_ptr += 1
        if len(shuffled_cards) < N:
            shuffled_cards.append(cards[bottom_ptr])
            bottom_ptr += 1
else:
    while len(shuffled_cards) < N:
        shuffled_cards.append(cards[bottom_ptr])
        bottom_ptr += 1
        if len(shuffled_cards) < N:
            shuffled_cards.append(cards[top_ptr])
            top_ptr += 1

print(" ".join(map(str, shuffled_cards)))
