import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

def wavelength_to_rgb(wavelength):
    R = G = B = 0.0
    if 380 <= wavelength < 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 <= wavelength < 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 <= wavelength < 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength < 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength < 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= wavelength <= 700:
        R = 1.0
        G = 0.0
        B = 0.0
    return (R, G, B)

st.title("🌈 波長可視化ツール")
wavelength = st.slider("波長 (nm)", 380, 700, 550)

rgb = wavelength_to_rgb(wavelength)
st.markdown(
    f"<div style='width:100%; height:100px; background-color:rgb({rgb[0]*255},{rgb[1]*255},{rgb[2]*255})'></div>",
    unsafe_allow_html=True,
)

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(3e8 / (wavelength * 1e-9) * x * 1e-14)
ax.plot(x, y, color="black")
ax.set_title("Waveform of Selected Wavelength")
st.pyplot(fig)
