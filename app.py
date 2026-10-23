import streamlit as st
import joblib
from src.preprocesamiento import limpiar_correo
from src.explicador import analizar_patrones


@st.cache_resource
def cargar_modelo():
    return joblib.load('modelos/modelo_rf.pkl')


modelo = cargar_modelo()

st.title("Detector de correos sospechosos — Rivas")
st.write(
    "Esta herramienta es un prototipo desarrollado como parte de una "
    "monografía universitaria sobre detección de phishing mediante "
    "Procesamiento de Lenguaje Natural (NLP)."
)
st.write("Pegue el texto de un correo o mensaje para analizarlo:")

texto_usuario = st.text_area("Texto del mensaje:", height=150)

if st.button("Analizar mensaje"):
    if texto_usuario.strip() == "":
        st.warning("Por favor ingrese un texto para analizar.")
    else:
        texto_limpio = limpiar_correo(texto_usuario)
        prediccion = modelo.predict([texto_limpio])[0]
        probabilidad = modelo.predict_proba([texto_limpio])[0][1]
        hallazgos = analizar_patrones(texto_usuario)

        if prediccion == 1:
            st.error(f"Resultado: probable phishing (confianza: {probabilidad:.0%})")
        else:
            st.success(f"Resultado: probablemente legítimo (confianza: {(1 - probabilidad):.0%})")

        if hallazgos:
            st.write("**Razones de la alerta:**")
            for h in hallazgos:
                st.write(f"- {h}")
        else:
            st.write("No se identificaron frases de alerta conocidas.")

        st.info(
            "Recomendación: ante cualquier duda, no haga clic en enlaces ni "
            "proporcione datos personales. Verifique directamente con la "
            "institución mencionada por un canal oficial."
        )

st.divider()
st.caption(
    "Prototipo académico — Detección de Phishing con NLP, municipio de Rivas, 2025-2026. "
    "El modelo principal de esta investigación es BERT (BETO); este prototipo usa "
    "Random Forest por razones de optimización del entorno gratuito de despliegue."
   "Agregar app principal"
)
