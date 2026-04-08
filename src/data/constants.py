# Display
INTERNAL_WIDTH = 640
INTERNAL_HEIGHT = 360
WINDOW_SCALE = 2
WINDOW_WIDTH = INTERNAL_WIDTH * WINDOW_SCALE
WINDOW_HEIGHT = INTERNAL_HEIGHT * WINDOW_SCALE
FPS = 30
TITLE = "CALAMARI UNION"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (40, 40, 40)
MID_GRAY = (100, 100, 100)
RED = (204, 0, 0)
GOLD = (255, 215, 0)

# Frank colors — each Frank encountered gets a unique color
FRANK_COLORS = {
    "player":   WHITE,
    "frank_2":  (102, 153, 204),  # Steel blue
    "frank_3":  (128, 128, 0),    # Olive
    "frank_4":  (183, 65, 14),    # Rust
    "frank_5":  (150, 111, 214),  # Mauve
    "frank_6":  (0, 153, 136),    # Teal
    "frank_7":  (170, 110, 80),   # Brown
    "frank_8":  (140, 140, 160),  # Slate
    "frank_9":  (100, 160, 100),  # Sage
    "frank_10": (180, 130, 170),  # Dusty pink
    "frank_11": (160, 160, 100),  # Khaki
    "frank_12": (120, 140, 180),  # Faded blue
    "frank_13": (184, 115, 51),   # Copper
    "frank_14": (178, 178, 178),  # Ash
    "frank_15": (128, 0, 32),     # Burgundy
    "frank_16": (80, 120, 60),    # Moss
    "frank_17": (150, 150, 140),  # Pewter
    "frank_18": (200, 160, 60),   # Amber
}
PEKKA_COLOR = GOLD

# Text
TYPEWRITER_SPEED = 35        # ms per character
TYPEWRITER_FAST = 8          # ms per character when holding key
CHOICE_BLINK_SPEED = 500     # ms for choice arrow blink
LINE_SPACING = 6             # extra pixels between lines
TEXT_MARGIN_X = 40
TEXT_MARGIN_TOP = 30
CHOICE_MARGIN_BOTTOM = 40
FONT_SIZE = 16               # main text size
FONT_NAME = "consolas"       # clean, readable, retro feel

# Transitions
FADE_SPEED = 8               # alpha increment per frame for fades
SCENE_PAUSE = 500            # ms pause before choices appear

# Game states
STATE_SPLASH = "splash"
STATE_INTRO = "intro"
STATE_PLAYING = "playing"
STATE_DEATH = "death"
STATE_LOST = "lost"
STATE_VICTORY = "victory"
STATE_CREDITS = "credits"
STATE_QUIT = "quit"
