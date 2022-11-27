import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")
st.header(':two: Simulation du mouvement brownien geometrique')

with st.expander("Introduction:"):
    st.markdown("""
            d$S_t$ = $\mu$($S_t$)dt +   $\sigma$($S_t$)d$W_t$ admet comme solution analytique \n
            > $S_t$ = $S_0$exp[($\mu$ - $\sigma$^2/2)t + $\sigma$($W_t$)] 

            
                """)
st.markdown("""
               > $S_t$ = $S_0$exp[($\mu$ - $\sigma$^2/2)t + $\sigma$($W_t$)] 
             
                """
    )

with st.form(key="my_form"):
    mu = st.number_input('mu', step=0.1)
    sigma = st.number_input('Donner la volatilité $\mu$', step=0.1)
    M = st.number_input('Donner le nombre de simalation', step=1)
    S0 = st.number_input('Le prix initil du stock', step=1, min_value=200)
    n = st.number_input('Donner la periode', step=1, min_value=50)
    st.form_submit_button("Simuler")




T = 1


dt = T/n
#simulating using np array
St = np.exp(
    (mu - sigma ** 2 / 2 ) * dt
    + sigma * np.random.normal(0, np.sqrt(dt), size = (M,n)).T
)
#imclude array of ones
St = np.vstack([np.ones(M), St])

#multiply bu S0 
St = S0 * St.cumprod(axis=0)

time = np.linspace(0, T, n+1)


tt = np.full(shape=(M, n+1), fill_value=time).T

plt.plot(tt, St)
plt.show()


st.subheader("Graphe generé :star2:")
st.line_chart(St, use_container_width=True)

st.subheader("Appercu des valeurs generé :1234:")

st.write(St)