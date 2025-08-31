import ast
from src.core.logging_utils import get_logger

logger = get_logger()

class Fusioner:
    def __init__(self, main_brain):
        self.main = main_brain

    def is_code(self, text: str) -> bool:
        return '\ndef ' in text or text.strip().startswith('def ')

    def code_syntax_ok(self, code: str) -> bool:
        try:
            ast.parse(code)
            return True
        except Exception as e:
            logger.debug(f'Code syntax error: {e}')
            return False

    def score_second(self, second_text: str) -> float:
        score = 0.0
        if self.is_code(second_text):
            score += 0.6
            if self.code_syntax_ok(second_text):
                score += 0.3
        if len(second_text) > 30:
            score += 0.1
        return min(score, 1.0)

    def verify_and_fuse(self, user_question: str, second_text: str) -> dict:
        score = self.score_second(second_text)
        needs_correction = False
        issues = []
        if self.is_code(second_text) and not self.code_syntax_ok(second_text):
            needs_correction = True
            issues.append('syntax_error')
        # Ask main brain to synthesize; include score & issues
        synth_prompt = (
            f"User question: {user_question}\n\n"
            f"Specialist output (score={score:.2f}):\n{second_text}\n\n"
            "If the specialist output has issues, correct them and explain briefly. Otherwise, integrate and provide final answer."
        )
        final = self.main.generate(synth_prompt, temperature=0.1, max_tokens=800)
        return {'final': final, 'score': score, 'issues': issues}
