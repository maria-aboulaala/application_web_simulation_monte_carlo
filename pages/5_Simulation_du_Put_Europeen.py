import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta


st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")

st.header(':four: Simulation du put :chart_with_downwards_trend:')

with st.expander("Introduction:"):
    
    st.markdown("""
Nous montrerons comment nous pouvons évaluer les options européennes avec la simulation de Monte Carlo en utilisant Python. Rappelons que les options européennes sont une version d'un contrat d'options qui limite l'exécution à sa date d'expiration. Nous nous concentrerons uniquement sur les options d'achat et de vente. \n
Nous pouvons calculer le prix des options de vente et d'achat européennes explicitement en utilisant la formule Black-Scholes \n
Le prix d'une option de vente correspondante basée sur la parité put-call est
> $P$($S_t$, $t$) = $K$ $e^{r(T - t)}$ - $S_t$ + $C$($S_t$ , $t$) \n
> = $N$(-$d_2$)$PV$($K$) - $N$(-$d_1$)$S_t$
               
                
                """)

st.subheader('Entrez les parametres: :key: ')                
with st.form(key="my_form"):   
    start_date = st.date_input('Donner le premier jour')
    stock_name = st.selectbox(
    'donner le marché',
    ('AAPL', 'MSFT', 'META', 'GOOG', 'AMZN'))
    nSim = st.number_input('Le nombre de simulation', step=1, min_value=1)
    st.form_submit_button("Simuler")



end_date = datetime.today()
stock_data = yf.download(
    stock_name,
    start = start_date,
    end= end_date
)
st.subheader('Informations du stock choisi: :1234: ')
st.dataframe(stock_data, use_container_width=True)

daily_returns = stock_data['Adj Close'].pct_change(1)
stock_volatility = daily_returns.std()
st.write('la volatilité du stock est: ', stock_volatility)

# european option parametre
stock_price = stock_data['Adj Close'][-1]
strike_price = stock_price 
risk_free_rate = 0.04
maturity = 1.0


z = np.random.standard_normal(nSim) #brownien motion
S_fwd = stock_price * np.exp((risk_free_rate-0.5* stock_volatility**2)*maturity + stock_volatility*np.sqrt(maturity)*z)
payoff = np.maximum(strike_price- S_fwd , 0)
put = np.exp(-risk_free_rate*maturity) * np.sum(payoff)/nSim  

st.write('la valeur du put est', put)


st.subheader("Mon code : :female-technologist: ")

code = '''
end_date = datetime.today()
stock_data = yf.download(
    stock_name,
    start = start_date,
    end= end_date
)
st.subheader('Informations du stock choisi: :1234: ')
st.dataframe(stock_data, use_container_width=True)

daily_returns = stock_data['Adj Close'].pct_change(1)
stock_volatility = daily_returns.std()
st.write('la volatilité du stock est: ', stock_volatility)

# european option parametre
stock_price = stock_data['Adj Close'][-1]
strike_price = stock_price 
risk_free_rate = 0.04
maturity = 1.0


z = np.random.standard_normal(nSim) #brownien motion
S_fwd = stock_price * np.exp((risk_free_rate-0.5* stock_volatility**2)*maturity + stock_volatility*np.sqrt(maturity)*z)
payoff = np.maximum(strike_price- S_fwd , 0)
put = np.exp(-risk_free_rate*maturity) * np.sum(payoff)/nSim  
'''
st.code(code, 
language='python')









st.markdown(
    """
---

 Realisé par Aboulaala Maria                  
 Encadré par Pr. Brahim El Asri
    """
)