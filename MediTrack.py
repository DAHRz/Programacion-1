from flask import Flask, request, render_template_string
import time
import csv

app = Flask(__name__)

# funcion para leer y formatear el contenido de un archivo CSV
def leer_csv(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                datos.append(fila)
    except FileNotFoundError:
        # por si el archivo aún no existe
        pass
    return datos

# Página principal con opciones

@app.route('/')
def index():
    return render_template_string("""
        <h1>🩺 MediTrack 🩺</h1>
        <ul>
            <li><a href="/registrar">Registrar paciente</a></li>
            <li><a href="/monitorear">Monitorear frecuencia cardíaca</a></li>
            <li><a href="/ver_registros">Ver Registros (Pacientes y Monitoreo)</a></li>
        </ul>
    """)


# registrar un paciente
@app.route('/registrar', methods=['GET', 'POST'])
def registrar_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        historial = request.form['historial']
        with open("pacientes.csv", "a", newline='') as archivo:
            archivo.write(f"{nombre},{edad},{historial}\n")
        return render_template_string("""
            <p>✅ Paciente registrado.</p>
            <p><a href="/">Volver al menú principal</a></p>
        """)
    
    return render_template_string("""
        <h2>📁 Registrar paciente</h2>
        <form method="post">
            Nombre: <input type="text" name="nombre"><br>
            Edad: <input type="text" name="edad"><br>
            Historial médico: <input type="text" name="historial"><br>
            <input type="submit" value="Registrar">
        </form>
        <br>
        <a href="/">Volver al menú principal</a>
    """)


# monitorear la frecuencia cardíaca
@app.route('/monitorear', methods=['GET', 'POST'])
def monitorear_paciente():
    if request.method == 'POST':
       
        try:
            nombre = request.form['nombre']
            sistolica = int(request.form['sistolica'])
            diastolica = int(request.form['diastolica'])
        except ValueError:
             return render_template_string("""
                <p>❌ Error: Asegúrate de ingresar números válidos para la presión.</p>
                <p><a href="/monitorear">Intentar de nuevo</a></p>
            """)

        # calculos
        if 121 <= sistolica <= 129 and diastolica <= 79:
            riesgo = "⚠️ Presión arterial elevada"
        elif 130 <= sistolica <= 139 and 80 <= diastolica <= 89: 
            riesgo = "⚠️ Hipertensión etapa 1"
        elif sistolica >= 140 or diastolica >= 90:
            riesgo = "⚠️ Hipertensión etapa 2 o más"
        else:
            riesgo = "✅ Frecuencia dentro del rango normal."

        frecuencia = f"{sistolica}/{diastolica}" 
        with open("monitoreo.csv", "a", newline='') as archivo: 
            archivo.write(f"{nombre},{frecuencia},{time.ctime()}\n")

        return render_template_string(f"""
            <h2>Resultado del Monitoreo</h2>
            <p>🫀 Frecuencia cardíaca actual: {sistolica} / {diastolica} mmHg</p>
            <p>{riesgo}</p>
            <p>📁 Datos guardados en historial.</p>
            <p><a href="/">Volver al menú principal</a></p>
        """)

    return render_template_string("""
        <h2>📊 Monitorear paciente</h2>
        <form method="post">
            Nombre del paciente: <input type="text" name="nombre"><br>
            Presión sistólica (ej: 120): <input type="number" name="sistolica" required><br>
            Presión diastólica (ej: 80): <input type="number" name="diastolica" required><br>
            <input type="submit" value="Monitorear">
        </form>
        <br>
        <a href="/">Volver al menú principal</a>
    """)
    
# ver el contenido de los archivos CSV
@app.route('/ver_registros')
def ver_registros():
    # datos de pacientes
    datos_pacientes = leer_csv("pacientes.csv")
    cabecera_pacientes = ["Nombre", "Edad", "Historial Médico"]
    
    # datos de monitoreo
    datos_monitoreo = leer_csv("monitoreo.csv")
    cabecera_monitoreo = ["Nombre", "Frecuencia (Sistólica/Diastólica)", "Fecha y Hora"]
    
    def generar_tabla_html(titulo, cabecera, datos):
        html = f"<h3>{titulo} ({len(datos)} registros)</h3>"
        if not datos:
            html += "<p>No hay registros disponibles.</p>"
            return html
            
        html += "<table border='1' style='width:100%; text-align:left;'>"
        
        # Cabecera
        html += "<tr>"
        for col in cabecera:
            html += f"<th>{col}</th>"
        html += "</tr>"
        
        # Filas 
        for fila in datos:
            html += "<tr>"
            for celda in fila:
                html += f"<td>{celda}</td>"
            html += "</tr>"
            
        html += "</table><br>"
        return html

    html_pacientes = generar_tabla_html("Registro de Pacientes", cabecera_pacientes, datos_pacientes)
    html_monitoreo = generar_tabla_html("Historial de Monitoreo Cardíaco", cabecera_monitoreo, datos_monitoreo)

    return render_template_string(f"""
        <h2>📊 Registros Guardados</h2>
        {html_pacientes}
        {html_monitoreo}
        <hr>
        <a href="/">Volver al menú principal</a>
    """)

if __name__ == '__main__':
    app.run(debug=True)