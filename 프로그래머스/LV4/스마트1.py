def solution(dust_list, r, c, move_list):
    for i in dust_list:
        dust_list.insert(0, -2)
    print(dust_list)
    return dust_list
    # side = 1; dust_sum = 0
    # for i in move:
    #     if i == "go":
    #         continue

print(solution([[5, -1, 4], [6, 3, -1], [2, -1, 1]], 1, 0, ["go", "go", "right", "go", "right", "go", "left", "go"]))

