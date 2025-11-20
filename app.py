import streamlit as st
from core import get_llm_response

# Configuração da Página
st.set_page_config(
    page_title="Blindagem Jurídica AI",
    page_icon="⚖️",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #EA1D2C;}
    .sub-header {font-size: 1.2rem; color: #666;}
    .stButton>button {
        background-color: #EA1D2C;
        color: white;
        border-radius: 5px;
        height: 3em;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2230/2230606.png", width=80)
    st.title("Controles")
    st.markdown("---")
    st.info(
        "Este agente utiliza **Llama 3.3 70B Versatile** via Groq para "
        "analisar riscos contratuais com base na legislação brasileira."
    )
    confidence_threshold = st.slider("Nível de Rigor (Temperatura)", 0.0, 1.0, 0.1)
    st.markdown("---")
    st.caption("Desenvolvido por Yuri Mandina")
    st.caption("Ferramenta para suporte jurídico automatizado. Não substitui um advogado especialista.")

# Corpo Principal
st.markdown('<h1 class="main-header">Blindagem Jurídica AI 🛡️</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Automação de Análise Contratual e Blindagem Jurídica</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

input_contract = ""

with col1:
    st.subheader("📄 Documento Original")
    input_contract = st.text_area(
        "Cole o texto do contrato aqui:",
        height=500,
        placeholder="EX: CONTRATO DE PRESTAÇÃO DE SERVIÇOS..."
    )
    
    analyze_btn = st.button("🔍 Analisar Riscos e Blindagem")

with col2:
    st.subheader("🤖 Análise da IA")
    
    if analyze_btn and input_contract:
        with st.spinner("O Agente está lendo e cruzando dados com a legislação..."):
            try:
                # Chamada ao Backend
                result = get_llm_response(input_contract, confidence_threshold)
                
                # Renderização do Resultado
                st.markdown(result)
                
                # Feedback Visual de Sucesso
                st.success("Análise concluída com sucesso!")
                
            except Exception as e:
                st.error(f"Ocorreu um erro sistêmico: {e}")
                
    elif analyze_btn and not input_contract:
        st.warning("Por favor, insira um texto de contrato para analisar.")
    else:
        st.info("Aguardando input para iniciar a análise...")

# Rodapé
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Blindagem Jurídica AI © 2025 | Powered by LangChain & Groq"
    "</div>", 
    unsafe_allow_html=True
)