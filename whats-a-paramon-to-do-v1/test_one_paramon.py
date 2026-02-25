import random

def starting_effects(table,effects):
    for x in range(0,8):
        effects.append(table[x])
    del table[0:8]
    return(table,effects)

def new_round(table,effects):
    index1 = random.randrange(len(effects))
    active_effect = effects[index1]
    print("The active effect is: " + str(active_effect))
    effects[index1] = table[0]
    del table[0]
    return(table,effects)

effect_table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
effect_set = []

random.shuffle(effect_table)

starting_effects(effect_table,effect_set)
print("Your starting effects are: " + str(effect_set))

new_round(effect_table,effect_set)
print("Your new set of effects are: " + str(effect_set))
print ("There are " + str(len(effect_table)) + " effects remaining. The remaining possible effects are: " + str(effect_table))