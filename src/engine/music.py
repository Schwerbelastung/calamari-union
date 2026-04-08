"""
Procedural music generator for Calamari Union.
Generates lo-fi ambient tracks at runtime using waveform synthesis.
No external audio files needed.
"""
import math
import struct
import io
import random
import pygame

SAMPLE_RATE = 22050
CHANNELS = 2       # stereo — matches pygame default mixer
SAMPLE_WIDTH = 2   # 16-bit
MAX_AMP = 16000


# --- Waveform generators ---

def sine(freq, t):
    return math.sin(2 * math.pi * freq * t)


def square(freq, t):
    return 1.0 if sine(freq, t) >= 0 else -1.0


def sawtooth(freq, t):
    phase = (freq * t) % 1.0
    return 2.0 * phase - 1.0


def triangle(freq, t):
    phase = (freq * t) % 1.0
    return 4.0 * abs(phase - 0.5) - 1.0


def noise():
    return random.uniform(-1.0, 1.0)


# --- Note/frequency helpers ---

NOTE_FREQS = {}
_NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
for _oct in range(1, 8):
    for _i, _name in enumerate(_NOTE_NAMES):
        _midi = (_oct + 1) * 12 + _i
        NOTE_FREQS[f"{_name}{_oct}"] = 440.0 * (2 ** ((_midi - 69) / 12.0))


def note_freq(name):
    return NOTE_FREQS.get(name, 440.0)


# --- Envelope ---

def envelope(t, duration, attack=0.05, decay=0.1, sustain=0.6, release=0.3):
    """ADSR envelope."""
    rel_start = duration - release
    if t < attack:
        return t / attack if attack > 0 else 1.0
    elif t < attack + decay:
        return 1.0 - (1.0 - sustain) * ((t - attack) / decay)
    elif t < rel_start:
        return sustain
    elif t < duration:
        return sustain * (1.0 - (t - rel_start) / release)
    return 0.0


def soft_envelope(t, duration):
    """Gentle pad envelope — slow attack, long sustain, slow release."""
    return envelope(t, duration, attack=duration * 0.2, decay=0.0,
                    sustain=0.8, release=duration * 0.3)


# --- Track synthesis ---

def render_samples(duration_sec, sample_func):
    """Render audio samples from a function f(t) -> [-1, 1]. Returns mono samples."""
    n_samples = int(SAMPLE_RATE * duration_sec)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = sample_func(t)
        val = max(-1.0, min(1.0, val))
        samples.append(int(val * MAX_AMP))
    return samples


def samples_to_wav_bytes(samples):
    """Convert mono sample list to stereo WAV file bytes."""
    buf = io.BytesIO()
    n = len(samples)
    # Stereo: each sample is duplicated to L and R channels
    data_size = n * CHANNELS * SAMPLE_WIDTH
    # WAV header
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + data_size))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<I', 16))  # chunk size
    buf.write(struct.pack('<H', 1))   # PCM
    buf.write(struct.pack('<H', CHANNELS))
    buf.write(struct.pack('<I', SAMPLE_RATE))
    buf.write(struct.pack('<I', SAMPLE_RATE * CHANNELS * SAMPLE_WIDTH))
    buf.write(struct.pack('<H', CHANNELS * SAMPLE_WIDTH))
    buf.write(struct.pack('<H', SAMPLE_WIDTH * 8))
    buf.write(b'data')
    buf.write(struct.pack('<I', data_size))
    for s in samples:
        # Write same sample to both L and R channels
        buf.write(struct.pack('<h', s))
        buf.write(struct.pack('<h', s))
    buf.seek(0)
    return buf


def generate_sound(duration_sec, sample_func):
    """Generate a pygame.mixer.Sound from a sample function."""
    samples = render_samples(duration_sec, sample_func)
    wav = samples_to_wav_bytes(samples)
    return pygame.mixer.Sound(wav)


# --- Music tracks (each returns a pygame.mixer.Sound) ---

