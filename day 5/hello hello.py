# list stuffs
fweinds = ['doge', 'birb', 'frogge', 'ducko']

first_fweind = fweinds[0]
last_fweind = fweinds[3]

print('me fweinds list: ', fweinds)
print('me first fweind: ', first_fweind)
print('me last fweind: ', last_fweind)

# i dunno whats negative index, now i do
nega_first_fweind = fweinds[-4]
nega_last_fweind = fweinds[-1]

print('me nega first fweind: ', nega_first_fweind)
print('me nega last fweind: ', nega_last_fweind)

fweind1, fweind2, fweind3, fweind4 = fweinds
print('me fweinds are: ', fweind1, fweind2, fweind3, fweind4)

first_three_fweind = fweinds[:3]
last_three_fweind = fweinds[-3:]

print('me first 3 fweinds: ', first_three_fweind)
print('me last 3 fweinds: ', last_three_fweind)

fweinds.append('chimken')
print('me new fweind on list: ', fweinds)

fweinds.pop()
print('nvm, not me fweind anymore>:(', fweinds)

fweinds.append(fweind1)
print('me add', fweind1, 'again hehe')
print('now there\'s', fweinds.count(fweind1), fweind1)

fweinds.pop()
print('me removed it anyway: ', fweinds)

fweinds.reverse()
print('me reverses me list: ', fweinds)

fweinds.sort()
print('me sorts me list: ', fweinds)

fweinds.insert(0, 'wolfe')
print('me new number one fweind: ', fweinds)

fweinds.clear()
print(';-; now idh fweinds: ', fweinds)

fweinds.extend('a')
print('idk what extend does so here it is anyways: ', fweinds)