import pygame
from src.scenes.scene_base import SceneBase
from src.data.constants import (
    INTERNAL_WIDTH, INTERNAL_HEIGHT, WHITE, DARK_GRAY, MID_GRAY, BLACK,
    FONT_NAME,
)
from src.data.strings import STRINGS


class SplashScene(SceneBase):
    SCENE_ID = "splash"
    ALLOW_UNDO = False

    def __init__(self, next_scene):
        super().__init__()
        self.next_scene = next_scene
        self.timer = 0
        self.title_alpha = 0
        self.subtitle_alpha = 0
        self.prompt_alpha = 0
        self.phase = "fade_title"
        self.title_surface = None
        self.subtitle_surface = None
        self.selected_lang = 0  # 0 = English, 1 = Suomeksi (käännös), 2 = Kaurismäki-versio

    def setup(self):
        renderer = self.scene_manager.renderer
        title_font = pygame.font.SysFont(FONT_NAME, 36)
        self.title_surface = title_font.render("C A L A M A R I", True, WHITE)
        self.title_surface2 = title_font.render("U N I O N", True, WHITE)
        sub_font = pygame.font.SysFont(FONT_NAME, 14)
        self.subtitle_surface = sub_font.render(
            STRINGS["en"]["subtitle"], True, MID_GRAY
        )
        # Language options
        self.lang_prompt_surface = renderer.small_font.render(
            STRINGS["en"]["lang_prompt"], True, MID_GRAY
        )
        self.lang_en_surface = renderer.font.render(
            STRINGS["en"]["lang_en"], True, WHITE
        )
        self.lang_fi_surface = renderer.font.render(
            STRINGS["en"]["lang_fi"], True, WHITE
        )
        self.lang_en_dim = renderer.font.render(
            STRINGS["en"]["lang_en"], True, DARK_GRAY
        )
        self.lang_fi_dim = renderer.font.render(
            STRINGS["en"]["lang_fi"], True, DARK_GRAY
        )
        self._generate_skyline()

    def _generate_skyline(self):
        import random
        self.skyline = pygame.Surface((INTERNAL_WIDTH, 80), pygame.SRCALPHA)
        x = 0
        while x < INTERNAL_WIDTH:
            w = random.randint(20, 60)
            h = random.randint(20, 65)
            pygame.draw.rect(self.skyline, (12, 12, 16), (x, 80 - h, w, h))
            for wy in range(80 - h + 5, 75, 8):
                for wx in range(x + 4, x + w - 4, 8):
                    if random.random() < 0.15:
                        pygame.draw.rect(self.skyline, (35, 32, 20), (wx, wy, 3, 4))
            x += w + random.randint(2, 8)

    def update(self, dt, input_handler):
        self.timer += dt

        if self.phase == "fade_title":
            self.title_alpha = min(255, self.title_alpha + 3)
            if self.title_alpha >= 255:
                self.phase = "fade_subtitle"
        elif self.phase == "fade_subtitle":
            self.subtitle_alpha = min(255, self.subtitle_alpha + 4)
            if self.subtitle_alpha >= 255:
                self.phase = "lang_select"
        elif self.phase == "lang_select":
            self.prompt_alpha = min(255, self.prompt_alpha + 5)
            if input_handler.just_pressed(pygame.K_UP):
                self.selected_lang = max(0, self.selected_lang - 1)
            elif input_handler.just_pressed(pygame.K_DOWN):
                self.selected_lang = min(2, self.selected_lang + 1)
            elif input_handler.just_pressed(pygame.K_RETURN):
                lang_map = {0: "en", 1: "fi", 2: "fi2"}
                self.scene_manager.language = lang_map[self.selected_lang]
                self.goto(self.next_scene)

    def draw(self, renderer):
        # Skyline at bottom
        renderer.surface.blit(self.skyline, (0, INTERNAL_HEIGHT - 80))

        # Title
        if self.title_alpha > 0:
            t = self.title_surface.copy()
            t.set_alpha(self.title_alpha)
            tx = (INTERNAL_WIDTH - t.get_width()) // 2
            renderer.surface.blit(t, (tx, 80))
            t2 = self.title_surface2.copy()
            t2.set_alpha(self.title_alpha)
            tx2 = (INTERNAL_WIDTH - t2.get_width()) // 2
            renderer.surface.blit(t2, (tx2, 115))

        # Subtitle
        if self.subtitle_alpha > 0:
            st = self.subtitle_surface.copy()
            st.set_alpha(self.subtitle_alpha)
            stx = (INTERNAL_WIDTH - st.get_width()) // 2
            renderer.surface.blit(st, (stx, 155))

        # Language selection
        if self.phase == "lang_select" and self.prompt_alpha > 0:
            # Prompt
            lp = self.lang_prompt_surface.copy()
            lp.set_alpha(self.prompt_alpha)
            lpx = (INTERNAL_WIDTH - lp.get_width()) // 2
            renderer.surface.blit(lp, (lpx, 195))

            ticks = pygame.time.get_ticks()
            arrow_visible = (ticks // 500) % 2 == 0

            options = [
                STRINGS["en"]["lang_en"],
                STRINGS["en"]["lang_fi"],
                STRINGS["en"]["lang_fi2"],
            ]
            for i, label in enumerate(options):
                prefix = "> " if i == self.selected_lang and arrow_visible else "  "
                color = WHITE if i == self.selected_lang else DARK_GRAY
                surf = renderer.font.render(prefix + label, True, color)
                surf.set_alpha(self.prompt_alpha)
                sx = (INTERNAL_WIDTH - surf.get_width()) // 2
                renderer.surface.blit(surf, (sx, 215 + i * 22))
