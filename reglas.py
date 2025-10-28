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
