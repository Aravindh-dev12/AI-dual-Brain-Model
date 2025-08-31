import os
from typing import Optional
import openai
from src.core.config import settings
from src.models.base_model import BaseLLM

class MainBrain(BaseLLM):
    def __init__(self, model: Optional[str]=None):
        self.model = model or settings.openai_model
        openai.api_key = settings.openai_api_key

    def generate(self, prompt: str, **kwargs) -> str:
        if not settings.openai_api_key:
            return f'[MainBrain stub] {prompt[:200]}'
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role":"system","content":"You are the Main Brain."}, {"role":"user","content":prompt}],
            temperature=kwargs.get('temperature', 0.2),
            max_tokens=kwargs.get('max_tokens', 512)
        )
        return resp['choices'][0]['message']['content']

    def route(self, question: str) -> dict:
        system = "You are the Main Brain. Return JSON {call_second: bool, reason: str, second_prompt: str or null}."
        prompt = f"Question: {question}\nRespond ONLY with JSON."
        if not settings.openai_api_key:
            low = question.lower()
            if any(k in low for k in ['code','implement','function','algorithm','sql','python','javascript']):
                return {'call_second': True, 'reason': 'heuristic', 'second_prompt': question}
            return {'call_second': False, 'reason': 'heuristic', 'second_prompt': None}
        resp = openai.ChatCompletion.create(model=self.model, messages=[{"role":"system","content":system},{"role":"user","content":prompt}], temperature=0)
        import json
        try:
            return json.loads(resp['choices'][0]['message']['content'])
        except Exception:
            return {'call_second': False, 'reason': 'parse_error', 'second_prompt': None}

    def health(self) -> dict:
        return {'status':'ok' if settings.openai_api_key else 'stub'}
