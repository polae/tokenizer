from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import tiktoken

class TokenRequest(BaseModel):
    text: str
    model_name: str = 'gpt-4'

app = FastAPI()

@app.post("/count_tokens/", tags=["Tokenizer"])
async def count_tokens(request: TokenRequest):
    try:
        encoding = tiktoken.encoding_for_model(request.model_name)
        num_tokens = len(encoding.encode(request.text))
        return {"token_count": num_tokens}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
