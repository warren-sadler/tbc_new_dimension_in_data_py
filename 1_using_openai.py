from dotenv import load_dotenv
from langchain.llms import OpenAI


if __name__ == '__main__':
    load_dotenv()
    model = OpenAI(temperature=0)
    res = model("Who gave the 'I have a Dream' speach?")
    print(res)