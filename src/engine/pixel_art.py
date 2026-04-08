"""
Programmatic pixel art generator for scenes and sprites.
Generates all art at runtime — no external image files needed.
"""
import pygame
import random
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT, BLACK, WHITE, DARK_GRAY


def create_surface(w=INTERNAL_WIDTH, h=INTERNAL_HEIGHT):
    s = pygame.Surface((w, h))
    s.fill(BLACK)
    return s


# --- Character sprites ---

def generate_frank_sprite(color=WHITE, scale=2):
    """Generate a simple 8x12 pixel Frank sprite (man in coat)."""
    # 8x12 pixel art of a man in a long coat and hat
    template = [
        "..XXXX..",
        "..XXXX..",
        ".XXXXXX.",
        "..XXXX..",
        ".XXXXXX.",
        "XXXXXXXX",
        ".XXXXXX.",
        ".XXXXXX.",
        ".XXXXXX.",
        "..X..X..",
        "..X..X..",
        "..XX.XX.",
    ]
    w, h = 8, 12
    surf = pygame.Surface((w * scale, h * scale), pygame.SRCALPHA)
    hat_color = tuple(max(0, c - 60) for c in color[:3])
    coat_color = tuple(max(0, c - 30) for c in color[:3])
    for row_i, row in enumerate(template):
        for col_i, ch in enumerate(row):
            if ch == "X":
                if row_i < 2:
                    c = hat_color
                elif row_i < 4:
                    c = color
                else:
                    c = coat_color
                pygame.draw.rect(surf, c,
                                 (col_i * scale, row_i * scale, scale, scale))
    return surf


def generate_frank_walk_frames(color=WHITE, scale=2, num_frames=4):
    """Generate walk cycle frames for Frank."""
    base = [
        "..XXXX..",
        "..XXXX..",
        ".XXXXXX.",
        "..XXXX..",
        ".XXXXXX.",
        "XXXXXXXX",
        ".XXXXXX.",
        ".XXXXXX.",
        ".XXXXXX.",
    ]
    legs = [
        ["..X..X..", "..X..X..", ".XX..XX."],
        [".X....X.", ".X....X.", "XX....XX"],
        ["..X..X..", "...XX...", "..XXXX.."],
        ["....XX..", "...XX...", "..XX...."],
    ]
    frames = []
    w, h = 8, 12
    hat_color = tuple(max(0, c - 60) for c in color[:3])
    coat_color = tuple(max(0, c - 30) for c in color[:3])
    for leg_frame in legs:
        template = base + leg_frame
        surf = pygame.Surface((w * scale, h * scale), pygame.SRCALPHA)
        for row_i, row in enumerate(template):
            for col_i, ch in enumerate(row):
                if ch == "X":
                    if row_i < 2:
                        c = hat_color
                    elif row_i < 4:
                        c = color
                    else:
                        c = coat_color
                    pygame.draw.rect(surf, c,
                                     (col_i * scale, row_i * scale, scale, scale))
        frames.append(surf)
    return frames


def generate_frank_death_frames(color=WHITE, scale=2):
    """Generate death animation — Frank falls over."""
    stages = [
        [  # standing
            "..XXXX..", "..XXXX..", ".XXXXXX.", "..XXXX..",
            ".XXXXXX.", "XXXXXXXX", ".XXXXXX.", ".XXXXXX.",
            ".XXXXXX.", "..X..X..", "..X..X..", "..XX.XX.",
        ],
        [  # leaning
            "...XXXX.", "...XXXX.", "..XXXXXX", "...XXXX.",
            "..XXXXXX", ".XXXXXXX", "..XXXXXX", "..XXXXXX",
            "..XXXXXX", "...X..X.", "...X..X.", "...XX.XX",
        ],
        [  # falling
            "........", "....XXXX", "....XXXX", "...XXXXX",
            "..XXXXXX", ".XXXXXXX", "..XXXXXX", "..XXXXXX",
            "..XXXXXX", "..XXXXXX", "........", "........",
        ],
        [  # on ground
            "........", "........", "........", "........",
            "........", "........", "........", "XXXXXXXX",
            "XXXXXXXX", "XXXXXXXX", "XXXX.XXX", "........",
        ],
    ]
    frames = []
    w, h = 8, 12
    for template in stages:
        surf = pygame.Surface((w * scale, h * scale), pygame.SRCALPHA)
        for row_i, row in enumerate(template):
            for col_i, ch in enumerate(row):
                if ch == "X":
                    c = tuple(max(0, v - 30) for v in color[:3])
                    pygame.draw.rect(surf, c,
                                     (col_i * scale, row_i * scale, scale, scale))
        frames.append(surf)
    return frames


# --- Scene backgrounds ---

