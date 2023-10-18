from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
import requests
import json

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <body>
            <form action="/summarize/" method="post">
                <input type="text" name="title" placeholder="Title">
                <textarea name="content" rows="5" placeholder="Content"></textarea>
                <button>Summarize</button>
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request):
    form_data = await request.form()

    title = form_data.get("title")
    content = form_data.get("content")

    # Your summarization code here...
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
        # Combine summaries into a single paragraph
        summarized_text = " ".join(summaries)

        # html_content = f"<html><body><h2>Summarized Text:</h2><p>{summarized_text}</p></body></html>"

        result = " ".join(response.text[12:-3].split("\\n"))

        html_content = (
            f"<html><body><h2>Summarized Text:</h2><p>{result}</p></body></html>"
        )

        return HTMLResponse(content=html_content, status_code=200)
    else:
        raise HTTPException(status_code=rescode, detail=f"Error: {response.text}")
