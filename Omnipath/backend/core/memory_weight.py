
class MemoryWeight:
    def __init__(self):
        self.emotion_weights = {
            "joy": 2,
            "resolve": 1,
            "curiosity": 3,
            "neutral": 1,
            "sadness": 8,
            "anger": 9,
            "fear": 7,
            "duty": 4,
            "grief": 9
        }

    def check_emotional_risk(self, emotion, intensity):
        base = self.emotion_weights.get(emotion, 5)
        return min(10, round(base + intensity * 0.5, 2))
