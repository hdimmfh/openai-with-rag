## 🏋🏼‍♀️ 소개
본 프로젝트는 langchain 을 활용한 챗봇 개발 프로젝트 입니다.</br>
벡터 DB인 faiss 와 구글 검색엔진 결과 데이터 기반 serp를 langchain에 접목하는</br>
RAG 기술을 적극 활용하여 기존 챗봇의 한계를 뛰어넘습니다. </br></br>
해당 프로젝트를 통해 </br> 사용자의 대화를 기억하고, 필요시 구글에 검색(serp)하거나 vector db(faiss)를 참고하는 챗봇을 실행할 수 있습니다. </br>
- 개발일자 : 2024.04.04

## ⚽️ 사용법
1. 필요한 라이브러리를 설치합니다. (langchain==0.0.281, google-search-results==2.4.2, faiss-cpu==1.7.4, openai==0.27.8)
2. 유사도 기반 검색 벡터DB(faiss)를 만들어둡니다.
3. RAG.util 에 faiss.py 와 serp.py에 발급받은 api key를 입력합니다.
4. faiss.py에 적절한 프롬프트를 설정합니다.
5. RAG.util 에서 작성한 도구(Tools)를 조합하여 실행할 수 있는 agent를 만듭니다.
6. agent가 사용할 메모리를 만듭니다.
7. 메모리를 만들고 agent 에게 메모리를 삽입하여 RAG 작업이 완료된 챗봇을 실행합니다.

## 🏀 코드 구조
### ① RAG/util/faiss.py
FAISS를 사용하여 벡터 검색을 수행합니다. 또한, 사용자로부터의 질문을 받아들이고 답변하기 위한 템플릿을 정의합니다.
### ② RAG/util/serp.py
SerpAPIWrapper를 사용하여 SerpAPI에 요청을 보내기 위해 API 키를 전달합니다.
### ③ RAG/chat_response.py
agent는 인자로 사용자 입력과 메모리를 받아들이고, 초기화된 에이전트 체인을 사용하여 대화를 처리합니다. 이 에이전트 체인은 사용자 입력에 따라 적절한 도구를 선택하여 실행하고, 그 결과를 반환합니다.
### ④ RAG/build_memory.py
ConversationBufferWindowMemory 클래스를 사용하여 메모리를 구성합니다. 이 메모리는 입력 및 출력 메시지의 대화를 기록합니다. "k=10" 매개변수는 최근 10개의 대화를 기억함을 의미합니다.
### ⑤ run.py
사용자의 대화를 기억하고, 필요시 구글에 검색(serp)하거나 vector db(faiss)를 참고하는 챗봇을 실행할 수 있습니다.
### ⑥ build_faiss_db.py
sample.txt로 faiss db를 만듭니다. 사용되는 라이브러리 버전이 다르므로 해당 부분에 유의합니다.
이후 다시 run.py 를 실행할 일이 있다면 라이브러리 버전을 재설정 한 이후 실행해야 오류 없이 진행할 수 있습니다.
