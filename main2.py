if __name__=='__main__':
    f = open("input.txt","r")
    #data = [[l.split("")[0],int(l.split("")[1])] for l f.read("\n")]
    data = f.read().split("\n")
    instructions = []
    horizontal = 0

    profondeur = 0
    resultat = 0
    objectif = 0

    for l in data:
        line = l.split (" ")
        tabline=[]
        tabline.append(line[0])
        tabline.append(int(line[1]))

        instructions.append(tabline)


    for l in instructions:
        if l[0]== "forward":
            horizontal = horizontal+l[1]
            profondeur = profondeur + objectif * l[1]

        if l[0]== "down":
            objectif = objectif + l[1]

        if l[0]== "up":
            objectif = objectif - l[1]



        resultat = horizontal*profondeur
    print("horizontal",horizontal)
    print("profondeur",profondeur)

    print("resultat",resultat)





    print(instructions)
