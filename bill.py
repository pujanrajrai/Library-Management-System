import datetime #importing datetime object
def billborrow(l1,l3):
    total1 = 0
    for i in l3:
        total1 += float(l1[i][-1]) #total amount to be paid for borrowing book
    return total1
        
def billreturn(l2,l4):
    total2 = 0
    for i in l4:
        string_date = l2[i][3]
        format = "%Y-%m-%d"#making datetime object
        datetime_object = datetime.datetime.strptime(string_date, format)
        t =datetime.datetime.today()-datetime_object
        if t.days > 10:#checking for fine
            total2 += (t.days - 10) * 0.1
    print(total2)
 
def billrecord(total1,total2,name):
    if total2 == None:
        total2 = 0
    bill = open("billrecord.txt","a")#opeing biirecord.txt file in append mode

    bill.write(f"""
*****************BILL************************
Mr/Mrs  {name} 
                 Book Borrowed = {total1}
                 Fine          ={total2}
YOU HAVE TO PAY  Total         ={total1+total2}
***********************************************
            """)
    print(f"""
*****************BILL************************
Mr/Mrs  {name} 
                 Book Borrowed = {total1}
                 Fine          ={total2}
YOU HAVE TO PAY  Total         ={total1+total2}
***********************************************
            """)
