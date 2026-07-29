INICIO Programa Flux

    // 1. Configuración inicial del entorno y sistema de logs
    Definir ruta_base como Directorio Actual del Script
    Definir ruta_logs como ruta_base + '/logs'
    
    SI la carpeta ruta_logs NO existe ENTONCES
        Crear carpeta ruta_logs
    FIN SI

    Configurar Sistema de Logging con archivo: ruta_logs/app.log
    Registrar en log: "Flux application started."

    // 2. Función principal del sistema
    Funcion Principal:
        Imprimir Encabezado "FLUX: PRODUCTIVITY INTELLIGENCE"
        Crear lista vacía: lista_tareas
        
        INTENTAR:
            // Bucle interactivo principal
            MIENTRAS VERDADERO:
                Imprimir "--- Registrar Nueva Tarea ---"
                Leer nombre_tarea
                
                SI nombre_tarea == 'salir' ENTONCES
                    Romper bucle
                FIN SI
                
                SI nombre_tarea está vacío ENTONCES
                    Mostrar error y continuar bucle
                FIN SI
                
                Leer duracion (convertir a número decimal)
                Leer prioridad (convertir a minúsculas: 'alta', 'media', 'baja')
                
                // Validación y respaldo (Fallback)
                SI prioridad NO ESTÁ en ["alta", "media", "baja"] ENTONCES
                    prioridad = "media"
                FIN SI
                
                // Motor de asignación sensorial automática
                SI prioridad == "alta" ENTONCES
                    volumen_alarma = 100
                    color_alerta = "Red"
                SINO SI prioridad == "media" ENTONCES
                    volumen_alarma = 60
                    color_alerta = "Yellow"
                SINO (baja)
                    volumen_alarma = 30
                    color_alerta = "Green"
                FIN SI
                
                // Estructurar datos de la tarea
                Crear objeto tarea_datos con:
                    - nombre: nombre_tarea
                    - duracion: duracion
                    - prioridad: prioridad
                    - volumen: volumen_alarma
                    - color: color_alerta
                    
                Agregar tarea_datos a lista_tareas
                
                Registrar en log: "Task registered: [nombre_tarea] | Priority: [prioridad]"
                Imprimir "[Éxito] Tarea registrada correctamente."
                
                Preguntar: ¿Deseas agregar otra tarea? (s/n)
                SI respuesta != 's' ENTONCES
                    Romper bucle
                FIN SI
            FIN MIENTRAS

            // 3. Panel de Resumen Final de Sesión
            Imprimir "========= RESUMEN DE PRODUCTIVIDAD ========="
            Imprimir Total de tareas en lista_tareas
            Imprimir Conteo de tareas con prioridad 'alta'
            
            PARA CADA tarea en lista_tareas HACER
                Imprimir detalles de la tarea (Nombre, Duración, Prioridad, Volumen, Color)
            FIN PARA
            
            Registrar en log: "Session ended. Total tasks processed: [Total]"

        CAPTURAR Error de Valor (ValueError):
            Registrar en log: "Invalid input: duration must be a number."
            Imprimir "[Error]: La duración debe ser un número válido."
            
        CAPTURAR Cualquier otro Error (Exception as e):
            Registrar en log: "Unexpected error: [e]"
            Imprimir "[Error inesperado]: [e]"

    FIN Función Principal

SI se ejecuta directamente ENTONCES
    Llamar Función Principal
FIN SI

FIN Programa Flux