def evaluar_hipertension(pas, pad):
    """
    Evalúa si una persona tiene hipertensión según los criterios ESC 2024.

    Parámetros:
    pas (int): Presión arterial sistólica
    pad (int): Presión arterial diastólica

    Retorna:
    str: Diagnóstico
    """
    
    if pas >= 140 or pad >= 90:
        return "Hipertensión etapa 2"
    elif 130 <= pas < 140 or 80 <= pad < 90:
        return "Hipertensión etapa 1"
    elif 120 <= pas < 130 and pad < 80:
        return "Presión arterial elevada"
    elif pas < 120 and pad < 80:
        return "Presión normal"
    else:
        return "Clasificación no definida"

# Ejemplo de uso
pas = 145
pad = 95
diagnostico = evaluar_hipertension(pas, pad)
print(f"Diagnóstico: {diagnostico}")


