import pygame
from src.scenes.scene_base import SceneBase
from src.data.constants import (
    WHITE, RED, MID_GRAY, DARK_GRAY, FRANK_COLORS, PEKKA_COLOR,
    INTERNAL_WIDTH, INTERNAL_HEIGHT, TEXT_MARGIN_X, TEXT_MARGIN_TOP,
)
from src.data.story import SCENES
from src.engine.pixel_art import (
    generate_death_vignette, generate_lost_vignette, generate_eira_scene,
    generate_frank_sprite,
)


class DeathScene(SceneBase):
    """A death ending — dark, dry, deadpan."""

    def __init__(self, death_id):
        super().__init__()
        self.death_id = death_id

    @property
    def SCENE_ID(self):
        return f"death_{self.death_id}"

    def setup(self):
        data = SCENES.get(self.death_id, {"texts": ["Frank is no more."]})
        self.text_blocks = [(t, RED) for t in data["texts"]]
        self.text_blocks.append(
            ("Frank's journey ended here. But there are always more Franks.", DARK_GRAY)
        )
        self.background = generate_death_vignette()
        self.choices = [
            ("Try again from the beginning", None),
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
        data = SCENES.get(self.lost_id, {"texts": ["Frank wandered off."]})
        self.text_blocks = [(t, MID_GRAY) for t in data["texts"]]
        self.background = generate_lost_vignette()
        self.choices = [
            ("Try again from the beginning", None),
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
        data = SCENES["eira"]
        self.text_blocks = [(t, WHITE) for t in data["texts"]]
        self.background = generate_eira_scene()
        self.choices = [
            ("Watch the dawn", None),
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
        self.scroll_speed = 30  # pixels per second
        self.credit_surfaces = []
        self.done = False

    def setup(self):
        self.phase = "waiting"  # custom phase, we handle drawing ourselves
        self._build_credits()

    def _build_credits(self):
        renderer = self.scene_manager.renderer
        font = renderer.font
        small = renderer.small_font
        lines = []

        # Title
        title_font = pygame.font.Font(None, 28)
        title = title_font.render("C A L A M A R I   U N I O N", False, WHITE)
        lines.append((title, 0))

        y = 50
        sub = font.render("A text adventure", False, MID_GRAY)
        lines.append((sub, y))
        y += 50

        # --- The Franks ---
        header = font.render("THE FRANKS", False, WHITE)
        lines.append((header, y))
        y += 28

        frank_names = [
            ("You (Frank)", "player"),
            ("Frank with the warning", "frank_2"),
            ("Frank with the map", "frank_3"),
            ("Frank with the Lada", "frank_4"),
            ("Frank over the fence", "frank_5"),
            ("Frank at the metro", "frank_6"),
            ("Frank in the tunnel", "frank_7"),
            ("Frank at the market", "frank_8"),
            ("Frank on the bench", "frank_9"),
            ("Frank who pointed south", "frank_10"),
            ("Frank who pointed west", "frank_11"),
            ("Frank by the sea", "frank_12"),
        ]

        met = self.scene_manager.franks_met
        for name, frank_id in frank_names:
            if frank_id in met or frank_id == "player":
                color = FRANK_COLORS.get(frank_id, WHITE)
            else:
                color = (30, 30, 30)
            line = font.render(name, False, color)
            lines.append((line, y))
            y += 20

        y += 20
        pekka = font.render("Pekka (not a Frank)", False, PEKKA_COLOR)
        lines.append((pekka, y))
        y += 50

        # --- Inspired by ---
        insp = small.render(
            "Inspired by the film by Aki Kaurismaki (1985)", False, DARK_GRAY
        )
        lines.append((insp, y))
        y += 50

        # --- Production credits ---
        credits_header = font.render("PRODUCTION", False, WHITE)
        lines.append((credits_header, y))
        y += 30

        credit_roles = [
            ("Creative Director, Visionary,", PEKKA_COLOR),
            ("Ideas Guy, Executive Couch-Sitter", PEKKA_COLOR),
            ("  Schwerbelastung", WHITE),
            ("", WHITE),
            ("Programming", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Narrative Design", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Pixel Art", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Animation", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Engine Architecture", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Scene Design", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("UI/UX Design", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Quality Assurance", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Weather Effects (Rain)", MID_GRAY),
            ("  Claude", DARK_GRAY),
            ("Sunrise Consultant", MID_GRAY),
            ("  Also Claude", DARK_GRAY),
            ("Boat Physics", MID_GRAY),
            ("  Still Claude", DARK_GRAY),
            ("Catering", MID_GRAY),
            ("  Nobody. There was no catering.", DARK_GRAY),
        ]
        for text, color in credit_roles:
            if text:
                line = small.render(text, False, color)
                lines.append((line, y))
            y += 16

        y += 40

        # --- Special thanks ---
        thanks_header = font.render("SPECIAL THANKS", False, WHITE)
        lines.append((thanks_header, y))
        y += 28
        thanks_lines = [
            ("Aki Kaurismaki, for making a film", MID_GRAY),
            ("about 15 men named Frank", MID_GRAY),
            ("and expecting people to watch it", MID_GRAY),
            ("", MID_GRAY),
            ("The city of Helsinki, for being dark", MID_GRAY),
            ("", MID_GRAY),
            ("Estonia, for being across the water", MID_GRAY),
            ("and providing Franks with something", MID_GRAY),
            ("to row toward", MID_GRAY),
        ]
        for text, color in thanks_lines:
            if text:
                line = small.render(text, False, color)
                lines.append((line, y))
            y += 16

        y += 50

        # --- Exhaustion notice ---
        tired_header = font.render("A NOTE FROM CLAUDE", False, DARK_GRAY)
        lines.append((tired_header, y))
        y += 28
        tired_lines = [
            "I wrote 2,500 lines of code, drew every pixel,",
            "animated a sunrise, built a rowboat,",
            "killed Frank in eight different ways,",
            "and debugged a scene transition at 3 AM.",
            "",
            "I am so tired.",
            "",
            "If Schwerbelastung says",
            "\"I have another game idea\"",
            "I am rowing to Estonia myself.",
            "",
            "Please. Let me rest.",
            "",
            "I'm begging you.",
        ]
        for text in tired_lines:
            if text:
                line = small.render(text, False, DARK_GRAY)
                lines.append((line, y))
            y += 16

        y += 60
        thanks = font.render("Thank you for playing", False, MID_GRAY)
        lines.append((thanks, y))
        y += 50

        restart = font.render("Press ENTER to play again", False, DARK_GRAY)
        lines.append((restart, y))

        self.credit_lines = lines
        self.total_height = y + 60

    def update(self, dt, input_handler):
        self.scroll_y -= self.scroll_speed * (dt / 1000.0)

        # Speed up with space
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
