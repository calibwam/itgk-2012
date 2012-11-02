cheeses = {
    'cheddar':
        ('A235-4','A236-1','A236-2','A236-3','A236-5','C31-1','C31-2'),
    'mozarella':
        ('Q456-9','Q456-8','A234-5','Q457-1','Q457-2'),
    'brie':
        ('ZLAFS55-4','ZLAFS55-9','GOMBOS-7','A236-4'),
    'geitost':
        ('SPAZ-1','SPAZ-3','EMACS45-0'),
    'port salut':
        ('B15-1','B15-2','B15-3','B15-4','B16-1','B16-2','B16-4'),
    'camembert':
        ('A243-1','A234-2','A234-3','A234-4','A235-1','A235-2','A235-3'),
    'ridder':
        ('GOMBOS-4','B16-3'),
}


print("Port salut is found in the following shelfs:")
list(map(print, cheeses['port salut']))


def check_cheese(cheese, shelf):
    if shelf.split('-')[0] in infected_shelfs and cheese not in pos_infected_cheeses:
        return 1
    return 0

print("\nThe following cheeses is potentionally infected:")
infected_shelfs = ['A234', 'A235', 'B13', 'B14', 'B15', 'C31']
pos_infected_cheeses = []
for cheese in cheeses.keys():
    for shelf in cheeses[cheese]:
        if check_cheese(cheese, shelf):
            pos_infected_cheeses.append(cheese)
list(map(print, pos_infected_cheeses))


print("\nCheeses to be sold:")
cheese_to_be_sold = []
for cheese in cheeses.keys():
    if cheese not in pos_infected_cheeses:
        for shelf in cheeses[cheese]:
            cheese_to_be_sold.append((shelf,cheese))

for t in cheese_to_be_sold:
    print("%s %s" % t)
