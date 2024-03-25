import random

Values = []
for i in range(10000):
  Players = [1, 2, 3, 4, 5, 6, 7, 8]
  Losers = 0

  while Losers < len(Players) - 1:
    WinnerIndex = random.randint(0, len(Players) - 1)
    CurrentPoints = Players[WinnerIndex]

    #print("Winner is player " + str(WinnerIndex) + ", who has " + str(CurrentPoints) + " points")

    if CurrentPoints == 0:
      continue

    for PlayerIndex in range(len(Players)):
      if PlayerIndex != WinnerIndex:
        Players[WinnerIndex] += min(Players[PlayerIndex], CurrentPoints)
        Players[PlayerIndex] = max(0, Players[PlayerIndex] - CurrentPoints)

    Losers = Players.count(0)

  Values.append(Players)

Sum = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(Values)):
  for j in range(len(Sum)):
    Sum[j] += Values[i][j] / 36

print("\n".join(str((x / 10000) * 100) + "%" for x in Sum))
