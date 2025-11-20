import streamlit as st
from core import get_llm_response
from utils import extract_text_from_pdf

# --- Configuração da Página ---
st.set_page_config(
    page_title="Blindagem Jurídica AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Design System (CSS Customizado) ---
st.markdown("""
<style>
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 3rem; 
        color: #EA1D2C; 
        font-weight: 700;
        margin-bottom: 0;
    }
    .sub-header {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 1.2rem; 
        color: #555; 
        margin-bottom: 2rem;
    }
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #EA1D2C;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3.5em;
        width: 100%;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #c91924;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### ⚙️ Configuração do Agente")
    
    st.info(
        "**Modelo Ativo:** Llama 3.3 70B (Groq)\n\n"
        "**RAG:** Ativado (Jurisprudência STF)\n\n"
        "**OCR:** Ativado (PDF Plumber)"
    )
    
    st.markdown("---")
    confidence = st.slider("🎚️ Nível de Rigor", 0.0, 1.0, 0.2, help="0 = Mais conservador, 1 = Mais criativo")
    st.markdown("---")
    st.caption("Desenvolvido por Yuri Mandina")
    st.caption("Uso destinado para suporte na analise contratural e não substitui consultoria jurídica profissional.")

# --- Header ---
st.markdown('<div class="main-header">Blindagem Jurídica AI 🛡️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Agente de Análise Contratual com RAG e OCR Integrados</div>', unsafe_allow_html=True)

# --- Layout Principal ---
col1, col2 = st.columns([1, 1], gap="large")

# Variável para armazenar o texto final
final_text_input = ""

with col1:
    st.markdown("### 📥 Entrada de Documento")
    
    # Tabs para escolher método de entrada
    tab_text, tab_file = st.tabs(["📝 Colar Texto", "📂 Upload PDF"])
    
    with tab_text:
        text_input = st.text_area(
            "Cole o contrato aqui:",
            height=400,
            placeholder="COLE O TEXTO DO CONTRATO AQUI..."
        )
        if text_input:
            final_text_input = text_input

    with tab_file:
        uploaded_file = st.file_uploader("Carregar PDF (Texto ou Digitalizado)", type="pdf")
        if uploaded_file is not None:
            with st.spinner("Extraindo texto do PDF..."):
                extracted_text = extract_text_from_pdf(uploaded_file)
                if "Erro" in extracted_text:
                    st.error(extracted_text)
                else:
                    st.success("PDF Processado com sucesso!")
                    st.text_area("Pré-visualização", extracted_text, height=200, disabled=True)
                    final_text_input = extracted_text

    st.markdown("---")
    analyze_btn = st.button("🚀 INICIAR ANÁLISE BLINDADA")

with col2:
    st.markdown("### 📊 Relatório de Inteligência")
    
    if analyze_btn:
        if not final_text_input:
            st.warning("⚠️ Por favor, forneça um texto ou faça upload de um PDF.")
        else:
            # Container visual para o resultado
            result_container = st.container()
            
            with result_container:
                with st.status("🤖 Agente trabalhando...", expanded=True) as status:
                    st.write("🔍 Consultando base vetorial (STF)...")
                    # O RAG acontece dentro do get_llm_response, mas simulamos steps visuais para UX
                    st.write("🧠 Processando lógica jurídica com Llama 3.3...")
                    
                    try:
                        result = get_llm_response(final_text_input, confidence)
                        status.update(label="✅ Análise Completa!", state="complete", expanded=False)
                        
                        st.markdown('<div class="card">', unsafe_allow_html=True)
                        st.markdown(result)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        status.update(label="❌ Erro no Processamento", state="error")
                        st.error(f"Erro técnico: {e}")

    elif not analyze_btn:
        st.info("Aguardando documento para iniciar o processamento...")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 0.8rem;'>"
    " Yuri Mandina - 2025<br>"
    "Powered by <b>LangChain, Groq, FAISS & HuggingFace</b>"
    "</div>", 
    unsafe_allow_html=True
)