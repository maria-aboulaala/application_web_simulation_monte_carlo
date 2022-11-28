import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_icon=":game_die:", page_title="Aboulaala Maria")
st.header(':one: Simulation du mouvement brownien standard')

with st.expander("Introduction:"):
    
    st.markdown("""

    Un processus stochastique est une collectionde variables aleatoires indicées {$W_t$}, ou $t \in T$  
    Un processus stochastique W : [0, +$\infty$[ x $\mathbb{R}$ $\longrightarrow$ $\mathbb{R}$ est mouvement brownien standard si: \n
    - $W_0$ = 0
    - Pour tout s$\leq$t , $W_t$ - $W_{t-1}$ suit la loi $\mathcal{N}$(0,t-s)
    - Pour tout n$\geq$1 , et tous $t_0$ = 0 < $t_1$ < ...< $t_n$, les accroissement ($W_{{t_i}+1}$ - $W_{t_i}$ : 0 $\leq$ i $\leq$ n-1) sont **independantes**.
    En d'autres termes, pour tout $t_0$, $W_t$ $\sim$ $\mathcal{N}$(0,t), les trajectoires de $W_t$ ,  $t_0$ sont presque surement continues.
                """
    )

st.write('Entrer le parametres de la simulation')
with st.form(key="my_form"):
    d = st.number_input('Le nombre de simulation', step=1,min_value=1 )
    n = st.number_input('La periode', step=1, min_value=200)
    

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

st.subheader("La simulation : :star2: ")
st.line_chart(B, use_container_width=True)
st.subheader("Appercu des valeurs generées: :1234:")
st.write(B)
#st._arrow_line_chart(B)



st.subheader("Mon code : :female-technologist: ")

code = '''times = np.linspace(0. , T, n)
dt = times[1] - times[0]
dB = np.sqrt(dt)* np.random.normal(size=(n-1,d))
B0 = np.zeros(shape=(1, d))
B = np.concatenate((B0, np.cumsum(dB, axis=0)) , axis = 0)
plt.plot(times, B)
figure=plt.show()
'''
st.code(code, 





language='python')




st.markdown(
    """
---

 Realisé par Aboulaala Maria                  
 Encadré par Pr. Brahim Elassri
    """
)




#Soit ( $\Omega$, $\mathcal{F}$, $\mathbb{F}$, $\mathcal{P}$) un espace probabilisé filtré \n