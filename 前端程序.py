import streamlit as st
from 后端应用 import get_response
from langchain.memory import ConversationBufferWindowMemory

st.title("自制AI聊天助手")

with st.sidebar:
    API = st.text_input("请输入Open ai 密钥：",type='password')
    st.markdown("[获取API密钥]((https://platform.openai.com/account/api-keys))")


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferWindowMemory(return_messages=True, k=5)
    st.session_state["messages"] = [{"role":"AI", "content":"请问需要什么帮助吗"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt and not API:
    st.info("请输入API")
    st.stop()

if prompt and API:
    st.session_state["messages"].append({"role":"human", "content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考，请稍等......."):
        response = get_response(prompt, memory=st.session_state["memory"], openai_api_key=API)
        st.session_state["messages"].append({"role":"AI", "content":response})
        st.chat_message("AI").write(response)
