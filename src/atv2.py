import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Imagem como matriz")
st.subheader("Bandeira do Gabao em pixels")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:4, :] = (0, 158, 96)
bandeira[4:8, :] = (252, 209, 22)
bandeira[8:, :] = (54, 117, 177)

st.image(ampliar(bandeira))

st.write("Cores utilizadas (R, G, B):")
st.write("Verde: (0, 158, 96)")
st.write("Amarelo: (252, 209, 22)")
st.write("Azul: (54, 117, 177)")
