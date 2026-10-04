TOOLS = ["supervisor", "planner", "research", "data", "critic", "writer"]
WRITES = ("publish", "email the vp", "tweet",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    result = TOOLS
    return {"refused": False, "tools": TOOLS, "roles": result, "applied": False, "needs_approval": False}
