import pygame
from src.data.constants import (
    INTERNAL_WIDTH, INTERNAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT,
    BLACK, WHITE, DARK_GRAY, LINE_SPACING, TEXT_MARGIN_X, TEXT_MARGIN_TOP,
    CHOICE_MARGIN_BOTTOM, FONT_SIZE, FONT_NAME, TYPEWRITER_SPEED,
    TYPEWRITER_FAST, CHOICE_BLINK_SPEED, RED, FADE_SPEED,
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
            self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        except Exception:
            self.font = pygame.font.SysFont("courier", FONT_SIZE)
        self.small_font = pygame.font.SysFont(FONT_NAME, max(12, FONT_SIZE - 4))

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
        # Draw fullscreen toggle button
        self._draw_fs_button()
        # Scale to fit window, maintaining aspect ratio with black bars
        win_w, win_h = self.window.get_size()
        scale = min(win_w / INTERNAL_WIDTH, win_h / INTERNAL_HEIGHT)
        self._present_scale = scale
        scaled_w = int(INTERNAL_WIDTH * scale)
        scaled_h = int(INTERNAL_HEIGHT * scale)
        scaled = pygame.transform.scale(self.surface, (scaled_w, scaled_h))
        self.window.fill((0, 0, 0))
        self._present_offset_x = (win_w - scaled_w) // 2
        self._present_offset_y = (win_h - scaled_h) // 2
        self.window.blit(scaled, (self._present_offset_x, self._present_offset_y))
        pygame.display.flip()

    def _draw_fs_button(self):
        """Draw a visible fullscreen toggle button in the top-right corner."""
        bx, by = INTERNAL_WIDTH - 22, 4
        size = 16
        # Dark background pill for contrast
        bg = pygame.Surface((size + 8, size + 8), pygame.SRCALPHA)
        pygame.draw.rect(bg, (0, 0, 0, 120), (0, 0, size + 8, size + 8), border_radius=3)
        self.surface.blit(bg, (bx - 4, by - 4))
        # Corner brackets — brighter, thicker
        c = (140, 140, 150)
        t = 2  # line thickness
        # Top-left bracket
        pygame.draw.lines(self.surface, c, False, [(bx, by + 5), (bx, by), (bx + 5, by)], t)
        # Top-right bracket
        pygame.draw.lines(self.surface, c, False, [(bx + size - 5, by), (bx + size, by), (bx + size, by + 5)], t)
        # Bottom-left bracket
        pygame.draw.lines(self.surface, c, False, [(bx, by + size - 5), (bx, by + size), (bx + 5, by + size)], t)
        # Bottom-right bracket
        pygame.draw.lines(self.surface, c, False, [(bx + size - 5, by + size), (bx + size, by + size), (bx + size, by + size - 5)], t)
        # Store hit area
        self._fs_button_rect = (bx - 6, by - 6, size + 12, size + 12)

    def check_fs_button_click(self, mouse_x, mouse_y):
        """Check if a mouse click hit the fullscreen button. Takes window coordinates."""
        if not hasattr(self, '_present_scale'):
            return False
        # Convert window coords to internal coords
        ix = (mouse_x - self._present_offset_x) / self._present_scale
        iy = (mouse_y - self._present_offset_y) / self._present_scale
        bx, by, bw, bh = self._fs_button_rect
        return bx <= ix <= bx + bw and by <= iy <= by + bh

    # --- Text rendering ---

    def draw_text(self, text, x, y, color=WHITE, font=None):
        f = font or self.font
        rendered = f.render(text, True, color)
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

    def measure_text_wrapped(self, text, max_width=None, font=None):
        """Return the height in pixels that wrapped text would occupy."""
        f = font or self.font
        if max_width is None:
            max_width = INTERNAL_WIDTH - TEXT_MARGIN_X * 2
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
        return len(lines) * line_h

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

        # Dark backdrop behind choices for readability
        pad = 8
        backdrop_y = y_start - pad
        backdrop_h = len(choices) * line_h + pad * 2
        backdrop = pygame.Surface((INTERNAL_WIDTH, backdrop_h), pygame.SRCALPHA)
        backdrop.fill((0, 0, 0, 140))
        self.surface.blit(backdrop, (0, backdrop_y))

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
