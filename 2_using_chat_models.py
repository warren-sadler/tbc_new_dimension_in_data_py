from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

if __name__ == '__main__':
    load_dotenv()
    chat = ChatOpenAI()
    res = chat([
        SystemMessage(content="You are a React JS expert. Answer any subsequent question tersely."),
        HumanMessage(content="What is ReactJS?")
    ])
    print(res.content)