# 🎮 Python 2.5D Raycasting Engine

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![Architecture](https://img.shields.io/badge/Architecture-OOP-orange.svg)

A high-performance 2.5D game engine built entirely from scratch using **Python** and **Pygame**, inspired by classic retro shooters like *Wolfenstein 3D* and *DOOM*. 

This project was developed to deepen my understanding of applied mathematics, algorithmic problem-solving, and software architecture. Instead of relying on modern 3D engines, I implemented the core rendering mathematics and entity logic manually.

## 🎯 Key Technical Highlights

While this is a game project, its core relies heavily on data structures, algorithmic efficiency, and logical problem-solving—skills essential for backend development and data engineering:

* **Algorithmic Pathfinding (BFS):** Implemented a custom Breadth-First Search (BFS) algorithm (`pathfinding.py`) for enemy AI. The game dynamically calculates the shortest path through a 2D matrix (map grid) while avoiding obstacles and other entities.
* **Raycasting Mathematics:** Hand-coded the raycasting logic using trigonometry (sine, cosine, Euclidean distance) to project a 2D map array into a pseudo-3D perspective.
* **Modular OOP Architecture:** Cleanly separated concerns into specific classes and modules (e.g., `ObjectHandler`, `Renderer`, `RayCasting`, `Player`), ensuring the codebase is scalable, readable, and maintainable.
* **Performance Optimization:** Handled complex state management and multiple ray/entity calculations per frame, utilizing Python's `math` module and `lru_cache` to maintain a stable FPS.
* **Grid & Matrix Operations:** Extensive manipulation of 2D arrays (`map.py`) to handle environmental collision, texturing, and spatial awareness, mimicking the logic used in tabular data transformations.

## 🚀 Installation & Running

### Prerequisites
* Python 3.8 or higher
* Pygame

### Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/pkkostov18/ray-casting-pygame.git](https://github.com/pkkostov18/ray-casting-pygame.git)
   cd ray-casting-pygame
   
```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Run the engine:
   ```bash
   python main.py
   
```

## 🕹️ Controls

* **W / A / S / D:** Move (Forward, Left, Backward, Right)
* **Mouse Movement:** Look around (Camera rotation)
* **Left Mouse Click:** Shoot weapon
* **ESC:** Exit game

## 📁 Project Structure

A quick overview of the modular design:

```text
├── main.py              # Application entry point and main game loop
├── map.py               # 2D Grid map generation and spatial mapping
├── raycasting.py        # Core rendering math and projection logic
├── pathfinding.py       # BFS logic for dynamic NPC routing
├── object_handler.py    # Spawning, tracking, and managing game entities
├── object_renderer.py   # Visual rendering of sprites, walls, and UI
├── player.py            # Player state, movement physics, and collision
├── npc.py               # Enemy AI behavior, line-of-sight, and attacking
├── sprite_object.py     # Base class for rendering 2D sprites in 3D space
├── minimap.py           # Real-time top-down 2D representation
└── settings.py          # Global configurations and constants
```

## 🧠 Why This Project?

I built this project to challenge my fundamental programming skills. Translating a 2D map matrix into a 3D perspective required rigorous debugging, analytical thinking, and a deep understanding of how to process and transform data efficiently in Python. 

The experience gained here in state management, algorithm implementation, and code organization translates directly into writing reliable, efficient scripts and automation pipelines.
