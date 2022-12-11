import streamlit as st
import pandas as pd


st.set_page_config(page_icon=":game_die:", page_title="Aboulaala Projet")

st.header('Bonjour :grinning:')
with st.expander("Objectifs:"):

    st.markdown(
    """
> Cette presentation est faite dans le cadre du projet du module Processus Stochastique, et vise a realiser les simulations suivantes:
- Simulation du mouvement Brownien Standard
- Simulation du mouvement Brownien geometrique
- Simulation du prix d'un stock avec Monte Carlo
- Simulation de la valeur du Put et du Call Europeen
   """
)
st.subheader('Introduction')




st.markdown(
    """
    Pourquoi on simule?
    >La simulation est un outil de la finance computationnelle. Elle est utilée par exemple dans la simulation du prix d'une action, ou le pricing du put et call (les simulations sont faites dans ce qui suivera), a titre d'exemple la methode de Monte Carlo. \n
    Durant cette presentation on s'interesse aux methode de simulation d'une diffusion de la forme: \n
    > d$S_t$ = $\mu$($S_t$)dt +   $\sigma$($S_t$)d$W_t$   \n
    - $S_t$ represente l'evolution de d- sous jacents sur un marché  
    - $W_t$ est une mouvement brownien 
    - $\mu$ est la derivé 
    - $\sigma$ est la volatilité

   """
)

st.success('les details de chaque simulation sont mentionnés dans chaque partie')














st.markdown(
    """
---

 Realisé par Aboulaala Maria                  

 
    """
)


