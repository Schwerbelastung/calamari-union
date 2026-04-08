import random
from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_esplanadi_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class EsplanadiScene(SceneBase):
    SCENE_ID = "ch09_esplanadi"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_10"]),
            (data["texts"][2], FRANK_COLORS["frank_11"]),
        ]
        self.background = generate_esplanadi_scene()

        sprite10 = generate_frank_sprite(FRANK_COLORS["frank_10"], scale=3)
        sprite11 = generate_frank_sprite(FRANK_COLORS["frank_11"], scale=3)
        self.background.blit(sprite10, (280, 240))
        self.background.blit(sprite11, (330, 240))
        self.meet_frank("frank_10")
        self.meet_frank("frank_11")

        from src.scenes.chapters.ch10_kaivopuisto import KaivopuistoScene
        from src.scenes.chapters.ch09_bulevardi import BulevardiScene
        from src.scenes.endings import LostScene

        self._kaivopuisto = KaivopuistoScene()
        self._lost = LostScene("lost_kamppi")

        self.choices = [
            (data["choices"][0], self._kaivopuisto),
            (data["choices"][1], self._lost),
            (data["choices"][2], None),
            (data["choices"][3], BulevardiScene()),
        ]

    def on_choice(self, index):
        if index == 2 and len(self.choices) > 2:
            seed = len(self.scene_manager.franks_met)
            if seed % 3 != 0:
                self.text_blocks.append(
                    (self.get_extra("follow_south"), FRANK_COLORS["frank_10"])
                )
                self.current_block = len(self.text_blocks) - 1
                self.scene_manager.renderer.start_typewriter(
                    self.text_blocks[-1][0], self.text_blocks[-1][1]
                )
                self.phase = "text"
                self.choices = [
                    (self.get_extra("follow_south_choice"), self._kaivopuisto),
                ]
            else:
                self.text_blocks.append(
                    (self.get_extra("follow_west"), FRANK_COLORS["frank_11"])
                )
                self.current_block = len(self.text_blocks) - 1
                self.scene_manager.renderer.start_typewriter(
                    self.text_blocks[-1][0], self.text_blocks[-1][1]
                )
                self.phase = "text"
                self.choices = [
                    (self.get_extra("follow_west_choice"), self._lost),
                ]
        else:
            super().on_choice(index)
