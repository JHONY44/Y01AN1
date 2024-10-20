import streamlit as st

#titulo de la aplicacion
st.title("ejercicios con bucles basicos en python")

#ejercicio 1 :imprimir 10 veces "hola mundo"
st.subheader("ejercicio 1: imprimir 'hola mundo' diez veces ")
if st.button("ejecutar ejercicio 1"):
    for i in range (10):
        st.write("hola mundo")
