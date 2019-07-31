""""
    Author      : YOANE KARATSUBA
    
    Title       : River
    
    Description : the program describes interactions within a river between bears and fish 
                  when fishes or bears of same gender collide the stronger kills the weaker, otherwise the create a new animal
                  that we add into our river.
                  However if a bear collides with a fish th fish dies no matter what.
                  
    Version     : 2.0
    
    Motto       : Learn, Love, Live code
               
"""""

import random
from Fish import Fish
from bear import Bear


def ecosystem(river):
    eco = list()
    for i in range(len(river)):
        eco.append(river[i].about())
    return eco


def main():
    fb = open("log.txt",'a')                # log file to store the ecosystem
    f1 = Fish("gray", 'f1', 100, False)
    f2 = Fish('red', 'f2', 120)
    f3 = Fish('yellow', 'f3', 150, False)

    b1 = Bear("black", 'b1', 200, False)
    b2 = Bear("gray", 'b2', 1000, True)
    b3 = Bear("white",'b3', 500, True)

    identifier = 4

    river = [f1, f2, b2, b1, f1, b2, b3, f2, f3]  # river as the ecosystem where bears and fish cohabit

    colors = ['black', 'gray', 'yellow', 'red', 'white']  # colors list where to pick colors for new object

    i = 0
    j = i + 1
    while i < len(river) and j < len(river):
        length = len(river)                     # the length of the river

        if (isinstance(river[i], Fish) and isinstance(river[j], Bear)) or (isinstance(river[i], Bear) and isinstance(river[j], Fish)):

            if isinstance(river[i], Bear):    # if the previous animal is a bear then the next is a fish

                if river[i].kill(river[j]):   # if kill return True
                    print("\nFish", river[j].get_id(), "died and killed by", river[i].get_id())
                    del river[j]              # we kill the fish by deleting it from the river

            else:                                                                                     # otherwise
                if river[j].kill(river[i]):                                                           # if kill return True
                    print("\nFish", river[i].get_id(), "died and killed by", river[j].get_id())
                    del river[i]                                                                       # then kill the fish by deleting it from the ecosystem

        else:
            if isinstance(river[i], Bear) and isinstance(river[j], Bear):       # check if previous and next are bears

                if river[i].get_gender() == river[j].get_gender():              # check whether two bears are same gender or not

                    if river[i].get_strength() > river[j].get_strength():       # if the previous is stronger than the next previous kills next

                        print("\nBear ", river[i].get_id(), "killed", river[j].get_id())

                        del river[j]                                            # delete next in river

                    else:                                                       # otherwise

                        print("\nBear ", river[j].get_id(), "killed", river[i].get_id())  # kill previous because next is stronger

                        del river[i]                                                    # delete previous in river

                else:
                    new_bear = Bear(random.choice(colors), ('b'+str(identifier)))   # create a new one if the condition above is met

                    k = random.randint(0, length)                                   # generate a random number to use as index

                    river[k-(length//3)] = new_bear                                 # set the new bear at a random place

                    print("\nbear", new_bear.get_id(), " is born \n")

                    identifier += 1                                                 # increment id for the next birth

            else:
                if river[i].get_gender() == river[j].get_gender():                     # check whether two fish are same gender or not

                    if river[i].get_strength() > river[j].get_strength():              # if previous is stronger than next

                        print("\nFish", river[i].get_id(), "killed", river[j].get_id())  # print

                        del river[j]                                                   # delete next in river

                    else:                                                              # otherwise

                        print("\nFish ", river[j].get_id(), "killed", river[i].get_id())

                        del river[i]                                                   # next kill previous fish
                else:
                    new_fish = Fish(random.choice(colors), ('f'+str(identifier)))

                    k = random.randint(0, length)                                   # generate a random number to use as index

                    river[k-(length//3)] = new_fish                                 # set the new bear at a random place

                    print("\nfish", new_fish.get_id(), "is born \n")

                    identifier += 1                                                 # increment id for the next birth

        i += 1
        j += 1

    print("\n",ecosystem(river))       # display the state of the ecosystem (river)
    print(ecosystem(river),file=fb)    # store the result in log file


if __name__ == "__main__":
    main()
