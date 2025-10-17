import streamlit as st

st.title("Calculadora Simples Exibindo A Media") 

nomeAluno = st.text_input("Digite o nome do aluno: ")

primeiraNota = st.number_input(label="Digite a primeira nota: ")

segundaNota = st.number_input(label="Digite a segunda nota: ")

terceiraNota = st.number_input(label="Digite a terceira nota: ")
 
if st.button("Calcular Média"):
    if not nomeAluno and not primeiraNota and not segundaNota and not terceiraNota:
        st.error("Campo obrigatório")
    else:
     media = (primeiraNota + segundaNota + terceiraNota) / 3
     if media >= 7:
         st.success(f"Parabéns {nomeAluno} ! Você foi aprovado com a média: {media:.2f}")
     else:
         st.error(f"Desculpe {nomeAluno} ! Você foi reprovado com a média: {media:.2f}")
    