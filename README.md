# TheGreatLibrary

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
One needs to install MYSQL first. All the necessary instructions for the installation of all the packages are given in the file : [instructions](:/