def gen_track_bar(duration=36.0):
    """Smoky bar — low jazz bass, muted piano chords, cigarette atmosphere."""
    # Minor blues progression in low register — extended
    bass_notes = [
        (note_freq('E2'), 0.0), (note_freq('E2'), 3.0),
        (note_freq('A2'), 6.0), (note_freq('A2'), 9.0),
        (note_freq('E2'), 12.0), (note_freq('B2'), 15.0),
        (note_freq('A2'), 18.0), (note_freq('E2'), 21.0),
        (note_freq('A2'), 24.0), (note_freq('E2'), 27.0),
        (note_freq('B2'), 30.0), (note_freq('A2'), 33.0),
    ]
    # Sparse piano-like chords — extended
    chord_hits = [
        ([note_freq('E3'), note_freq('G3'), note_freq('B3')], 1.5),
        ([note_freq('A3'), note_freq('C4'), note_freq('E4')], 7.0),
        ([note_freq('E3'), note_freq('G3'), note_freq('B3')], 13.0),
        ([note_freq('B3'), note_freq('D4'), note_freq('F#4')], 16.0),
        ([note_freq('A3'), note_freq('C4'), note_freq('E4')], 19.5),
        ([note_freq('E3'), note_freq('G3'), note_freq('B3')], 24.5),
        ([note_freq('A3'), note_freq('C4'), note_freq('E4')], 28.0),
        ([note_freq('B3'), note_freq('D4'), note_freq('F#4')], 31.5),
    ]

    def sample(t):
        val = 0.0
        # Bass — warm sine with slight overdrive
        for freq, start in bass_notes:
            if start <= t < start + 2.8:
                lt = t - start
                env = envelope(lt, 2.8, attack=0.02, decay=0.3, sustain=0.5, release=0.8)
                v = sine(freq, t) * 0.6 + sine(freq * 2, t) * 0.15
                val += v * env * 0.35
        # Chord hits — triangle wave for muted piano feel
        for freqs, start in chord_hits:
            if start <= t < start + 2.0:
                lt = t - start
                env = envelope(lt, 2.0, attack=0.005, decay=0.4, sustain=0.2, release=0.8)
                for f in freqs:
                    val += triangle(f, t) * env * 0.08
        return val

    return generate_sound(duration, sample)


def gen_track_alley(duration=30.0):
    """Dark alleys — ambient drone, distant rumble, tension."""
    base_freq = note_freq('D2')
    fifth = note_freq('A2')

    def sample(t):
        val = 0.0
        # Low drone
        drift = sine(0.07, t) * 2.0
        val += sine(base_freq + drift, t) * 0.2
        val += sine(fifth + drift * 0.5, t) * 0.1
        # Subtle high overtone — eerie
        val += sine(note_freq('D5'), t) * sine(0.15, t) * 0.03
        # Rumble
        val += sine(30 + sine(0.1, t) * 5, t) * 0.08
        return val

    return generate_sound(duration, sample)


def gen_track_metro(duration=30.0):
    """Metro station — fluorescent buzz, industrial echoes."""
    def sample(t):
        val = 0.0
        # Fluorescent light buzz (120Hz hum)
        val += sine(120, t) * 0.06
        val += sine(240, t) * 0.02
        # Slow chord pad — hollow
        pad_freq = note_freq('F#2')
        pad_env = 0.5 + 0.5 * sine(0.05, t)
        val += sawtooth(pad_freq, t) * pad_env * 0.07
        val += sawtooth(pad_freq * 1.5, t) * pad_env * 0.04
        # Distant metallic echoes (irregular pings)
        for i in range(5):
            ping_t = (t + i * 4.3) % 4.3
            if ping_t < 0.3:
                ping_env = envelope(ping_t, 0.3, attack=0.001, decay=0.05, sustain=0.1, release=0.2)
                freq = note_freq('C5') * (1 + i * 0.3)
                val += sine(freq, t) * ping_env * 0.06
        return val

    return generate_sound(duration, sample)


