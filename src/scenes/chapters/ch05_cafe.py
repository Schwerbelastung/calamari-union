from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.engine.pixel_art import generate_cafe_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class CafeScene(SceneBase):
    SCENE_ID = "ch05_cafe"

    def setup(self):
        data = self.get_scene_data()
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], MID_GRAY),
            (data["texts"][2], FRANK_COLORS["frank_14"]),
        ]
        self.background = generate_cafe_scene()

        colors = [WHITE, FRANK_COLORS["frank_2"], MID_GRAY, FRANK_COLORS["frank_14"]]
        positions = [(90, 222), (230, 222), (370, 222), (500, 200)]
        for pos, color in zip(positions, colors):
            sprite = generate_frank_sprite(color, scale=2)
            self.background.blit(sprite, pos)
        self.meet_frank("frank_14")

        from src.scenes.chapters.ch06_limo import LimoScene
        from src.scenes.chapters.ch06_market import MarketScene
        from src.scenes.endings import LostScene

        self.choices = [
            (data["choices"][0], LimoScene()),
            (data["choices"][1], MarketScene()),
            (data["choices"][2], LostScene("lost_cafe")),
        ]
