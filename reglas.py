reglas_regar = [
    # en caso de lluvia
    {
        "condiciones": ["esta_lluviendo"],
        "conclusion": "mantener_plan_riego",
        "razon": "Está lloviendo, seguir el plan de riego existente."
    },
    
    # para humedad alta 
    {
        "condiciones": ["humedad_alta"],
        "conclusion": "mantener_plan_riego",
        "razon": "El suelo ya tiene suficiente agua, no es necesario regar."
    },
    
    # para humedad media, consideradno etapa germinacion
    {
        "condiciones": ["humedad_media", "etapa_germinacion"],
        "conclusion": "regar_ahora",
        "razon": "Durante germinación se necesita humedad constante."
    },
    
    # para humedad media, considerando necesidad alta de agua
    {
        "condiciones": ["humedad_media", "necesidad_agua_alta"],
        "conclusion": "regar_ahora",
        "razon": "El cultivo requiere mucha agua, aunque el suelo esté moderadamente húmedo."
    },
    
    # humedad media, sin consideraciones
    {
        "condiciones": ["humedad_media"],
        "conclusion": "mantener_plan_riego",
        "razon": "Humedad moderada, seguir el plan de riego."
    },
    
    # humedad baja baja con temp alta, pero necesidad de agua baja
    {
        "condiciones": ["humedad_baja", "temperatura_alta", "necesidad_agua_baja"],
        "conclusion": "mantener_plan_riego",
        "razon": "Suelo seco y alta temperatura, pero cultivo tolera sequía."
    },

     # humedad baja baja con temp alta
    {
        "condiciones": ["humedad_baja", "temperatura_alta"],
        "conclusion": "regar_ahora",
        "razon": "Suelo seco, alta temperatura y cultivo con necesidad de agua."
    },
   
    # humedad baja con temp media pero necesidad baja de agua
    {
        "condiciones": ["humedad_baja", "temperatura_media", "necesidad_agua_baja"],
        "conclusion": "mantener_plan_riego",
        "razon": "Suelo seco pero cultivo tolera sequía."
    },

     # humedad baja con temp media 
    {
        "condiciones": ["humedad_baja", "temperatura_media"],
        "conclusion": "regar_ahora",
        "razon": "Suelo seco y cultivo con necesidad de agua."
    },
    
    # humedad baja, temperatura baja con necesidad alta de agua
    {
        "condiciones": ["humedad_baja", "temperatura_baja", "necesidad_agua_alta"],
        "conclusion": "regar_ahora",
        "razon": "Suelo seco y cultivo con alta necesidad de agua, aunque la temperatura sea baja."
    },
    
    # humedad baja, temperatura baja, sin otras consideraciones
    {
        "condiciones": ["humedad_baja", "temperatura_baja"],
        "conclusion": "mantener_plan_riego",
        "razon": "Temperatura baja y necesidad de agua media, puede esperar."
    }
]

