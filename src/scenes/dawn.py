import pygame
import math
from src.scenes.scene_base import SceneBase
from src.data.constants import (
    WHITE, DARK_GRAY, MID_GRAY, FRANK_COLORS,
    INTERNAL_WIDTH, INTERNAL_HEIGHT,
)
from src.engine.pixel_art import generate_frank_sprite


class DawnScene(SceneBase):
    """Animated sunrise over the sea, with a rowboat heading to Estonia."""
    SCENE_ID = "dawn"
    ALLOW_UNDO = False

    def __init__(self):
        super().__init__()
        self.time = 0.0            # animation time in seconds
        self.sun_y = 145.0         # sun starts at horizon (y=140 is horizon line)
        self.sun_target_y = 80.0   # sun rises to here
        self.sun_rise_duration = 12.0  # seconds for full sunrise
        self.boat_x = 500.0        # boat starts right side
        self.boat_target_x = -80.0 # boat exits left (heading west toward Estonia)
        self.boat_duration = 18.0  # seconds to cross
        self.speech_shown = False
        self.speech_time = 0.0
        self.speech_alpha = 0
        self.phase = "animating"
        self.prompt_timer = 0.0
        # Pre-generate sprites for the two Franks on the boat
        self.frank_a = generate_frank_sprite(FRANK_COLORS["frank_10"], scale=2)
        self.frank_b = generate_frank_sprite(FRANK_COLORS["frank_11"], scale=2)
        # Building silhouettes (fixed, not random — we redraw every frame)
        self.buildings = []

    def setup(self):
        # Pre-calculate building silhouettes so they're consistent across frames
        import random
        random.seed(42)  # deterministic for this scene
        for i in range(6):
            bx = i * 110 + 10
            bh = random.randint(40, 70)
            has_spire = random.random() < 0.4
            self.buildings.append((bx, bh, has_spire))
        random.seed()  # reset

    def update(self, dt, input_handler):
        dt_s = dt / 1000.0
        self.time += dt_s

        # Sun rises
        if self.time < self.sun_rise_duration:
            t = self.time / self.sun_rise_duration
            # Ease-out for natural sunrise feel
            t = 1.0 - (1.0 - t) ** 2
            self.sun_y = 145.0 + (self.sun_target_y - 145.0) * t

        # Boat moves
        if self.time > 3.0:  # boat appears after 3 seconds
            boat_t = (self.time - 3.0) / self.boat_duration
            boat_t = min(1.0, boat_t)
            self.boat_x = 500.0 + (self.boat_target_x - 500.0) * boat_t

            # Show speech bubble when boat is roughly centered
            if not self.speech_shown and self.boat_x < 320 and self.boat_x > 200:
                self.speech_shown = True
                self.speech_time = self.time

        # Speech bubble fade
        if self.speech_shown:
            elapsed = self.time - self.speech_time
            if elapsed < 0.5:
                self.speech_alpha = int(elapsed / 0.5 * 255)
            elif elapsed < 5.0:
                self.speech_alpha = 255
            elif elapsed < 6.0:
                self.speech_alpha = int((1.0 - (elapsed - 5.0)) * 255)
            else:
                self.speech_alpha = 0

        # After boat exits, show prompt to continue
        if self.boat_x < self.boat_target_x + 10:
            self.prompt_timer += dt_s
            if input_handler.just_pressed(pygame.K_RETURN):
                from src.scenes.endings import CreditsScene
                self.goto(CreditsScene())

    def draw(self, renderer):
        s = renderer.surface

        # --- Animated sky gradient ---
        # Sky brightens as sun rises
        sun_progress = max(0.0, min(1.0, (145.0 - self.sun_y) / (145.0 - self.sun_target_y)))

        for y in range(140):
            # Base dark sky → warm dawn
            inv_y = 139 - y  # 0 = top, 139 = horizon
            horizon_factor = y / 140.0  # 1.0 at horizon, 0.0 at top

            # Dark starting colors
            r = int(5 + horizon_factor * 45 * (0.3 + 0.7 * sun_progress))
            g = int(5 + horizon_factor * 30 * (0.3 + 0.7 * sun_progress))
            b = int(15 + horizon_factor * 20 * (0.5 + 0.5 * sun_progress))

            # Add warm sunrise tones
            r = min(255, int(r + sun_progress * 60 * horizon_factor))
            g = min(255, int(g + sun_progress * 30 * horizon_factor))

            # Upper sky gets blue
            if inv_y < 60:
                top_factor = 1.0 - inv_y / 60.0
                b = min(255, int(b + sun_progress * 25 * top_factor))

            pygame.draw.line(s, (r, g, b), (0, inv_y), (INTERNAL_WIDTH, inv_y))

        # --- Sun ---
        sun_x = INTERNAL_WIDTH // 2
        sun_iy = int(self.sun_y)

        # Sun glow (large, soft)
        glow_radius = int(40 + 20 * sun_progress)
        glow_surf = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
        for r_i in range(glow_radius, 0, -1):
            alpha = int((1.0 - r_i / glow_radius) * 35 * sun_progress)
            gr = min(255, int(180 + 75 * sun_progress))
            gg = min(255, int(100 + 55 * sun_progress))
            gb = min(255, int(30 + 30 * sun_progress))
            pygame.draw.circle(glow_surf, (gr, gg, gb, alpha), (glow_radius, glow_radius), r_i)
        s.blit(glow_surf, (sun_x - glow_radius, sun_iy - glow_radius))

        # Sun disc
        sun_radius = int(8 + 4 * sun_progress)
        sun_color = (
            min(255, int(200 + 55 * sun_progress)),
            min(255, int(150 + 60 * sun_progress)),
            min(255, int(50 + 40 * sun_progress)),
        )
        pygame.draw.circle(s, sun_color, (sun_x, sun_iy), sun_radius)
        # Bright center
        pygame.draw.circle(s, (255, 240, 200), (sun_x, sun_iy), max(2, sun_radius - 3))

        # --- Sea ---
        wave_time = self.time * 0.8
        for sy in range(140, 220):
            depth = (sy - 140) / 80.0  # 0 at surface, 1 at bottom
            wave = math.sin(wave_time + sy * 0.15) * 2

            # Base sea color, brightens with sunrise
            r = int(10 + (1.0 - depth) * 25 * sun_progress + wave)
            g = int(14 + (1.0 - depth) * 18 * sun_progress)
            b = int(28 + (1.0 - depth) * 8 + depth * 5)

            # Sun reflection on water (vertical stripe below sun)
            dist_from_center = abs(INTERNAL_WIDTH // 2 - 320)  # reflection center
            for px in range(INTERNAL_WIDTH):
                reflect_dist = abs(px - sun_x)
                if reflect_dist < 60 and depth < 0.4:
                    reflect_strength = (1.0 - reflect_dist / 60.0) * (1.0 - depth / 0.4) * sun_progress
                    shimmer = math.sin(wave_time * 2 + px * 0.3 + sy * 0.5) * 0.3 + 0.7
                    reflect_strength *= shimmer
                    rr = min(255, int(r + 80 * reflect_strength))
                    rg = min(255, int(g + 50 * reflect_strength))
                    rb = min(255, int(b + 20 * reflect_strength))
                    s.set_at((px, sy), (rr, rg, rb))
                else:
                    pass  # leave pixel unset, draw line below

            # Draw the base sea line (pixels not individually set will be covered)
            pygame.draw.line(s, (max(0, r), max(0, g), max(0, b)), (0, sy), (INTERNAL_WIDTH, sy))

        # Redraw reflection on top (shimmer effect)
        for sy in range(140, min(180, 140 + int(40 * sun_progress))):
            depth = (sy - 140) / 80.0
            for offset in range(-50, 51, 2):
                px = sun_x + offset
                if 0 <= px < INTERNAL_WIDTH:
                    reflect_dist = abs(offset)
                    reflect_strength = (1.0 - reflect_dist / 50.0) * (1.0 - depth * 2.5) * sun_progress
                    shimmer = math.sin(wave_time * 3 + px * 0.4 + sy * 0.7) * 0.4 + 0.6
                    reflect_strength *= shimmer
                    if reflect_strength > 0.05:
                        rr = min(255, int(180 * reflect_strength))
                        rg = min(255, int(120 * reflect_strength))
                        rb = min(255, int(50 * reflect_strength))
                        # Additive-ish blend
                        try:
                            existing = s.get_at((px, sy))
                            nr = min(255, existing[0] + rr)
                            ng = min(255, existing[1] + rg)
                            nb = min(255, existing[2] + rb)
                            s.set_at((px, sy), (nr, ng, nb))
                        except IndexError:
                            pass

        # --- Shore ---
        shore_color = (
            int(25 + 15 * sun_progress),
            int(22 + 12 * sun_progress),
            int(18 + 8 * sun_progress),
        )
        pygame.draw.rect(s, shore_color, (0, 220, INTERNAL_WIDTH, 15))

        # --- Building silhouettes ---
        for bx, bh, has_spire in self.buildings:
            building_color = (
                int(20 + 10 * sun_progress),
                int(18 + 8 * sun_progress),
                int(22 + 5 * sun_progress),
            )
            pygame.draw.rect(s, building_color, (bx, 140 - bh, 100, bh))
            if has_spire:
                pygame.draw.rect(s, building_color, (bx + 45, 140 - bh - 20, 10, 20))

        # --- Grass and path ---
        grass_color = (
            int(12 + 10 * sun_progress),
            int(18 + 15 * sun_progress),
            int(10 + 5 * sun_progress),
        )
        pygame.draw.rect(s, grass_color, (0, 235, INTERNAL_WIDTH, 125))
        path_color = (
            int(22 + 10 * sun_progress),
            int(20 + 8 * sun_progress),
            int(16 + 6 * sun_progress),
        )
        pygame.draw.rect(s, path_color, (200, 260, 240, 100))

        # --- Rowboat ---
        if self.time > 3.0:
            bx = int(self.boat_x)
            # Boat bobs on water
            bob = math.sin(self.time * 1.5) * 2
            by = int(165 + bob)

            # Boat hull
            hull_color = (50, 35, 20)
            pygame.draw.polygon(s, hull_color, [
                (bx, by + 6),
                (bx + 6, by + 12),
                (bx + 50, by + 12),
                (bx + 56, by + 6),
            ])
            # Boat rim
            pygame.draw.line(s, (65, 48, 30), (bx, by + 6), (bx + 56, by + 6), 1)

            # Oars (animated)
            oar_angle = math.sin(self.time * 2.5) * 0.4
            oar_color = (60, 45, 25)
            # Left oar
            oar_lx = bx + 15
            oar_ly = by + 8
            oar_end_lx = oar_lx - int(12 * math.cos(oar_angle))
            oar_end_ly = oar_ly + int(8 + 4 * math.sin(oar_angle))
            pygame.draw.line(s, oar_color, (oar_lx, oar_ly), (oar_end_lx, oar_end_ly), 1)
            # Right oar
            oar_rx = bx + 41
            oar_ry = by + 8
            oar_end_rx = oar_rx + int(12 * math.cos(oar_angle))
            oar_end_ry = oar_ry + int(8 + 4 * math.sin(oar_angle))
            pygame.draw.line(s, oar_color, (oar_rx, oar_ry), (oar_end_rx, oar_end_ry), 1)

            # Two Franks in the boat
            # Rowing Frank (slightly animated)
            lean = int(math.sin(self.time * 2.5) * 1)
            s.blit(self.frank_a, (bx + 10 + lean, by - 16))
            # Sitting Frank (looking forward/left toward Estonia)
            s.blit(self.frank_b, (bx + 30, by - 16))

            # Wake/splash behind boat
            wake_color = (
                min(255, int(30 + 30 * sun_progress)),
                min(255, int(35 + 25 * sun_progress)),
                min(255, int(45 + 15 * sun_progress)),
            )
            for wi in range(4):
                wx = bx + 56 + wi * 8 + int(math.sin(self.time * 2 + wi) * 2)
                wy = by + 8 + int(math.sin(self.time * 3 + wi * 1.5) * 1)
                if 0 <= wx < INTERNAL_WIDTH:
                    pygame.draw.line(s, wake_color, (wx, wy), (wx + 4, wy), 1)

        # --- Speech bubble ---
        if self.speech_shown and self.speech_alpha > 0:
            bx = int(self.boat_x)
            bob = math.sin(self.time * 1.5) * 2
            by = int(165 + bob)

            text = self.get_string("speech_bubble")
            font = renderer.small_font
            text_surf = font.render(text, True, WHITE)
            tw = text_surf.get_width()
            th = text_surf.get_height()

            # Bubble background
            bubble_w = tw + 12
            bubble_h = th + 8
            bubble_x = bx + 28 - bubble_w // 2
            bubble_y = by - 38

            bubble = pygame.Surface((bubble_w, bubble_h + 6), pygame.SRCALPHA)
            # Bubble body
            pygame.draw.rect(bubble, (0, 0, 0, min(200, self.speech_alpha)),
                             (0, 0, bubble_w, bubble_h), border_radius=3)
            pygame.draw.rect(bubble, (255, 255, 255, min(180, self.speech_alpha)),
                             (0, 0, bubble_w, bubble_h), 1, border_radius=3)
            # Bubble tail
            tail_x = bubble_w // 2
            pygame.draw.polygon(bubble, (0, 0, 0, min(200, self.speech_alpha)), [
                (tail_x - 3, bubble_h),
                (tail_x + 3, bubble_h),
                (tail_x, bubble_h + 5),
            ])

            bubble.set_alpha(self.speech_alpha)
            s.blit(bubble, (bubble_x, bubble_y))

            # Text
            text_with_alpha = text_surf.copy()
            text_with_alpha.set_alpha(self.speech_alpha)
            s.blit(text_with_alpha, (bubble_x + 6, bubble_y + 4))

        # --- Continue prompt ---
        if self.boat_x < self.boat_target_x + 10:
            pulse = int(abs(math.sin(self.prompt_timer * 1.5)) * 150) + 40
            prompt_color = (pulse, pulse, pulse)
            prompt = renderer.small_font.render(self.get_string("continue_prompt"), True, prompt_color)
            px = (INTERNAL_WIDTH - prompt.get_width()) // 2
            s.blit(prompt, (px, INTERNAL_HEIGHT - 30))