def generate_bar_scene():
    """Smoky bar in Kallio."""
    s = create_surface()
    # Floor
    pygame.draw.rect(s, (30, 25, 20), (0, 260, INTERNAL_WIDTH, 100))
    # Bar counter
    pygame.draw.rect(s, (60, 40, 25), (0, 200, INTERNAL_WIDTH, 60))
    pygame.draw.rect(s, (80, 55, 35), (0, 195, INTERNAL_WIDTH, 8))
    # Bottles on shelf
    for i in range(12):
        x = 50 + i * 48
        h = random.randint(20, 35)
        color = random.choice([(60, 80, 60), (80, 60, 40), (40, 50, 70), (90, 70, 50)])
        pygame.draw.rect(s, color, (x, 160 - h, 12, h))
    # Dim ceiling light
    pygame.draw.circle(s, (50, 45, 30), (320, 10), 80)
    pygame.draw.circle(s, (70, 60, 40), (320, 10), 40)
    # Smoke haze (semi-transparent overlay)
    haze = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
    for _ in range(60):
        x = random.randint(0, INTERNAL_WIDTH)
        y = random.randint(40, 200)
        r = random.randint(20, 60)
        pygame.draw.circle(haze, (80, 80, 90, 15), (x, y), r)
    s.blit(haze, (0, 0))
    # Stools
    for x in [100, 220, 340, 460]:
        pygame.draw.rect(s, (50, 35, 25), (x, 250, 8, 30))
        pygame.draw.rect(s, (50, 35, 25), (x + 20, 250, 8, 30))
        pygame.draw.rect(s, (65, 45, 30), (x - 2, 240, 32, 12))
    return s


def generate_alley_scene():
    """Dark alley behind apartment blocks."""
    s = create_surface()
    # Buildings on both sides
    pygame.draw.rect(s, (25, 25, 30), (0, 0, 150, 300))
    pygame.draw.rect(s, (20, 22, 28), (490, 0, 150, 300))
    # Windows (some lit)
    for bx in [0, 490]:
        for wy in range(30, 280, 50):
            for wx in range(bx + 20, bx + 130, 40):
                if random.random() < 0.2:
                    pygame.draw.rect(s, (60, 55, 30), (wx, wy, 15, 20))
                else:
                    pygame.draw.rect(s, (15, 15, 20), (wx, wy, 15, 20))
    # Ground
    pygame.draw.rect(s, (20, 20, 22), (0, 300, INTERNAL_WIDTH, 60))
    # Puddle reflections
    for _ in range(3):
        px = random.randint(180, 460)
        pw = random.randint(30, 80)
        pygame.draw.ellipse(s, (15, 18, 25), (px, 310, pw, 8))
    # Dumpster
    pygame.draw.rect(s, (35, 40, 35), (200, 270, 50, 35))
    pygame.draw.rect(s, (40, 45, 40), (198, 265, 54, 8))
    return s


def generate_dumpster_alley_scene():
    """Alternative alley with prominent dumpsters."""
    s = generate_alley_scene()
    # Extra dumpsters
    pygame.draw.rect(s, (35, 40, 35), (350, 270, 50, 35))
    pygame.draw.rect(s, (40, 45, 40), (348, 265, 54, 8))
    pygame.draw.rect(s, (30, 35, 30), (420, 275, 45, 30))
    # Scattered trash
    for _ in range(15):
        x = random.randint(160, 500)
        y = random.randint(300, 340)
        pygame.draw.rect(s, (40, 38, 35), (x, y, 3, 3))
    return s


def generate_hameentie_scene():
    """Wide dark boulevard with tram tracks."""
    s = create_surface()
    # Sky hint
    pygame.draw.rect(s, (8, 10, 18), (0, 0, INTERNAL_WIDTH, 120))
    # Buildings far side
    for i in range(8):
        bx = i * 80
        bh = random.randint(100, 180)
        pygame.draw.rect(s, (18, 20, 25), (bx, 120 - bh + 100, 75, bh))
        # Windows
        for wy in range(120 - bh + 110, 220, 20):
            for wx in range(bx + 8, bx + 68, 18):
                if random.random() < 0.15:
                    pygame.draw.rect(s, (50, 45, 25), (wx, wy, 8, 10))
    # Road
    pygame.draw.rect(s, (25, 25, 27), (0, 220, INTERNAL_WIDTH, 140))
    # Tram tracks
    for ty in [270, 275, 310, 315]:
        pygame.draw.line(s, (40, 40, 45), (0, ty), (INTERNAL_WIDTH, ty), 1)
    # Streetlight
    pygame.draw.rect(s, (50, 50, 55), (500, 140, 4, 100))
    pygame.draw.circle(s, (70, 65, 40), (502, 138), 12)
    pygame.draw.circle(s, (50, 48, 30), (502, 138), 20)
    return s


def generate_courtyard_scene():
    """Quiet residential courtyard."""
    s = create_surface()
    # Walls surrounding
    pygame.draw.rect(s, (28, 26, 30), (0, 50, INTERNAL_WIDTH, 250))
    # Central open area
    pygame.draw.rect(s, (12, 14, 16), (80, 80, 480, 200))
    # Ground
    pygame.draw.rect(s, (22, 22, 20), (80, 280, 480, 80))
    # Windows — one lit (the woman's window)
    for side_x in [10, 570]:
        for wy in range(80, 260, 40):
            pygame.draw.rect(s, (15, 15, 20), (side_x, wy, 20, 25))
    # The lit window
    pygame.draw.rect(s, (80, 70, 40), (570, 120, 20, 25))
    pygame.draw.rect(s, (100, 85, 50), (572, 122, 16, 21))
    # Laundry lines
    pygame.draw.line(s, (40, 40, 45), (100, 130), (540, 125), 1)
    pygame.draw.line(s, (40, 40, 45), (120, 170), (520, 168), 1)
    # Clothes on line
    for lx in range(150, 500, 60):
        c = random.choice([(50, 50, 55), (45, 40, 50), (55, 50, 45)])
        pygame.draw.rect(s, c, (lx, 125, 12, 15))
    # Fence at bottom
    for fx in range(80, 560, 12):
        pygame.draw.rect(s, (35, 35, 30), (fx, 275, 3, 25))
    pygame.draw.line(s, (35, 35, 30), (80, 280), (560, 280), 1)
    return s


