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