# reglas para determinar cada cuánto regar los cultivos
# para esto utiliza las etapa de crecimiento, la temperatura, los tipos de suelo y los tipos de riego
reglas_frecuencia = [

    #  etapa de crecimiento: germinación
    {
        "condiciones": ["etapa_germinacion", "temperatura_alta", "suelo_arenoso"],
        "conclusion": "regar_2_vez_al_dia",
        "razon": "El suelo arenoso drena rápidamente el agua y las altas temperaturas incrementan su evaporación: se recomienda regar dos veces al día"
    },
    {
        "condiciones": ["etapa_germinacion", "temperatura_media", "suelo_arenoso"],
        "conclusion": "regar_1_vez_al_dia",
        "razon": "El suelo arenoso retiene poca agua, por lo que conviene regar una vez al día incluso con temperatura media."
    },
    {
        "condiciones": ["etapa_germinacion", "temperatura_alta", "riego_aspersion"],
        "conclusion": "regar_2_vez_al_dia",
        "razon": "El riego por aspersión pierde más agua por evaporación en altas temperaturas; se recomienda regar dos veces al día."
    },
    {
        "condiciones": ["etapa_germinacion", "temperatura_alta"],
        "conclusion": "regar_1_vez_al_dia",
        "razon": "Con temperatura alta y sin pérdidas por aspersión, un riego diario mantiene la humedad necesaria en germinación."
    },
        # para todas las combinaciones que no calzan con las reglas anteriores
    {
        "condiciones": ["etapa_germinacion"],
        "conclusion": "regar_dia_por_medio",
        "razon": "Durante la germinación se requiere mantener una humedad constante, por lo que se recomienda riego frecuente."
    },

    #  etapa de crecimiento: en_crecimiento
    {
        "condiciones": ["etapa_en_crecimiento", "suelo_arenoso"],
        "conclusion": "regar_cada_2_dias",
        "razon": "El suelo arenoso retiene poca humedad; se recomienda regar cada dos días."
    },
    {
        "condiciones": ["etapa_en_crecimiento", "temperatura_alta"],
        "conclusion": "regar_cada_2_dias",
        "razon": "Las altas temperaturas incrementan la evaporación; conviene regar cada dos días."
    },
    {
        "condiciones": ["etapa_en_crecimiento", "temperatura_alta", "riego_aspersion"],
        "conclusion": "regar_dia_por_medio",
        "razon": "La combinación de aspersión y calor acelera la pérdida de agua; se recomienda regar día por medio."
    },
    {
        "condiciones": ["etapa_en_crecimiento", "temperatura_alta", "suelo_arenoso"],
        "conclusion": "regar_dia_por_medio",
        "razon": "Suelo arenoso y alta temperatura reducen la retención de humedad; se aconseja regar día por medio."
    },
    {
        "condiciones": ["etapa_en_crecimiento", "temperatura_media", "suelo_arenoso"],
        "conclusion": "regar_cada_2_dias",
        "razon": "Con suelo arenoso y temperatura media, regar cada dos días mantiene la humedad adecuada."
    },
        # para todas las combinaciones que no calzan con las reglas anteriores
    {
        "condiciones": ["etapa_en_crecimiento"],
        "conclusion": "regar_cada_3_dias",
        "razon": "Durante el crecimiento, las plantas requieren humedad moderada; regar cada tres días es suficiente."
    },

    #  etapa de crecimiento: madurez
    {
        "condiciones": ["etapa_madurez", "temperatura_alta", "riego_aspersion"],
        "conclusion": "regar_cada_2_dias",
        "razon": "Con aspersión y calor, el agua se evapora más rápido; se recomienda regar cada dos días."
    },
    {
        "condiciones": ["etapa_madurez", "temperatura_alta", "suelo_arenoso"],
        "conclusion": "regar_cada_2_dias",
        "razon": "Alta temperatura y suelo arenoso reducen la retención de agua; se recomienda regar cada dos días."
    },
    {
        "condiciones": ["etapa_madurez", "temperatura_media", "suelo_arenoso"],
        "conclusion": "regar_cada_3_dias",
        "razon": "Con suelo arenoso y temperatura media, regar cada tres días mantiene un nivel adecuado de humedad."
    },
    {
        "condiciones": ["etapa_madurez", "suelo_arenoso"],
        "conclusion": "regar_cada_3_dias",
        "razon": "El suelo arenoso se seca más rápido; se ajusta el riego a cada tres días en la etapa de madurez."
    },
    {
        "condiciones": ["etapa_madurez", "temperatura_alta"],
        "conclusion": "regar_cada_3_dias",
        "razon": "Las altas temperaturas incrementan la evaporación; se recomienda aumentar la frecuencia de riego."
    },
        # para todas las combinaciones que no calzan con las reglas anteriores
    {
        "condiciones": ["etapa_madurez"],
        "conclusion": "regar_cada_4_dias",
        "razon": "En madurez, las plantas requieren menos humedad, frecuencia recomendada: cada cuatro días."
    },
]
# reglas base sobre la cantidad de agua
reglas_agua = [
    {"condiciones": ["suelo_arenoso", "humedad_baja"], "conclusion": 25,
     "razon": "Base de riego para suelo arenoso y baja humedad: 25 litro"},
    {"condiciones": ["suelo_arenoso", "humedad_media"], "conclusion": 20,
     "razon": "Base de riego para suelo arenoso y humedad media: 20 litro"},
    {"condiciones": ["suelo_arenoso", "humedad_alta"], "conclusion": 15,
     "razon": "Base de riego para suelo arenoso y alta humedad: 15 litro"},
    {"condiciones": ["suelo_franco", "humedad_baja"], "conclusion": 20,
     "razon": "Base de riego para suelo franco y baja humedad: 20 litro"},
    {"condiciones": ["suelo_franco", "humedad_media"], "conclusion": 20,
     "razon": "Base de riego para suelo franco y humedad media: 20 litro"},
    {"condiciones": ["suelo_franco", "humedad_alta"], "conclusion": 15,
     "razon": "Base de riego para suelo franco y alta humedad: 15 litro"},
    {"condiciones": ["suelo_arcilloso", "humedad_baja"], "conclusion": 20,
     "razon": "Base de riego para suelo arcilloso y baja humedad: 20 litro"},
    {"condiciones": ["suelo_arcilloso", "humedad_media"], "conclusion": 15,
     "razon": "Base de riego para suelo arcilloso y humedad media: 15 litro"},
    {"condiciones": ["suelo_arcilloso", "humedad_alta"], "conclusion": 10,
     "razon": "Base de riego para suelo arcilloso y alta humedad: 10 litro"}
]

