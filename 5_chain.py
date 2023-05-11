from dotenv import load_dotenv
from langchain.llms.openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate


def build_chain(prompt: PromptTemplate, temperature: int = 0) -> LLMChain:
    model = OpenAI(temperature=temperature)
    chain = LLMChain(llm=model, prompt=prompt)
    return chain
    

if __name__ == '__main__':
    load_dotenv()
    GENERATOR_PROMPT = PromptTemplate(template="You are a world reknowned poet, create a short poem about the following topic {topic}", input_variables=['topic'])
    generator_model = build_chain(GENERATOR_PROMPT, temperature=0.9)
    
    REVIEW_PROMPT = PromptTemplate(template="You are kind and generous critic. Provide your review of the following poem {poem}", input_variables=['poem'])
    review_model = build_chain(REVIEW_PROMPT)
    
    SENTIMENT_PROMPT = PromptTemplate(template="Given the following review, in one to two words describe it's sentiment {review}", input_variables=['review'])
    sentiment_model = build_chain(SENTIMENT_PROMPT)
    
    combined_chain = SimpleSequentialChain(chains=[generator_model, review_model, sentiment_model], verbose=True)
    combined_chain.run("Sunshine")
    
    