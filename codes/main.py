from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

try:
    import codes.prediction as prediction
except ImportError:
    import sys
    sys.path.append("codes/")
    import codes.prediction as prediction

#uvicorn codes.main:app --host 0.0.0.0
    
app = FastAPI()

class UserRequest(BaseModel):
    userid: str

@app.post("/api/recommend/")
def extract_features(request: UserRequest):
    try:
        response = prediction.recommend(request.userid)
        return response
    except Exception as e:
        # You can customize the status code and the detail message
        raise HTTPException(status_code=500, detail=str(e))
    

# Will return true if online
@app.get("/health-check")
def health_check(request: UserRequest):
    try:
        return True
    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))
