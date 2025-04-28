import os
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def parse_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def create_document_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)

def embed_documents(text_chunks):
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )
    return embedding_model, text_chunks

# def store_embeddings(embedding_model, text_chunks):
#     vectorstore = Chroma.from_texts(
#         texts=text_chunks,
#         embedding=embedding_model,
#---------------------------------------
#         # persist_directory="./chroma_db"
# --------------------------------------
#         vectorstore = Chroma.from_texts(
#     texts=text_chunks,
#     embedding=embedding_model,
#     persist_directory="/tmp/chroma_db"
# )

#     )
#     vectorstore.persist()
#     return vectorstore
def store_embeddings(embedding_model, text_chunks):
    vectorstore = FAISS.from_texts(
        texts=text_chunks,
        embedding=embedding_model
    )
    return vectorstore

def retrieve_relevant_chunks(vectorstore, query, k=3):
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    return retriever.get_relevant_documents(query)

def get_context_from_chunks(relevant_chunks, splitter="\n\n---\n\n"):
    return splitter.join([f"[Chunk {i+1}]: {chunk.page_content}" for i, chunk in enumerate(relevant_chunks)])

def build_prompt(context, user_query):
    return f"""You are a helpful assistant answering questions based on provided context.

Context:
{context}

Question: {user_query}

Answer:"""

def generate_response(prompt, model="gemini-2.0-flash-thinking-exp-01-21"):
    llm = ChatGoogleGenerativeAI(
        model=model,
        temperature=0.2,
        top_p=0.95
    )
    return llm.invoke(prompt).content
