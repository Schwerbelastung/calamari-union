from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_bulevardi_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class BulevardiScene(SceneBase):
    SCENE_ID = "ch09_bulevardi"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], FRANK_COLORS["frank_18"]),
        ]
        self.background = generate_bulevardi_scene()

        sprite = generate_frank_sprite(FRANK_COLORS["frank_18"], scale=3)
        self.background.blit(sprite, (225, 170))
        self.meet_frank("frank_18")

        from src.scenes.chapters.ch10_kaivopuisto import KaivopuistoScene
        from src.scenes.endings import VictoryScene, LostScene

        self.choices = [
            (data["choices"][0], VictoryScene()),
            (data["choices"][1], LostScene("lost_kiosk")),
            (data["choices"][2], KaivopuistoScene()),
        ]
