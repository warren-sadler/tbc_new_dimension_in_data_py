from dotenv import load_dotenv
from pathlib import Path
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders.text import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

HERE = Path.cwd()
TEXT_PATH = Path.resolve(HERE / "data/tbc_newsletter.txt")

if __name__ == '__main__':
    load_dotenv()
    documents = TextLoader("./data/tbc_newsletter.txt", "utf-8").load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=50)
    split_documents = splitter.split_documents(documents)
    store = VectorstoreIndexCreator(embedding=OpenAIEmbeddings()).from_documents(documents=split_documents)
    res = store.query(question="Who's birthday is in May?")
    print(res)