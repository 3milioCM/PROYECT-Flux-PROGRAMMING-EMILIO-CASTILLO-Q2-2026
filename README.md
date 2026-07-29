<div align="center">

# ⚡ FLUX — PRODUCTIVITY INTELLIGENCE
### Automated Sensory Engine & Python CLI Core

[![Python](https://img.shields.io/badge/Python-3.x-8B7FFF?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Production_Ready-4ADE80?style=flat)]()
[![Institution](https://img.shields.io/badge/UPY-Data_%26_AI-FF5A6B?style=flat)]()

*Eliminating decision fatigue through intelligent task automation, absolute path logging, and dynamic sensory mapping.*

</div>

---

## 🚀 Overview

**Flux** is a next-generation productivity intelligence framework built in Python. Designed for high-performance execution, it processes tasks interactively via CLI, automatically evaluates urgency tiers, maps dynamic behavioral weights (haptic volume and warning colors), and ensures complete auditability through robust local logging.

---

## 🛠️ System Architecture & Workflow

```mermaid
flowchart TD
    Start([Inicio: Ejecutar Flux]) --> Input[Ingresar Nombre, Duración y Prioridad]
    Input --> Valide{¿Prioridad válida?}
    
    Valide -- No --> Default[Asignar Prioridad por Defecto: Media]
    Valide -- Sí --> CheckPrio{Evaluar Nivel}
    Default --> CheckPrio
    
    CheckPrio -- Alta --> PrioAlta[Volumen: 100 \n Alerta: Rojo / Urgente]
    CheckPrio -- Media --> PrioMed[Volumen: 60 \n Alerta: Amarillo / Moderado]
    CheckPrio -- Baja --> PrioBaj[Volumen: 30 \n Alerta: Verde / Estable]
    
    PrioAlta --> Log[Registrar Evento en /logs/app.log]
    PrioMed --> Log
    PrioBaj --> Log
    
    Log --> More{¿Agregar otra tarea?}
    More -- Sí --> Input
    More -- No --> Summary[Generar Panel de Resumen Final]
    
    Summary --> End([Fin de Sesión])

    style Start fill:#1A1928,stroke:#8B7FFF,stroke-width:2px,color:#F4F2FF
    style End fill:#1A1928,stroke:#8B7FFF,stroke-width:2px,color:#F4F2FF
    style Input fill:#211F3A,stroke:#8B7FFF,stroke-width:1.5px,color:#F4F2FF
    style Valide fill:#1A1928,stroke:#33324C,stroke-width:1px,color:#F4F2FF
    style Default fill:#1A1928,stroke:#33324C,stroke-width:1px,color:#F4F2FF
    style CheckPrio fill:#1A1928,stroke:#33324C,stroke-width:1px,color:#F4F2FF
    style PrioAlta fill:#3A2029,stroke:#FF5A6B,stroke-width:1.5px,color:#FF5A6B
    style PrioMed fill:#3A2E14,stroke:#FFB454,stroke-width:1.5px,color:#FFB454
    style PrioBaj fill:#1A2E22,stroke:#4ADE80,stroke-width:1.5px,color:#4ADE80
    style Log fill:#211F3A,stroke:#8B7FFF,stroke-width:1.5px,color:#F4F2FF
    style More fill:#1A1928,stroke:#33324C,stroke-width:1px,color:#F4F2FF
    style Summary fill:#1A1928,stroke:#8B7FFF,stroke-width:1.5px,color:#F4F2FF
