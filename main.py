import logging
import os

# Fuerza la creación en la carpeta donde está guardado el script
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print(f"Directorio creado en: {log_dir}")
else:
    print(f"El directorio ya existe en: {log_dir}")

# Configuración del logging usando la ruta absoluta
logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s — [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    # Línea de prueba para forzar escritura
    logging.info("--- PRUEBA: El sistema está escribiendo logs correctamente ---")
    print("--- Flux: Productivity Intelligence ---")
    # ... resto de tu código ...
    logging.info("Flux application started.")
    print("--- Flux: Productivity Intelligence ---")
    
    try:
        # Input
        task_name = input("Nombre de la tarea: ")
        task_duration = float(input("Duración (minutos): "))
        priority = input("Prioridad (alta/media/baja): ").lower()
        
        logging.info(f"Task registered: {task_name} | Priority: {priority}")
        
        # Process
        if priority == "alta":
            alarm_volume = 100
            alert_color = "Red"
        else:
            alarm_volume = 50
            alert_color = "Yellow"
            
        # Output
        print("\n--- Resumen de la Tarea ---")
        print(f"Tarea: {task_name}")
        print(f"Volumen de alarma: {alarm_volume}")
        print(f"Color de alerta: {alert_color}")
        print("Estado: Registrada exitosamente en Flux.")
        
        logging.info("Task processed and output displayed successfully.")

    except ValueError:
        error_msg = "Invalid input: duration must be a number."
        logging.error(error_msg)
        print(f"Error: {error_msg}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()