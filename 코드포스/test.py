string = 'abcdef'
# print(string[2:4:-1])
# input 3 4
# # print(string[:2]+string[3:1:-1]+string[4:])

# def switch(list, str):
#     print('1', str[:list[0]-1], '2',  str[list[1]-1:list[0]-2:-1], '3', str[list[1]:])
#     return str[:list[0]-1]+str[list[1]-1:list[0]-2:-1]+str[list[1]:]
# print(switch([1, 3], 'abcedfg'))

#23
print(string[0:2-1]+''.join(reversed(string[2-1:3]))+string[3:])