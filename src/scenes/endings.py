import pygame
from src.scenes.scene_base import SceneBase
from src.data.constants import (
    WHITE, RED, MID_GRAY, DARK_GRAY, FRANK_COLORS, PEKKA_COLOR,
    INTERNAL_WIDTH, INTERNAL_HEIGHT, TEXT_MARGIN_X, TEXT_MARGIN_TOP,
    FONT_NAME,
)
from src.engine.pixel_art import (
    generate_death_vignette, generate_lost_vignette, generate_eira_scene,
    generate_frank_sprite,
)
from src.data.strings import STRINGS


class DeathScene(SceneBase):
    """A death ending — dark, dry, deadpan."""

    def __init__(self, death_id):
        super().__init__()
        self.death_id = death_id

    @property
    def SCENE_ID(self):
        return f"death_{self.death_id}"

    def setup(self):
        data = self.get_scene_data(self.death_id)
        self.text_blocks = [(t, RED) for t in data.get("texts", ["Frank is no more."])]
        self.text_blocks.append(
            (self.get_string("death_footer"), DARK_GRAY)
        )
        self.background = generate_death_vignette()
        self.choices = [
            (self.get_string("try_again"), None),
        ]

    def on_choice(self, index):
        from src.scenes.chapters.ch01_bar import BarScene
        self.scene_manager.game_flags.clear()
        self.scene_manager.visited_scenes.clear()
        self.scene_manager.franks_met.clear()
        self.goto(BarScene())


class LostScene(SceneBase):
    """A lost ending — wistful, ironic."""

    def __init__(self, lost_id):
        super().__init__()
        self.lost_id = lost_id

    @property
    def SCENE_ID(self):
        return f"lost_{self.lost_id}"

    def setup(self):
        data = self.get_scene_data(self.lost_id)
        self.text_blocks = [(t, MID_GRAY) for t in data.get("texts", ["Frank wandered off."])]
        self.background = generate_lost_vignette()
        self.choices = [
            (self.get_string("try_again"), None),
        ]

    def on_choice(self, index):
        from src.scenes.chapters.ch01_bar import BarScene
        self.scene_manager.game_flags.clear()
        self.scene_manager.visited_scenes.clear()
        self.scene_manager.franks_met.clear()
        self.goto(BarScene())


class VictoryScene(SceneBase):
    """Eira — the destination. Dawn. First light."""
    SCENE_ID = "eira"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [(t, WHITE) for t in data["texts"]]
        self.background = generate_eira_scene()
        self.choices = [
            (self.get_string("watch_dawn"), None),
        ]

    def on_choice(self, index):
        from src.scenes.dawn import DawnScene
        self.goto(DawnScene())


class CreditsScene(SceneBase):
    """Credits — show all Franks encountered, grayed out if they didn't make it."""
    SCENE_ID = "credits"

    def __init__(self):
        super().__init__()
        self.scroll_y = INTERNAL_HEIGHT
        self.scroll_speed = 30
        self.credit_surfaces = []
        self.done = False

    def setup(self):
        self.phase = "waiting"
        self._build_credits()

    def _build_credits(self):
        renderer = self.scene_manager.renderer
        font = renderer.font
        small = renderer.small_font
        lang = self.scene_manager.language
        s = STRINGS.get(lang, STRINGS["en"])
        lines = []

        # Color map for credits_roles
        color_map = {
            "gold": PEKKA_COLOR,
            "white": WHITE,
            "mid": MID_GRAY,
            "dark": DARK_GRAY,
        }

        # Title
        title_font = pygame.font.SysFont(FONT_NAME, 28)
        title = title_font.render(s["credits_title"], True, WHITE)
        lines.append((title, 0))

        y = 50
        sub = font.render(s["credits_subtitle"], True, MID_GRAY)
        lines.append((sub, y))
        y += 50

        # The Franks
        header = font.render(s["credits_franks_header"], True, WHITE)
        lines.append((header, y))
        y += 28

        met = self.scene_manager.franks_met
        for name, frank_id in s["credits_frank_names"]:
            if frank_id in met or frank_id == "player":
                color = FRANK_COLORS.get(frank_id, WHITE)
            else:
                color = (30, 30, 30)
            line = font.render(name, True, color)
            lines.append((line, y))
            y += 20

        y += 20
        pekka = font.render(s["credits_pekka"], True, PEKKA_COLOR)
        lines.append((pekka, y))
        y += 50

        # Inspired by
        insp = small.render(s["credits_inspired"], True, DARK_GRAY)
        lines.append((insp, y))
        y += 50

        # Production
        credits_header = font.render(s["credits_production"], True, WHITE)
        lines.append((credits_header, y))
        y += 30

        for text, color_key in s["credits_roles"]:
            if text:
                color = color_map.get(color_key, DARK_GRAY)
                line = small.render(text, True, color)
                lines.append((line, y))
            y += 16

        y += 40

        # Special thanks
        thanks_header = font.render(s["credits_thanks_header"], True, WHITE)
        lines.append((thanks_header, y))
        y += 28
        for text in s["credits_thanks"]:
            if text:
                line = small.render(text, True, MID_GRAY)
                lines.append((line, y))
            y += 16

        y += 50

        # Claude note
        tired_header = font.render(s["credits_claude_header"], True, DARK_GRAY)
        lines.append((tired_header, y))
        y += 28
        for text in s["credits_claude_note"]:
            if text:
                line = small.render(text, True, DARK_GRAY)
                lines.append((line, y))
            y += 16

        y += 60
        thanks = font.render(s["credits_thanks_final"], True, MID_GRAY)
        lines.append((thanks, y))
        y += 50

        restart = font.render(s["credits_restart"], True, DARK_GRAY)
        lines.append((restart, y))

        self.credit_lines = lines
        self.total_height = y + 60

    def update(self, dt, input_handler):
        self.scroll_y -= self.scroll_speed * (dt / 1000.0)

        if input_handler.is_pressed(pygame.K_SPACE):
            self.scroll_y -= self.scroll_speed * 2 * (dt / 1000.0)

        if self.scroll_y < -self.total_height:
            self.done = True

        if input_handler.just_pressed(pygame.K_RETURN):
            from src.scenes.chapters.ch01_bar import BarScene
            self.scene_manager.game_flags.clear()
            self.scene_manager.visited_scenes.clear()
            self.scene_manager.franks_met.clear()
            self.goto(BarScene())

    def draw(self, renderer):
        for surface, base_y in self.credit_lines:
            draw_y = int(self.scroll_y + base_y)
            if -50 < draw_y < INTERNAL_HEIGHT + 50:
                x = (INTERNAL_WIDTH - surface.get_width()) // 2
                renderer.surface.blit(surface, (x, draw_y))
