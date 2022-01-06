import PyPDF2

def new_word(word):
    new_word = ""
    for i in range(0,len(word)):
        if word[i].isalpha():
            new_word += word[i]

    return new_word

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        word = new_word(word)   
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1

    return counts



pdfFileObj = open('Emil und die Detektive.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)

print(pdfReader.numPages)
# Page number entered returns 1 less with respect to actual book's page number

#start = input("Enter the page number of the first page")
#end = input("Enter the page number of the last page")

start = 8
end = 172
book = ""

for i in range(8,173):
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText()
    book = book + page

s = word_count(book)
# Sorting Dictionary
final = sorted(s.items(), key=lambda x: x[1], reverse=True)
for i in range(0,len(final)):
    print(final[i])
pdfFileObj.close()
