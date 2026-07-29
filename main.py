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
    logging.info("Flux application started.")
    print("\n" + "="*40)
    print("   FLUX: PRODUCTIVITY INTELLIGENCE")
    print("="*40)
    
    tasks_list = []
    
    try:
        # Permitir registrar múltiples tareas en una sesión
        while True:
            print("\n--- Registrar Nueva Tarea ---")
            task_name = input("Nombre de la tarea (o escribe 'salir' para terminar): ").strip()
            
            if task_name.lower() == 'salir':
                break
                
            if not task_name:
                print("El nombre de la tarea no puede estar vacío.")
                continue
                
            task_duration = float(input("Duración (minutos): "))
            
            print("Niveles de prioridad: alta, media, baja")
            priority = input("Prioridad: ").lower().strip()
            
            if priority not in ["alta", "media", "baja"]:
                print("Prioridad no válida. Se asignará 'media' por defecto.")
                priority = "media"
            
            # Lógica del motor de alertas de Flux
            if priority == "alta":
                alarm_volume = 100
                alert_color = "Red"
            elif priority == "media":
                alarm_volume = 60
                alert_color = "Yellow"
            else: # baja
                alarm_volume = 30
                alert_color = "Green"
                
            # Guardar la tarea en la lista de la sesión
            task_data = {
                "name": task_name,
                "duration": task_duration,
                "priority": priority,
                "volume": alarm_volume,
                "color": alert_color
            }
            tasks_list.append(task_data)
            
            logging.info(f"Task registered: {task_name} | Duration: {task_duration}m | Priority: {priority} | Volume: {alarm_volume} | Color: {alert_color}")
            
            print(f"\n[Éxito] Tarea '{task_name}' registrada correctamente en Flux.")
            
            continuar = input("\n¿Deseas agregar otra tarea? (s/n): ").lower()
            if continuar != 's':
                break

        # Panel de Resumen Final (Simulando la vista de estadísticas de la app)
        print("\n" + "="*40)
        print("         RESUMEN DE PRODUCTIVIDAD")
        print("="*40)
        print(f"Total de tareas registradas: {len(tasks_list)}")
        
        high_priority_count = sum(1 for t in tasks_list if t['priority'] == 'alta')
        print(f"Tareas de alta prioridad: {high_priority_count}")
        print("-" * 40)
        
        for i, t in enumerate(tasks_list, 1):
            print(f"\n[Tarea {i}]")
            print(f"  • Nombre: {t['name']}")
            print(f"  • Duración: {t['duration']} min")
            print(f"  • Prioridad: {t['priority'].upper()}")
            print(f"  • Volumen de Alarma: {t['volume']}")
            print(f"  • Color de Alerta: {t['color']}")
            
        print("\n" + "="*40)
        print("Estado: Sesión finalizada y guardada exitosamente en logs.")
        print("="*40)
        
        logging.info(f"Session ended. Total tasks processed: {len(tasks_list)}")

    except ValueError:
        error_msg = "Invalid input: duration must be a valid number."
        logging.error(error_msg)
        print(f"\n[Error]: {error_msg}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"\n[Error inesperado]: {e}")

if __name__ == "__main__":
    main()