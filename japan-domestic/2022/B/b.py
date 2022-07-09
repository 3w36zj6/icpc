while True:
    N = int(input())

    if N == 0:
        break

    players = [list(map(int,input().split())) for _ in range(N)]
    players_set = [set(cards) for cards in players]

    ans = 0

    # init
    for i in range(N):
        if players[i][0] == players[i][1]:
            players[i] = []
            players_set[i] = set()

    giver_index = -1
    taker_index = 0

    while any(players):

        for j in range(N):
            if players[(giver_index+j)%N]  and (giver_index)%N != (giver_index+j)%N:
                giver_index = giver_index + j
                break
        else:
            break

        for j in range(N):
            if players[(giver_index+1+j)%N] and (giver_index)%N != (giver_index+1+j)%N:
                taker_index = giver_index + 1 + j
                break



        min_card = min(players[giver_index%N])
        min_card_index = players[giver_index%N].index(min_card)
        players[(taker_index)%N].append(min_card)
        players[giver_index%N].pop(min_card_index)
        ans += 1
        players_set[giver_index%N].remove(min_card)

        if min_card in players_set[(taker_index)%N]:
            players[(taker_index)%N].remove(min_card)
            players[(taker_index)%N].remove(min_card)
            players_set[(taker_index)%N].remove(min_card)
        else:
            players_set[(taker_index)%N].add(min_card)

    print(ans)
