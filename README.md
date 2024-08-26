## 👨‍🍳 프로젝트 개요

### **🍔 목적**  
본 프로젝트는 langchain 을 활용한 챗봇 개발 프로젝트 입니다.
1. **faiss 벡터DB**와 **serp의 검색엔진**를 langchain에 접목합니다.
2. RAG를 활용하여 기존 챗봇의 **기억손실**, **최신정보 반영불가**의 한계를 극복합니다.
3. 사용자의 대화를 **기억**하고, 필요시 구글에 `검색(serp)`하거나 `벡터DB(faiss)`를 참고하는 챗봇을 구현합니다.

### **🍟 개발 기간**  
- `2024.04.04`: 기본 코드 구성

### **🍖 구성**  
<kbd>
<p align="center">
  <img src="https://private-user-images.githubusercontent.com/74033655/361417236-30ff5e5c-7437-4f11-afd7-fe8bc400334f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ2NzIxODIsIm5iZiI6MTcyNDY3MTg4MiwicGF0aCI6Ii83NDAzMzY1NS8zNjE0MTcyMzYtMzBmZjVlNWMtNzQzNy00ZjExLWFmZDctZmU4YmM0MDAzMzRmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODI2VDExMzEyMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI1ZGY3N2ZkNzc2YTdjYWQyM2QzNTY2MTg4NWM3MWMwZWM5ZDQ1MmEwMzRhMTZiOWQ5ZTgxNjdjODg0N2QyYTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.O8dX6L8ja-0tYnfcn9hT9jrX8QUsYVo6MhtP4R2BJ2A" width="80%"/>
</p>
</kbd>

### **🍕 사용법**  
1. 필요한 라이브러리를 설치합니다. (`requirements.txt`, `build_faiss_db.ipynb` 참고)
2. 유사도 기반 검색 벡터DB(faiss)를 만들어둡니다.
3. `/RAG/util` 경로에 위치한 `faiss.py`와 `serp.py`에 발급받은 api key를 입력합니다.
4. `faiss.py`에 적절한 프롬프트를 설정합니다.
5. `/RAG/util` 에서 작성한 도구(Tools)를 조합하여 실행할 수 있는 agent를 만듭니다.
6. agent가 사용할 메모리를 만듭니다.
7. `run.py`를 실행하여 agent를 실행합니다.


### **🍰 사용법**
1. **/RAG/util/faiss.py** </br>
FAISS를 사용하여 벡터 검색을 수행합니다. 또한, 사용자로부터의 질문을 받아들이고 답변하기 위한 템플릿을 정의합니다.
2. **/RAG/util/serp.py** </br>
SerpAPIWrapper를 사용하여 SerpAPI에 요청을 보내기 위해 API 키를 전달합니다.
3. **/RAG/chat_response.py** </br>
agent는 인자로 사용자 입력과 메모리를 받아들이고, 초기화된 에이전트 체인을 사용하여 대화를 처리합니다. 이 에이전트 체인은 사용자 입력에 따라 적절한 도구를 선택하여 실행하고, 그 결과를 반환합니다.
4. **/RAG/build_memory.py** </br>
ConversationBufferWindowMemory 클래스를 사용하여 메모리를 구성합니다. 이 메모리는 입력 및 출력 메시지의 대화를 기록합니다. "k=10" 매개변수는 최근 10개의 대화를 기억함을 의미합니다.
5. **/run.py** </br>
사용자의 대화를 기억하고, 필요시 구글에 검색(serp)하거나 vector db(faiss)를 참고하는 챗봇을 실행할 수 있습니다.
6. **/build_faiss_db.ipynb** </br>
sample.txt로 faiss db를 만듭니다. 사용되는 라이브러리 버전이 다르므로 해당 부분에 유의합니다.
이후 다시 run.py 를 실행할 일이 있다면 라이브러리 버전을 재설정 한 이후 실행해야 오류 없이 진행할 수 있습니다.


