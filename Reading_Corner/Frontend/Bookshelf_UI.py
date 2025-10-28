import requests
from tkinter import Tk, Frame, Label, Entry, Button, Scrollbar, Canvas, messagebox
from PIL import Image, ImageTk
from io import BytesIO
from book import Books

class BookLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" My TBR Library")
        self.root.geometry("1400x2400")
        self.root.configure(bg='#FFF0F5')

        self.library = []
        self.bookshelf = []

        self.isbn_input = Entry(self.root, font=('Comic Sans MS', 12))
        self.isbn_input.insert(0, "Enter ISBN")
        self.isbn_input.bind("<FocusIn>", self.clear_placeholder)
        self.isbn_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.search_button = Button(self.root, text="Add to Shelf", command=self.search_book, bg="#FFB6C1", font=('Comic Sans MS', 12))
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.find_button = Button(self.root, text="Find Book", command=self.find_book, bg="#FFB6C1", font=('Comic Sans MS', 12))
        self.find_button.grid(row=0, column=2, padx=10, pady=10)

        self.remove_button = Button(self.root, text="Remove Book", command=self.remove_book, bg="#FFB6C1", font=('Comic Sans MS', 12))
        self.remove_button.grid(row=0, column=3, padx=10, pady=10)

        self.scroll_canvas = Canvas(self.root, bg="#FFF0F5")
        self.scroll_frame = Frame(self.scroll_canvas)
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.grid(row=1, column=4, sticky="ns", padx=10, pady=10)
        self.scroll_canvas.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.scroll_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.scroll_frame.bind("<Configure>", lambda e: self.scroll_canvas.config(scrollregion=self.scroll_canvas.bbox("all")))

    def clear_placeholder(self, event):
        if self.isbn_input.get() == "Enter ISBN":
            self.isbn_input.delete(0, "end")

    def search_book(self):
        isbn = self.isbn_input.get().strip()
        if not isbn.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid numeric ISBN.")
            return
        try:
            if any(book.isbn == isbn for book in self.library):
                messagebox.showinfo("Duplicate", "This book is already in your library.")
                return
            book = Books(isbn)
            book.extract_data()
            self.add_book_to_shelf(book)
        except requests.RequestException:
            messagebox.showerror("Network Error", "Failed to fetch book data. Check your internet connection.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def find_book(self):
        isbn = self.isbn_input.get().strip()
        if not isbn.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid numeric ISBN.")
            return
        for book in self.library:
            if book.isbn == isbn:
                messagebox.showinfo("Book Found", f"Book: {book.title}\nAuthor: {book.author}\nPublished: {book.published_date}")
                return
        messagebox.showinfo("Not Found", "This book is not in your library.")

    def remove_book(self):
        isbn = self.isbn_input.get().strip()
        if not isbn.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid numeric ISBN.")
            return
        for book_frame in list(self.bookshelf):
            if getattr(book_frame, "book", None) and book_frame.book.isbn == isbn:
                self.bookshelf.remove(book_frame)
                book_frame.destroy()
                self.library = [book for book in self.library if book.isbn != isbn]
                messagebox.showinfo("Removed", "Book removed from your library.")
                return
        messagebox.showinfo("Not Found", "This book is not in your library.")

    def add_book_to_shelf(self, book):
        book_frame = Frame(self.scroll_frame, bg="black", bd=5, relief="sunken")
        book_frame.book = book
        book_frame.grid(row=len(self.library), column=0, padx=1, pady=10, sticky="ew")
        self.bookshelf.append(book_frame)
        self.library.append(book)

        img_label = Label(book_frame, text="No Image")
        if book.cover_image:
            try:
                response = requests.get(book.cover_image, timeout=5)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content)).resize((100, 150))
                img_tk = ImageTk.PhotoImage(img)
                img_label = Label(book_frame, image=img_tk)
                img_label.image = img_tk
            except Exception:
                pass
        img_label.grid(row=0, column=0, padx=10, pady=10)

        info = f"{book.title}\nAuthor(s): {book.author}"
        info_label = Label(book_frame, text=info, font=('Comic Sans MS', 10), justify="left", bg="#FFFACD")
        info_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

def main():
    root = Tk()
    app = BookLibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
