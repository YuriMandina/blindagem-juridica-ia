# 🛡️ Blindagem Juridica IA

> **Agente de Inteligência Artificial para Blindagem Jurídica e Análise de Contratos.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Interface-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-RAG%20Pipeline-green.svg)
![Llama 3.3](https://img.shields.io/badge/Model-Llama%203.3%2070B%20(SOTA)-purple.svg)
![FAISS](https://img.shields.io/badge/VectorStore-FAISS-yellow.svg)

## 🎯 O Problema
A revisão manual de contratos é um processo lento, oneroso e sujeito a falhas humanas. Pequenas empresas e profissionais autônomos frequentemente assumem riscos legais ocultos (passivos trabalhistas, cláusulas abusivas) por falta de acesso rápido a uma auditoria jurídica preliminar.

## 💡 A Solução
**Blindagem Juridica AI** não é apenas um wrapper de GPT. É um sistema de **Engenharia de GenAI** completo que utiliza RAG (Retrieval-Augmented Generation) para cruzar minutas contratuais com uma base de conhecimento vetorial contendo jurisprudência atualizada do STF, CLT e LGPD.

O sistema atua como uma "primeira linha de defesa", sugerindo reescritas de blindagem e apontando riscos críticos em segundos.

### Diferenciais Técnicos
- **RAG Jurídico:** O modelo consulta uma base vetorial (FAISS) antes de responder, garantindo que a análise cite leis reais (STF, CDC, CLT) e reduza alucinações.
- **OCR Integrado:** Processamento de PDFs nativos e digitalizados via `pdfplumber`.
- **Modelo SOTA:** Utiliza o **Llama 3.3 70B Versatile** (via Groq) para raciocínio lógico complexo e nuances de linguagem PT-BR.
- **Arquitetura Modular:** Separação clara entre Frontend (Streamlit), Lógica de Negócio e Camada de Dados.

## 🛠️ Arquitetura do Sistema

1. **Ingestão:** O usuário faz upload de PDF ou cola texto.
2. **Retrieval (RAG):** O sistema vetoriza o input e busca os 3 tópicos mais relevantes na Base de Conhecimento Jurídica (`knowledge_base.txt`) usando FAISS.
3. **Augmentation:** O prompt do sistema é enriquecido dinamicamente com a jurisprudência recuperada.
4. **Generation:** O Llama 3.3 processa o contrato + jurisprudência e gera o relatório de blindagem.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Python 3.9+
* Chave de API da Groq (Gratuita em [console.groq.com](https://console.groq.com))

### Instalação

1. **Clone o repositório:**
   ```bash
    git clone https://github.com/YuriMandina/blindagem-juridica-ia.git
   cd blindagem-juridica-ia