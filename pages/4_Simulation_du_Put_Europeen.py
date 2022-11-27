import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")

st.header(':three: Simulation du put :chart_with_downwards_trend:')

with st.expander("Introduction:"):
    
    st.markdown("""

                Soit ( $\Omega$, $\mathcal{F}$, $\mathbb{F}$, $\mathcal{P}$) un espace probabilisé filtré \n
                Un processus stochastique W : [0, +$\infty$[ \times $\mathbb{R}$ $\longrightarrow$ $\mathbb{R}$ est mouvement brownien standard si: \n
                - $W_0$ = 0
                - Pour tout s$\leq$t , $W_t$ - $W_{t-1}$ suit la loi $\mathcal{N}$(0,t-s)
                - Pour tout n$\geq$1 , et tous $t_0$ = 0 < $t_1$ < ...< $t_n$, les accroissement ($W_{{t_i}+1}$ - $W_{t_i}$ : 0 $\leq$ i $\leq$ n-1) sont **independantes**.
                En d'autres termes, pour tout $t_0$, $W_t$ $\sim$ $\mathcal{N}$(0,t), les trajectoires de $W_t$ ,  $t_0$ sont presque surement continues.

                
                """
    )
with st.form(key="my_form"):
    end_date = st.date_input('Donner le dernier jour' )
    start_date = st.date_input('Donner le premier jour')
    stock_name = st.selectbox(
    'donner le marché',
    ('AAPL', 'MSFT'))
    stock_name = st.selectbox(
    'donner le ',
    ('PUT', 'CALL'))

    st.form_submit_button("Simuler")




stock_data = yf.download(
    stock_name,
    start = start_date,
    end= end_date
)
st.dataframe(stock_data, use_container_width=True)


st.markdown(
    """
---

 Realisé par Aboulaala Maria                  
 Encadré par Pr. Brahim Elassri
    """
)