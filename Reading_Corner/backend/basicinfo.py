
'''
utilizing google book api to get isbn: author: title: date: and pissibly a picture
to access APIs through done through HTTPS: request, process, and response.

The requests package in Python is a popular, third-party library designed to simplify making HTTP requests
'''
import requests



class Books:
    def __init__(self, isbn):
        self.author = ''
        self.title = ''
        self.isbn = ''
        self.full_name = ''
        self.url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
        self.respnse = requests.get(self.url)

    def extract_data(self):
        data = self.respnse.json()
        volume_info = data["items"][0]["volumeInfo"]
        self.title = volume_info.get("title", "No Title")
        authors = volume_info.get("authors", ["Unknown Author"])
        self.author = ", ".join(authors)
        self.published_date = volume_info.get("publishedDate", "Unknown Date")


    def __str__(self):
        return (f'(Title: {self.title})\n'
                f'Author(s): {self.author}\n'
                f'Published Date: {self.published_date}')


def main():

    isbn_input = int(input("Enter ISBN: "))
    user = Books(isbn_input)
    user.extract_data()
    return user


if __name__ == "__main__":
    print(main())
