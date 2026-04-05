from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from env.environment import SafeRouteEnv
import random

app = FastAPI(title="Safe Route AI Environment", description="OpenEnv Open Hackathon Baseline Endpoint")

# Global environment mock handler for stateless REST pings natively
global_env = SafeRouteEnv()

class StepRequest(BaseModel):
    action: str

@app.get("/")
def health_check():
    """HF Space deployment uptime listener dynamically returning standard 200 OK headers automatically"""
    return {"status": "ok", "message": "SafeRoute OpenEnv Server OK"}

@app.post("/reset")
def reset_env():
    """Generates a perfectly distinct routing state mathematically mapping OpenEnv endpoints"""
    state = global_env.reset()
    return {"state": state}

@app.post("/step")
def step_env(req: StepRequest):
    """Executes dynamic route interactions securely propagating reward statistics exactly"""
    try:
        state, reward, done, info = global_env.step(req.action)
        return {
            "state": state,
            "reward": reward,
            "done": done,
            "info": info
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