# ajustes segun temperatura y tipo de riego
ajuste_agua = {
    "temperatura_media": 0,
    "temperatura_baja": 0,
    "temperatura_alta": 5,
    "riego_aspersion": 5,
    "riego_goteo": 0
}

# metodo utilizado para generar un resumen de las recomendaciones generadas por el sistema
def generar_explicacion(temperatura, humedad, esta_lloviendo, hechos, etapa, necesidad, suelo, tipo_riego):
    explicacion = []

    # reporte temperatura
    if "temperatura_alta" in hechos:
        explicacion.append(f"La temperatura actual es de {temperatura}°C, lo cual es alta. Esto acelera la evaporación del agua.\n")
    elif "temperatura_media" in hechos:
        explicacion.append(f"La temperatura actual es de {temperatura}°C, adecuada para la mayoría de las plantas.\n")
    else:
        explicacion.append(f"La temperatura actual es de {temperatura}°C, baja, por lo que la planta pierde menos agua por evaporación.\n")

    # reporte humedad
    if "humedad_baja" in hechos:
        explicacion.append(f"La humedad del suelo es del {humedad}%, considerada baja. Lo ideal para una planta con necesidad hídrica {necesidad} en etapa de {etapa} es mantenerla sobre el 70%.\n")
    elif "humedad_media" in hechos:
        explicacion.append(f"La humedad del suelo es del {humedad}%, lo cual es moderado. Para una planta con necesidad {necesidad}, se recomienda vigilar que no descienda demasiado.\n")
    else:
        explicacion.append(f"La humedad del suelo es del {humedad}%, considerada alta. No se recomienda regar en este momento.\n")

    #reporte lluvia
    if esta_lloviendo:
        explicacion.append("Está lloviendo actualmente, por lo tanto no es necesario regar manualmente.\n")
    else:
        explicacion.append("No hay lluvia, por lo que el riego dependerá de la humedad y tipo de suelo.\n")

    # reporte suelo
    if "suelo_arenoso" in hechos:
        explicacion.append("El suelo es arenoso, lo que significa que el agua se filtra rápidamente y se debe regar con mayor frecuencia.\n")
    elif "suelo_arcilloso" in hechos:
        explicacion.append("El suelo es arcilloso, retiene más agua, por lo que se puede espaciar más el riego.\n")
    else:
        explicacion.append("El suelo es franco, tiene buen equilibrio entre retención y drenaje de agua.\n")

    # reporte tipo de suelo
    if "riego_aspersion" in hechos:
        explicacion.append("El riego por aspersión es menos eficiente con temperaturas altas por la evaporación.\n")
    elif "riego_goteo" in hechos:
        explicacion.append("El riego por goteo es eficiente y reduce la pérdida de agua en temperaturas altas.\n")

    return "\n".join(explicacion)
