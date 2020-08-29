def returnBook(l1,sno):
    l1[int(sno)][3] = str(int(l1[int(sno)][3])+1)
    file = open("librarybook.txt","w")
    for i in l1:
        i = ','.join(i)
        file.write(i)
    file.close()
