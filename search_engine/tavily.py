import requests
from pydantic import BaseModel, NonNegativeFloat
from tavily import TavilyClient
from utils import TAVILY_API_KEY

class SearchResponse(BaseModel):
    title: str
    url: str
    content: str
    score: NonNegativeFloat

    def __str__(self):
        return f"Title: {self.title}\nurl: {self.url}\nContent:\n{'\n'.join(self.content)}"


def search(query):
    try:
        client = TavilyClient(TAVILY_API_KEY)
        response = client.search(
            query=query,
            max_results=10,
            include_answer="basic",
        )
        results = []
        for result in response['results']:
            res = SearchResponse(title=result['title'], url=result['url'], content=result['content'], score=result['score'])
            results.append(res)
        return results

    except requests.exceptions.RequestException as e:
        # to be done in logging
        print(f"Error getting results from Tavily: {str(e)}")
        return []