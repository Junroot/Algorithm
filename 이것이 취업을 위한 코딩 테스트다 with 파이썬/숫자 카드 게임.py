n, m = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]
min_per_row = [min(cards_per_row) for cards_per_row in cards]

print(max(min_per_row))