def generate_car_scene():
    """Inside/beside a stolen car at night."""
    s = create_surface()
    # Street
    pygame.draw.rect(s, (22, 22, 24), (0, 250, INTERNAL_WIDTH, 110))
    # Car body
    pygame.draw.rect(s, (35, 35, 45), (120, 200, 300, 70))
    pygame.draw.rect(s, (30, 30, 40), (150, 170, 220, 35))
    # Windshield
    pygame.draw.rect(s, (15, 20, 30), (165, 175, 90, 25))
    # Rear window
    pygame.draw.rect(s, (15, 20, 30), (290, 175, 70, 25))
    # Wheels
    pygame.draw.circle(s, (20, 20, 20), (180, 270), 15)
    pygame.draw.circle(s, (20, 20, 20), (370, 270), 15)
    # Headlights
    pygame.draw.rect(s, (60, 55, 30), (120, 220, 10, 8))
    # Light beam
    beam = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
    pygame.draw.polygon(beam, (40, 38, 20, 15),
                        [(120, 224), (0, 200), (0, 260)])
    s.blit(beam, (0, 0))
    return s


def generate_metro_scene():
    """Empty metro station — fluorescent lights buzzing."""
    s = create_surface()
    # Ceiling
    pygame.draw.rect(s, (30, 30, 35), (0, 0, INTERNAL_WIDTH, 80))
    # Fluorescent lights
    for lx in range(60, INTERNAL_WIDTH, 120):
        pygame.draw.rect(s, (70, 75, 65), (lx, 75, 60, 4))
        # Light glow
        glow = pygame.Surface((100, 40), pygame.SRCALPHA)
        pygame.draw.ellipse(glow, (50, 55, 45, 20), (0, 0, 100, 40))
        s.blit(glow, (lx - 20, 60))
    # Walls
    pygame.draw.rect(s, (35, 35, 40), (0, 80, INTERNAL_WIDTH, 140))
    # Tile pattern
    for ty in range(85, 220, 15):
        pygame.draw.line(s, (30, 30, 35), (0, ty), (INTERNAL_WIDTH, ty), 1)
    # Platform
    pygame.draw.rect(s, (25, 25, 28), (0, 220, INTERNAL_WIDTH, 20))
    pygame.draw.line(s, (50, 50, 20), (0, 218), (INTERNAL_WIDTH, 218), 2)
    # Track area (dark pit)
    pygame.draw.rect(s, (5, 5, 8), (0, 240, INTERNAL_WIDTH, 60))
    # Rails
    pygame.draw.line(s, (50, 50, 55), (0, 280), (INTERNAL_WIDTH, 280), 2)
    pygame.draw.line(s, (50, 50, 55), (0, 290), (INTERNAL_WIDTH, 290), 2)
    # Floor
    pygame.draw.rect(s, (28, 28, 30), (0, 300, INTERNAL_WIDTH, 60))
    # Bench
    pygame.draw.rect(s, (40, 35, 30), (250, 290, 80, 8))
    pygame.draw.rect(s, (40, 35, 30), (255, 298, 4, 15))
    pygame.draw.rect(s, (40, 35, 30), (321, 298, 4, 15))
    return s


def generate_tunnel_scene():
    """Dark subway tunnel — minimal visibility."""
    s = create_surface()
    # Tunnel walls (converging perspective)
    pygame.draw.polygon(s, (18, 18, 22),
                        [(0, 0), (200, 100), (200, 260), (0, 360)])
    pygame.draw.polygon(s, (18, 18, 22),
                        [(640, 0), (440, 100), (440, 260), (640, 360)])
    # Tunnel ceiling
    pygame.draw.polygon(s, (15, 15, 18),
                        [(0, 0), (640, 0), (440, 100), (200, 100)])
    # Tunnel floor
    pygame.draw.polygon(s, (12, 12, 14),
                        [(0, 360), (640, 360), (440, 260), (200, 260)])
    # Rails (perspective)
    pygame.draw.line(s, (35, 35, 40), (100, 360), (280, 180), 1)
    pygame.draw.line(s, (35, 35, 40), (540, 360), (360, 180), 1)
    # Distant light
    pygame.draw.circle(s, (20, 22, 18), (320, 180), 30)
    pygame.draw.circle(s, (30, 32, 25), (320, 180), 10)
    # Dripping water effect (static drops)
    for _ in range(8):
        dx = random.randint(220, 420)
        dy = random.randint(110, 250)
        pygame.draw.line(s, (25, 30, 40), (dx, dy), (dx, dy + 5), 1)
    return s


def generate_market_scene():
    """Hakaniemi market at night — stalls shuttered."""
    s = create_surface()
    # Sky
    pygame.draw.rect(s, (8, 10, 18), (0, 0, INTERNAL_WIDTH, 100))
    # Market hall in background
    pygame.draw.rect(s, (30, 28, 25), (100, 60, 440, 120))
    pygame.draw.polygon(s, (35, 32, 28),
                        [(100, 60), (320, 30), (540, 60)])
    # Shuttered stalls
    for sx in range(40, INTERNAL_WIDTH - 40, 90):
        pygame.draw.rect(s, (25, 25, 28), (sx, 200, 70, 60))
        # Shutters (horizontal lines)
        for sy in range(200, 260, 5):
            pygame.draw.line(s, (30, 30, 33), (sx, sy), (sx + 70, sy), 1)
    # Ground
    pygame.draw.rect(s, (18, 18, 20), (0, 260, INTERNAL_WIDTH, 100))
    # Cobblestones
    for _ in range(40):
        cx = random.randint(0, INTERNAL_WIDTH)
        cy = random.randint(265, 350)
        pygame.draw.rect(s, (22, 22, 24), (cx, cy, 8, 5))
    return s


