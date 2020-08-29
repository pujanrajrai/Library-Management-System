def borrowReturnBook(l1,sno,types):
    if types == '1':
        l1[int(sno)][3] = str(int(l1[int(sno)][3])-1)# decreasing the quantity when book is borrowed
    if types == '2':
        l1[int(sno)][3] = str(int(l1[int(sno)][3])+1)# increasing the quantity when book is returned
    file = open("librarybook.txt","w")#opening the library.txt file in write mode
    for i in l1:
        i = ','.join(i)
        file.write(i)#over writing in file
    file.close()
    

