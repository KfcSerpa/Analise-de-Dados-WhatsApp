import streamlit as st

# Configuração da página
st.set_page_config(page_title="Kaique Serpa - Projetos", layout="wide", page_icon="📊")

# Estilo customizado para o tema da página
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    .stApp {
        background-color: #000000;
    }
    h1, h2, p, .stMarkdown, .footer {
        color: #ffffff !important;
    }
    .top-left {
        position: absolute;
        top: 10px;
        left: 10px;
        text-align: left;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
    }
    .top-left img {
        border-radius: 50%;
        width: 70px;
        height: 70px;
        margin-right: 10px;
    }
    .top-left h1 {
        font-size: 1.5em;
        color: #ffffff !important;
        margin: 0;
    }
    iframe {
        width: 100%;
        height: 1000px;
    }
    .footer {
        text-align: center;
        font-size: 1em;
        color: #ffffff !important;
        background-color: #000000;
        padding: 15px;
        margin-top: 20px;
        border-top: 1px solid #333333;
    }
    .footer a {
        color: #e63946;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .projeto-nome {
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        padding-top: 20px;
    }
    @media only screen and (max-width: 600px) {
        .top-left {
            position: relative;
            top: 0;
            left: 0;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .top-left img {
            margin-bottom: 10px;
        }
        .top-left h1 {
            font-size: 1.2em;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Foto e nome no canto superior esquerdo
st.markdown("""
    <div class="top-left">
        <img src="https://media.licdn.com/dms/image/v2/D5603AQGrQQlmRf0oPw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1706541572740?e=1744243200&v=beta&t=_636F7ubEFB2EDRm0OgI3d1Gs4J6n_b-2tyoHoto7uA" alt="Foto de Kaique">
        <h1>Kaique Serpa - Analista de Dados</h1>
    </div>
""", unsafe_allow_html=True)

# Introdução
st.markdown("""
    <div style="text-align: center;">
        <h2>Bem-vindo ao meu portfólio de projetos!</h2>
        <p>Esta página apresenta alguns dos meus projetos pessoais. Navegue, explore e veja o que eu fiz!</p>
    </div>
""", unsafe_allow_html=True)

# Nome do projeto
st.markdown("""
    <div class="projeto-nome">
        Análise de grupo do WhatsApp
    </div>
""", unsafe_allow_html=True)

# Explicativo do projeto
st.markdown("""
    ### Explicativo do Processo de Análise  
    Este projeto consiste na análise de dados extraídos de um grupo de WhatsApp. A partir de um arquivo de texto exportado do WhatsApp, foi utilizado Python para tratar e organizar as mensagens em formato tabular. Após o tratamento dos dados, foi gerado um arquivo CSV, que foi importado para o Power BI para criação de visualizações interativas.  

    **As análises incluem:**  
    - 📆 Mensagens por ano  
    - 🗓️ Distribuição de conversas por dia da semana e horário  
    - 😂 Emojis mais utilizados  
    - 🗣️ Participantes mais ativos  
    - 🏛️ Discussões sobre política  

    O projeto visa demonstrar a aplicação de ferramentas de análise de dados e visualização interativa, combinando Python, Power BI e Streamlit para apresentar insights de maneira acessível e interativa.
""")

# Dashboard Power BI
st.markdown("### 📊 Dashboard Interativo - Power BI")
st.markdown(
    """
    <iframe src="https://app.powerbi.com/view?r=eyJrIjoiMmVhNzNiY2QtNDQwNi00MWM4LWFhMWEtNTY1MTgwMzI4ZGFjIiwidCI6IjgxNGUxYjdjLTg5NzUtNDM3Yy05ZTE4LWJhOWY5NzUzZDUwYyJ9" 
    frameborder="0" allowFullScreen="true" width="100%" height="600"></iframe>
    """, unsafe_allow_html=True
)

# Seção para download do currículo
st.markdown("""
    ### 📄 Baixe Meu Currículo  
    [Clique aqui para baixar meu currículo](https://github.com/KfcSerpa/Curr-culo/blob/main/Kaique%20Serpa.2025.pdf)
""")

# Rodapé personalizado
st.markdown("""
    <div class="footer">
        <p>Desenvolvido por Kaique Serpa | <a href="https://www.linkedin.com/in/kaique-serpa-689387144/" target="_blank">LinkedIn</a></p>
    </div>
""", unsafe_allow_html=True)