def generate_park_scene():
    """Kaisaniemi Park at night — trees, benches, distant sea."""
    s = create_surface()
    # Dark sky with hint of sea
    pygame.draw.rect(s, (6, 8, 15), (0, 0, INTERNAL_WIDTH, 120))
    # Distant water line
    pygame.draw.rect(s, (10, 15, 25), (0, 110, INTERNAL_WIDTH, 15))
    # Trees
    for tx in range(50, INTERNAL_WIDTH, 100):
        trunk_h = random.randint(60, 100)
        pygame.draw.rect(s, (25, 20, 15), (tx, 200 - trunk_h, 6, trunk_h))
        # Canopy
        for _ in range(3):
            cx = tx + random.randint(-20, 20)
            cy = 200 - trunk_h + random.randint(-25, 5)
            r = random.randint(15, 25)
            pygame.draw.circle(s, (12, 18, 10), (cx, cy), r)
    # Path
    pygame.draw.rect(s, (20, 18, 16), (0, 280, INTERNAL_WIDTH, 30))
    # Grass
    pygame.draw.rect(s, (10, 15, 8), (0, 200, INTERNAL_WIDTH, 80))
    pygame.draw.rect(s, (10, 15, 8), (0, 310, INTERNAL_WIDTH, 50))
    # Bench
    pygame.draw.rect(s, (40, 35, 25), (300, 275, 60, 6))
    pygame.draw.rect(s, (35, 30, 20), (305, 281, 4, 12))
    pygame.draw.rect(s, (35, 30, 20), (351, 281, 4, 12))
    # Stars
    for _ in range(20):
        sx = random.randint(0, INTERNAL_WIDTH)
        sy = random.randint(0, 80)
        s.set_at((sx, sy), (60, 60, 70))
    return s


def generate_kruununhaka_scene():
    """Wealthy neighborhood — grander architecture."""
    s = create_surface()
    # Ornate buildings
    for i in range(5):
        bx = i * 130
        bh = random.randint(140, 200)
        color = (30 + i * 3, 28 + i * 2, 32 + i * 2)
        pygame.draw.rect(s, color, (bx, 240 - bh, 125, bh))
        # Ornamental top
        pygame.draw.rect(s, tuple(c + 5 for c in color), (bx, 240 - bh - 8, 125, 8))
        # Larger, fancier windows
        for wy in range(240 - bh + 20, 230, 35):
            for wx in range(bx + 12, bx + 115, 28):
                if random.random() < 0.2:
                    pygame.draw.rect(s, (55, 50, 30), (wx, wy, 14, 20))
                else:
                    pygame.draw.rect(s, (12, 12, 18), (wx, wy, 14, 20))
                # Window frame
                pygame.draw.rect(s, (35, 33, 38), (wx - 1, wy - 1, 16, 22), 1)
    # Wide sidewalk
    pygame.draw.rect(s, (28, 28, 30), (0, 240, INTERNAL_WIDTH, 20))
    # Road
    pygame.draw.rect(s, (20, 20, 22), (0, 260, INTERNAL_WIDTH, 100))
    # Streetlight
    pygame.draw.rect(s, (45, 45, 50), (450, 150, 3, 90))
    glow = pygame.Surface((60, 60), pygame.SRCALPHA)
    pygame.draw.circle(glow, (40, 38, 25, 30), (30, 30), 30)
    s.blit(glow, (423, 130))
    return s


def generate_esplanadi_scene():
    """Wide boulevard with trees — smell of the sea."""
    s = create_surface()
    # Sky — slightly lighter, sea nearby
    pygame.draw.rect(s, (8, 12, 22), (0, 0, INTERNAL_WIDTH, 100))
    # Tree-lined boulevard
    pygame.draw.rect(s, (15, 18, 12), (0, 100, INTERNAL_WIDTH, 160))
    # Path down the middle
    pygame.draw.rect(s, (22, 20, 18), (200, 260, 240, 100))
    # Trees on both sides
    for tx in range(30, 180, 50):
        pygame.draw.rect(s, (25, 20, 12), (tx, 160, 5, 80))
        pygame.draw.circle(s, (14, 22, 12), (tx + 2, 150), 22)
    for tx in range(460, INTERNAL_WIDTH, 50):
        pygame.draw.rect(s, (25, 20, 12), (tx, 160, 5, 80))
        pygame.draw.circle(s, (14, 22, 12), (tx + 2, 150), 22)
    # Sides
    pygame.draw.rect(s, (18, 18, 15), (0, 260, 200, 100))
    pygame.draw.rect(s, (18, 18, 15), (440, 260, 200, 100))
    # Benches
    pygame.draw.rect(s, (40, 35, 25), (220, 270, 40, 5))
    pygame.draw.rect(s, (40, 35, 25), (380, 270, 40, 5))
    return s


