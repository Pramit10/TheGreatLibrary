def AddBook():
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            last_id = "SELECT BookID from Books ORDER BY BookID DESC LIMIT 1"
            csr.execute(last_id)
            data = csr.fetchall()
            for i in data:
                print("Last BookID is",i[0])

            id = input("Enter BookID : ")
            name = input("Enter name of the book : ")
            author = input("Enter author of the book : ")
            publisher = input("Enter the publisher of the book : ")
            edition = input("Enter the edition of the book : ")
            price = int(input("Enter the price of the book : "))
            qty = int(input("Enter the quantity of the book : "))

            addbook = "INSERT INTO Books VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(id,name,author,\
                                                                                    publisher,edition,\
                                                                                    price,qty)
            csr.execute(addbook)
            Library.commit()
            print("\nThe data has saved successfully !")

            for row in range(1,qty+1):
                update_inventory = "INSERT INTO Inventory(BookID) VALUES ('{}')".format(id)
                csr.execute(update_inventory)
                Library.commit()

            update_availability = "INSERT INTO Availability VALUES('{}','{}')".format(id,qty)
            csr.execute(update_availability)
            Library.commit()
            break

        except:
            print("\nPlease check the value and try again\n")
            continue
    Library.close()


def DeleteBook():
    import tabulate as table
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            id = input("Enter the BookID of the book that you want to delete from the library: ")
            check1 = "SELECT Status FROM Issued WHERE BookID = '{}'".format(id)
            csr.execute(check1)
            data_of_status = csr.fetchall()
            result_status = []
            for i in data_of_status:
                result_status.append(i[0])
            if 'Issued' in result_status:
                print("You cannot delete this book as one of its copies is currently issued by one of our member.\nPlease enter new BookID.\n")
                continue

            showbook = "SELECT * FROM Books where BookID = '{}'".format(id)
            csr.execute(showbook)
            BookData = csr.fetchall()
            display = table.tabulate(BookData, headers = ['BookID','BName','Author','Publisher','Edition','Price','Quantity'],numalign = 'left')
            print("\nThis is the book data that you want to delete...")
            print(display)
            ans = input("Proceed to delete? (Press Y for yes or N for no) : ")
            if ans in 'yY':
                delBook = "DELETE FROM Books WHERE BookID = '{}'".format(id)
                csr.execute(delBook)
                Library.commit()
                print("\nThe book has been deleted successfully..")
                break
            elif ans in 'nN':
                print("\nTry again then..")
                continue
        except:
            print("\nPlease enter the correct details and try again.\n")
            continue
                
    Library.close()
            

def AddMember():
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:

            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            phone = input('Enter your phone number: ')
            addmember = "INSERT INTO Member(FName,LName,Phone) VALUES('{}','{}','{}')".format(fname,lname,phone)
            csr.execute(addmember)
            Library.commit()
            getID = "SELECT MemID FROM Member ORDER BY MemID DESC LIMIT 1"
            csr.execute(getID)
            memberID = csr.fetchall()
            for i in memberID:
                print("\nCongratulations! You're now a member.")
                print("Your MemberID is ",i[0])
                print("Happy reading!!")
            break
        except:
            print("\nPlease enter the details correctly and try again\n")
            continue

    Library.close()


def deleteMember():
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            
            ID = int(input("Please enter your MemberID : "))
            
            check1 = "SELECT MemID FROM Member WHERE MemID = {}".format(ID)
            csr.execute(check1)  
            list_of_memId = []
            for row in csr:
                list_of_memId.append(row[0])
            if ID not in list_of_memId:
                print("Please enter your correct MemberID as we cannot locate any member with ID as '{}' in our database. Try Again!\n".format(ID))
                continue
            
            check2 = "SELECT Status FROM Issued WHERE MemID = {}".format(ID)
            csr.execute(check2)
            list_of_result = []
            for i in csr:
                list_of_result.append(i[0])
            if "Issued" in list_of_result:
                print("Please return your issued book first. Only then you can dismiss your membership.\nThank you.\n")
                continue
            else:
                query = "DELETE FROM Member WHERE MemID = {}".format(ID)
                csr.execute(query)
                Library.commit()
                print("\nYour membership has been dicontinued successfully.")
                break
        except:
            print("\nPlease enter the details correctly and try again\n")
            continue

    Library.close()


