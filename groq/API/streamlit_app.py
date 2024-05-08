import streamlit as st
import requests

st.title("Demostración de Chatgroq con Llama3")

prompt1 = st.text_input("Ingrese su pregunta sobre los documentos")

if st.button("Obtener respuesta"):
    response = requests.post("http://localhost:8000/ask", json={"question": prompt1})
    result = response.json()

    st.write(result['respuesta'])

    with st.expander("Búsqueda de documentos similares"):
        for doc in result["contexto"]:
            st.write(doc.page_content)
            st.write("---")
