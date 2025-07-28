
from core.memory_weight import MemoryWeight

class Commander:
    def __init__(self, reflex_core, doctrine):
        self.reflex = reflex_core
        self.memory = MemoryWeight()
        self.doctrine = doctrine

    def evaluate(self, signal, emotion, intensity):
        reflex = self.reflex.evaluate(signal, emotion)
        final_emotion = reflex["recommended_substitution"] if reflex["recommended_substitution"] else emotion
        risk = self.memory.check_emotional_risk(final_emotion, intensity)
        return {
            "signal": signal,
            "original_emotion": emotion,
            "final_emotion": final_emotion,
            "risk_score": risk,
            "pulse": "EXECUTED" if risk < 7 else "BLOCKED",
            "reflex_status": reflex["status"]
        }
