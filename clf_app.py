import streamlit as st # <3
import pickle
from sklearn.feature_extraction.text import CountVectorizer    # processamento de textos

# Lendo os picles 🥒🥒
model = pickle.load(open('model_clf.pkl','rb'))
count_vect = pickle.load(open('count_vect.pkl','rb'))

# Configurações gerais da página
st.beta_set_page_config(
    page_title="EM | Previsão de Categoria de Ebooks Infantis",
    page_icon="📚",      # polimento e chiquezas
    layout="centered",
    initial_sidebar_state="expanded",
)

# Funções para formatação html (arquivo .css)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)  # último parâmetro: permite formatação html
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)
#local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# Logo
from PIL import Image
image = Image.open('logoEM.png')
st.image(image,
      use_column_width=True)

# Função que recebe um input, formata e chama o modelo
def predict_category(text):
    input=count_vect.transform([text])   # processando o texto
    prediction = model.predict(input)    # famigerada categoria prevista

    return prediction
# (uau o computador pensa 🧠)

# Função bambambã
def main():
    st.title("Classificador de Ebooks Infantis")       # título da página
    html_temp = """
    <div style="background:#21618C; padding:10px">
    <h2 style="color:white;text-align:center;"> App de aprendizado de máquina da EM (time de dados 🎲 <3) </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)   # markdown da 'descrição'
    st.markdown("\n\n")
    
    # Recebe o texto do usuário e guarda na variável 'text'
    text = st.text_input("Insira o texto para prever a categoria que ele se enxaixa:")   # o primeiro parâmetro é o título do botão. O segundo é a descrição
    
    # Formatação para resposta safe
    safe_html ="""  
    <div style="background-color:#21618C; padding:10px >
    <h2 style="color:red;text-align:center;"> xx </h2>
    </div>
    """
    
    # Clickbait para roubar informações sensíveis do usuário:
    # ...quer dizer, botão para rodar a função e mostrar output do modelo 😅:
    if st.button('Prever categoria'):
        output = predict_category(text)
        st.success('Humm... acho que a categoria é {} 🤔'.format(output))            # bem pensado, que orgulho! 👏
        
        if output == 1:
            st.markdown(safe_html,unsafe_allow_html=True)
        # Mensagens de warning/error (não programado):
        elif output == 2:
            st.markdown(warn_html,unsafe_allow_html=True)
        elif output == 3:
            st.markdown(danger_html,unsafe_allow_html=True)  
        
if __name__=='__main__':
    main()
