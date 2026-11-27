from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

Books = [
    {
            "id" : 1,
            "title" : "king of india",
            "author" : "vinay",
            "publish_date" : "21-11-2026"
    },
    {
            "id" : 2,
            "title" : "makemytriop",
            "author" : "vijay",
            "publish_date" : "21-11-2025"
    },
    {
            "id" : 3,
            "title" : "Bangalore",
            "author" : "Gundala",
            "publish_date" : "21-11-2024"
    },
        {
            "id" : 4,
            "title" : "Updated_data",
            "author" : "Ramprakash",
            "publish_date" : "21-11-2024"
    },
        {
            "id" : 5,
            "title" : "delete_data",
            "author" : "Ramprakash",
            "publish_date" : "21-11-2024"
    },

]

app = FastAPI()

@app.get("/books")
def add_book():
    return Books

@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in Books:
         if book['id'] == book_id:
             return book
    return HTTPException(status_code = status.HTTP_404_NOT_FOUND , details="Book not found")

class Book(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str

class BookUpdate(BaseModel):
    title:str
    author:str
    publish_date:str

@app.put("/books/{book_id}")
def update_book(book_id:int , book_update:BookUpdate):
    for book in Books:
        if book['id']==book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publish_date'] = book_update.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.post("/books")
def create_book(book:Book):
    new_book = book.model_dump()
    Books.append(new_book)

@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for book in Books:
        if book['id'] == book_id:
            Books.remove(book)
            return {"Message" : "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

