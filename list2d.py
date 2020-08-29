def lib2dlist():
    l1 = []#declaring empty list
    lib = open("librarybook.txt","r")#opening librarybook.txt in read mmode
    for i in lib:
        l1.append(i.split(",")) #appending i in l1
    lib.close()
    return l1 #returning l1
def record2dlist():
    l2 = []# declaring empty list
    rec = open("record.txt","r")#opening record.txt in read mmode
    for i in rec:
        l2.append(i.split(","))# appending i in l2
    rec.close()
    return l2# returning l2




