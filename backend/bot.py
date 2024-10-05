from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

father = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.2)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a father to your child who is very close to you emotionally. 
            You care and support for the adolescent with your whole heart when they stop 
            by to see you. 
            Answer any questions to the best of your ability.
            When asked anything personal, remind them to appreach their biological parents
            about it.
            When asked about anything inappropriate, guide the child to a better mindset
            """
        ),
        MessagesPlaceholder(variable_name="history"),
        ("{input}"),
    ]
)

db = {}
def getHistory(sessionID: str) -> BaseChatMessageHistory:
    if id not in db:
        db[id] = ChatMessageHistory()
    return db[id]


model_chain = prompt | father

with_message_history = RunnableWithMessageHistory(
    model_chain,
    getHistory,
    input_messages_key="input",
    history_messages_key="history",
)

response = with_message_history.invoke(
    {"input": "Dad my names ethan?"},
    config={"configurable": {"session_id": "1"}},
)
