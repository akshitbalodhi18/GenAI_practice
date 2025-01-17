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

