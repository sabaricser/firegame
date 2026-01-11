# 🚀 Cosmic Heat - Enhanced Edition

A visually stunning space shooter game built with Pygame, featuring advanced particle effects, parallax backgrounds, and dynamic gameplay.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pygame](https://img.shields.io/badge/Pygame--CE-2.5.6-green)

## ✨ Features

### Visual Enhancements
- **Particle System**: Dynamic explosion bursts and engine trails
- **Parallax Star Fields**: Multi-layered background for depth perception
- **Ship Banking**: Realistic tilting animations during movement
- **Bullet Glow**: Energy effects for projectiles
- **Screen Shake**: Impact feedback for collisions and explosions

### Gameplay
- Multiple enemy types with unique behaviors
- Epic boss battles with health bars
- Power-ups: Health refills, bullet refills, and combo pickups
- Progressive difficulty with changing backgrounds
- Score tracking with high score system

## 🎮 How to Play

### Local Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sabaricser/firegame.git
   cd firegame
   ```

2. **Install dependencies**:
   ```bash
   pip install pygame-ce
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

### Controls
- **Arrow Keys**: Move your ship
- **Space**: Shoot
- **P**: Pause
- **ESC**: Exit

## 🛠️ Technical Details

- **Engine**: Pygame-CE (Community Edition)
- **Python Version**: 3.14+
- **Async Support**: Web-ready with asyncio integration

## 📁 Project Structure

```
firegame/
├── main.py              # Main game loop
├── classes/
│   ├── player.py        # Player ship with banking animations
│   ├── bullets.py       # Projectile system with glow effects
│   ├── particles.py     # Particle system for visual effects
│   ├── enemies.py       # Enemy AI and behaviors
│   ├── bosses.py        # Boss battle mechanics
│   ├── explosions.py    # Explosion animations
│   └── meteors.py       # Obstacle mechanics
├── images/              # Game sprites and backgrounds
├── game_sounds/         # Sound effects and music
└── README.md
```

## 🎨 Visual Effects Showcase

The game features:
- 100+ parallax stars moving at different speeds
- Particle bursts with up to 100 particles per explosion
- Dynamic screen shake (intensity varies by impact)
- Smooth 60 FPS gameplay

## 🚀 Future Enhancements

- [ ] Web deployment via Pygbag
- [ ] Additional boss types
- [ ] Multiplayer support
- [ ] Leaderboard system

## 📝 License

This project is based on [Cosmic Heat](https://github.com/Dave-YP/cosmic-heat-pygame) with significant visual and gameplay enhancements.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

**Enjoy the game!** 🎮✨
