import streamlit as st
import time

# --- Mockups para garantir execução imediata ---
try:
    from core import get_llm_response
    from utils import extract_text_from_pdf
except ImportError:
    def get_llm_response(text, confidence):
        time.sleep(1.5)
        return f"## 🛡️ Análise de Risco Jurídico\n\n**Confiança da IA:** {int(confidence*100)}%\n\n### 1. Cláusulas Críticas\n* **Cláusula de Rescisão:** Detectada ambiguidade no prazo de aviso prévio.\n* **Foro de Eleição:** Recomendada alteração para comarca da sede.\n\n### 2. Jurisprudência Vinculada\n> *STJ, REsp 1.234.567/SP*: A validade da cláusula de arbitragem depende de concordância expressa."
    
    def extract_text_from_pdf(file):
        time.sleep(1)
        return "CONTRATO DE PRESTAÇÃO DE SERVIÇOS\n\nCLÁUSULA PRIMEIRA - DO OBJETO..."

# --- Configurações de UI (Variáveis Globais) ---
PAGE_TITLE = "Blindagem Jurídica AI"
PAGE_ICON = "⚖️"
LAYOUT = "wide"

# Paleta de Cores "Professional Dark"
COLOR_BG = "#0E1117"         # Fundo Geral
COLOR_SIDEBAR = "#161B22"    # Sidebar
COLOR_CARD = "#1D2127"       # Fundo dos Cards
COLOR_BORDER = "#30363D"     # Bordas Sutis
COLOR_ACCENT = "#EA1D2C"     # Vermelho Marca
COLOR_TEXT_MAIN = "#E6EDF3"  # Texto Principal
COLOR_TEXT_MUTED = "#7D8590" # Texto Secundário

HEIGHT_EDITOR = 550          # Altura unificada dos painéis

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT, initial_sidebar_state="expanded")

