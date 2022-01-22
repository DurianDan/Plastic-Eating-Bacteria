import PyPDF2
from os import listdir


pdfs = []
for i in listdir():
    if "pdf" in i:
        pdfs.append(i)
words_dict = {}
for i in pdfs:
    # creating a pdf file object
    pdfFileObj = open(i, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    #number of pages in pdf file
    for j in range(pdfReader.numPages):
        # creating a page object
        pageObj = pdfReader.getPage(j)
        
        # extracting text from page
        page_words = map(str.lower,pageObj.extractText().split())
        for k in page_words:
            if k in words_dict:
                words_dict[k] = words_dict[k] + 1
            else:
                words_dict[k] = 1
        # closing the pdf file object
    pdfFileObj.close()

words_dict = {k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1],reverse = True)}

with open("words_mentioned_in_pdfs.txt","w") as tx:
    for i in words_dict:
        tx.write(str(i)+" "+str(words_dict[i])+"\n")