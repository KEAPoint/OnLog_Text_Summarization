import sys
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json
from starlette.config import Config

config = Config(".env")
CLOVA_CLIIENT_ID = config('CLOVA_CLIIENT_ID')
CLOVA_CLIIENT_SECRET = config('CLOVA_CLIIENT_SECRET')

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    stream=sys.stdout  # 로그를 표준 출력으로 전송
)

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

    headers = {
        "X-NCP-APIGW-API-KEY-ID": CLOVA_CLIIENT_ID,
        "X-NCP-APIGW-API-KEY": CLOVA_CLIIENT_SECRET,
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
    result_json = response.json()

    # Clova API 응답 로깅
    logging.info(f"Clova API Response: {result_json}")

    if response.status_code == 200:
        summaries = result_json["summary"]
        summarized_text = " ".join(summaries)
        response_data = BaseResponse(
            isSuccess=True,
            code=200,
            message="요청에 성공하였습니다.",
            data=summarized_text
        )
    else:
        error_message = result_json['error']['message']
        response_data = BaseResponse(
            isSuccess=False,
            code=response.status_code,
            message=error_message
        )

    # 요청과 응답 로깅
    logging.info(f"Request: {text}, Response: {response_data}")

    return response_data
