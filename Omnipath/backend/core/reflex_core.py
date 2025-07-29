
class ReflexCore:
    def __init__(self, lessons):
        self.lessons = lessons
        self.substitution_map = self.build_substitution_map()

    def build_substitution_map(self):
        subs = {}
        for entry in self.lessons:
            signal = entry["signal"]
            forks = entry["key_difference"]
            fork_ids = list(forks.keys())
            from_emotion = forks[fork_ids[0]]["emotion"]
            to_emotion = forks[fork_ids[1]]["emotion"]
            subs[signal] = {
                "substitute_from": from_emotion,
                "substitute_to": to_emotion,
                "rationale": entry["lesson"]
            }
        return subs

    def evaluate(self, signal, emotion):
        if signal in self.substitution_map:
            sub = self.substitution_map[signal]
            if emotion == sub["substitute_from"]:
                return {
                    "recommended_substitution": sub["substitute_to"],
                    "rationale": sub["rationale"],
                    "status": "RECOMMENDED"
                }
        return {
            "recommended_substitution": None,
            "status": "UNCHANGED"
        }
