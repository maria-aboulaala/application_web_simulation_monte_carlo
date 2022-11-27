import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")
st.header('Simulation du mouvement brownien geometrique')

with st.expander("Introduction:"):
    st.markdown("""

                Soit ( $\Omega$, $\mathcal{F}$, $\mathbb{F}$, $\mathcal{P}$) un espace probabilisé filtré  
                Un mouvement brownien  \{$W_t$: t$\geq$0\} avec $\mu$=0 et $\sigma$=1 est appelé mouvement brownien standard. Dans ce cas $W_t$ a une moyenne 0 et une variance t.
                N’importe quel mouvement brownien \{$W_t$: t$\geq$0\} de d´erive $\mu$
                st.latex(et de variance $\sigma^2$ peut alors s’´ecrire $W_t$ = $\mu$t + $\sigma$Z_t$ \{$Z_t$: t$\geq$0\} est un mouvement brownien standard.)
                For an indication of uncertainty, the following 1-$\sigma$ errors
                were observed when comparing model predictions to an independent
                test set of experimental observations:
                - Glass transition temperature: 19 K
                - Density: 0.02 g/cm\u00b3
                - Optical refractive index: 0.006
                - Configurational entropy: 0.9 J/(mol K)
                The Vogel-Fulcher-Tammann (VFT) equation given assumes that $T$ is
                specified in degrees Kelvin.
                """)




