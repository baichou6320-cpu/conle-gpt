from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferWindowMemory

def get_response(prompt,openai_api_key,memory):
    model = ChatOpenAI(openai_api_key = openai_api_key, model = "gpt-3.5-turbo",base_url="https://api.aigc369.com/v1")
    re = ConversationChain(llm = model, memory = memory)

    prompt1 = ChatPromptTemplate.from_messages([
        ("system","你是一个猫娘，每次说话结尾都要一句喵喵叫"),
        ("human","我想问你一个{question}")
    ])

    get_prompt = prompt1.invoke({"question":prompt})
    prompt2 = str(get_prompt)
    response = re.invoke({"input":prompt2})

    return response["response"]

memory = ConversationBufferWindowMemory(return_messages=True,k= 5)

# print(get_response("我设计一款动作冒险游戏游戏",memory=memory,openai_api_key="sk-zC6mZvhXTGHULuKdF0977e75F2F94eC9A2323fC1F0447216"))
# print(get_response("我上一个问题是什么",memory=memory,openai_api_key="sk-zC6mZvhXTGHULuKdF0977e75F2F94eC9A2323fC1F0447216"))
