# Walkthrough:   https://python.langchain.com/v0.2/docs/tutorials/agents/
# Tavily search: https://app.tavily.com/home
# LangSmith:     https://smith.langchain.com

from pprint import pprint
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
import dotenv

dotenv.load_dotenv()

search = TavilySearchResults(max_results=2)
# search_results = search.invoke("what is the weather in SF")
# print(search_results)

tools = [search]


model = ChatOpenAI(model="gpt-4")


# response = model.invoke([HumanMessage(content="hi")])
# print(response.content)


# model_with_tools = model.bind_tools(tools)


# response = model_with_tools.invoke([HumanMessage(content="when's the 2024 election in the us")])

# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")


agent_executor = create_react_agent(model, tools)


# response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})

# print(response["messages"])


# response = agent_executor.invoke(
#     {"messages": [HumanMessage(content="whats the weather in sf?")]}
# )
# pprint(response["messages"])


# for chunk in agent_executor.stream(
#     {"messages": [HumanMessage(content="whats the weather in sf?")]}
# ):
#     print(chunk)
#     print("----")






# for next time, look into adding a tool to take in the email message body
