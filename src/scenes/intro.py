import pygame
from src.scenes.scene_base import SceneBase
from src.data.constants import WHITE, MID_GRAY, DARK_GRAY, INTERNAL_WIDTH


class IntroScene(SceneBase):
    SCENE_ID = "intro"
    ALLOW_UNDO = False

    def __init__(self, next_scene):
        super().__init__()
        self.next_scene = next_scene

    def setup(self):
        data = self.get_scene_data()
        colors = [MID_GRAY, WHITE, MID_GRAY, WHITE, MID_GRAY, WHITE]
        self.text_blocks = [
            (data["texts"][i], colors[i]) for i in range(len(data["texts"]))
        ]
        self.choices = [
            (data["choices"][0], self.next_scene),
        ]
