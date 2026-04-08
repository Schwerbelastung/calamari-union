import pygame
from src.data.constants import (
    WHITE, DARK_GRAY, TEXT_MARGIN_X, TEXT_MARGIN_TOP, SCENE_PAUSE,
    INTERNAL_WIDTH, INTERNAL_HEIGHT,
)
from src.data.story import SCENES, SCENES_FI
from src.data.strings import STRINGS


class SceneBase:
    """Base class for all game scenes."""

    SCENE_ID = "base"
    ALLOW_UNDO = True  # subclasses can disable (e.g. splash, intro)

    def __init__(self):
        self.scene_manager = None
        self.background = None
        self.text_blocks = []       # list of (text, color) to display in sequence
        self.current_block = 0
        self.choices = []           # list of (text, target_scene_or_callback)
        self.choice_colors = None   # optional per-choice colors
        self.selected_choice = 0
        self.phase = "text"         # "text", "choices", "waiting"
        self.pause_timer = 0
        self.rain = None            # optional RainSystem

    def enter(self, scene_manager):
        self.scene_manager = scene_manager
        scene_manager.record_scene(self.SCENE_ID)
        self.setup()
        if self.text_blocks:
            scene_manager.renderer.start_typewriter(
                self.text_blocks[0][0],
                self.text_blocks[0][1],
            )

    def exit(self):
        pass

    def setup(self):
        """Override to set up text_blocks, choices, background, etc."""
        pass

    def update(self, dt, input_handler):
        renderer = self.scene_manager.renderer

        if self.rain:
            self.rain.update(dt)

        # Undo with Backspace — available in all phases
        if self.ALLOW_UNDO and input_handler.just_pressed(pygame.K_BACKSPACE):
            if self.scene_manager.undo():
                return

        if self.phase == "text":
            # Advance typewriter
            fast = input_handler.is_pressed(pygame.K_SPACE)
            renderer.update_typewriter(dt, fast=fast)

            if input_handler.just_pressed(pygame.K_RETURN):
                if not renderer.tw_done:
                    renderer.skip_typewriter()
                else:
                    # Move to next text block or choices
                    self.current_block += 1
                    if self.current_block < len(self.text_blocks):
                        text, color = self.text_blocks[self.current_block]
                        renderer.start_typewriter(text, color)
                    else:
                        if self.choices:
                            self.phase = "choices"
                            self.selected_choice = 0
                        else:
                            self.phase = "waiting"

        elif self.phase == "choices":
            if input_handler.just_pressed(pygame.K_UP):
                self.selected_choice = (self.selected_choice - 1) % len(self.choices)
            elif input_handler.just_pressed(pygame.K_DOWN):
                self.selected_choice = (self.selected_choice + 1) % len(self.choices)
            elif input_handler.just_pressed(pygame.K_RETURN):
                self.on_choice(self.selected_choice)

        elif self.phase == "waiting":
            if input_handler.just_pressed(pygame.K_RETURN):
                self.on_continue()

    def draw(self, renderer):
        if self.background:
            renderer.draw_background(self.background)

        if self.rain:
            self.rain.draw(renderer.surface)

        # Calculate how much vertical space choices need
        choice_reserve = 0
        if self.phase == "choices" and self.choices:
            line_h = renderer.font.get_linesize() + 6
            choice_reserve = len(self.choices) * line_h + 50

        max_y = INTERNAL_HEIGHT - max(choice_reserve, 30)

        # Measure all content to determine scroll offset
        block_heights = []
        for i in range(self.current_block):
            text, color = self.text_blocks[i]
            h = renderer.measure_text_wrapped(text)
            block_heights.append(h + 8)

        # Measure current typewriter block
        tw_height = 0
        if self.current_block < len(self.text_blocks):
            text, color = self.text_blocks[self.current_block]
            tw_height = renderer.measure_text_wrapped(text)

        total_height = sum(block_heights) + tw_height
        scroll = 0
        if TEXT_MARGIN_TOP + total_height > max_y:
            scroll = TEXT_MARGIN_TOP + total_height - max_y

        # Draw text blocks with scroll offset
        y = TEXT_MARGIN_TOP - scroll
        for i in range(self.current_block):
            text, color = self.text_blocks[i]
            if y + block_heights[i] > 0:  # skip fully scrolled-off blocks
                y = renderer.draw_text_wrapped(text, TEXT_MARGIN_X, y, color)
                y += 8
            else:
                y += block_heights[i]

        # Draw current typewriter text
        if self.current_block < len(self.text_blocks):
            y = renderer.draw_typewriter(TEXT_MARGIN_X, y)

        # Draw choices
        if self.phase == "choices":
            choice_texts = [c[0] for c in self.choices]
            renderer.draw_choices(choice_texts, self.selected_choice, colors=self.choice_colors)

        # Undo hint
        if self.ALLOW_UNDO and self.scene_manager.history:
            hint = self.get_string("undo_hint")
            renderer.draw_text(hint, INTERNAL_WIDTH - 160, INTERNAL_HEIGHT - 16,
                               DARK_GRAY, renderer.small_font)

    def on_choice(self, index):
        """Handle a choice selection. Override for custom logic."""
        if index < len(self.choices):
            _, target = self.choices[index]
            if callable(target):
                target()
            elif isinstance(target, SceneBase):
                self.scene_manager.set_scene(target)

    def on_continue(self):
        """Called when player presses enter with no choices left. Override as needed."""
        pass

    def goto(self, scene):
        self.scene_manager.set_scene(scene)

    def set_flag(self, key, value=True):
        self.scene_manager.set_flag(key, value)

    def get_flag(self, key, default=False):
        return self.scene_manager.get_flag(key, default)

    def meet_frank(self, frank_id):
        self.scene_manager.meet_frank(frank_id)

    def get_scene_data(self, scene_id=None):
        """Get scene data dict for current language."""
        sid = scene_id or self.SCENE_ID
        if self.scene_manager.language == "fi":
            return SCENES_FI.get(sid, SCENES.get(sid, {}))
        return SCENES.get(sid, {})

    def get_extra(self, key):
        """Get an extras string for current language."""
        data = self.get_scene_data()
        return data.get("extras", {}).get(key, "")

    def get_string(self, key):
        """Get a UI string for current language."""
        lang = self.scene_manager.language
        return STRINGS.get(lang, STRINGS["en"]).get(key, key)
