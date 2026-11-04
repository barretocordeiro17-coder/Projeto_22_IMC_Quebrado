import streamlit as st

st.title("🧮 Calculadora de IMC")

st.set_page_config(page_title="Calculadora de IMC", page_icon="🧮")

st.write("Preencha os dados abaixo pra descubrir o seu IMC:")

nome = st.text_input("Qual é o seu nome")
peso = st.number_input("Peso (kg)", min_value=0.5, max_value=300.0, value=70.0,step=1.0)
altura = st.number_input("Altura (cm)", min_value=0.5, max_value=2.5, value=1.70)

if st.button("Calcular IMC"):
    imc = round(peso / (altura**2))

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc >18.5 and imc <= 25:
        classificacao = "Peso normal"
    elif imc > 25 and imc <=29.9:
        classificacao = "Sobrepeso"
    elif imc >= 30 and imc <=34.9:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade gráve"

    st.success("Calculo realizado com sucesso!")
    st.write("Seu IMC é: " , imc)
    st.info(f"{nome}, sua classificação é: {classificacao}")
    st.progress(imc)

with st.expander("Como o IMC é calculado?"):
    st.latex(f"IMC = \frac{peso}{altura}")
    st.write("Divida o peso em quilos pela altura em metros, elevada ao quadrado.")

st.warning("Atensão: esse resultado nao substitui a avaliação de um profissional de saude.")
