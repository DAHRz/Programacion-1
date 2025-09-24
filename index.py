import time

def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    historial = input("Historial médico: ")
    with open("pacientes.csv", "a") as archivo:
        archivo.write(f"{nombre},{edad},{historial}\n")
    print("✅ Paciente registrado.")

def simular_frecuencia():
    sistolica = int(input("ingrese la sistolica: "))  # se agrega la presion sistolica
    diastolica = int(input("ingrese la diastolica: "))  # se agrega la presion diastolica
    if sistolica >= 121 and sistolica <= 129 and diastolica <= 79:
        print(f"\n🫀 Frecuencia cardíaca actual: {sistolica} / {diastolica} bpm")
        print("⚠️ Riesgo detectado: Presión arterial elevada") 
    elif sistolica >= 130 and sistolica <= 139 and diastolica >= 81 and diastolica <= 89:
        print(f"\n🫀 Frecuencia cardíaca actual: {sistolica} / {diastolica} bpm")
        print("\n⚠️ Riesgo detectado: Hipertensión etapa 1")
    elif sistolica >= 140 and diastolica >= 90:
        print(f"\n🫀 Frecuencia cardíaca actual: {sistolica} / {diastolica} bpm")
        print("⚠️ Riesgo detectado: Hipertensión etapa 2")
    else:
        print(f"🫀 Frecuencia cardíaca actual: {sistolica} / {diastolica} bpm")
        print("✅ Frecuencia dentro del rango normal.")

    frecuencia = (sistolica, diastolica) # se guardan los datos ingresados de frecuencia cardíaca en una sola variable
    return frecuencia

def monitorear_paciente():
    nombre = input("Nombre del paciente a monitorear: ")
    frecuencia = simular_frecuencia()
    with open("monitoreo.csv", "a") as archivo:
        archivo.write(f"{nombre},{frecuencia},{time.ctime()}\n")
    print("\n📁 Datos guardados en historial.")

# Menú principal para elegir la opcion a realizar
while True:
    print("\n--- MEDITRACK ---")
    print("1. Registrar paciente")
    print("2. Monitorear frecuencia cardíaca")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        monitorear_paciente()
    elif opcion == "3":
        print("👋 Cerrando Meditrack...")
        break
    else:
        print("❗ Opción inválida.")