import streamlite as st

##funcion principal para verificar automoviles
def verificar_automoviles():
    st.title("centro de verificacion de automoviles")

    #lista para almacenar los puntos contaminantes
    if 'puntos_contaminantes' not in st.session_state:
        st.session_state.puntos_contaminantes=[]
    
    #input para los puntos contaminantes del automovil
    puntos = st.number_input("ingrese los puntos contaminantes del automovil", min_value=0.0, step= 0.1 )

    #boton para registrar el automovil
    if st.button("registrar automovil")
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"automovil registrado con {puntos} puntos contaminantes.")
    
    #mostrar los datos registrado hasta el momento
    if.len(st.session_state_puntos.puntos_contaminantes) >0 st.button("calcular resultados")
        promedio=sum(st.session_state.puntos_contaminantes)/len(st.session_state.puntos_contaminantes)
        menos_contaminacion=min(st.session_state.puntos_contaminantes)
        max_contaminacion= max(st.session_state.puntos_contaminantes)

        #mostrar los resultados
        st.write(f"promedio de puntos contaminantes: {promedio:.2f}")
        st.write(f"el automovil que menos contamino tiene {menos_contaminacion}")
        st.write(f"el automovil que mas contamino tiene {mas_contaminacion}")

        #opcion para reiniciar los datos
        if st.button("reiniciar los datos"):
            st.session_state.puntos_contaminantes=[]
            st.success("datos reiniciados correctamente")
        
        #ejecutar la funcion
        if __name__ == "__main__":
            verificar_automoviles()


    