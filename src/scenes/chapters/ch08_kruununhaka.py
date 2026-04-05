import random
from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_kruununhaka_scene
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class KruununhakaScene(SceneBase):
    SCENE_ID = "ch08_kruununhaka"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_kruununhaka_scene()

        from src.scenes.chapters.ch09_esplanadi import EsplanadiScene
        from src.scenes.endings import DeathScene

        self._esplanadi = EsplanadiScene()
        self._death_stop = DeathScene("death_police_stop")
        self._death_run = DeathScene("death_police_run")

        self.choices = [
            (data["choices"][0], self._esplanadi),
            (data["choices"][1], None),  # 50/50 handled in on_choice
            (data["choices"][2], self._death_run),
        ]

    def on_choice(self, index):
        if index == 1 and len(self.choices) > 2:
            # Deterministic based on visited scenes for fairness
            seed = len(self.scene_manager.visited_scenes)
            if self.get_flag("has_map"):
                # Map gives you better odds
                safe = True
            else:
                safe = (seed % 2 == 0)

            if safe:
                self.text_blocks.append(
                    ("Frank walks. The police car passes. Its occupants are "
                     "drinking coffee and arguing about football. They do not "
                     "look at Frank. Frank does not look at them. "
                     "Two ships in the night.", MID_GRAY)
                )
                self.current_block = len(self.text_blocks) - 1
                self.scene_manager.renderer.start_typewriter(
                    self.text_blocks[-1][0], self.text_blocks[-1][1]
                )
                self.phase = "text"
                self.choices = [
                    ("Continue to Esplanadi", self._esplanadi),
                ]
            else:
                self.goto(self._death_stop)
        else:
            super().on_choice(index)
