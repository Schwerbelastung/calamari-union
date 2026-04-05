import pygame
from src.data.constants import (
    INTERNAL_WIDTH, INTERNAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT,
    BLACK, WHITE, DARK_GRAY, LINE_SPACING, TEXT_MARGIN_X, TEXT_MARGIN_TOP,
    CHOICE_MARGIN_BOTTOM, FONT_SIZE, TYPEWRITER_SPEED, TYPEWRITER_FAST,
    CHOICE_BLINK_SPEED, RED, FADE_SPEED,
)


class Renderer:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT))
        self.font = None
        self.small_font = None
        self._load_fonts()
        # Typewriter state
        self.tw_text = ""
        self.tw_revealed = 0
        self.tw_timer = 0
        self.tw_done = False
        self.tw_color = WHITE
        # Fade state
        self.fade_alpha = 0
        self.fading_in = False
        self.fading_out = False
        self.fade_surface = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT))
        self.fade_surface.fill(BLACK)
        # CRT scanline overlay
        self.scanline_surface = self._create_scanlines()

    def _load_fonts(self):
        try:
            self.font = pygame.font.Font(None, FONT_SIZE)
        except Exception:
            self.font = pygame.font.SysFont("courier", FONT_SIZE)
        self.small_font = pygame.font.Font(None, max(12, FONT_SIZE - 4))

    def clear(self):
        self.surface.fill(BLACK)

    def _create_scanlines(self):
        scanlines = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
        for y in range(0, INTERNAL_HEIGHT, 3):
            pygame.draw.line(scanlines, (0, 0, 0, 30), (0, y), (INTERNAL_WIDTH, y))
        return scanlines

    def present(self):
        # Apply scanlines
        self.surface.blit(self.scanline_surface, (0, 0))
        scaled = pygame.transform.scale(self.surface, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.blit(scaled, (0, 0))
        pygame.display.flip()

    # --- Text rendering ---

    def draw_text(self, text, x, y, color=WHITE, font=None):
        f = font or self.font
        rendered = f.render(text, False, color)
        self.surface.blit(rendered, (x, y))
        return rendered.get_height()

    def draw_text_wrapped(self, text, x, y, color=WHITE, max_width=None, font=None):
        f = font or self.font
        if max_width is None:
            max_width = INTERNAL_WIDTH - x - TEXT_MARGIN_X
        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test = current_line + (" " if current_line else "") + word
            if f.size(test)[0] > max_width and current_line:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test
        if current_line:
            lines.append(current_line)

        line_h = f.get_linesize() + LINE_SPACING
        for i, line in enumerate(lines):
            self.draw_text(line, x, y + i * line_h, color, f)
        return y + len(lines) * line_h

    # --- Typewriter effect ---

    def start_typewriter(self, text, color=WHITE):
        self.tw_text = text
        self.tw_revealed = 0
        self.tw_timer = 0
        self.tw_done = False
        self.tw_color = color

    def update_typewriter(self, dt, fast=False):
        if self.tw_done:
            return
        speed = TYPEWRITER_FAST if fast else TYPEWRITER_SPEED
        self.tw_timer += dt
        while self.tw_timer >= speed and self.tw_revealed < len(self.tw_text):
            self.tw_timer -= speed
            self.tw_revealed += 1
        if self.tw_revealed >= len(self.tw_text):
            self.tw_revealed = len(self.tw_text)
            self.tw_done = True

    def skip_typewriter(self):
        self.tw_revealed = len(self.tw_text)
        self.tw_done = True

    def draw_typewriter(self, x, y, max_width=None):
        visible = self.tw_text[:self.tw_revealed]
        return self.draw_text_wrapped(visible, x, y, self.tw_color, max_width)

    # --- Choices ---

    def draw_choices(self, choices, selected, y_start=None, colors=None):
        if y_start is None:
            y_start = INTERNAL_HEIGHT - CHOICE_MARGIN_BOTTOM - len(choices) * (self.font.get_linesize() + LINE_SPACING)

        line_h = self.font.get_linesize() + LINE_SPACING
        ticks = pygame.time.get_ticks()
        arrow_visible = (ticks // CHOICE_BLINK_SPEED) % 2 == 0

        for i, choice in enumerate(choices):
            color = WHITE
            if colors and i < len(colors):
                color = colors[i]
            prefix = "> " if i == selected and arrow_visible else "  "
            if i == selected:
                self.draw_text(prefix + choice, TEXT_MARGIN_X, y_start + i * line_h, color)
            else:
                self.draw_text(prefix + choice, TEXT_MARGIN_X, y_start + i * line_h, DARK_GRAY)

        return y_start + len(choices) * line_h

    # --- Fade transitions ---

    def start_fade_in(self):
        self.fade_alpha = 255
        self.fading_in = True
        self.fading_out = False

    def start_fade_out(self):
        self.fade_alpha = 0
        self.fading_in = False
        self.fading_out = True

    def update_fade(self):
        if self.fading_in:
            self.fade_alpha = max(0, self.fade_alpha - FADE_SPEED)
            if self.fade_alpha <= 0:
                self.fading_in = False
                return True  # fade complete
        elif self.fading_out:
            self.fade_alpha = min(255, self.fade_alpha + FADE_SPEED)
            if self.fade_alpha >= 255:
                self.fading_out = False
                return True  # fade complete
        return False

    @property
    def is_fading(self):
        return self.fading_in or self.fading_out

    def draw_fade(self):
        if self.fade_alpha > 0:
            self.fade_surface.set_alpha(self.fade_alpha)
            self.surface.blit(self.fade_surface, (0, 0))

    # --- Scene backgrounds ---

    def draw_background(self, bg_surface):
        if bg_surface:
            self.surface.blit(bg_surface, (0, 0))

    # --- Sprites ---

    def draw_sprite(self, sprite_surface, x, y):
        if sprite_surface:
            self.surface.blit(sprite_surface, (x, y))
