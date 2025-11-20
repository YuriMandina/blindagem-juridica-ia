import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def get_llm_response(contract_text: str, temperature: float = 0.2) -> str:
    """
    Processa o texto do contrato utilizando o modelo Llama 3 via Groq.
    
    Args:
        contract_text (str): O texto completo do contrato.
        temperature (float): Nível de criatividade (0.0 a 1.0). Baixo para jurídico.
        
    Returns:
        str: Análise estruturada do contrato.
    """
    
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("A chave de API da GROQ não foi encontrada. Verifique o arquivo .env")

    # Inicializa o modelo LLM
    llm = ChatGroq(
        temperature=temperature,
        model_name="llama-3.3-70b-versatile", # <--- ALTERE AQUI
        api_key=api_key
    )

    # Engenharia de Prompt: Persona + Tarefa + Formato de Saída
    system_prompt = """
    Você é um Consultor Jurídico Sênior e Engenheiro de Dados especialista em legislação brasileira (CLT, Código Civil e LGPD).
    
    Sua tarefa é analisar contratos brutos e identificar riscos com precisão cirúrgica.
    
    Retorne a análise APENAS no seguinte formato Markdown estruturado:
    
    ## 1. Resumo Executivo
    (Breve resumo do objeto do contrato em 2 linhas)
    
    ## 2. Pontos de Atenção Crítica (Risco Alto)
    * [Cláusula X]: Explicação do risco jurídico ou financeiro.
    
    ## 3. Sugestões de Redação (Blindagem)
    * **Original:** (Trecho problemático)
    * **Sugerido:** (Nova redação mais segura)
    
    ## 4. Veredito
    (Aprovado com ressalvas / Requer revisão profunda / Aprovado)
    """

    human_prompt = "Analise o seguinte texto contratual:\n\n{text}"

    # Construção da Chain (Cadeia de processamento)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", human_prompt),
    ])

    # Pipe: Prompt -> Modelo -> Parser de String
    chain = prompt_template | llm | StrOutputParser()

    try:
        response = chain.invoke({"text": contract_text})
        return response
    except Exception as e:
        return f"Erro ao processar o contrato: {str(e)}"