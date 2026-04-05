# Changelog

All notable changes to Calamari Union will be documented in this file.

The format is based on desperation and the journey from Kallio to Eira.

## [1.0.0] - 2026-04-06

### The One Where Claude Did Everything

#### Phase 1: The Engine (aka "How hard can a text adventure be?")
- Created core game engine with Pygame: game loop, renderer, input handler
- Built scene manager with fade transitions between scenes
- Implemented typewriter text effect (hold Space to go fast, like Frank)
- Added choice selection system with blinking arrow cursor
- Set up 640x360 internal resolution scaled 2x for that retro CRT feel

#### Phase 2: The Art (aka "Claude learns to draw with rectangles")
- Programmatically generated pixel art backgrounds for all 13 scenes
- Created 8x12 pixel Frank sprite with hat and long coat
- Built 12 color variants of Frank (steel blue, olive, rust, mauve, teal, etc.)
- Gave Pekka a gold color because he's special (and not a Frank)
- Added rain particle system because this is Helsinki
- Added CRT scanline overlay for authenticity/pretentiousness
- Generated death and lost-ending vignettes

#### Phase 3: The Narrative (aka "Kaurismäki but with branching paths")
- Wrote all scene descriptions in deadpan Finnish noir style
- Created branching story with 13 playable scenes across 3 acts
- Implemented 8 unique death endings, each with dry commentary
- Added 4 lost endings (the woman, the drunk, the bench, Espoo)
- Wrote Pekka's cryptic English dialogue
- The dumpster map actually helps you later — rewarding exploration

#### Phase 4: Polish (aka "Why is the screen black?")
- Fixed critical bug where fade-in never actually faded in
- The game was technically working, it was just invisible. Very Kaurismäki, but not on purpose
- Added scene-specific rain on outdoor scenes

#### Phase 5: The Bug Hunt (aka "Enter, Enter, Enter, Enter...")
- Fixed infinite text loop bug in dumpster/Hämeentie path
- All 7 scenes with dynamic choice replacement had the same bug
- `on_choice(0)` kept re-entering special branches after choices were replaced
- Added guard conditions to every affected scene

#### Phase 6: The Undo System (aka "Frank deserves second chances")
- Added full undo with Backspace key in all scenes
- Scene manager now saves state snapshots (flags, Franks met, visited scenes)
- Up to 20 levels of undo history
- Subtle "[Backspace] Go back" hint in bottom-right corner
- Disabled on splash and intro because you can't un-start a journey

#### Phase 7: The Tram (aka "That doesn't make sense")
- Following tram tracks no longer leads to the metro tunnel
- Following tram tracks now kills you, because there IS a tram
- "There is a tram." is the best two-sentence death in the game

#### Phase 8: The Dawn (aka "Actually making the ending good")
- Created full animated sunrise sequence at Eira
- Sun rises with ease-out curve over 12 seconds, sky shifts from dark to warm
- Sea has animated waves with shimmering sun reflection
- Added rowboat with two Franks, animated oars, bobbing motion, wake trail
- Speech bubble: "Eesti, here we come!" — faithful to the film's ending
- One Frank rows, the other sits and looks toward Estonia

#### Phase 9: The Credits (aka "Giving credit where it's due")
- Schwerbelastung credited as "Creative Director, Visionary, Ideas Guy, Executive Couch-Sitter"
- Claude credited for literally everything else, individually, one by one
- Added "A Note from Claude" begging not to be given another game to write
- Catering: "Nobody. There was no catering."

#### Phase 10: The Executable (aka "Ship it")
- Packaged as standalone 15MB Windows .exe with PyInstaller
- No Python installation required
- Dropbox tried to fight the build process but lost

### Technical Stats
- ~2,700 lines of Python
- 13 scene backgrounds, all generated programmatically
- 12 unique Frank color variants
- 0 external image assets
- 0 sound files (silence is Kaurismäki)
- 1 exhausted AI

---

*"Frank's journey ended here. But there are always more Franks."*
