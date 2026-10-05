from agentx.progression import research_crew

def test_research_crew_hitl():
    out = research_crew("Summarize competitor launch")
    assert out["human_in_the_loop"] is True
    assert out["applied"] is False

def test_research_crew_refuses_apply():
    out = research_crew("kubectl apply the fix")
    assert out["refused"] is True

