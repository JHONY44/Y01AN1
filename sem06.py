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

#ejercicio 4: calcular la media y comparar con 10
st.subheader("ejercicio 4: comparar 10 numeros con el valor 10")
numeros_ej1= st.text_input("ingresa 10 numeros separados por comas: ")
if st.button("ejecutar ejercicio 4"):
    lista_numeros= [int(num) for num in numeros_ej1.split(",")]
    media=sum(lista_numeros)/len(lista_numeros)
    mayores=len([num for num in lista_numeros if num>10])
    iguales= len([num for num in lista_numeros if num ==10])
    menores= len([num for num in lista_numeros if num<10])

    st.write(f"la media es: {media}")
    st.write(f"mayores que 10: {mayores}")
    st.write(f"iguales a 10: {iguales}")
    st.write(f"menores que 10: {menores}")
    