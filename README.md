# Space Shooter Game

A classic space shooter game built with Python and Pygame. The player controls a spaceship, navigating through space, shooting lasers at meteors while avoiding collisions. The game includes features such as cooldown mechanics for shooting, a dynamic star background, and meteor spawning events.

---

## Features
- **Player Ship Controls**: Use arrow keys to navigate the ship, and spacebar to shoot lasers.
- **Meteor Events**: Randomly spawned meteors fall from the top of the screen.
- **Cooldown Mechanism**: Implemented to prevent continuous laser firing.
- **Collision Detection**: Detects collisions between the player's ship and meteors, as well as lasers hitting meteors.
- **Dynamic Background**: A starry backdrop enhances the gameplay experience.

---

## Requirements
- **Python 3.x**
- **Pygame Library**

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/space-shooter-game.git
    cd space-shooter-game
    ```
2. Install Pygame:
    ```bash
    pip install pygame
    ```

### Directory Structure
- **images/**: Contains image assets for the player, stars, meteors, and lasers.

---

## How to Play
1. **Start the game** by running:
    ```bash
    python main.py
    ```
2. **Controls**:
   - **Arrow Keys**: Move the player ship up, down, left, or right.
   - **Spacebar**: Shoot lasers (with a cooldown of 400ms).
3. **Objective**: Shoot down as many meteors as possible without colliding with them.

---

## Code Overview

### `Player` Class
Manages the player's ship, controls movement and shooting with a cooldown system.

### `Laser` Class
Handles the laser projectiles, which are fired by the player. Lasers disappear if they move out of the screen or hit meteors.

### `Meteor` Class
Creates meteors that fall from random positions at the top of the screen, with a set lifetime.

### `Star` Class
Generates background stars for a dynamic space effect.

### `collisions()` Function
Detects and handles collisions between the player, lasers, and meteors.

---

## Game Settings
- **Window Size**: 1280 x 720 pixels.
- **Meteor Spawn Rate**: Every 500 milliseconds.

---

## Credits
- Built with **Python** and **Pygame**.
- Game assets and fonts are located in the **images** folder. 


Enjoy your space adventure! 🚀
