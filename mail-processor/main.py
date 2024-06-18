from langchain_community.tools.tavily_search import TavilySearchResults
import dotenv

dotenv.load_dotenv()

search = TavilySearchResults(max_results=2)
search_results = search.invoke("what is the weather in SF")
print(search_results)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]
