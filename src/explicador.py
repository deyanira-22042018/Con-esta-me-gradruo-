import re

# Patrones lingüísticos de alerta, basados en la sección 6.3.2 del marco teórico
PATRONES_ALERTA = {
    r'(suspend|bloque|cancel).{0,25}(cuenta|servicio|acceso|tarjeta)':
        'Amenaza de suspensión o bloqueo de cuenta',
    r'(verifiqu|confirm|actualic).{0,25}(datos|contraseñ|cuenta|informaci|identidad)':
        'Solicitud de verificación de datos personales',
    r'(http|www\.|bit\.ly|tinyurl|url)\S*':
        'Enlace incluido en el mensaje',
    r'(gan[óo]|premio|regalo|sorteo|bono)':
        'Oferta de premio, regalo o sorteo',
    r'(urgente|inmediato|24 horas|de inmediato|ultimo aviso|ultima notificacion)':
        'Lenguaje de urgencia o presión de tiempo',
    r'(banco|tarjeta|cuenta bancaria|tigo|claro|inss|dgi)':
        'Mención de institución financiera o gubernamental',
}


def analizar_patrones(texto):
    """Identifica frases de alerta presentes en el texto (en minúsculas)."""
    hallazgos = []
    texto_normalizado = texto.lower()
    for patron, descripcion in PATRONES_ALERTA.items():
        if re.search(patron, texto_normalizado):
            hallazgos.append(descripcion)
    return hallazgos
