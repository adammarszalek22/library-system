# import requests
# from PIL import Image
# import json

# '''
# This file was only used once and is not needed anymore
# '''

# url = 'https://www.googleapis.com/books/v1/volumes?q='

# #random books and authors
# some_books = ["Harry Potter", "The Lord of the Rigns", "His Dark Materials",
#               "The Lion, the Witch and the Wardrobe", "The Hobbit", "Football",
#               "Messi", "Ronaldo", "Cookbook", "Lee Child", "Peter James", 
#               "Stephen Hawking", "David Baldacci", "Believe Me",
#               "Pride and Prejudice", "1984", "Crime and Punishment", "Hamlet",
#               "Anna Karenina", "The Odyssey", "The Stranger", "Great Expectations",
#               "War and Peace"]


# def function(url, id):
#     # saving images
#     image = requests.get(url).content
#     name = f'images/img{id}.jpg'
#     file = open(name,'wb')
#     file.write(image)
#     file.close()
#     return name
#     #img = Image.open('img.jpg')
#     #img.show()

# def random_books(url=url, some_books=some_books):
#     # creating a list with books collected from the internet
#     my_books = []
#     titles = []
#     id = 1

#     for book in some_books:
#         req = requests.get(url + book)
#         items = json.loads(req.text)["items"]
#         for item in items:
#             try:
#                 vol = item["volumeInfo"]
#                 title = vol["title"]
#                 desc = vol["description"]
#                 if title not in titles:
#                     my_books.append([id, title, desc, "False", "", ""])
#                     titles.append(title)
#                     function(vol["imageLinks"]["thumbnail"], id)
#                     id += 1
#             except KeyError:
#                 pass
    
#     return my_books
    