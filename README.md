# OnLog_Text_Summarization

## 🌐 프로젝트 개요

본 프로젝트의 목표는 사용자가 작성한 게시글을 요약하여 제공하는 서비스를 개발하는 것입니다. 이 서비스는 사용자가 복잡하고 어려운 내용의 글을 간결하게 요약할 수 있도록 도와주며, 이를 통해 사용자의 정보 소비
효율성을 향상시키는 데 목표를 두고 있습니다.

## 🛠️ 프로젝트 개발 환경

프로젝트는 아래 환경에서 개발되었습니다.

> OS: macOS Sonoma  
> IDE: Pycharm  
> Python: 3.11.6

## 🔗 프로젝트 구조

```text
.
├── .dockerignore           🚫 Docker 이미지 생성 시 무시하는 파일 목록
├── .env                    🔐 프로젝트에서 사용하는 환경 변수 설정 파일
├── .git                    📂 Git 버전 관리를 위한 디렉토리
├── .gitignore              🙈 Git 버전 관리 시 무시하는 파일 목록
├── .idea                   🧠 IntelliJ IDEA 설정 파일이 저장된 디렉토리
├── Dockerfile              🐳 Docker 이미지 생성을 위한 스크립트
├── README.md               📚 프로젝트에 대한 설명과 사용 방법 등을 담은 문서
├── __pycache__             🗂️ 파이썬이 컴파일한 버전의 파일을 저장하는 디렉토리
├── main.py                 🚀 프로그램의 시작점
└── requirements.txt        📌 프로젝트에서 필요한 파이썬 패키지 목록
```

## ✅ 프로젝트 개발/실행

해당 프로젝트를 추가로 개발 혹은 실행시켜보고 싶으신 경우 아래의 절차에 따라 진행해주세요

1. 가상 환경 생성

```commandline
python3 -m venv venv
```

2. 가상 환경 활성화

```commandline
source venv/bin/activate
```

3. requirements 다운로드

```commandline
pip install -r requirements.txt
```

4. `.env` 파일 생성

```commandline
touch .env
```

5. `.env` 파일에 CLOVA Client 정보 입력

```text
CLOVA_CLIIENT_ID = "{CLOVA_CLIIENT_ID}"
CLOVA_CLIIENT_SECRET = "{CLOVA_CLIIENT_SECRET}"
```

6. 프로그램 실행

```commandline
uvicorn main:app --port 8000 --reload
```

참고) 프로젝트가 실행 중인 환경에 한해 아래 URL에서 API 명세서를 확인할 수 있습니다

```commandline
http://localhost:8000/docs
http://localhost:8000/redoc
```
