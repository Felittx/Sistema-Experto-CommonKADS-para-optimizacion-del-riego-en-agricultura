from flask import Flask, render_template, request
from reglas import reglas_regar, reglas_frecuencia, clasificar_temperatura, clasificar_humedad, inferir, calcular_agua, generar_explicacion
import requests
from datetime import datetime

app = Flask(__name__)

 # <- DATOS PARA LA API DEL CLIMA->
LAT = -36.6000
LON = -72.1000
API_KEY = '951feb009bc819fc103de91bf2ce7b9a' # Key Felipe 
URL_CLIMA = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=es'
# <- DATOS PARA LA API DEL CLIMA->

@app.route('/')
def index():
    try:
        # consumir api del clima
        response = requests.get(URL_CLIMA)
        data = response.json()

        esta_lloviendo_api = False
        for weather in data['weather']:
            if "rain" in weather['main'].lower():
                esta_lloviendo_api = True
                break

        # se extraen los datos
        clima = {
            'temperatura': round(data['main']['temp'], 1),
            'humedad': data['main']['humidity'],
            'condicion': data['weather'][0]['description'].capitalize(),
            'icono': data['weather'][0]['icon'],
            'hora': datetime.now().strftime('%H:%M'),
            'esta_lloviendo': esta_lloviendo_api  
        }
    except Exception as e:
        # valores por defecto en caso de error
        clima = {
            'temperatura': '--',
            'humedad': '--',
            'condicion': 'No disponible',
            'icono': '01d',
            'hora': datetime.now().strftime('%H:%M'),
            'esta_lloviendo': False
        }

    return render_template('index.html', clima=clima)


@app.route('/resultado', methods=['POST'])
def resultado():
    # se obtienen los valores del frontend
    temperatura = float(request.form['temperatura'])
    humedad = float(request.form['humedad'])
    etapa = request.form['etapa']
    necesidad = request.form['necesidad']
    suelo = request.form['suelo']
    tipo_riego = request.form['tipo_riego']
    esta_lloviendo = request.form.get('esta_lloviendo') == '1'

    # <- se utiliza el motor de inferencia ->
    temp = clasificar_temperatura(temperatura)
    hum = clasificar_humedad(humedad)

    hechos = {temp, hum, suelo, f"etapa_{etapa}", tipo_riego, f"necesidad_agua_{necesidad}"}
    hechos.add("esta_lloviendo" if esta_lloviendo else "no_llueve")

    accion, razon1 = inferir(hechos, reglas_regar)
    frecuencia, razon2 = inferir(hechos, reglas_frecuencia)
    agua, razon3 = calcular_agua(hechos)

    explicacion = generar_explicacion(
        temperatura, humedad, esta_lloviendo, hechos, etapa, necesidad, suelo, tipo_riego
    )
     # <- se utiliza el motor de inferencia ->

    return render_template(
        'resultado.html',
        accion=accion,
        razon1=razon1,
        frecuencia=frecuencia,
        razon2=razon2,
        agua=agua,
        razon3=razon3,
        explicacion=explicacion
    )


if __name__ == '__main__':
    app.run(debug=True)
