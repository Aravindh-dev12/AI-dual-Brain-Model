from core.orchestration import Orchestrator

def test_orchestrator_dual_mode():
    o = Orchestrator()
    # use a question that triggers code path
    res = o.answer('Write a Python function to compute fibonacci')
    assert 'final' in res
    assert res['mode'] in ('dual','single')
