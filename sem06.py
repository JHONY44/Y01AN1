import streamlit as st

#titulo de la aplicacion
st.title("ejercicios con bucles basicos en python")

#ejercicio 1 :imprimir 10 veces "hola mundo"
st.subheader("ejercicio 1: imprimir 'hola mundo' diez veces ")
if st.button("ejecutar ejercicio 1"):
    for i in range (10):
        st.write("hola mundo")

#ejercicio 2: imprimir los 10 primeros numeros
st.subheader("ejercicio 2: imprimir los primeros 10 numeros")
if st.button("ejecutar ejercicio 2"):
    for i in range (1,11):
        st.write(i)

#ejercicio 3:tabla de multiplicar
st.subheader("ejercicio 3: imprimir la tabla de multiplicar del numero ingresado")
num=st.number_input("ingrese un numero para ver su tabla de multiplicar del 1 al 12", min_value=1)
if st.button("ejecitar ejercicio 3"):
    for i in range (1,13):
        st.write(f"{num} x {i} ={num * i}")
        