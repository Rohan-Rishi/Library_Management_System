print("Welcome to our Library Management System!")
print("Here we offer 12 book categories ranging from story books to novels, books on programming language, science fiction and so on. Enjoy your time here.")
print()

print("Categories we offer: ")
with open("bookCategory.txt", "r") as file:
    data = file.read()
    print(data)

serialNumList = []

with open("libDb.txt", "r") as file:
        books = file.readlines()    #list

def issueBooks():
    #ISSUE BOOKS
    catChoice = input("Enter book category under which you want to issue books: ")
    print()
    print("Searching for books under this category... ")
    with open("libDb.txt", "r") as file:
        books = file.readlines()
        bookFound = False
        for book in books:
            data = book.strip().split(",")
            if catChoice.upper() == str(data[3]).upper():
                print(data[0]," ",data[1]," - ", data[2])
                bookFound = True
        if bookFound == False:
            print("No books available under mentioned category.")

    bookQnt = int(input("Enter the number of books you want to issue: "))
    print("Enter serial no(s). of the book(s) you want to issue: ")
    count = 1
    while count<=bookQnt:
        serialNum = input("Enter SN: ")
        serialNumList.append(serialNum)
        count+=1
    found = False


def displayIssuedBooks():
    for serialNum in serialNumList:
        if int(serialNum) <= 50:
            for book in books:
                data = book.strip().split(",") #book string as a list
                if serialNum == data[0]:
                    print(data[1]," - ", data[2])
                    found = True
        else:
            found = False
            print("Book with SN ",serialNum," is not in the collection.")

issueBooks() 
displayIssuedBooks()