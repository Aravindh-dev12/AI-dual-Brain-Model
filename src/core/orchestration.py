from src.models.main_brain import MainBrain
from src.models.second_brain import SecondBrain
from src.core.fusion import Fusioner
from src.core.logging_utils import get_logger

logger = get_logger()

class Orchestrator:
    def __init__(self):
        self.main = MainBrain()
        self.second = SecondBrain()
        self.fusion = Fusioner(self.main)

    def answer(self, question: str) -> dict:
        # Step 1: ask main brain for routing decision
        route = self.main.route(question)
        logger.info(f'Route decision: {route}')
        if route.get('call_second'):
            second_prompt = route.get('second_prompt') or question
            second_out = self.second.generate(second_prompt)
            fused = self.fusion.verify_and_fuse(question, second_out)
            return {'mode':'dual','final':fused['final'],'meta':{'score':fused['score'],'issues':fused['issues']}}
        else:
            ans = self.main.generate(question)
            return {'mode':'single','final':ans,'meta':{}}
