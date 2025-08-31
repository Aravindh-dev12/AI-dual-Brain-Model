from core.fusion import Fusioner
class DummyMain:
    def generate(self, prompt, **kwargs):
        return 'ok: ' + prompt[:50]
def test_score_code():
    f = Fusioner(DummyMain())
    code = 'def foo():\n  return 1'
    assert f.code_syntax_ok(code)
    assert f.score_second(code) > 0.5
