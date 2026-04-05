from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, FRANK_COLORS, MID_GRAY
from src.data.story import SCENES
from src.engine.pixel_art import generate_tunnel_scene, generate_frank_sprite
from src.data.constants import INTERNAL_WIDTH, INTERNAL_HEIGHT


class TunnelScene(SceneBase):
    SCENE_ID = "ch05_tunnels"

    def setup(self):
        data = SCENES[self.SCENE_ID]
        self.text_blocks = [
            (data["texts"][0], MID_GRAY),
            (data["texts"][1], FRANK_COLORS["frank_7"]),
            (data["texts"][2], FRANK_COLORS["frank_7"]),
        ]
        self.background = generate_tunnel_scene()
        self.meet_frank("frank_7")

        from src.scenes.chapters.ch07_park import ParkScene
        from src.scenes.chapters.ch04_metro import MetroScene
        from src.scenes.endings import DeathScene

        self.choices = [
            (data["choices"][0], ParkScene()),
            (data["choices"][1], DeathScene("death_tunnel_train")),
            (data["choices"][2], MetroScene()),
        ]
