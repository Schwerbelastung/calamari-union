from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_kaivopuisto_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class KaivopuistoScene(SceneBase):
    SCENE_ID = "ch10_kaivopuisto"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_12"]),
            (data["texts"][2], WHITE),
        ]
        self.background = generate_kaivopuisto_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_12"], scale=3)
        self.background.blit(sprite, (300, 175))
        self.meet_frank("frank_12")

        from src.scenes.endings import DeathScene, VictoryScene

        self._victory = VictoryScene()

        self.choices = [
            (data["choices"][0], self._victory),
            (data["choices"][1], None),
            (data["choices"][2], DeathScene("death_street_patrol")),
        ]

    def on_choice(self, index):
        if index == 1 and len(self.choices) > 2:
            self.text_blocks.append(
                (self.get_extra("talk_1"), FRANK_COLORS["frank_12"])
            )
            self.text_blocks.append(
                (self.get_extra("talk_2"), MID_GRAY)
            )
            self.text_blocks.append(
                (self.get_extra("talk_3"), WHITE)
            )
            self.current_block = len(self.text_blocks) - 3
            self.scene_manager.renderer.start_typewriter(
                self.text_blocks[self.current_block][0],
                self.text_blocks[self.current_block][1],
            )
            self.phase = "text"
            self.choices = [
                (self.get_extra("talk_choice"), self._victory),
            ]
        else:
            super().on_choice(index)
