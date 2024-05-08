inventory = []

book1 = {
    "title": "The Red and The Black",
    "author": "Stendal",
    "price": 6000
}

book2 = {
    "title": "The Picture of Dorian Gray",
    "author": "Oscar Wilde",
    "price": 4500
}

inventory.append(book1)
inventory.append(book2)

def add_book(title, author, price):
   
    new_book = {
        "title": title,
        "author": author,
        "price": price
    }
    inventory.append(new_book)

add_book("The Count of Monte Cristo", " Alexandre Dumas", 8700)

def search_books(title):
    
    matching_books = []
    for book in inventory:
        if title.lower() in book["title"].lower():
            matching_books.append(book)

    if matching_books:
        print("Matching Books:")
        for book in matching_books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Price:", book["price"])
            print()
    else:
        print("No matching books found.")
        print()

search_books(input("Enter a title to search: "))

def list_books():
    
    print("Inventory List:")
    for book in inventory:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Price:", book["price"])
        print()

list_books()
