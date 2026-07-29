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
# Flux: Productivity Intelligence

Flux is an intelligent academic task management system. Every task gets a
priority level, and Flux automatically assigns it an alarm volume and an
alert color — no manual configuration needed.

| Priority       | Alarm volume | Alert color |
|----------------|:------------:|:-----------:|
| High (alta)    | 100          | Red         |
| Medium / Low   | 50           | Yellow      |

This is a real, runnable desktop app (not just a mockup) built with
`tkinter`, so it works with just a standard Python install — no extra
packages to download.

## Requirements

- Python 3.8 or newer
- `tkinter` (included with most Python installs)

If you're on Debian/Ubuntu and get a `No module named 'tkinter'` error:

```bash
sudo apt install python3-tk
```

On Windows and macOS, tkinter is bundled with the official Python installer
from [python.org](https://www.python.org/downloads/), so no extra step is
usually needed.

## Run it

```bash
git clone https://github.com/your-username/flux.git
cd flux
python3 main.py
```

## What it does

- **Home screen** — shows every registered task with a color-coded
  priority badge.
- **New task** — enter a name, a duration in minutes, and pick a priority.
- **Confirmation** — Flux shows the assigned alarm volume and alert color
  for the task you just registered.

## Project structure

```
main.py        Full application: UI, task logic, persistence, logging.
data/          tasks.json — where your registered tasks are saved between runs.
logs/          app.log — a timestamped record of every action, generated automatically.
```

Both `data/` and `logs/` are created automatically the first time you run
the app.

## About

Proposed by **Emilio Eduardo Castillo Manzano**
Universidad Politécnica de Yucatán

