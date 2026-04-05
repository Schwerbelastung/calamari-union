import pygame
from src.scenes.scene_base import SceneBase
from src.data.constants import (
    INTERNAL_WIDTH, INTERNAL_HEIGHT, WHITE, DARK_GRAY, MID_GRAY, BLACK,
)


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

    def setup(self):
        renderer = self.scene_manager.renderer
        # Pre-render title
        title_font = pygame.font.Font(None, 36)
        self.title_surface = title_font.render("C A L A M A R I", False, WHITE)
        self.title_surface2 = title_font.render("U N I O N", False, WHITE)
        sub_font = pygame.font.Font(None, 14)
        self.subtitle_surface = sub_font.render(
            "A text adventure inspired by the film by Aki Kaurismaki", False, MID_GRAY
        )
        self.prompt_surface = renderer.small_font.render(
            "Press ENTER to begin", False, DARK_GRAY
        )
        # Generate the Helsinki skyline silhouette
        self._generate_skyline()

    def _generate_skyline(self):
        import random
        self.skyline = pygame.Surface((INTERNAL_WIDTH, 80), pygame.SRCALPHA)
        x = 0
        while x < INTERNAL_WIDTH:
            w = random.randint(20, 60)
            h = random.randint(20, 65)
            pygame.draw.rect(self.skyline, (12, 12, 16), (x, 80 - h, w, h))
            # Windows
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
                self.phase = "waiting"
        elif self.phase == "waiting":
            self.prompt_alpha = int(abs((self.timer % 2000) - 1000) / 1000 * 180) + 40

        if input_handler.just_pressed(pygame.K_RETURN):
            self.goto(self.next_scene)

    def draw(self, renderer):
        # Skyline at bottom
        renderer.surface.blit(self.skyline, (0, INTERNAL_HEIGHT - 80))

        # Title
        if self.title_alpha > 0:
            t = self.title_surface.copy()
            t.set_alpha(self.title_alpha)
            tx = (INTERNAL_WIDTH - t.get_width()) // 2
            renderer.surface.blit(t, (tx, 100))
            t2 = self.title_surface2.copy()
            t2.set_alpha(self.title_alpha)
            tx2 = (INTERNAL_WIDTH - t2.get_width()) // 2
            renderer.surface.blit(t2, (tx2, 135))

        # Subtitle
        if self.subtitle_alpha > 0:
            st = self.subtitle_surface.copy()
            st.set_alpha(self.subtitle_alpha)
            stx = (INTERNAL_WIDTH - st.get_width()) // 2
            renderer.surface.blit(st, (stx, 175))

        # Prompt
        if self.phase == "waiting" and self.prompt_alpha > 0:
            p = self.prompt_surface.copy()
            p.set_alpha(self.prompt_alpha)
            px = (INTERNAL_WIDTH - p.get_width()) // 2
            renderer.surface.blit(p, (px, 240))
