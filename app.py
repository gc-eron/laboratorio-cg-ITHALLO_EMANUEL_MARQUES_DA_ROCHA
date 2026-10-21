import streamlit as st
import numpy as np

st.set_page_config(page_title="Laboratorio de Computacao Grafica", page_icon="🎨")

st.title("Laboratorio de Computacao Grafica")
st.header("Ithallo Emanuel")
st.write("UniFil - Centro Universitario Filadelfia")
st.write("Computacao Grafica - 2026/2")
st.write("Atividade 1 - Relatorio de Instalacao do Ambiente")

st.divider()

st.subheader("Ambiente funcionando")
st.write("Primeiro app Streamlit rodando com uv, Python 3.12 e as bibliotecas da disciplina.")

n = st.slider("Tamanho", 2, 64, 8)
img = np.random.randint(0, 256, (n, n), dtype=np.uint8)
st.image(img, caption=f"Imagem {n}x{n}", width=300)