def generate_kaivopuisto_scene():
    """Park by the sea — stars, wind, almost there."""
    s = create_surface()
    # Night sky with more stars
    pygame.draw.rect(s, (5, 8, 18), (0, 0, INTERNAL_WIDTH, 140))
    for _ in range(50):
        sx = random.randint(0, INTERNAL_WIDTH)
        sy = random.randint(0, 100)
        brightness = random.randint(40, 90)
        s.set_at((sx, sy), (brightness, brightness, brightness + 10))
    # Sea
    for sy in range(110, 145):
        wave_color = (8 + (sy % 3), 12 + (sy % 4), 25 + (sy % 5))
        pygame.draw.line(s, wave_color, (0, sy), (INTERNAL_WIDTH, sy))
    # Rocky shore
    pygame.draw.rect(s, (18, 16, 14), (0, 145, INTERNAL_WIDTH, 20))
    for _ in range(20):
        rx = random.randint(0, INTERNAL_WIDTH)
        pygame.draw.circle(s, (25, 22, 18), (rx, random.randint(145, 165)), random.randint(3, 8))
    # Grass
    pygame.draw.rect(s, (10, 16, 8), (0, 165, INTERNAL_WIDTH, 195))
    # Path
    pygame.draw.rect(s, (20, 18, 15), (250, 200, 140, 160))
    # Trees
    for tx in [80, 200, 450, 550]:
        pygame.draw.rect(s, (22, 18, 10), (tx, 190, 5, 60))
        pygame.draw.circle(s, (12, 20, 10), (tx + 2, 180), 20)
    return s


