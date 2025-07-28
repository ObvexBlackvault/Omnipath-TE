
class Guardian:
    def validate(self, risk_score):
        return "BLOCKED" if risk_score >= 7 else "APPROVED"