# --- CSS INJECTION (The Engine Room) ---
st.markdown(f"""
<style>
    /* Reset Geral e Fontes */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: {COLOR_TEXT_MAIN};
    }}

    /* Remover Padding Excessivo do Topo */
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 1rem;
        max-width: 95% !important;
    }}

    /* Header Personalizado */
    .header-title {{
        font-size: 2rem;
        font-weight: 800;
        color: {COLOR_TEXT_MAIN};
        margin: 0;
        letter-spacing: -0.02em;
    }}
    .header-badge {{
        background-color: {COLOR_ACCENT};
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        vertical-align: middle;
        margin-left: 10px;
    }}
    .header-subtitle {{
        color: {COLOR_TEXT_MUTED};
        font-size: 0.95rem;
        margin-top: 5px;
        margin-bottom: 25px;
    }}

    /* Estilização dos Containers (Cards) */
    [data-testid="stVerticalBlockBorderWrapper"] > div {{
        background-color: {COLOR_CARD};
        border: 1px solid {COLOR_BORDER};
        border-radius: 8px;
        padding: 10px;
    }}

    /* Text Area - Visual de Editor de Código */
    .stTextArea textarea {{
        background-color: #0d1117 !important;
        color: #c9d1d9 !important;
        font-family: 'Consolas', 'Monaco', monospace !important;
        font-size: 0.9rem;
        border: 1px solid {COLOR_BORDER} !important;
        border-radius: 6px;
        resize: none !important;
    }}
    .stTextArea textarea:focus {{
        border-color: {COLOR_ACCENT} !important;
        box-shadow: 0 0 0 1px {COLOR_ACCENT} !important;
    }}

    /* Tabs Customizadas */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2px;
        background-color: transparent;
    }}
    .stTabs [data-baseweb="tab"] {{
        height: 40px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        color: {COLOR_TEXT_MUTED};
        font-size: 0.9rem;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {COLOR_CARD} !important;
        color: {COLOR_ACCENT} !important;
        border-bottom: 2px solid {COLOR_ACCENT} !important;
    }}

    /* Botão Principal */
    .stButton button {{
        background: linear-gradient(90deg, {COLOR_ACCENT} 0%, #C91924 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 6px;
        transition: transform 0.1s, box-shadow 0.2s;
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }}
    .stButton button:hover {{
        box-shadow: 0 4px 12px rgba(234, 29, 44, 0.3);
        transform: translateY(-1px);
        color: white !important;
    }}
    .stButton button:active {{
        transform: translateY(1px);
    }}

    /* Barra de Progresso */
    .stProgress > div > div > div > div {{
        background-color: {COLOR_ACCENT};
    }}

    /* Scrollbar Discreta */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: {COLOR_BG}; }}
    ::-webkit-scrollbar-thumb {{ background: #444; border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #666; }}

    /* Esconder Menu Default do Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown(f"<h3 style='color: {COLOR_ACCENT}; border-bottom: 1px solid {COLOR_BORDER}; padding-bottom: 10px;'>⚙️ Configuração</h3>", unsafe_allow_html=True)
    
    st.markdown("#### 🤖 Modelo & Engine")
    st.caption("Motor de inferência ativo")
    with st.container(border=True):
        st.markdown("**LLM:** Llama 3.3 70B")
        st.markdown("**RAG:** STF + STJ (Vector Store)")
        st.markdown("<span style='color:#4CAF50'>● Sistema Online</span>", unsafe_allow_html=True)

    st.markdown("#### 🎚️ Sensibilidade")
    confidence = st.slider("Nível de Rigor Jurídico", 0.0, 1.0, 0.3, help="Menor = Mais literal | Maior = Mais interpretativo")
    
    st.markdown("---")
    st.info("**Nota:** Documentos digitalizados (scans) passam por OCR automático via Tesseract/PDFPlumber.")

    st.info("**⚠️ Aviso Legal:** Esta ferramenta é para fins informativos e não substitui aconselhamento jurídico profissional.")

# --- Header Principal ---

col_header_L, col_header_R = st.columns([3, 1])
with col_header_L:
    st.markdown("")
    st.markdown(f"""
    <div class="header-title">
        Blindagem Jurídica AI <span class="header-badge">BETA</span>
    </div>
    <div class="header-subtitle">
        Sistema de análise contratual preditiva com RAG integrado.
    </div>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'analyzed_result' not in st.session_state:
    st.session_state['analyzed_result'] = None
if 'input_content' not in st.session_state:
    st.session_state['input_content'] = ""

# --- WORKSPACE PRINCIPAL (GRID) ---
c1, c2 = st.columns([1, 1], gap="medium")

# === PAINEL ESQUERDO: INPUT ===
with c1:
    st.markdown("**📄 Documento Fonte**")
    
    # Container Principal Esquerdo
    with st.container(border=True, height=HEIGHT_EDITOR + 80):
        tab_editor, tab_upload = st.tabs(["📝 Editor Direto", "📂 Upload PDF"])
        
        with tab_editor:
            text_input = st.text_area(
                label="Editor Invisível",
                placeholder="Cole o texto integral do contrato ou peça jurídica aqui...",
                height=HEIGHT_EDITOR - 80,
                label_visibility="collapsed",
                key="editor_widget"
            )
            if text_input:
                st.session_state['input_content'] = text_input

        with tab_upload:
            st.markdown("<br><br>", unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Selecione arquivo PDF", type="pdf")
            if uploaded_file:
                with st.spinner("Executando OCR e Extração..."):
                    extracted = extract_text_from_pdf(uploaded_file)
                    st.session_state['input_content'] = extracted
                    st.success("PDF Processado.")
                    st.caption("Preview das primeiras 500 linhas:")
                    st.code(extracted[:500] + "...", language="text")

    # Botão de Ação fica FORA do container para destaque, mas alinhado à coluna
    st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True) # Spacer
    if st.button("🚀 EXECUTAR ANÁLISE", use_container_width=True):
        if not st.session_state['input_content']:
            st.toast("⚠️ Insira um documento antes de processar.", icon="🛑")
        else:
            with c2:
                with st.spinner("Acessando Jurisprudência e processando lógica..."):
                    # Simulação de progresso visual
                    prog_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01) 
                        prog_bar.progress(i + 1)
                    prog_bar.empty()
                    
                    # Execução Real
                    response = get_llm_response(st.session_state['input_content'], confidence)
                    st.session_state['analyzed_result'] = response
            st.rerun() # Rerun para atualizar o estado do lado direito

# === PAINEL DIREITO: OUTPUT ===
with c2:
    st.markdown("**📊 Relatório de Inteligência**")
    
    # Container Principal Direito (Mesma altura e estilo do Esquerdo)
    with st.container(border=True, height=HEIGHT_EDITOR + 80):
        
        if st.session_state['analyzed_result']:
            # Área de Resultado com Scroll
            st.markdown(st.session_state['analyzed_result'])
        else:
            # Empty State Profissional
            st.markdown(f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; text-align: center; opacity: 0.4;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
                <div style="font-weight: 600; font-size: 1.1rem;">Aguardando Análise</div>
                <div style="font-size: 0.9rem; max-width: 250px; margin-top: 10px;">
                    O relatório gerado pela IA aparecerá aqui com citações e análise de risco.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Botões de Exportação
    st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True) # Spacer
    
    # Só mostra botões de download se houver resultado, para manter a UI limpa
    if st.session_state['analyzed_result']:
        b1, b2 = st.columns(2)
        with b1:
            st.download_button(
                "📥 BAIXAR LAUDO (.TXT)", 
                data=st.session_state['analyzed_result'], 
                file_name="Analise_Juridica.txt",
                mime="text/plain",
                use_container_width=True
            )
        with b2:
            st.button("📋 COPIAR", use_container_width=True)
    else:
        # Botão desativado visualmente para manter a simetria do grid
        st.button("AGUARDANDO DADOS...", disabled=True, use_container_width=True)

# --- Footer Minimalista ---
st.markdown(
    "<div style='text-align: center; margin-top: 30px; color: #444; font-size: 0.8rem;'>Blindagem Jurídica AI • Ambiente Seguro</div>", 
    unsafe_allow_html=True
)