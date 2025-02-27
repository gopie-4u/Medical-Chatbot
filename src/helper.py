from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


#Extract Data From the PDF File
def load_pdf_file(data):
    loader = DirectoryLoader(path=data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


#Split the Data into Text Chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


# Gemini Embeddings

# Using Google Gemini Embeddings instead of HuggingFace
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Initialize Google Gemini Embeddings
def get_gemini_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings

embeddings = get_gemini_embeddings()