def gen_track_tunnel(duration=30.0):
    """Dark tunnel — deep reverberant drone, dripping water."""
    def sample(t):
        val = 0.0
        # Deep drone — almost subsonic
        drone_freq = note_freq('B1')
        val += sine(drone_freq, t) * 0.25
        val += sine(drone_freq * 1.5, t) * 0.08
        # Slow modulation
        val *= 0.7 + 0.3 * sine(0.04, t)
        # Water drips (periodic sharp sine pings)
        drip_period = 3.7
        drip_t = t % drip_period
        if drip_t < 0.05:
            drip_env = envelope(drip_t, 0.05, attack=0.001, decay=0.01, sustain=0.2, release=0.03)
            val += sine(note_freq('E6'), t) * drip_env * 0.15
        # Second drip, offset
        drip_t2 = (t + 1.8) % 5.1
        if drip_t2 < 0.04:
            drip_env2 = envelope(drip_t2, 0.04, attack=0.001, decay=0.01, sustain=0.15, release=0.02)
            val += sine(note_freq('G6'), t) * drip_env2 * 0.1
        return val

    return generate_sound(duration, sample)


def gen_track_street(duration=33.0):
    """Hämeentie / Kruununhaka — tense urban ambient, slow pulse."""
    def sample(t):
        val = 0.0
        # Pulsing low synth
        pulse_env = 0.5 + 0.5 * sine(0.25, t)
        val += sine(note_freq('E2'), t) * pulse_env * 0.15
        val += sine(note_freq('B2'), t) * pulse_env * 0.08
        # High tension tone — slowly shifting
        shift = sine(0.03, t) * 20
        val += sine(note_freq('G#4') + shift, t) * 0.04
        val += sine(note_freq('D5') + shift * 0.7, t) * 0.025
        # Sparse melodic hint
        mel_t = t % 11.0
        if 4.0 < mel_t < 5.5:
            lt = mel_t - 4.0
            env = soft_envelope(lt, 1.5)
            val += triangle(note_freq('E4'), t) * env * 0.06
        if 8.0 < mel_t < 9.0:
            lt = mel_t - 8.0
            env = soft_envelope(lt, 1.0)
            val += triangle(note_freq('D4'), t) * env * 0.05
        return val

    return generate_sound(duration, sample)


def gen_track_park(duration=36.0):
    """Park scenes — open, quieter, hint of sea, melancholic beauty."""
    def sample(t):
        val = 0.0
        # Warm pad — major feel, open
        pad_a = sine(note_freq('A2'), t) * 0.12
        pad_e = sine(note_freq('E3'), t) * 0.08
        pad_mod = 0.6 + 0.4 * sine(0.06, t)
        val += (pad_a + pad_e) * pad_mod
        # Gentle high melody — pentatonic, sparse — extended
        mel_notes = [
            (note_freq('E4'), 0.0, 2.5),
            (note_freq('G4'), 4.0, 2.0),
            (note_freq('A4'), 8.0, 3.0),
            (note_freq('G4'), 12.5, 2.0),
            (note_freq('E4'), 16.0, 2.5),
            (note_freq('D4'), 20.0, 2.0),
            (note_freq('E4'), 24.0, 2.5),
            (note_freq('A4'), 28.0, 2.0),
            (note_freq('G4'), 31.5, 2.5),
        ]
        for freq, start, dur in mel_notes:
            if start <= t < start + dur:
                lt = t - start
                env = soft_envelope(lt, dur)
                val += sine(freq, t) * env * 0.07
                # Soft octave above
                val += sine(freq * 2, t) * env * 0.02
        return val

    return generate_sound(duration, sample)


