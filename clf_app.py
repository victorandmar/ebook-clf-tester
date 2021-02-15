import streamlit as st # <3
import pickle
from sklearn.feature_extraction.text import CountVectorizer    # processamento de textos

# Lendo os picles que tirei do hambúrguer
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
    st.title("Teste - Classificador de Ebooks Infantis")       # título da página
    st.markdown("\nApp para testar o modelo do **time de dados da EM** (🎲🖤) para classificação automática de ebooks infantis. Basta inserir o texto abaixo para ver como o algoritmo o classificaria!")
    html_temp = """
    <div style="background:#21618C; padding:10px">
    <h2 style="color:white;text-align:center;"> App de aprendizado de máquina da EM (time de dados 🎲 <3) </h2>
    </div>
    """
    #st.markdown(html_temp, unsafe_allow_html = True)   # markdown da 'descrição'
    
    #st.markdown("\n")
    
    # Recebe o texto do usuário e guarda na variável 'text'
    text = st.text_input("Texto:")   # o primeiro parâmetro é o título do botão. O segundo é a descrição
    
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
        st.success('Humm... acho que a categoria é {} 🤔'.format(output))            # bem pensado! 👏
        
        if output == 1:
            st.markdown(safe_html,unsafe_allow_html=True)
        # Mensagens de warning/error (não programado):
        elif output == 2:
            st.markdown(warn_html,unsafe_allow_html=True)
        elif output == 3:
            st.markdown(danger_html,unsafe_allow_html=True) 
    
    # Notas
    st.markdown("\n\n\n")
    st.write("**Algoritmo de machine learning**: LinearSVC")
    st.write("**Acurácia do modelo** (medida para chance de acerto): 67%")
    st.markdown("**Categorias e respectivas acurácias:**")
    st.write("\t - Amigos da natureza - 83%")
    st.write("\t - Animais - 78%")
    st.write("\t - Lidando com os sentimentos - 76%")
    st.write("\t - Família - 71%")
    st.write("\t - Sonhos - 70%")
    st.write("\t - Amizade - 67%")
    st.write("\t - Mistério - 64%")
    st.write("\t - Seres fantásticos - 58%")
    st.write("\t - Aventura - 53%")
    st.write("\t - Contos de fadas - 38%")
    
if __name__=='__main__':
    main()
