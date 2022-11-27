import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")
st.header('Simulation du mouvement brownien standard')

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

st.write('Entrer le parametres de la simulation')
with st.form(key="my_form"):
    d = st.number_input('Donner le nombre de simulation', step=1)
    n = st.number_input('Donner le temps', step=1, min_value=200)
    

    st.form_submit_button("Simuler")
 #nbr de simulation
T=4

times = np.linspace(0. , T, n)
dt = times[1] - times[0]
dB = np.sqrt(dt)* np.random.normal(size=(n-1,d))
B0 = np.zeros(shape=(1, d))
B = np.concatenate((B0, np.cumsum(dB, axis=0)) , axis = 0)
plt.plot(times, B)
figure=plt.show()

st.set_option('deprecation.showPyplotGlobalUse', False)

#st.pyplot(figure)


st.line_chart(B, use_container_width=True)
st.write(B)
#st._arrow_line_chart(B)









