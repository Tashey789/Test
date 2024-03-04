# initialize empty lists, set, and dictionary
books_list =[]
authors_set = set()
books_dic = {}

# Add books
books_list.append("python programming")
authors_set . add("John Smith")
books_dic["python programming"] = "John Smith"

books_list.append("data structures and algorithim")
authors_set.add("Jane Doe")
books_dic["data structures and algorithim"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dic["Machine Learning Basics"] = "Alice johnson"
 
# Search for a book
Search_title = input("Enter the title of the book to search: ")
if Search_title in books_list:
    print(f"Book found! Author: {books_dic[Search_title]}")
else:
    print("Book not found!")

 # dsplay all books 
print("list of books:")
for book in books_list:
    print(book)
     
 # Remove a book    
remove_title  = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dic[remove_title]   
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dic[remove_title]
    print("book removed successfully!")
    print("books available: ", books_list)

else:
    print("book not found")