def generate_eira_scene():
    """Eira at dawn — first light. The destination."""
    s = create_surface()
    # Dawn sky — gradient from dark to warm
    for y in range(140):
        r = int(5 + (y / 140) * 45)
        g = int(5 + (y / 140) * 30)
        b = int(15 + (y / 140) * 20)
        pygame.draw.line(s, (r, g, b), (0, 139 - y), (INTERNAL_WIDTH, 139 - y))
    # Horizon glow
    glow = pygame.Surface((INTERNAL_WIDTH, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(glow, (80, 50, 30, 40), (150, -10, 340, 50))
    s.blit(glow, (0, 110))
    # Sea with dawn reflection
    for sy in range(140, 220):
        wave_offset = (sy * 3) % 7
        r = int(15 + (220 - sy) / 80 * 30)
        g = int(18 + (220 - sy) / 80 * 20)
        b = int(30 + (220 - sy) / 80 * 10)
        pygame.draw.line(s, (r + wave_offset, g, b), (0, sy), (INTERNAL_WIDTH, sy))
    # Shore
    pygame.draw.rect(s, (25, 22, 18), (0, 220, INTERNAL_WIDTH, 15))
    # Eira buildings in distance (elegant, art nouveau silhouettes)
    for i in range(6):
        bx = i * 110 + 10
        bh = random.randint(40, 70)
        pygame.draw.rect(s, (20, 18, 22), (bx, 140 - bh, 100, bh))
        # Spire/tower on some
        if random.random() < 0.4:
            pygame.draw.rect(s, (22, 20, 25), (bx + 45, 140 - bh - 20, 10, 20))
    # Grass and path
    pygame.draw.rect(s, (12, 18, 10), (0, 235, INTERNAL_WIDTH, 125))
    pygame.draw.rect(s, (22, 20, 16), (200, 260, 240, 100))
    # Fading stars
    for _ in range(10):
        sx = random.randint(0, INTERNAL_WIDTH)
        sy = random.randint(0, 40)
        s.set_at((sx, sy), (35, 35, 40))
    return s


def generate_rooftop_scene():
    """Kallio rooftop at night — city skyline, ventilation pipes, gap between buildings."""
    s = create_surface()
    # Night sky
    pygame.draw.rect(s, (5, 8, 18), (0, 0, INTERNAL_WIDTH, 180))
    # Stars
    for _ in range(30):
        sx = random.randint(0, INTERNAL_WIDTH)
        sy = random.randint(0, 120)
        brightness = random.randint(35, 75)
        s.set_at((sx, sy), (brightness, brightness, brightness + 10))
    # Distant city skyline
    for i in range(12):
        bx = i * 55
        bh = random.randint(30, 80)
        pygame.draw.rect(s, (12, 14, 20), (bx, 180 - bh, 50, bh))
        if random.random() < 0.3:
            pygame.draw.rect(s, (40, 35, 20), (bx + random.randint(5, 35),
                             180 - bh + random.randint(5, max(6, bh - 10)), 6, 8))
    # Current rooftop (left building)
    pygame.draw.rect(s, (28, 26, 30), (0, 180, 280, 180))
    pygame.draw.rect(s, (32, 30, 34), (0, 175, 280, 8))
    # Ventilation pipes
    pygame.draw.rect(s, (40, 40, 45), (60, 160, 20, 20))
    pygame.draw.rect(s, (45, 45, 50), (58, 155, 24, 8))
    pygame.draw.rect(s, (40, 40, 45), (180, 150, 25, 30))
    pygame.draw.rect(s, (45, 45, 50), (178, 145, 29, 8))
    # Gap
    pygame.draw.rect(s, (2, 3, 8), (280, 180, 60, 180))
    # Target building (right)
    pygame.draw.rect(s, (25, 23, 28), (340, 190, 300, 170))
    pygame.draw.rect(s, (30, 28, 32), (340, 185, 300, 8))
    # Chimney on right building
    pygame.draw.rect(s, (35, 33, 38), (500, 155, 15, 35))
    # Alley far below (faint details)
    pygame.draw.rect(s, (8, 8, 10), (290, 340, 40, 20))
    return s


def generate_metro_train_scene():
    """Maintenance train in the metro tunnel — controls, dim cab light."""
    s = create_surface()
    # Tunnel around the train
    pygame.draw.polygon(s, (15, 15, 18),
                        [(0, 0), (150, 80), (150, 280), (0, 360)])
    pygame.draw.polygon(s, (15, 15, 18),
                        [(640, 0), (490, 80), (490, 280), (640, 360)])
    pygame.draw.polygon(s, (12, 12, 14),
                        [(0, 0), (640, 0), (490, 80), (150, 80)])
    # Train cab interior
    pygame.draw.rect(s, (30, 30, 35), (150, 80, 340, 200))
    # Windshield (dark tunnel ahead)
    pygame.draw.rect(s, (8, 10, 15), (180, 90, 280, 100))
    # Distant tunnel light through windshield
    pygame.draw.circle(s, (18, 20, 16), (320, 140), 20)
    pygame.draw.circle(s, (25, 27, 22), (320, 140), 8)
    # Dashboard
    pygame.draw.rect(s, (25, 25, 30), (180, 190, 280, 30))
    # Controls — lever, buttons
    pygame.draw.rect(s, (50, 45, 35), (250, 175, 8, 20))
    pygame.draw.circle(s, (60, 50, 35), (254, 172), 5)
    # Indicator lights
    pygame.draw.circle(s, (30, 60, 30), (300, 198), 4)
    pygame.draw.circle(s, (60, 30, 30), (330, 198), 4)
    pygame.draw.circle(s, (50, 50, 20), (360, 198), 4)
    # Cab ceiling light (dim)
    glow = pygame.Surface((120, 60), pygame.SRCALPHA)
    pygame.draw.ellipse(glow, (40, 40, 35, 25), (0, 0, 120, 60))
    s.blit(glow, (260, 75))
    # Floor
    pygame.draw.rect(s, (20, 20, 22), (150, 280, 340, 80))
    # Rails visible below windshield
    pygame.draw.line(s, (35, 35, 40), (220, 190), (280, 140), 1)
    pygame.draw.line(s, (35, 35, 40), (420, 190), (360, 140), 1)
    return s


def generate_cafe_scene():
    """Late-night cafe in Kallio — harsh light, many Franks."""
    s = create_surface()
    # Ceiling
    pygame.draw.rect(s, (35, 30, 28), (0, 0, INTERNAL_WIDTH, 60))
    # Fluorescent light
    pygame.draw.rect(s, (80, 75, 60), (200, 55, 240, 4))
    glow = pygame.Surface((300, 50), pygame.SRCALPHA)
    pygame.draw.ellipse(glow, (50, 48, 38, 18), (0, 0, 300, 50))
    s.blit(glow, (170, 35))
    # Walls
    pygame.draw.rect(s, (32, 28, 26), (0, 60, INTERNAL_WIDTH, 160))
    # Window (dark outside, rain streaks)
    pygame.draw.rect(s, (8, 12, 20), (400, 80, 180, 100))
    pygame.draw.rect(s, (35, 32, 30), (398, 78, 184, 104), 2)
    for _ in range(6):
        rx = random.randint(405, 575)
        pygame.draw.line(s, (15, 20, 30), (rx, 82), (rx - 3, 175), 1)
    # Floor
    pygame.draw.rect(s, (28, 24, 22), (0, 220, INTERNAL_WIDTH, 140))
    # Tables with chairs
    for tx in [80, 220, 360]:
        pygame.draw.rect(s, (50, 40, 30), (tx, 240, 60, 4))
        pygame.draw.rect(s, (45, 38, 28), (tx + 26, 244, 8, 30))
        # Chairs
        pygame.draw.rect(s, (40, 35, 28), (tx - 10, 250, 6, 20))
        pygame.draw.rect(s, (40, 35, 28), (tx + 64, 250, 6, 20))
    # Counter in background
    pygame.draw.rect(s, (45, 35, 28), (0, 200, 150, 25))
    # Coffee cups on tables
    for tx in [95, 235, 375]:
        pygame.draw.rect(s, (60, 55, 50), (tx, 236, 6, 5))
    return s


def generate_limo_scene():
    """Inside a long black car — city lights passing."""
    s = create_surface()
    # Car interior (dark leather)
    pygame.draw.rect(s, (18, 16, 14), (0, 0, INTERNAL_WIDTH, INTERNAL_HEIGHT))
    # Roof
    pygame.draw.rect(s, (15, 13, 12), (0, 0, INTERNAL_WIDTH, 40))
    # Rear window (city passing by)
    pygame.draw.rect(s, (8, 12, 22), (60, 50, 520, 130))
    # Passing city lights through window
    for _ in range(8):
        lx = random.randint(70, 570)
        ly = random.randint(100, 160)
        lw = random.randint(15, 40)
        color = random.choice([(40, 35, 20), (35, 40, 45), (45, 30, 20)])
        pygame.draw.rect(s, color, (lx, ly, lw, random.randint(5, 15)))
    # Streetlights streaks
    for _ in range(4):
        lx = random.randint(80, 560)
        pygame.draw.line(s, (50, 48, 30), (lx, 55), (lx + 20, 55), 2)
    # Back seat
    pygame.draw.rect(s, (22, 18, 15), (40, 200, 560, 80))
    pygame.draw.rect(s, (25, 21, 18), (40, 180, 560, 25))
    # Seat dividers
    pygame.draw.line(s, (20, 16, 13), (240, 200), (240, 280), 1)
    # Floor
    pygame.draw.rect(s, (12, 10, 10), (40, 280, 560, 80))
    # Pine air freshener hanging from mirror (barely visible)
    pygame.draw.polygon(s, (20, 35, 15), [(320, 50), (315, 65), (325, 65)])
    return s


def generate_harbor_scene():
    """Industrial harbor at night — cranes, bollards, dark water."""
    s = create_surface()
    # Night sky
    pygame.draw.rect(s, (5, 7, 15), (0, 0, INTERNAL_WIDTH, 100))
    # Cranes (silhouettes)
    for cx in [120, 400]:
        # Vertical mast
        pygame.draw.rect(s, (18, 18, 22), (cx, 20, 6, 160))
        # Horizontal boom
        pygame.draw.line(s, (18, 18, 22), (cx - 60, 30), (cx + 80, 30), 3)
        # Cable
        pygame.draw.line(s, (22, 22, 26), (cx + 70, 30), (cx + 70, 80), 1)
    # Warehouse buildings
    pygame.draw.rect(s, (20, 18, 16), (0, 100, 200, 80))
    pygame.draw.rect(s, (22, 20, 18), (450, 90, 190, 90))
    # Dock/pier
    pygame.draw.rect(s, (25, 22, 18), (0, 180, INTERNAL_WIDTH, 40))
    # Bollards
    for bx in [100, 250, 420, 550]:
        pygame.draw.rect(s, (40, 38, 35), (bx, 175, 10, 12))
        pygame.draw.rect(s, (45, 42, 38), (bx - 2, 172, 14, 6))
    # Water
    for wy in range(220, 360):
        wave_color = (5 + (wy % 3), 8 + (wy % 4), 18 + (wy % 5))
        pygame.draw.line(s, wave_color, (0, wy), (INTERNAL_WIDTH, wy))
    # Ship silhouette in distance
    pygame.draw.rect(s, (12, 12, 16), (350, 230, 150, 30))
    pygame.draw.rect(s, (14, 14, 18), (440, 210, 20, 25))
    # Dock light reflection in water
    for _ in range(5):
        rx = random.randint(80, 560)
        ry = random.randint(240, 340)
        pygame.draw.line(s, (15, 18, 25), (rx, ry), (rx + random.randint(5, 20), ry), 1)
    return s


def generate_katajanokka_scene():
    """Red brick diplomatic quarter — embassies, iron gates."""
    s = create_surface()
    # Sky with cathedral silhouette
    pygame.draw.rect(s, (6, 8, 16), (0, 0, INTERNAL_WIDTH, 120))
    # Uspenski Cathedral silhouette (onion domes)
    pygame.draw.rect(s, (14, 12, 18), (400, 40, 120, 80))
    pygame.draw.circle(s, (14, 12, 18), (430, 35), 15)
    pygame.draw.circle(s, (14, 12, 18), (460, 25), 20)
    pygame.draw.circle(s, (14, 12, 18), (490, 35), 15)
    # Spires on domes
    for dx in [430, 460, 490]:
        pygame.draw.line(s, (16, 14, 20), (dx, 10), (dx, 25), 2)
    # Red brick buildings
    for i in range(4):
        bx = i * 140
        bh = random.randint(100, 140)
        # Brick color (dark red-brown)
        pygame.draw.rect(s, (35, 18, 15), (bx, 200 - bh, 130, bh))
        # Brick pattern hints
        for by in range(200 - bh + 5, 195, 8):
            for bbx in range(bx + 2, bx + 128, 16):
                offset = 8 if ((by - (200 - bh)) // 8) % 2 else 0
                pygame.draw.rect(s, (32, 16, 13),
                                 (bbx + offset, by, 14, 6), 1)
        # Windows with frames
        for wy in range(200 - bh + 15, 190, 30):
            for wx in range(bx + 15, bx + 115, 30):
                if random.random() < 0.15:
                    pygame.draw.rect(s, (45, 40, 25), (wx, wy, 12, 18))
                else:
                    pygame.draw.rect(s, (10, 10, 14), (wx, wy, 12, 18))
    # Iron gate
    pygame.draw.rect(s, (30, 30, 32), (250, 170, 4, 35))
    pygame.draw.rect(s, (30, 30, 32), (310, 170, 4, 35))
    for gx in range(254, 310, 8):
        pygame.draw.rect(s, (28, 28, 30), (gx, 172, 2, 30))
    pygame.draw.line(s, (30, 30, 32), (250, 178), (314, 178), 1)
    # Sidewalk
    pygame.draw.rect(s, (22, 20, 18), (0, 200, INTERNAL_WIDTH, 20))
    # Cobblestone road
    pygame.draw.rect(s, (18, 16, 14), (0, 220, INTERNAL_WIDTH, 140))
    for _ in range(30):
        cx = random.randint(0, INTERNAL_WIDTH)
        cy = random.randint(225, 350)
        pygame.draw.rect(s, (22, 20, 18), (cx, cy, 8, 5))
    return s


def generate_senate_square_scene():
    """Senate Square — massive white cathedral, empty cobblestones."""
    s = create_surface()
    # Night sky
    pygame.draw.rect(s, (5, 7, 15), (0, 0, INTERNAL_WIDTH, 80))
    # Stars
    for _ in range(15):
        sx = random.randint(0, INTERNAL_WIDTH)
        sy = random.randint(0, 60)
        s.set_at((sx, sy), (50, 50, 55))
    # Cathedral (white, massive)
    pygame.draw.rect(s, (40, 40, 45), (150, 40, 340, 100))
    # Dome
    pygame.draw.ellipse(s, (45, 45, 50), (250, 10, 140, 60))
    # Cross on top
    pygame.draw.line(s, (55, 55, 60), (320, 2), (320, 15), 2)
    pygame.draw.line(s, (55, 55, 60), (314, 8), (326, 8), 2)
    # Columns (front facade)
    for cx in range(180, 470, 30):
        pygame.draw.rect(s, (48, 48, 52), (cx, 60, 6, 80))
    # Steps (wide, cascading down)
    for step in range(6):
        y = 140 + step * 12
        w_shrink = step * 15
        color_val = 35 - step * 2
        pygame.draw.rect(s, (color_val, color_val, color_val + 3),
                         (150 - w_shrink, y, 340 + w_shrink * 2, 12))
    # Square (cobblestones)
    pygame.draw.rect(s, (18, 18, 20), (0, 212, INTERNAL_WIDTH, 148))
    for _ in range(50):
        cx = random.randint(0, INTERNAL_WIDTH)
        cy = random.randint(215, 355)
        pygame.draw.rect(s, (22, 22, 24), (cx, cy, 8, 5))
    # Alexander II statue
    pygame.draw.rect(s, (30, 30, 32), (310, 240, 20, 50))
    pygame.draw.rect(s, (35, 35, 38), (305, 235, 30, 10))
    pygame.draw.rect(s, (32, 32, 35), (315, 220, 10, 18))
    return s


def generate_bulevardi_scene():
    """Bulevardi — long dark street, kiosk glow, old apartment buildings."""
    s = create_surface()
    # Sky
    pygame.draw.rect(s, (6, 9, 18), (0, 0, INTERNAL_WIDTH, 80))
    # Old apartment buildings (both sides, tall, dignified)
    for i in range(4):
        bx = i * 50
        bh = random.randint(120, 170)
        pygame.draw.rect(s, (25 + i * 2, 23 + i, 28 + i), (bx, 200 - bh, 45, bh))
        for wy in range(200 - bh + 15, 195, 25):
            for wx in range(bx + 8, bx + 40, 15):
                if random.random() < 0.12:
                    pygame.draw.rect(s, (45, 40, 25), (wx, wy, 8, 12))
                else:
                    pygame.draw.rect(s, (12, 12, 16), (wx, wy, 8, 12))
    for i in range(4):
        bx = 440 + i * 50
        bh = random.randint(120, 170)
        pygame.draw.rect(s, (25 + i * 2, 23 + i, 28 + i), (bx, 200 - bh, 45, bh))
        for wy in range(200 - bh + 15, 195, 25):
            for wx in range(bx + 8, bx + 40, 15):
                if random.random() < 0.12:
                    pygame.draw.rect(s, (45, 40, 25), (wx, wy, 8, 12))
                else:
                    pygame.draw.rect(s, (12, 12, 16), (wx, wy, 8, 12))
    # Street
    pygame.draw.rect(s, (18, 18, 20), (200, 200, 240, 160))
    # Sidewalks
    pygame.draw.rect(s, (22, 20, 18), (180, 200, 25, 160))
    pygame.draw.rect(s, (22, 20, 18), (435, 200, 25, 160))
    # Kiosk (glowing warm — the lighthouse)
    pygame.draw.rect(s, (45, 40, 25), (280, 220, 80, 50))
    pygame.draw.rect(s, (60, 55, 30), (285, 225, 70, 20))
    # Kiosk glow
    glow = pygame.Surface((160, 100), pygame.SRCALPHA)
    pygame.draw.ellipse(glow, (50, 45, 25, 20), (0, 0, 160, 100))
    s.blit(glow, (240, 200))
    # Streetlight
    pygame.draw.rect(s, (40, 40, 45), (380, 130, 3, 70))
    light_glow = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(light_glow, (35, 33, 22, 25), (20, 20), 20)
    s.blit(light_glow, (362, 115))
    # Lamppost
    pygame.draw.rect(s, (40, 40, 45), (220, 140, 3, 60))
    return s


def generate_death_vignette():
    """Dark death screen with vignette effect."""
    s = create_surface()
    # Slight red tint at edges
    vignette = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
    for radius in range(300, 50, -5):
        alpha = int((300 - radius) / 250 * 40)
        pygame.draw.circle(vignette, (30, 0, 0, alpha),
                           (INTERNAL_WIDTH // 2, INTERNAL_HEIGHT // 2), radius)
    s.blit(vignette, (0, 0))
    return s


def generate_lost_vignette():
    """Foggy lost screen."""
    s = create_surface()
    fog = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
    for _ in range(30):
        x = random.randint(0, INTERNAL_WIDTH)
        y = random.randint(0, INTERNAL_HEIGHT)
        r = random.randint(40, 120)
        pygame.draw.circle(fog, (20, 20, 25, 12), (x, y), r)
    s.blit(fog, (0, 0))
    return s
