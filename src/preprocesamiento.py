import re
from bs4 import BeautifulSoup


def limpiar_correo(texto):
    """Limpia un correo o mensaje y lo deja listo para el modelo."""

    # Eliminar etiquetas HTML si existen
    texto = BeautifulSoup(texto, "html.parser").get_text()

    # Reemplazar URLs por un token genérico
    texto = re.sub(r'http\S+|www\S+', ' URL ', texto)

    # Convertir a minúsculas
    texto = texto.lower()

    # Eliminar caracteres especiales (conservando letras, ñ, tildes y espacios)
    texto = re.sub(r'[^a-záéíóúüñ\s]', ' ', texto)

    # Eliminar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto
