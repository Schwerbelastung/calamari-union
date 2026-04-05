"""
CALAMARI UNION — A text adventure
Inspired by the film by Aki Kaurismaki (1985)

Run: python main.py
"""
import sys
import os

# Ensure src is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.engine.game import Game
from src.scenes.splash import SplashScene
from src.scenes.intro import IntroScene
from src.scenes.chapters.ch01_bar import BarScene


def main():
    game = Game()
    bar = BarScene()
    intro = IntroScene(bar)
    splash = SplashScene(intro)
    game.run(splash)


if __name__ == "__main__":
    main()
