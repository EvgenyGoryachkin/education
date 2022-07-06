import itertools
for p in itertools.permutations('012', 3):
    print(''.join(str(x) for x in p))

for p in itertools.combinations('01235', 3):
    print(''.join(p))
