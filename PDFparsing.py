# 1. Install and import library

# pip install PyPDF2
# import PyPDF2

# 2. Open a PDF file in read-binary mode
# import PyPDF2

# file = open("sample.pdf", "rb")
# reader = PyPDF2.PdfReader(file)

# 3. Display total number of pages
# print(len(reader.pages))

# 4. Extract text from first page
# print(reader.pages[0].extract_text())

# 5. Extract text from last page
# last_page = len(reader.pages) - 1
# print(reader.pages[last_page].extract_text())

# 6. Extract text from all pages
# for page in reader.pages:
#     print(page.extract_text())

# 7. Save extracted text into .txt file
# text = ""
# for page in reader.pages:
#     text += page.extract_text()

# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# 8. Count total characters
# text = ""
# for page in reader.pages:
#     text += page.extract_text()

# print(len(text))

# 9. Count total words
# words = text.split()
# print(len(words))

# 10. Count total lines
# lines = text.split("\n")
# print(len(lines))

# 11. Check whether specific word exists
# word = "Python"
# print(word in text)

# 12. Count how many times a word appears
# print(text.count("Python"))