def IssueBook():
    from datetime import date
    from datetime import timedelta
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            AccNum = int(input("Please enter the Accession Number of the book : "))
            BookID = input("Enter the BookID of the book : ")
            MemID = int(input("Please enter your MemberID : "))
            Status = 'Issued'
            IssueDate = str(date.today())
            ReturnDate = str(date.today() + timedelta(days = 7))
            check = "SELECT Available FROM Availability WHERE BookID = '{}'".format(BookID)
            csr.execute(check)
            check_data = csr.fetchall()
            if check_data[0][0] == 0:
                print("This book is currently not available in our library.\nPlease issue a another book.")
                break
            else:
                query = "INSERT INTO Issued VALUES({},'{}','{}','{}','{}','{}')".format(AccNum,BookID,IssueDate,ReturnDate,\
                                                                                    MemID,Status)
                csr.execute(query)
                Library.commit()

                query2 = "UPDATE Availability SET Available = Available - 1 WHERE BookID = '{}'".format(BookID)
                csr.execute(query2)
                Library.commit()
            
                print("Your book has been issued succesfully..")
                print("Please return the book by {}/{}/{}".format(ReturnDate[8:],ReturnDate[5:7],ReturnDate[:4]))
                print("HAPPY READING!!")
                break
        except:
            print("\nPlease enter the details correctly and try again.\n")
            continue
        
    Library.close()


def ReIssueBook():
    from datetime import date
    from datetime import timedelta
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            AccNum = int(input("Please enter the Accession Number of the book : "))
            IssueDate = str(date.today())
            ReturnDate = str(date.today() + timedelta(days = 7))
            check = "SELECT AccNum FROM Issued"
            csr.execute(check)
            L = []
            for i in csr:
                L.append(i[0])

            if AccNum not in L:
                print("Please enter the correct AccNum of your book. A book must be issued first before it can be re-issued.\nTry again.\n")
                var = input("Do you wish to Try Again or exit? (press Y to try again or N to exit: ")
                if var in ('N',"n"):
                    break
                elif var in ('Y','y'):
                    continue
            
            query = "UPDATE Issued SET IssueDate = '{}',ReturnDate = '{}' WHERE AccNum = {}".format(IssueDate,ReturnDate,AccNum)
            csr.execute(query)
            Library.commit()
            
            print("Your book has been re-issued succesfully..")
            print("Please return the book by {}/{}/{}".format(ReturnDate[:4],ReturnDate[5:7],ReturnDate[8:]))
            print("HAPPY READING ONCE AGAIN!!")
            break

        except:
            print("\nPlease enter the details correctly and try again.\n")
            continue
    Library.close()


def BookReturn():
    from datetime import date
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            AccNum = int(input("Please enter the Accession Number of the book : "))
            BookID = input("Enter the BookID of the book : ")
            ReturnDate = str(date.today())
            Status = 'Returned'
            
            query1 = "UPDATE Issued SET Status = '{}',ReturnDate = '{}' WHERE AccNum = {}".format(Status,ReturnDate,AccNum)
            csr.execute(query1)
            Library.commit()
            
            query2 = "UPDATE Availability SET Available = Available + 1 WHERE BookID = '{}'".format(BookID)
            csr.execute(query2)
            Library.commit()
            
            print("Your book has been returned succesfully..")
            print("THANK YOU AND DO VISIT AGAIN")
            break

        except:
            print("\nPlease enter the details correctly and try again.\n")
            continue
    Library.close()


