import pygame


class SpriteAnimation:
    """Frame-based sprite animation from a spritesheet or list of frames."""

    def __init__(self, frames, frame_duration=150, loop=True):
        self.frames = frames  # list of pygame.Surface
        self.frame_duration = frame_duration  # ms per frame
        self.loop = loop
        self.current_frame = 0
        self.timer = 0
        self.finished = False

    def update(self, dt):
        if self.finished:
            return
        self.timer += dt
        while self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    self.finished = True

    def get_frame(self):
        return self.frames[self.current_frame]

    def reset(self):
        self.current_frame = 0
        self.timer = 0
        self.finished = False


class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.age = 0

    def update(self, dt):
        dt_s = dt / 1000.0
        self.x += self.vx * dt_s
        self.y += self.vy * dt_s
        self.age += dt

    @property
    def alive(self):
        return self.age < self.lifetime

    @property
    def alpha(self):
        return max(0, 1.0 - self.age / self.lifetime)


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add(self, particle):
        self.particles.append(particle)

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
        self.particles = [p for p in self.particles if p.alive]

    def draw(self, surface):
        for p in self.particles:
            alpha = int(p.alpha * 255)
            color = (*p.color[:3], alpha) if len(p.color) == 3 else p.color
            # Simple 1px or 2px particle
            if alpha > 30:
                surface.set_at((int(p.x), int(p.y)), p.color[:3])


class RainSystem(ParticleSystem):
    """Rain falling across the screen — very Helsinki."""

    def __init__(self, width, height, intensity=40):
        super().__init__()
        self.width = width
        self.height = height
        self.intensity = intensity  # particles per second
        self.spawn_timer = 0

    def update(self, dt):
        import random
        self.spawn_timer += dt
        spawn_interval = 1000.0 / self.intensity
        while self.spawn_timer >= spawn_interval:
            self.spawn_timer -= spawn_interval
            x = random.randint(0, self.width)
            self.add(Particle(
                x=x, y=0,
                vx=random.uniform(-10, -5),
                vy=random.uniform(120, 180),
                color=(150, 160, 180),
                lifetime=random.uniform(2000, 4000),
            ))
        super().update(dt)

    def draw(self, surface):
        for p in self.particles:
            if p.alive:
                x, y = int(p.x), int(p.y)
                if 0 <= x < self.width and 0 <= y < self.height - 1:
                    surface.set_at((x, y), (100, 110, 130))
                    if y + 1 < self.height:
                        surface.set_at((x, y + 1), (70, 80, 100))
