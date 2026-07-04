def main():
    print("--- Flux: Productivity Intelligence ---")
    
    # Input (Lo que definiste en tu IPO)
    task_name = input("Nombre de la tarea: ")
    task_duration = float(input("Duración (minutos): "))
    priority = input("Prioridad (alta/media/baja): ").lower()
    
    # Process (Lógica basada en tu diseño)
    # Definimos umbrales de alerta y color
    if priority == "alta":
        alarm_volume = 100
        alert_color = "Red"
    else:
        alarm_volume = 50
        alert_color = "Yellow"
        
    # Output (Lo que tu diseño indica mostrar)
    print("\n--- Resumen de la Tarea ---")
    print(f"Tarea: {task_name}")
    print(f"Volumen de alarma: {alarm_volume}")
    print(f"Color de alerta: {alert_color}")
    print("Estado: Registrada exitosamente en Flux.")

if __name__ == "__main__":
    main() 