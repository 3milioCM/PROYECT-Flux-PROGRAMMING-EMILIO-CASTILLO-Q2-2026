INICIO

MOSTRAR "--- Flux: Productivity Intelligence ---"

// ENTRADA
LEER task_name
LEER task_duration (convertir a decimal)
LEER priority (convertir a minúsculas)

// PROCESO
SI priority ES IGUAL A "alta" ENTONCES
    alarm_volume = 100
    alert_color = "Red"
SINO
    alarm_volume = 50
    alert_color = "Yellow"
FIN SI

// SALIDA
MOSTRAR "--- Resumen de la Tarea ---"
MOSTRAR "Tarea: " + task_name
MOSTRAR "Volumen de alarma: " + alarm_volume
MOSTRAR "Color de alerta: " + alert_color
MOSTRAR "Estado: Registrada exitosamente en Flux."

FIN 