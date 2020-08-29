import datetime #importing datetime
def record(name,l1,types,sno):
    fh = open("record.txt", "a")#opening record.txt in append mode
    fh.write(name)#user name
    fh.write(",")
    fh.write(l1[int(sno)][1])#book_name
    fh.write(",")
    fh.write("YES")#borrow_book
    fh.write(",")
    fh.write(str(datetime.date.today()))#borrowed_time
    fh.write(",")
    fh.write("NO")#reutrn_book
    fh.write(",")
    fh.write("NO")#return_time
    fh.write(",")
    fh.write(str(l1[int(sno)][4]))#price
    fh.write("\n")
    
    fh.close()
    
def recordReturn(l2,a):
    rec = open("record.txt","w")# opening record.txt in write mode
    l2[a][4] = "YES" 
    l2[a][5] = str(datetime.date.today())
    for i in l2:
        i = ','.join(i)
        rec.write(i)#writing in record file
    rec.close()
def recordindividual(name,types,sno,l1):
    indv = open(name+str(datetime.datetime.now())+".txt","w")#opening new file for each trasaction in write mode
    indv.write(l1[int(sno)][1])
    indv.write(",")
    if types == '1':#when borrwing
        indv.write("borrowed")
        indv.write(",")
        indv.write(str(datetime.date.today()))
    elif types == '2':#while returning
        indv.write("returned")
        indv.write(",")
        indv.write(str(datetime.date.today()))
        indv.write("\n")
        
    
