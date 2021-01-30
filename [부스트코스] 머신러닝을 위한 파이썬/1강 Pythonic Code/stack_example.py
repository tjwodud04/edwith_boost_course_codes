word = input("Input a word: ")
world_list = list(word)

print(world_list)
'''example result
['C', 'a', 'r', 'n', 'i', 'v', 'a', 'l']
'''

result = []

for _ in range(len(world_list)):
    result.append(world_list.pop())

print(result)
print(word[::-1])
'''
['l', 'a', 'v', 'i', 'n', 'r', 'a', 'C']
lavinraC
'''