def gen_track_market(duration=30.0):
    """Hakaniemi market — bluesy, slightly more alive, tango hint."""
    # Simple tango-ish bass pattern — extended
    bass_pattern = [
        (note_freq('A2'), 0.0), (note_freq('E2'), 1.5),
        (note_freq('A2'), 3.0), (note_freq('C3'), 4.5),
        (note_freq('D3'), 6.0), (note_freq('E3'), 7.5),
        (note_freq('A2'), 9.0), (note_freq('E2'), 10.5),
        (note_freq('A2'), 12.0), (note_freq('C3'), 13.5),
        (note_freq('D3'), 15.0), (note_freq('A2'), 16.5),
        (note_freq('E2'), 18.0), (note_freq('A2'), 19.0),
        (note_freq('D3'), 20.5), (note_freq('E3'), 22.0),
        (note_freq('A2'), 23.5), (note_freq('C3'), 25.0),
        (note_freq('E2'), 26.5), (note_freq('A2'), 28.0),
    ]

    def sample(t):
        val = 0.0
        # Bass line
        for freq, start in bass_pattern:
            if start <= t < start + 1.3:
                lt = t - start
                env = envelope(lt, 1.3, attack=0.01, decay=0.2, sustain=0.4, release=0.5)
                val += sine(freq, t) * env * 0.2
                val += sine(freq * 2, t) * env * 0.05
        # Accordion-like pad (triangle + slight vibrato)
        acc_freq = note_freq('A3')
        vibrato = sine(5.5, t) * 3
        acc_env = 0.4 + 0.3 * sine(0.1, t)
        val += triangle(acc_freq + vibrato, t) * acc_env * 0.06
        val += triangle(note_freq('C4') + vibrato, t) * acc_env * 0.04
        val += triangle(note_freq('E4') + vibrato, t) * acc_env * 0.035
        return val

    return generate_sound(duration, sample)


def gen_track_esplanadi(duration=33.0):
    """Esplanadi — you can smell the sea. Hopeful but uncertain."""
    def sample(t):
        val = 0.0
        # Warmer pad — rising feel
        base = note_freq('C3')
        val += sine(base, t) * 0.1
        val += sine(base * 1.5, t) * 0.06  # fifth
        val += sine(base * 2, t) * 0.04   # octave
        mod = 0.6 + 0.4 * sine(0.05, t)
        val *= mod
        # Melodic fragments — ascending — extended
        mel = [
            (note_freq('C4'), 0.0, 2.0),
            (note_freq('E4'), 3.0, 2.0),
            (note_freq('G4'), 6.0, 2.5),
            (note_freq('A4'), 10.0, 2.0),
            (note_freq('G4'), 13.0, 2.0),
            (note_freq('E4'), 16.0, 2.5),
            (note_freq('C4'), 19.0, 2.0),
            (note_freq('E4'), 22.0, 2.0),
            (note_freq('G4'), 25.0, 2.5),
            (note_freq('A4'), 28.5, 2.0),
            (note_freq('C5'), 31.0, 2.0),
        ]
        for freq, start, dur in mel:
            if start <= t < start + dur:
                lt = t - start
                env = soft_envelope(lt, dur)
                val += sine(freq, t) * env * 0.06
                val += sine(freq * 2, t) * env * 0.015
        return val

    return generate_sound(duration, sample)


def gen_track_dawn(duration=45.0):
    """Eira dawn — warmth, resolution, sunrise. The most beautiful track."""
    def sample(t):
        val = 0.0
        # Progression: builds warmth over time — extended ramp
        progress = min(1.0, t / 30.0)  # ramps up over 30 sec
        # Warm drone — rises in pitch slightly
        base = note_freq('D3') + progress * 10
        val += sine(base, t) * (0.08 + 0.07 * progress)
        val += sine(base * 1.5, t) * (0.04 + 0.04 * progress)
        val += sine(base * 2, t) * 0.03 * progress
        # Melody — pentatonic D major, slow and deliberate — extended
        mel = [
            (note_freq('D4'), 2.0, 3.0),
            (note_freq('F#4'), 6.0, 2.5),
            (note_freq('A4'), 9.5, 3.0),
            (note_freq('B4'), 13.0, 2.5),
            (note_freq('A4'), 16.5, 2.5),
            (note_freq('F#4'), 20.0, 3.0),
            (note_freq('D4'), 24.0, 3.0),
            (note_freq('D5'), 27.5, 2.5),
            (note_freq('A4'), 31.0, 3.0),
            (note_freq('F#4'), 35.0, 2.5),
            (note_freq('D4'), 38.5, 3.0),
            (note_freq('D5'), 42.0, 3.0),
        ]
        for freq, start, dur in mel:
            if start <= t < start + dur:
                lt = t - start
                env = soft_envelope(lt, dur)
                val += sine(freq, t) * env * (0.05 + 0.04 * progress)
                val += sine(freq * 2, t) * env * 0.015 * progress
        # Shimmer — high gentle tones
        if progress > 0.3:
            shimmer_amp = (progress - 0.3) * 0.05
            val += sine(note_freq('D6'), t) * sine(0.2, t) * shimmer_amp
            val += sine(note_freq('A5'), t) * sine(0.15, t + 0.5) * shimmer_amp * 0.6
        return val

    return generate_sound(duration, sample)


