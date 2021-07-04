from newsapi import NewsApiClient
import os

TOP_HEADLINES_API_KEY = os.getenv("TOP_HEADLINES_API_KEY")


class ApiProvider:

    @staticmethod
    def get_top_headlines_api():
        return NewsApiClient(api_key=TOP_HEADLINES_API_KEY)
