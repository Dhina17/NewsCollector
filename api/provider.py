from newsapi import NewsApiClient
import os

TECHNOLOGY_NEWS_API_KEY = os.getenv("TOP_HEADLINES_API_KEY")


class ApiProvider:

    @staticmethod
    def get_newsapi_for_technology():
        return NewsApiClient(api_key=TECHNOLOGY_NEWS_API_KEY)