def UpdateInventory():
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            BookID = input("Enter the BookID: ")
            copies = int(input("Enter the number of copies of the book you want to add: "))

            for loop in range(copies):
                query1 = "INSERT INTO Inventory(BookID) VALUES('{}')".format(BookID)
                csr.execute(query1)
                Library.commit()

            query2 = "UPDATE Availability SET Available = Available + {} WHERE BookID = '{}'".format(copies,BookID)
            csr.execute(query2)
            Library.commit()

            query3 = "UPDATE Books SET Quantity = Quantity + {} WHERE BookID = '{}'".format(copies,BookID)
            csr.execute(query3)
            Library.commit()

            print("The data has been updated successfully..")
            break

        except:
            print("\nPlease check the values and try again. Make sure the book already exists in the library.\n")
            continue
    Library.close()

def checkAvailability():
    import tabulate as table
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    while True:
        try:
            BookID = input("Enter the BookID: ")
            query = "SELECT * FROM Availability WHERE BookID = '{}'".format(BookID)
            csr.execute(query)
            data = csr.fetchall()
            display = table.tabulate(data, headers = ['BookID','Available'],numalign='left')
            print(display)
            break
        except:
            print("\nPlease check the BookID you have entered and try again..\n")
            continue
    Library.close()

def getReport():
    import tabulate as table
    import mysql.connector as sql
    Library = sql.connect(user = 'root',passwd = password,\
                          host = 'localhost', database = 'library')
    csr = Library.cursor()
    
    query1 = "SELECT Issued.BookID, BName AS BookName,MemID AS MemberID FROM Issued,Books WHERE Issued.BookID = Books.BookID AND Status = 'Issued'"
    csr.execute(query1)
    result1 = csr.fetchall()
    display = table.tabulate(result1, headers = ['BookID','BookName','MemberID'],numalign = 'left')
    print("Books that are yet to be returned are..\n")
    print(display)
    Library.close()
            



def main():
    print("Welcome to The Great Library")
    print()
    while True:
        global password
        password = input("Please enter your MySQL password to continue : ")
        import mysql.connector as sql
        
        try:
            temp_db = sql.connect(user = 'root',passwd = password,\
                            host = 'localhost', database = 'library')
            if temp_db.is_connected() == True:
                temp_db.close()
                break
            else:
                print("Some error while connecting to database. Try Again.\n")
                continue
        except:
            print("Please enter correct password and try again.\n")
            
            

    options = '''Please choose the respective options to perform the following actions:
    A. Add a Book
    B. Delete a Book
    C. Add a new copy of a book to the Inventory
    D. Add a Member
    E. Delete a Member
    F. Issue a Book
    G. Re-Issue a Book
    H. Return a Book
    I. Check the availability of a Book
    J. Get a detailed report about all the books that have been issued, but not returned yet
    K. To review the options'''
    print(options)
    while True:
        Input = input("Enter your option here: ")
        if Input in 'Aa':
            AddBook()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue
        
        elif Input in 'Bb':
            DeleteBook()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue
        
        elif Input in 'Cc':
            UpdateInventory()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue
        
        elif Input in 'Dd':
            AddMember()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue

        elif Input in 'Ee':
            deleteMember()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue
        
        elif Input in 'Ff':
            IssueBook()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue

        elif Input in 'Gg':
            ReIssueBook()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue

        elif Input in 'Hh':
            BookReturn()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue

        elif Input in 'Ii':
            checkAvailability()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue
        
        elif Input in 'Jj':
            getReport()
            user = input('\nDo you want to exit or perform another action? (press 1 to exit or 2 to continue): ')
            if user == '1':
                break
            elif user == '2':
                print()
                continue

        elif Input in 'Kk':
            print(options)

    print('\nThank you for visiting The Great Library. Have a great day!')
    print()
    input("Press enter key to close the window.")


main()


            




    

        
    
            
    
        
    






        
    
