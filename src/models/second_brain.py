import os
import requests
from src.core.config import settings
from src.models.base_model import BaseLLM

class SecondBrain(BaseLLM):
    def __init__(self):
        self.endpoint = settings.deepseek_endpoint
        self.api_key = settings.deepseek_api_key

    def generate(self, prompt: str, **kwargs) -> str:
        if not self.api_key or not self.endpoint:
            # stubbed outputs for demo
            if 'fibonacci' in prompt.lower():
                return 'def fib(n):\n    a,b=0,1\n    for _ in range(n):\n        a,b=b,a+b\n    return a'
            return '[SecondBrain stub] ' + prompt[:300]
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type':'application/json'}
        payload = {'prompt': prompt, 'max_tokens': kwargs.get('max_tokens',512), 'temperature': kwargs.get('temperature',0)}
        r = requests.post(self.endpoint, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        return data.get('text') or data.get('output') or data.get('result') or ''

    def health(self) -> dict:
        return {'status':'ok' if self.api_key else 'stub'}