def gen_track_death(duration=18.0):
    """Death screen — low somber drone, finality."""
    def sample(t):
        val = 0.0
        # Descending drone
        freq = note_freq('D2') - t * 2
        val += sine(max(20, freq), t) * 0.2
        val += sine(max(20, freq * 1.5), t) * 0.06
        # Fading
        fade = max(0, 1.0 - t / duration)
        val *= fade
        # Dissonant overtone
        val += sine(note_freq('Ab3'), t) * fade * 0.04
        return val

    return generate_sound(duration, sample)


def gen_track_lost(duration=24.0):
    """Lost ending — melancholic, wistful, fading away."""
    def sample(t):
        val = 0.0
        fade = max(0, 1.0 - t / (duration * 1.2))
        # Sad pad — minor
        val += sine(note_freq('A2'), t) * 0.12 * fade
        val += sine(note_freq('C3'), t) * 0.07 * fade
        val += sine(note_freq('E3'), t) * 0.05 * fade
        # Slow descending melody — extended
        mel = [
            (note_freq('E4'), 1.0, 3.0),
            (note_freq('D4'), 5.0, 2.5),
            (note_freq('C4'), 8.5, 3.0),
            (note_freq('A3'), 12.0, 3.5),
            (note_freq('E4'), 16.5, 2.5),
            (note_freq('C4'), 20.0, 3.0),
        ]
        for freq, start, dur in mel:
            if start <= t < start + dur:
                lt = t - start
                env = soft_envelope(lt, dur)
                val += sine(freq, t) * env * 0.07 * fade
        return val

    return generate_sound(duration, sample)


def gen_track_splash(duration=24.0):
    """Title screen — atmospheric, sets the tone."""
    def sample(t):
        val = 0.0
        # Building drone
        build = min(1.0, t / 10.0)
        val += sine(note_freq('E2'), t) * 0.12 * build
        val += sine(note_freq('B2'), t) * 0.07 * build
        # Sparse high notes — extended
        if 4.0 < t < 6.0:
            lt = t - 4.0
            env = soft_envelope(lt, 2.0)
            val += sine(note_freq('E4'), t) * env * 0.06
        if 8.0 < t < 10.5:
            lt = t - 8.0
            env = soft_envelope(lt, 2.5)
            val += sine(note_freq('G4'), t) * env * 0.05
        if 12.0 < t < 14.5:
            lt = t - 12.0
            env = soft_envelope(lt, 2.5)
            val += sine(note_freq('B4'), t) * env * 0.06
        if 16.0 < t < 18.5:
            lt = t - 16.0
            env = soft_envelope(lt, 2.5)
            val += sine(note_freq('E4'), t) * env * 0.05
        if 20.0 < t < 22.5:
            lt = t - 20.0
            env = soft_envelope(lt, 2.5)
            val += sine(note_freq('G4'), t) * env * 0.06
        return val

    return generate_sound(duration, sample)


def gen_track_credits(duration=45.0):
    """Credits — reflective, all the themes echo."""
    def sample(t):
        val = 0.0
        # Warm foundation
        val += sine(note_freq('D3'), t) * 0.1
        val += sine(note_freq('A3'), t) * 0.06
        mod = 0.6 + 0.4 * sine(0.04, t)
        val *= mod
        # Recapitulation melody — fragments from the journey — extended
        mel = [
            (note_freq('D4'), 0.0, 2.5),   # Eira theme
            (note_freq('F#4'), 4.0, 2.0),
            (note_freq('E4'), 8.0, 2.5),   # Bar echo
            (note_freq('G4'), 11.0, 2.0),
            (note_freq('A4'), 14.0, 3.0),  # Climax
            (note_freq('F#4'), 18.0, 2.5),
            (note_freq('D4'), 22.0, 3.0),  # Return
            (note_freq('A3'), 26.0, 3.5),  # Resolve
            (note_freq('D4'), 30.5, 2.5),  # Reprise
            (note_freq('E4'), 34.0, 2.0),
            (note_freq('F#4'), 37.0, 2.5),
            (note_freq('D4'), 40.5, 3.5),  # Final resolve
        ]
        for freq, start, dur in mel:
            if start <= t < start + dur:
                lt = t - start
                env = soft_envelope(lt, dur)
                val += sine(freq, t) * env * 0.06
                val += sine(freq * 2, t) * env * 0.02
        return val

    return generate_sound(duration, sample)


