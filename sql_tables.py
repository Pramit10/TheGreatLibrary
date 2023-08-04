import mysql.connector as sql

print()

while True:
    try:
        password = input("Enter your MySQL password: ")
        db = sql.connect(user='root',passwd=password, host='localhost')
        csr = db.cursor()

        #create database & use it
        query = "create database library;"
        csr.execute(query)
        db.commit()

        #use database
        query1 = "use library;"
        csr.execute(query1)
        db.commit()

        #add books table
        query2 = "CREATE TABLE books\
                (\
                BookID varchar(10) NOT NULL,\
                BName varchar(100) NOT NULL,\
                Author varchar(100) NOT NULL,\
                Publisher varchar(100) NOT NULL,\
                Edition varchar(50) NOT NULL,\
                Price int NOT NULL,\
                Quantity int NOT NULL,\
                PRIMARY KEY (`BookID`)\
                );"
        csr.execute(query2)
        db.commit()

        #inventory table
        query3 = "CREATE TABLE inventory\
                (\
                AccNum int NOT NULL AUTO_INCREMENT,\
                BookID` varchar(10) NOT NULL,\
                PRIMARY KEY (`AccNum`),\
                KEY BookID (`BookID`),\
                FOREIGN KEY (`BookID`)\
                REFERENCES books (`BookID`)\
                ON DELETE CASCADE\
                );"
        csr.execute(query3)
        db.commit()

        #add member
        query4 = "CREATE TABLE member\
                (\
                MemID int NOT NULL AUTO_INCREMENT,\
                FName varchar(100) NOT NULL,\
                LName varchar(100) NOT NULL,\
                Phone char(10) NOT NULL UNIQUE,\
                PRIMARY KEY (`MemID`),\
                );"
        csr.execute(query4)
        db.commit()

        #issued table
        query5 = "CREATE TABLE issued\
                (\
                AccNum int NOT NULL,\
                BookID varchar(10) DEFAULT NULL,\
                IssueDate date NOT NULL,\
                ReturnDate date NOT NULL,\
                MemID int NOT NULL,\
                Status varchar(10) NOT NULL,\
                PRIMARY KEY AccNum (AccNum),\
                FOREIGN KEY (BookID)\
                REFERENCES books (BookID)\
                ON DELETE CASCADE,\
                FOREIGN KEY (AccNum)\
                REFERENCES inventory (AccNum)\
                ON DELETE CASCADE,\
                FOREIGN KEY (MemID)\
                REFERENCES member (MemID)\
                ON DELETE CASCADE\
                );"
        csr.execute(query5)
        db.commit()

        #availability table
        query6 = "CREATE TABLE availability\
                (\
                BookID varchar(10) NOT NULL,\
                Available int NOT NULL,\
                PRIMARY KEY (BookID),\
                FOREIGN KEY (BookID)\
                REFERENCES books (BookID)\
                ON DELETE CASCADE\
                );"
        csr.execute(query6)
        db.commit()
        break

    except:
        print("\nPlease check your password and try again\n")
        




