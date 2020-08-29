def showBooks(l1):
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if j == 0:
                print(l1[i][j],end="  ")
            elif len(l1[i][j])>18:
                print(l1[i][j],end="\t")
            elif len(l1[i][j])>13:
                print(l1[i][j],end="\t\t")
            else:
                print(l1[i][j],end="\t\t\t")
        print("\n")
            
