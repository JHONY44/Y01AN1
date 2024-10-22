import streamlite as st

def mostrar_menu():
    st.title("Ejemplo de menu")
    st.write("selecciona una opcion del menu")

    menu_["archivo","editar", "ver", "salir"]
    seleccion =""


    seleccion=st.radio("menu", menu)

        if seleccion=="archivo":
            st.write("seleccionaste: archivo")
        elif seleccion =="editar":
            st.write("seleccionaste: editar")
        elif seleccion =="ver":
            st.write("seleccionaste: ver")
        elif seleccion=="salir":
            st.write("!SALIENDO DEL MENU¡")
            break

if__name__=="__main__":
    mostrar_menu()