# --- Music Manager ---

class MusicManager:
    """Manages background music playback with crossfading."""

    # Track mood categories — scenes map to these
    MOODS = {
        'splash': gen_track_splash,
        'bar': gen_track_bar,
        'alley': gen_track_alley,
        'street': gen_track_street,
        'metro': gen_track_metro,
        'tunnel': gen_track_tunnel,
        'market': gen_track_market,
        'park': gen_track_park,
        'esplanadi': gen_track_esplanadi,
        'dawn': gen_track_dawn,
        'death': gen_track_death,
        'lost': gen_track_lost,
        'credits': gen_track_credits,
    }

    # Scene ID -> mood mapping
    SCENE_MOODS = {
        'splash': 'splash',
        'intro': 'splash',
        'ch01_bar': 'bar',
        'ch02_alley': 'alley',
        'ch02_dumpster': 'alley',
        'ch03_hameentie': 'street',
        'ch03_courtyard': 'alley',
        'ch03_rooftop': 'alley',
        'ch04_car': 'street',
        'ch04_metro': 'metro',
        'ch04_metro_train': 'metro',
        'ch05_tunnels': 'tunnel',
        'ch05_cafe': 'bar',
        'ch05_harbor': 'alley',
        'ch06_market': 'market',
        'ch06_limo': 'street',
        'ch07_park': 'park',
        'ch07_katajanokka': 'street',
        'ch08_kruununhaka': 'street',
        'ch08_senate_square': 'street',
        'ch09_esplanadi': 'esplanadi',
        'ch09_bulevardi': 'esplanadi',
        'ch10_kaivopuisto': 'park',
        'eira': 'dawn',
        'dawn': 'dawn',
        'credits': 'credits',
    }

    def __init__(self):
        self.tracks = {}
        self.current_channel = None
        self.current_mood = None
        self.volume = 0.5
        self._initialized = False

    def init(self):
        """Initialize the mixer. Call after pygame.init()."""
        try:
            # Force reinit with our format in case pygame.init() already started it
            if pygame.mixer.get_init():
                pygame.mixer.quit()
            pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=2, buffer=2048)
            self._initialized = True
        except Exception as e:
            print(f"Audio init failed: {e}")
            self._initialized = False

    def _get_track(self, mood):
        """Get or generate a track for the given mood."""
        if mood not in self.tracks:
            gen_func = self.MOODS.get(mood)
            if gen_func:
                self.tracks[mood] = gen_func()
        return self.tracks.get(mood)

    def play_for_scene(self, scene_id):
        """Play appropriate music for a scene. Handles mood matching and transitions."""
        if not self._initialized:
            return

        # Determine mood — check direct mapping, then check for death/lost prefixes
        mood = self.SCENE_MOODS.get(scene_id)
        if mood is None:
            if 'death' in scene_id:
                mood = 'death'
            elif 'lost' in scene_id:
                mood = 'lost'
            else:
                mood = 'alley'  # default dark ambient

        # Don't restart if same mood
        if mood == self.current_mood:
            return

        self.current_mood = mood
        track = self._get_track(mood)
        if track:
            # Stop current
            if self.current_channel:
                self.current_channel.fadeout(800)
            # Play new track looping
            track.set_volume(self.volume)
            self.current_channel = track.play(loops=-1, fade_ms=1200)

    def stop(self):
        if self.current_channel:
            self.current_channel.fadeout(1000)
            self.current_mood = None

    def set_volume(self, vol):
        self.volume = max(0.0, min(1.0, vol))
        if self.current_channel:
            self.current_channel.set_volume(self.volume)
