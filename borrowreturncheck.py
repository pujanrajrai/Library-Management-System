import record
import borrowreturnBook as br
import returnBook
#importing all the required module
def recordborrow(l1,l2,name,sno,types,l3):
    for i in l2:
        if name  in i and l1[int(sno)][1] in i and i[2]=="YES" and i[4]=="NO":#checking for eligibility
            print("NOT ALLOWED TO BORROW\nYOU HAVE NOT RETURNED PREVIOUS BOOKS\n")
            return 
    
    l3.append(int(sno))
    br.borrowReturnBook(l1,sno,types)#calling borrowReturn fuction from borrowreturnBook.py
    print("Book borrowed")
    record.record(name,l1,types,sno)#calling record function from record.py
    record.recordindividual(name,types,sno,l1)#calling record function from recordindividual from record.py
    return 
        
def recordreturn(l1,l2,name,sno,l3,l4,types):
    a = 0
    for i in l2:
        a += 1
        if name  in i and l1[int(sno)][1] in i and i[2]=="YES" and i[4]=="NO":#checking for eligibility
            l4.append(a-1)
            if int(sno) in l3:
                l3.remove(int(sno))
            br.borrowReturnBook(l1,sno,types)#calling borrowReturn function from borrowreturn.py
            print("book returned")
            record.recordReturn(l2,a-1) #calling record function from record.py
            record.recordindividual(name,types,sno,l1)#calling record function record.py
            return 
    print("NO RECORD FOUND\nYOU HAVE NOT BORROWED BOOK FROM THIS LIBRARY\n")
    return
        
        
