import pdfplumber
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_text_splitters import CharacterTextSplitter
import os

# --- MÓDULO OCR / PDF ---
def extract_text_from_pdf(file_path):
    """Extrai texto de um arquivo PDF usando pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        return f"Erro ao ler PDF: {e}"
    return text

# --- MÓDULO RAG (Retrieval Augmented Generation) ---
def setup_rag_vectorstore():
    """
    Cria um Vector Store local (FAISS) com a base de conhecimento.
    Usa embeddings leves (all-MiniLM-L6-v2) para rodar rápido na CPU.
    """
    # 1. Carregar dados
    if not os.path.exists("knowledge_base.txt"):
        return None

    with open("knowledge_base.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # 2. Dividir texto em chunks
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.create_documents([raw_text])

    # 3. Criar Embeddings (Open Source e Leve)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Criar Vector Store
    print(f"DEBUG: Carregados {len(docs)} chunks de conhecimento na memória.")
    vector_store = FAISS.from_documents(docs, embeddings)
    
    return vector_store

def retrieve_context(vector_store, query):
    """Busca trechos relevantes na base vetorial."""
    if not vector_store:
        return ""
    
    # Busca os 2 trechos mais similares
    docs = vector_store.similarity_search(query, k=2)
    
    # Concatena o conteúdo
    context_text = "\n\n".join([d.page_content for d in docs])
    return context_text