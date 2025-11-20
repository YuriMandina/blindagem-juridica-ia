import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from utils import setup_rag_vectorstore, retrieve_context

# Carrega variáveis
load_dotenv()

# Inicializa o Vector Store apenas uma vez (Singleton pattern simplificado)
print("Inicializando base de conhecimento (RAG)...")
VECTOR_STORE = setup_rag_vectorstore()

def get_llm_response(contract_text: str, temperature: float = 0.2) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("API Key não encontrada.")

    # 1. Recuperação de Contexto (RAG)
    # O sistema busca na jurisprudência tópicos relacionados ao contrato
    contexto_juridico = retrieve_context(VECTOR_STORE, contract_text[:1000]) # Usa o início do contrato para busca

    # 2. Setup do Modelo
    llm = ChatGroq(
        temperature=temperature,
        model_name="llama-3.3-70b-versatile",
        api_key=api_key
    )

    # 3. Prompt Aumentado (RAG)
    system_prompt = f"""
    Você é um Consultor Jurídico Sênior e Engenheiro de Dados (foco em GenAI).
    
    BASE DE CONHECIMENTO (JURISPRUDÊNCIA STF/LEGISLAÇÃO):
    {contexto_juridico}
    
    Use o contexto acima para enriquecer sua análise se for relevante.
    Se o contrato violar os itens da base de conhecimento, cite explicitamente.
    
    Sua tarefa é analisar contratos e identificar riscos com precisão.
    Retorne APENAS no formato Markdown estruturado:
    
    ## 1. Resumo Executivo
    ## 2. Pontos de Atenção Crítica (Risco Alto)
    ## 3. Sugestões de Redação (Blindagem)
    ## 4. Veredito
    """

    human_prompt = "Analise este contrato:\n\n{text}"

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", human_prompt),
    ])

    chain = prompt_template | llm | StrOutputParser()

    try:
        response = chain.invoke({"text": contract_text})
        return response
    except Exception as e:
        return f"Erro: {str(e)}"