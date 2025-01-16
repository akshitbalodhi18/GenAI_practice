##### In this we will look into how we import data for using it in langchain. Basically how ingestion works in langchain. So lagnchain provides us document_loaders using which we can import different types of documents as data source.



## TEXT LOADER USED TO READ .TXT FILES
from langchain_community.document_loaders import TextLoader
loader = TextLoader("speech.txt")
print("Below is a loader\n")
print(loader)
document = loader.load()
print("\n this is a document. this is how every document will look like in gen ai using langchain\n")
print(document)


# PYPDF TO READ PDF FILES
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("attention.pdf")
document = loader.load()
print("\nBelow is a pdf document.\n")
#print(document)
print("\nType of pdf file is : ")
print(type(document))
print("\nType of one document inside a pdf file is : ")
print(type(document[0]))


# WEB BASED LOADER
from langchain_community.document_loaders import WebBaseLoader
import bs4
print("\n Below is one single section of a website that is strained using bs4\n")
loader = WebBaseLoader(web_paths=("https://www.codechef.com/",),
                       bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                           class_=("wideSection")
                       ))
                    )
document = loader.load()
print(document)


#WIKIPEDIA BASED LOADER
from langchain_community.document_loaders import WikipediaLoader
loader = WikipediaLoader(query="FC Barcelona",load_max_docs=2)
document = loader.load()
print("\n This is a wikipedia document that was returned by searching a query\n")
print("The first document is\n")
print(document[0])
print("\nThe second document is\n")
print(document[1])