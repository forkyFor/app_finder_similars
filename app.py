import streamlit as st
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.document_loaders.csv_loader import CSVLoader

# Caricamento delle variabili d'ambiente
load_dotenv()

# Configurazione della pagina Streamlit
st.set_page_config(page_title="Educate Kids", page_icon="🤖")
st.header("Hey, Ask me something & I will give out similar things")

# Inizializzazione di OpenAI Embeddings
embeddings = OpenAIEmbeddings()

# Caricamento del file CSV
loader = CSVLoader(file_path="myData.csv", csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})
data = loader.load()

# Creazione del database FAISS
db = FAISS.from_documents(data, embeddings)

# Funzione per raccogliere input dell'utente
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

# Raccolta input e pulsante per la ricerca
user_input = get_text()
submit = st.button("Find similar Things")

# Esecuzione della ricerca in FAISS
if submit:
    docs = db.similarity_search(user_input)
    st.subheader("Top Matches:")
    st.text(docs[0].page_content)
    st.text(docs[1].page_content)
