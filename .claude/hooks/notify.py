#!/usr/bin/env python3
import math
import struct
import subprocess


class Notification:
    RATE: int = 44100
    VOL: float = 0.35
    FADE: float = 0.015

    @classmethod
    def _tone(cls, freq: float, dur: float) -> list[int]:
        n = int(cls.RATE * dur)
        fade_n = int(cls.RATE * cls.FADE)
        out: list[int] = []
        for i in range(n):
            v = math.sin(2 * math.pi * freq * i / cls.RATE)
            if i < fade_n:
                v *= i / fade_n
            elif i > n - fade_n:
                v *= (n - i) / fade_n
            out.append(int(v * cls.VOL * 32767))
        return out

    @classmethod
    def _note(cls, freq: float, gap: float) -> list[int]:
        note_dur = gap * 0.82
        rest_dur = gap - note_dur
        return cls._tone(freq, note_dur) + [0] * int(cls.RATE * rest_dur)

    @classmethod
    def play(cls) -> None:
        score: list[tuple[float, float]] = [
            (523.3, 0.15),
            (659.3, 0.15),
            (784.0, 0.40),
        ]
        samples: list[int] = []
        for freq, gap in score:
            samples.extend(cls._note(freq, gap))
        data = struct.pack(f"<{len(samples)}h", *samples)
        proc = subprocess.Popen(
            ["pacat", "--rate", str(cls.RATE), "--channels", "1", "--format", "s16le"],
            stdin=subprocess.PIPE,
        )
        assert proc.stdin is not None
        proc.stdin.write(data)
        proc.stdin.close()
        proc.wait()


if __name__ == "__main__":
    Notification.play()
