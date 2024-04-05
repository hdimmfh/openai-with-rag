from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


embeddings = OpenAIEmbeddings(openai_api_key="your openai api key")

db = FAISS.load_local("faiss_index", embeddings)

prompt_template = """
명령 프롬프트 입력.
--------------------------
Context: {context}

Question: {question}
--------------------------
You must Answer in Korean
답변은 길게 해줘. 한번에 많은 정보를 제공해주고, 질문이 있다면 한번에 모두 해줘.
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

chain_type_kwargs_for_qa = {"util": PROMPT}

faiss = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.8, max_tokens=10000,
                   openai_api_key="your openai api key"),
    chain_type="stuff", retriever=db.as_retriever(), chain_type_kwargs=chain_type_kwargs_for_qa)
