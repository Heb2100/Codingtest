def solution(dust_list, r, c, move_list):
    for i in dust_list:
        i.insert(0, -2)
        i.append(-2)
    dust_list.append([-2 for i in range(len(dust_list)+2)])
    dust_list.insert(0, [-2 for i in range(len(dust_list)+2)])

    side = 0; dust_sum = 0
    x=r+1;y=c+1
    dust_sum += dust_list[x][y]
    dust_list[x][y] = 0
    for i in move_list:
        if i == "go":
            if side == 0:
                if dust_list[x-1][y] not in [-1, -2]:
                    dust_sum += dust_list[x-1][y]
                    dust_list[x-1][y] = 0
                    x -= 1
                else: continue
            if side == 1:
                if dust_list[x][y+1] not in [-1, -2]:
                    dust_sum += dust_list[x][y+1]
                    dust_list[x][y+1] = 0
                    y += 1
                else: continue
            if side == 2:
                if dust_list[x+1][y] not in [-1, -2]:
                    dust_sum += dust_list[x+1][y]
                    dust_list[x][y+1] = 0
                    x += 1
                else: continue
            if side == 3:
                if dust_list[x][y-1] not in [-1, -2]:
                    dust_sum += dust_list[x][y-1]
                    dust_list[x][y+1] = 0
                    y -= 1
                else: continue
        elif i == "right":
            side = (side+1)%4
        else:
            side = (side-1)%4
    return dust_sum

print(solution([[5, -1, 4], [6, 3, -1], [2, -1, 1]], 1, 0, ["go", "go", "right", "go", "right", "go", "left", "go"]))
