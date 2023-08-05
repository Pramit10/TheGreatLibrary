# TheGreatLibrary

### Video Demo : <https://youtu.be/ononGgyteHY>

## Introduction
This is a very user friendly Library Managment System that can help a librarian to store data very efficiently without any hassle. All the possble actions can be performed using this.

One can:
* Add a book
* Delete a book
* Add a new Member
* Delete a member
* Issue a book
* Return a book
* Check the availability of a book
* Get a detailed report of the books that are yet to be returned

I have tried to make this project as much real-life like as possible. With the help of this, a librarian can do all the works efficiently and due to its ease of use, anyone, without any prior knowledge of coding can work with this program.

I have done this project it keeping in mind that this will be used in a real library and not in a ficticious digital one. I will try to explain all the questions that may arise while going through this in the following sections.

## The tables that are required
1. The **Books** table stores data regarding books like bookID, book name, author, publisher, edition, price and quantity.
   
3. The **Inventory** table stores data like Accession Number(AccNum) and BookID. Here AccnNum is unique for every book in the library and BookID indicates the ID of a given book. The AccNum comes in handy when there a multiple copies of a book and hence each book is uniquely identified using its AccNum.
   
5. The **Member** table stores the member data like MemberID, Name and Phone.
   
7. The **Issued** table stores the details of issuing a book, including the AccnNum of the book issued, Issue Date, Return Date, MemberID, Status (Issued or Returned) of the member who was issued the book.
   
9. The **Availability** table stores the data about where a book is available to issue or not. It contains information like the BookID and a field called Available, that stores the number of copies available.

## How to use it ?
1. One needs to install MYSQL first. All the necessary instructions for the installation of all the packages are given in the file : [Instructions To Install MySQL](https://github.com/Pramit10/TheGreatLibrary/blob/main/INSTRUCTIONS%20TO%20INSTALL%20MYSQL.pdf)

2. After installing MYSQL and the required packages, you need to create the tables that are required by running the [sql_tables.py](./sql_tables.py) file.

3. Run the [main.py](./main.py) file to start the program.
   
5. Now, you are ready to use ***THE GREAT LIBRARY***

## How does it work and what are its features ?
In this whole project, I have been making very minute changes which I think would make the job of librarian easier. I wanted to program this code so that everyone can use it without any hesitation.

In all of the functions, I have incorporated a ‘try-except’ block system, i.e whenever there is any sort mistake during inputting the values from the user (datatype error), the program will display the “Try Again” statement and allow the user to enter again from the beginning instead of showing an error and terminating the code. If the error message would have shown then it might become uneasy for the person who is using the program at that time, he/she might not know what to do next. So, this program will guide the user in every step.

* Whenever the **AddBook** module is called, the first thing it shows is the last BookID of the book stored in the database. This lets the librarian know what he must enter as the next BookID. If a new person is using it, it will be helpful for him/her also. This also updates the Inventory as well as the *Availability* table. The Accession number(AccNum) is auto generated.

* Talking about the **DeleteBook** module, it will stop you from deleting a book, if the book has been issued and not returned yet. I suppose this makes sense! Because you cannot remove a book from a library if it is being issued by one of the member. So that feature is intact! While using this, the user will get a confirmation about the choice of book they selected to delete. If they confirm the deletion only then will the book be deleted, or else the user gets to choose a different book.

* In the **UpdateInventory** module, the user cannot just add any BookID in the inventory. The module checks whether the entered BookID is present in the database or not from the Books table. If it is there, then the inventory is updated as well as the quantity value in the *Books* table of that respective book.

* The **IssueBook** module is totally life-like! It receives the BookID and Accession Number(AccNum) from the user. Here the AccNum is not auto generated because when a member comes to the counter to issue a book, the AccNum is already stamped on the book. The user just has to say the AccNum and the BookID from the book in hand to the librarian and the job is done! No need to enter any date, the program will automatically tell the user the date of returning the book. How pleasant is that!

* One can alway reissue a book in a library. And one can do that in The Great Library too! The **ReIssue** module reissues a previously issued book and returns the new date of returning the date and updates it in the *Issued* table.

* When a book is returned, the **BookReturn** module updates the ‘Status’ of that issue to ‘Returned’ in the *Issued* table and updates the *Availability* table by incrementing 1 to the ‘Available’ field of that BookID as it is now available to issue.

* The member subscription feature is also quite life-like. The **AddMember** module receives the details of the user and returns their unique MemberID. This memberID is used when they try to issue or return a book. The MemberID uniquely identifies a member in our library.

* Similarly, when the **DeleteMember** module is running, it will allow a member to discontinue their membership only if they have returned all the books they issued. The module checks this from the MemberID that it receives from the user and gets the information from the *Issued* table, whether that member has any pending books to return

* Some extra features like generating a report of all the books that are issued but yet to be returned, and checking the availability of a book with the entered BookID are also available.

### NOTE: How to run the the programes ?
Just double-click the program you want to run! It's that simple :)

#### If there are any errors or any sort of issue you experience, please feel free to leave a comment or get in touch with me, so that I can rectify it and update the project. 

#### Thank you. 
#### This was **The Great Library**
#### Have a great day!

