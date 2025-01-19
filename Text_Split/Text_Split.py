#Importing / Ingesting pdf into python
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("attention.pdf")
document = loader.load()
#print(document)




# Recursive Character Text Splitting. In this method the context is maintained as some ending characters of the first document are present in the starting characters of the second document




#Recursive text splitting in a pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
final_documents = text_splitter.split_documents(document)
print(type(final_documents))
#print(final_documents)

# Final documents is a list of documents. The original document was split into multiple document of 100 characters with 20 characters overlapping
print(final_documents[0])
print(final_documents[1])
print(type(final_documents[0]))


#Recursive text splitting in a string or text
#importing text and converting it into a string so that we can create a langchain document
speech = ""
with open ("speech.txt") as f:
    speech = f.read()

#print(speech) This will print the text or string

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
#Text splitter only accepts list as a input. Therefore we had to convert that string into a list that is why we used [speech] instead of speech
final_docs = text_splitter.create_documents([speech])
print(final_docs)




##Character text splitter
# This splits the text into different documents on the basis of the character that we provide. The default seperator is /n/n

#first importing a text file to be split
newspeech = ""
with open ("speech.txt") as f:
    newspeech = f.read()

#Import character text splitter function
from langchain_text_splitters import CharacterTextSplitter
text_splitter = CharacterTextSplitter(separator="/n", chunk_size=100, chunk_overlap=20)
final=text_splitter.create_documents([newspeech])
print(final)








##HTMLHeaderTextSplitter
#This text splitter splits the text based on the html selector that we have queried. It also adds some relevant information.
print("/n/n Now we are going to see HTMLHeaderTextSplitter")
from langchain_text_splitters import HTMLHeaderTextSplitter

html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""

headers_to_split_on=[
    ("h1","Header 1"),
    ("h2","Header 2"),
    ("h3","Header 3")
]

html_splitter=HTMLHeaderTextSplitter(headers_to_split_on)
html_header_splits=html_splitter.split_text(html_string)
print(html_header_splits)