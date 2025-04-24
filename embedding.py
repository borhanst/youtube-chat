from typing import List, Self
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
class BaseEmbedding:
    def __init__(self, documents: List[Document]=None, **kwargs):
        self.documents = documents
        self.models = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        self.vector_db = Chroma(
            embedding_function=self.models,
            persist_directory="./chroma_db",
            collection_name="youtube_chat",
        )
        self.retriever = self.vector_db.as_retriever(search_kwargs={"k": 3, "filter":{'source': kwargs.get("video_id")}})
        

    def document_split(self):
        if not self.documents:
            raise Exception("document not submit")
        return self.spliter.split_documents(self.documents)
        

    def save_embedding(self):
        chunks = self.document_split()
        data = self.vector_db.add_documents(chunks)
        return data

    def query(self, question):
        return self.retriever.invoke(question)
