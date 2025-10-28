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
