# Sistema-Experto-CommonKADS-para-optimizacion-del-riego-en-agricultura
# Tema 10: Sistema Experto de Agricultura Inteligente

## Descripción
Este proyecto consiste en el desarrollo de un sistema experto utilizando metodología CommonKADS, el sistema permite gestionar la cantidad y frecuencia de riego según características de plantas, tipo de suelo y factores ambientales. Antes de desarrollar el sistema hicimos los modelos correspondientes a la metodologia CommonKADS, para tener claro como seria el sistema.

El sistema se compone de:

- **Backend**: desarrollado en python usando pandas, con lógica de reglas para decidir riego.
- **Frontend**: interfaz web para registrar datos de cultivos y visualizar resultados (HTML y CSS).
- **Base de conocimiento**: reglas extraídas de información investigada, apoyándose en la IAG para validar factores y obtener información inicial.

el sistema cuenta con 3 grupos de reglas cada uno orientado a cada una de las recomendaciones que da:
1. si regar o mantener el plan de riego
2. frecuencia de riego
3. cuantos litros de agua usar por metro cuadrado

## Funcionalidades principales
- Registrar los datos ingresadoe por el usuario.
- a partir de estos en cada grupo de reglas, busca la reglas que calzan con los datos ingresos, cuando hay mas de una coincidencia utiliza la mas presisa (con mas atributos).
- envia las recomendaciones de riego en la interfaz.
- ademas entrega un detalle donde se explica por que se dieron estas recomendaciones.
- adicionalmente se agrego una api de clima para visualizar la temperatura, humedad ambiental, etc.

## Tecnologías utilizadas
- python con pandas
- HTML y CSS
- json con conocimientos

## Autores
- Felipe Araneda Arias
- Mallerly Carrasco Guerra
- Benjamín Castillo Molina


