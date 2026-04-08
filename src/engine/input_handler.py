import pygame


class InputHandler:
    def __init__(self):
        self.keys_pressed = set()
        self.keys_just_pressed = set()
        self.quit_requested = False
        self.mouse_just_clicked = False
        self.mouse_click_pos = (0, 0)

    def update(self, events):
        self.keys_just_pressed.clear()
        self.mouse_just_clicked = False
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_requested = True
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed.add(event.key)
                self.keys_just_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                self.keys_pressed.discard(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_just_clicked = True
                self.mouse_click_pos = event.pos

    def is_pressed(self, key):
        return key in self.keys_pressed

    def just_pressed(self, key):
        return key in self.keys_just_pressed

    def any_key_just_pressed(self):
        return len(self.keys_just_pressed) > 0
