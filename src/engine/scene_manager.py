import copy


class SceneManager:
    """Manages scene transitions and the scene stack."""

    def __init__(self, renderer, music=None):
        self.renderer = renderer
        self.music = music
        self.current_scene = None
        self.next_scene = None
        self.transitioning = False
        self.transition_phase = None  # "out" or "in"
        self.language = "en"  # "en" or "fi"
        self.game_flags = {}  # persistent flags across scenes (e.g. "has_map")
        self.visited_scenes = []  # track which scenes were visited
        self.franks_met = []  # track which Franks were encountered
        self.last_scene_id = None
        # Undo history — stores (scene_class, scene_id, flags_snapshot, franks_snapshot)
        self.history = []
        self.max_history = 20

    def set_scene(self, scene, immediate=False):
        # Save current scene to history before switching (skip if no current scene)
        if self.current_scene is not None:
            self.history.append({
                "scene_class": type(self.current_scene),
                "scene_id": getattr(self.current_scene, 'SCENE_ID', None),
                "init_args": self._get_init_args(self.current_scene),
                "flags": dict(self.game_flags),
                "franks": list(self.franks_met),
                "visited": list(self.visited_scenes),
            })
            if len(self.history) > self.max_history:
                self.history.pop(0)

        if immediate or self.current_scene is None:
            self.current_scene = scene
            self.current_scene.enter(self)
            self.renderer.start_fade_in()
        else:
            self.next_scene = scene
            self.transitioning = True
            self.transition_phase = "out"
            self.renderer.start_fade_out()

    def _get_init_args(self, scene):
        """Extract constructor args for scenes that need them (death/lost scenes)."""
        if hasattr(scene, 'death_id'):
            return (scene.death_id,)
        if hasattr(scene, 'lost_id'):
            return (scene.lost_id,)
        return ()

    def undo(self):
        """Go back to the previous scene. Returns True if successful."""
        if not self.history:
            return False
        snapshot = self.history.pop()
        # Restore state
        self.game_flags = snapshot["flags"]
        self.franks_met = snapshot["franks"]
        self.visited_scenes = snapshot["visited"]
        # Recreate the scene
        scene_class = snapshot["scene_class"]
        init_args = snapshot["init_args"]
        scene = scene_class(*init_args)
        # Set it without adding to history again
        self.next_scene = scene
        self.transitioning = True
        self.transition_phase = "out"
        self.renderer.start_fade_out()
        return True

    def update(self, dt, input_handler):
        # Always update fade (handles both transition fades and immediate fade-ins)
        if self.renderer.is_fading:
            done = self.renderer.update_fade()
            if done and self.transitioning:
                if self.transition_phase == "out":
                    # Switch scenes
                    if self.current_scene:
                        self.current_scene.exit()
                    self.current_scene = self.next_scene
                    self.next_scene = None
                    self.current_scene.enter(self)
                    self.transition_phase = "in"
                    self.renderer.start_fade_in()
                elif self.transition_phase == "in":
                    self.transitioning = False
                    self.transition_phase = None

        if self.current_scene and not self.transitioning:
            self.current_scene.update(dt, input_handler)

    def draw(self):
        if self.current_scene:
            self.current_scene.draw(self.renderer)
        self.renderer.draw_fade()

    def set_flag(self, key, value=True):
        self.game_flags[key] = value

    def get_flag(self, key, default=False):
        return self.game_flags.get(key, default)

    def record_scene(self, scene_id):
        if scene_id not in self.visited_scenes:
            self.visited_scenes.append(scene_id)
        self.last_scene_id = scene_id
        # Trigger music for this scene
        if self.music:
            self.music.play_for_scene(scene_id)

    def meet_frank(self, frank_id):
        if frank_id not in self.franks_met:
            self.franks_met.append(frank_id)
