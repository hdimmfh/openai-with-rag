from langchain.utilities import SerpAPIWrapper

params = {
    "engine": "google",
    'gl': "kr",
    'hl': "ko"
}

serp = SerpAPIWrapper(params=params, serpapi_api_key="your serp api key")
