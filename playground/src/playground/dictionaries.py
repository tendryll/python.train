book = {
    "title": "Python Illustrated",
    "author": ["Maaike van Putten", "Imke van Putten"],
    "publish_year": 2026,
    "publisher": "Packt Publishing Ltd.",
    "publisher_address": {
        "address_1": "11 St. Paul's Square",
        "city": "Birmingham",
        "country": "UK"
    }
}

# print(book["title"]) # if key not found, KeyError is thrown
# print(book.get("author")) # if key not found, None is returned
# print(book.get("description", "no description found"))
#
# print(book.get("author")[0])
#
# print(book.get("publisher_address").get("address_1"))
# print(book.get("publisher_address").get("city")[1])

book["description"] = ("This is not your average Python programming book, because the world doesn’t need another one of those. "
                       "Instead, it’s an illustrated, fun, and hands-on guide that treats learning Python like the adventure "
                       "it should be. It’s designed especially for beginners who want to understand how code works without "
                       "getting overwhelmed. You’ll be guided by a cheeky, know-it-all cat who’s surprisingly good at teaching "
                       "Python from scratch. Don’t worry about going through it alone; a slightly moody dachshund dog is your "
                       "study buddy, learning right alongside you. Each chapter introduces a core programming concept, "
                       "explains it with a playful twist, and reinforces it through human-friendly examples, analogies, and "
                       "exercises. Whether you’re a software professional or someone who’s never written a single line of code, "
                       "this book will help you build real Python coding skills… and even enjoy the process (shocking, right?). "
                       "Forget dry tutorials and walls of text. Python Illustrated speaks to visual learners, creative thinkers, ...")

# print(book.keys())
# print(book.values())
# print(book.items())

if "isbn-10" not in book:
    print("There is no ISBN-10 value.")

# print(book)

# book["description"] = "no description"
# print(book)