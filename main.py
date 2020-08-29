import showBooks
import list2d
import borrowreturncheck as check
import bill

# importing all required module
l3 = []
l4 = []
cond = "y"
while cond == "y":
    f_name = input("Enter your first name\n").upper()
    l_name = input("Enter your last name\n").upper()
    name = f_name + ' ' + l_name
    # taking name from user and storing it
    cond1 = 'y'
    while cond1 == 'y':
        l1 = list2d.lib2dlist()  # calling lib2dlist() from list2d function
        l2 = list2d.record2dlist()  # calling record2dlist() from list2d function
        ans1 = True
        while ans1:
            types = input(
                "Enter 1 to borrow book\nEnter 2 to return book\n")  # taking user choice either they want to take or return book
            if types == '1' or types == '2':
                ans1 = False
            else:
                print("invalid\nEnter again\n")
        showBooks.showBooks(l1)  # displaying book
        ans2 = True
        while ans2:
            try:  # exceptional handling
                if types == '1':
                    sno = int(
                        input("Enter serial number to borrow book\n"))  # asking user which book they want to borrow
                elif types == '2':
                    sno = int(
                        input("Enter serial number to return book\n"))  # asking user which book they want to return
                if int(sno) > 0 and int(sno) < len(l1):
                    ans2 = False
                else:
                    print("invalid\nEnter again\n")
            except:
                print("invalid \nEnter again\n")
        if types == '1':
            if int(l1[sno][3]) < 1:  # checking either the book is available or not
                print("Book not avilable\nout of stock")
            else:
                check.recordborrow(l1, l2, name, sno, types,
                                   l3)  # calling recordborrow function from borrowreturncheck
        elif types == '2':
            check.recordreturn(l1, l2, name, sno, l3, l4, types)  ##calling recordreturn function from borrowreturncheck

        while ans2 == False:
            cond1 = input(
                "Press y to take/return more books and n exit\n").lower()  # asking user either they want to take/return book
            if cond1 == "y" or cond1 == "n":
                ans2 = True
            else:
                ans2 = False

    total1 = bill.billborrow(l1, l3)  # calling billborrow function from bill and storing return value
    total2 = bill.billreturn(l2, l4)  # calling billreturn function from bill and storing return value
    bill.billrecord(total1, total2, name)
    while ans2 == True:
        cond = input("Any new customer y/n\n").lower()  # asking either any newcustomer
        if cond == "y" or cond == "n":
            ans2 = False
