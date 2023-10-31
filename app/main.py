from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json

app = FastAPI()


class Text(BaseModel):
    text: str


class BaseResponse(BaseModel):
    isSuccess: bool
    code: int
    message: str
    data: str = None


@app.post("/summarize", response_model=BaseResponse)
async def summarize(text: Text):
    title = text.text
    content = text.text

    client_id = "k67mhpzvaq"
    client_secret = "1gdJOKKmebWbKdLFVsp3H3xQqS6eerIZi3Ys7jeq"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/json",
    }

    language = "ko"
    model = "general"
    tone = "0"
    summaryCount = "3"

    url = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"

    data = {
        "document": {"title": title, "content": content},
        "option": {
            "language": language,
            "model": model,
            "tone": tone,
            "summaryCount": summaryCount,
        },
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    rescode = response.status_code

    if rescode == 200:
        result_json = response.json()
        summaries = result_json["summary"]
        summarized_text = " ".join(summaries)

        return BaseResponse(
            isSuccess=True,
            code=200,
            message="요청에 성공하였습니다.",
            data=summarized_text
        )
    else:
        return BaseResponse(
            isSuccess=False,
            code=rescode,
            message=f"Error: {response.text}"
        )
