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
        self.text_blocks = [
            ("Helsinki. Late at night. Or early in the morning. "
             "It makes no difference in Kallio.", MID_GRAY),
            ("Fourteen men named Frank have gathered in a bar. "
             "They share a name, a cigarette brand, and a conviction "
             "that life must be better somewhere else.", WHITE),
            ("That somewhere is Eira. The seaside. The promised land. "
             "Or at least a neighborhood with better restaurants.", MID_GRAY),
            ("A fifteenth man, Pekka, has joined them. "
             "He is not named Frank. He speaks English. "
             "Nobody asks why.", WHITE),
            ("Tonight, they move. Through alleys, tunnels, and the "
             "endless dark of a Finnish night. Most will not make it. "
             "Some will die. Some will simply... stop.", MID_GRAY),
            ("You are Frank.", WHITE),
        ]
        self.choices = [
            ("Begin the journey", self.next_scene),
        ]
