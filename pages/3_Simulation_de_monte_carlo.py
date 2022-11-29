import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta


st.set_page_config(page_icon="🐤", page_title="Aboulaala Maria")

st.header(':three: Simulation monte Carlo du prix d un stock: :bar_chart:')

with st.expander("Qu'est-ce que la simulation Monte-Carlo ?:"):
    st.markdown("""

 > La simulation Monte-Carlo, également appelée méthode de Monte-Carlo ou la simulation de probabilités multiples, est une technique mathématique utilisée pour estimer les résultats possibles d'un événement incertain. Son nom est emprunté à une ville de casinos renommée, Monaco, car l'élément de hasard est au cœur de l'approche de modélisation, comme dans le jeu de roulette.
                                 
                """)
st.subheader('Entrez les parametres: :key: ')
with st.form(key="my_form"):   
    start_date = st.date_input('La date du depart')
    stock_name = st.selectbox(
    'Le symbole du stock',
    ('AAPL', 'MSFT', 'META', 'GOOG', 'AMZN'))
    n_sim = st.number_input('Le nombre de simulation', step=1, min_value=1)

    st.form_submit_button("Simuler")

st.subheader('Informations du stock choisi: :1234: ')

end_date = datetime.today()

stock_data = yf.download(
    stock_name,
    start = start_date,
    end= end_date
)
st.dataframe(stock_data, use_container_width=True)
nl = len(stock_data)
initial_price = stock_data['Adj Close'].iloc[len(stock_data)-1]
st.write('Vous avez choisis le stock ', stock_name)

st.write('Le prix initial du stock est :',initial_price)
st.write('La date d aujourdhui est: ', end_date)




all_sims = []
returns = np.log(1 + stock_data['Adj Close'].pct_change())
mu = returns.mean()
sigma = returns.std()

for i in range (n_sim):
    sim_rets = np.random.normal(mu, sigma, len(stock_data))
    sim_prices = initial_price * (sim_rets + 1 ).cumprod()
    all_sims.append(sim_prices)   
    #plt.axhline(initial_price, c='k')
    #plt.plot(sim_prices)   
    #st.pyplot(sim_prices)
df = pd.DataFrame(all_sims)
dff = df.transpose()
#st.dataframe(dff)

st.write('la volatilite du stock est', sigma)
st.subheader("Graphe generé :star2:")
st.line_chart(dff)


st.subheader("Mon code : :female-technologist: ")

code = '''
end_date = datetime.today()
stock_data = yf.download(
    stock_name,
    start = start_date,
    end= end_date
)
st.dataframe(stock_data, use_container_width=True)

initial_price = stock_data['Adj Close'].iloc[len(stock_data)-1]
st.write(initial_price)

all_sims = []
returns = np.log(1 + stock_data['Adj Close'].pct_change())
mu = returns.mean()
sigma = returns.std()

for i in range (250):
    sim_rets = np.random.normal(mu, sigma, len(stock_data))
    sim_prices = initial_price * (sim_rets + 1 ).cumprod()
    all_sims.append(sim_prices)   
    plt.axhline(initial_price, c='k')
    plt.plot(sim_prices)   
    
df = pd.DataFrame(all_sims)
dff = df.transpose()
st.dataframe(dff)
st.line_chart(dff)
'''
st.code(code, 
language='python')

st.markdown(
    """---
 Realisé par Aboulaala Maria                  
 Encadré par Pr. Brahim El Asri
    """
    )