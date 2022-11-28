import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta


st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")

st.header(':four: Simulation du put :chart_with_downwards_trend:')

with st.expander("Introduction:"):
    
    st.markdown("""
> Les options sont des dérivés financiers basés sur la valeur des titres sous-jacents. Ils donnent à l'acheteur le droit d'acheter (options d'achat) ou de vendre (options de vente) l'actif sous-jacent à un prix prédéterminé dans un délai précis. Il existe également deux styles d'options de base : américain et européen. Les options américaines peuvent être exercées à tout moment avant la date d'expiration de l'option, tandis que les options européennes ne peuvent être exercées qu'à la date d'expiration. Ce Notebook plonge dans un modèle d'évaluation des options pour comprendre l'évaluation des options européennes
               
                
                """
    )
with st.form(key="my_form"):   
    start_date = st.date_input('Donner le premier jour')
    stock_name = st.selectbox(
    'donner le marché',
    ('AAPL', 'MSFT'))
    nSim = st.number_input('Le prix initil du stock', step=1, min_value=1)

   

    st.form_submit_button("Simuler")



end_date = datetime.today()
stock_data = yf.download(
    stock_name,
    start = start_date,
    end= end_date
)
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












st.markdown(
    """
---

 Realisé par Aboulaala Maria                  
 Encadré par Pr. Brahim Elassri
    """
)