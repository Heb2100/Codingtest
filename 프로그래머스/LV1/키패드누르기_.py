import math
def dist(li1, li2):
    return abs(li1[0]-li2[0])+abs(li1[1]-li2[1])
solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
loc = [[1, 0], [0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [2, 2], [0, 1], [1, 1], [2, 1]]
ans = []
L_loc = [0, 0]; R_loc = [2, 0]
for num in solution:
    if num in [1, 4, 7]:
        ans.append('L')
    if num in [3, 6, 9]:
        ans.append('R')
    if num in [2, 5, 8, 0]:
        if dist(L_loc, loc[num]) < dist(R_loc, loc[num]):
            ans.append('L')
        elif dist(L_loc, loc[num]) > dist(R_loc, loc[num]):
            ans.append('R')
        else:
            if hand == 'left':
                ans.append('L')
            if hand == 'right':
                ans.append('R')
    if ans[-1] == 'L':
        L_loc = loc[num]
    else:
        R_loc = loc[num]
print(''.join(ans))


