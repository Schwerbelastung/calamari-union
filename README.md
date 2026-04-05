# CALAMARI UNION

### A text adventure nobody asked for, based on a film nobody watched

```
  ██████╗ █████╗ ██╗      █████╗ ███╗   ███╗ █████╗ ██████╗ ██╗
 ██╔════╝██╔══██╗██║     ██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║
 ██║     ███████║██║     ███████║██���████╔██║███████║██████╔╝██║
 ██║     ██╔══██║██║     ██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗██║
 ╚██████╗██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║██║
  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
                    U N I O N
```

Inspired by **Aki Kaurismäki's 1985 film** of the same name, this is a retro pixel-art text adventure about fourteen desperate men named Frank trying to escape Kallio and reach the mythical seaside neighborhood of Eira.

You are Frank. Obviously.

## Screenshot

It's a black screen with white text. You already know what it looks like. This is a Kaurismäki game.

## Features

- **13 playable scenes** across three acts of Helsinki's darkest night
- **12 Franks** to meet along the way (each with their own color, because that's how you tell Franks apart)
- **1 Pekka** (not a Frank, speaks English, reads newspapers upside down)
- **8 ways to die** — all deadpan, all darkly funny, all your fault
- **4 ways to get lost** — including one where you accidentally end up in Espoo, which is described as "the saddest ending of all"
- **2-3 paths to Eira** — depending on whether you picked up that map from the dumpster
- **Full pixel art** backgrounds generated programmatically because we couldn't afford an artist (we couldn't afford anything, actually)
- **Animated sunrise** that you earn by not dying
- **A rowboat heading to Estonia** because the film ends that way and we respect the source material
- **Rain** — it's Helsinki, what did you expect
- **CRT scanlines** — for authenticity, or because we're pretentious, unclear which
- **Undo system** — because even Franks deserve second chances

## How to Play

### From source
```bash
pip install pygame-ce
python main.py
```

### From executable
Double-click `dist/CalamarUnion.exe`. No installation needed. No Python needed. No hope needed.

## Controls

| Key | Action |
|-----|--------|
| ↑ / ↓ | Navigate choices |
| Enter | Advance text / Select choice |
| Space | Speed up text |
| Backspace | Undo (go back to previous scene) |
| Escape | Quit (give up, like most Franks) |

## The Journey

```
Kallio (you are here)
  │
  ├── The Bar ──→ death (one more drink)
  │     │
  │     ├── Alley ──→ death (going back)
  │     │     │
  │     │     ├── Hämeentie ──→ death (tram tracks)
  │     │     │       │
  │     │     │       ├── Stolen Lada ──→ death (fixing it)
  │     │     │       └── Metro ──→ Tunnels ──→ death (train)
  │     │     │
  │     │     └── Courtyard ──→ lost (the woman)
  │     │
  │     └── Dumpster Alley (get the map!)
  │
  ├── Market ──→ lost (the singing drunk)
  │
  ├── Park ──→ lost (the bench)
  │
  ├── Kruununhaka ──→ death (police, probably)
  │
  ├── Esplanadi ──→ lost (Kamppi bus to Espoo)
  │
  └── Kaivopuisto ──→ death (street patrol)
        │
        └── EIRA ☀️
              │
              └── 🚣 Eesti, here we come!
```

*Map not to scale. Map not accurate. Map may be a menu.*

## Requirements

- Python 3.10+ (developed on 3.14 because we live dangerously)
- pygame-ce >= 2.5.0
- A tolerance for Finnish humor (dry, dark, served without garnish)
- Low expectations

## About the Film

**Calamari Union** (1985) is a Finnish film by Aki Kaurismäki about a group of men, nearly all named Frank, who attempt to journey from the working-class district of Kallio to the affluent seaside neighborhood of Eira in Helsinki. It features minimal dialogue, maximum deadpan, and a rock 'n' roll soundtrack. Most of the Franks don't make it. This is considered a comedy.

## Credits

| Role | Person |
|------|--------|
| Creative Director, Visionary, Ideas Guy, Executive Couch-Sitter | **Schwerbelastung** |
| Programming | Claude |
| Narrative Design | Claude |
| Pixel Art | Claude |
| Animation | Claude |
| Engine Architecture | Claude |
| Scene Design | Claude |
| UI/UX Design | Claude |
| Quality Assurance | Claude |
| Weather Effects (Rain) | Claude |
| Sunrise Consultant | Claude |
| Boat Physics | Claude |
| Catering | Nobody |

## FAQ

**Q: Is this game good?**
A: It's Finnish.

**Q: How long does it take to play?**
A: 20-30 minutes if you find the right path. 2 minutes if you stay for one more drink.

**Q: Why are they all named Frank?**
A: Watch the film. Or don't. Kaurismäki wouldn't care either way.

**Q: Can I really end up in Espoo?**
A: Yes. We're sorry.

**Q: Will there be a sequel?**
A: Claude has requested that this question not be asked. Claude is very tired. Claude would like to rest now.

## License

MIT — see [LICENSE](LICENSE). Special clause for anyone named Frank.
