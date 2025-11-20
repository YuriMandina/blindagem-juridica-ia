# 🛡️ Juridical Shield AI

> **Automating Legal Risk Analysis using Large Language Models.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green.svg)
![Llama3.3](https://img.shields.io/badge/Model-Llama3.3--70B-purple.svg)

## 🎯 O Problema
A revisão manual de contratos é um processo lento, caro e sujeito a erro humano. Pequenas empresas muitas vezes assinam documentos com cláusulas abusivas por falta de assessoria jurídica imediata.

## 💡 A Solução
**Juridical Shield AI** é um agente inteligente que atua como uma primeira linha de defesa. Ele utiliza LLMs de última geração (Llama 3.3 via Groq) para ler minutas contratuais, identificar riscos baseados na legislação brasileira e sugerir reescritas de cláusulas para blindagem jurídica.

### Funcionalidades Principais
- **Detecção de Risco:** Identifica cláusulas ambíguas ou perigosas.
- **Sugestão de Redação:** Propõe textos alternativos mais seguros.
- **Interface Intuitiva:** Design limpo focado em usuários não-técnicos.

## 🛠️ Tech Stack (Tecnologias)
Este projeto demonstra o uso de Engenharia de Software moderna aplicada à IA:

* **Frontend:** Streamlit (para prototipagem rápida de Data Apps).
* **Orquestração de IA:** LangChain (Framework padrão da indústria).
* **LLM Inference:** Groq API (Inferência de baixa latência rodando Llama 3.3 70B).
* **Engenharia de Prompt:** Templates estruturados para garantir outputs consistentes.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Python 3.9+
* Chave de API da Groq (Gratuita)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/YuriMandina/blindagem-juridica-ia.git
   cd blindagem-juridica-ia