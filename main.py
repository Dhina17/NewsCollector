from api.provider import ApiProvider
from db.mongodb import MongoDb

# Get mongodb atlas cloud connection
mongo_connect = MongoDb.get_connection()

# Get db instance
db = mongo_connect.news_data

# function to update top_headlines


def update_top_headlines():
    # Get api for top headlines from provider
    api = ApiProvider.get_top_headlines_api()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     language='en',
                                     page_size=100)

    # get top headlines collection from db
    collection = db.top_headlines

    # Only do db actios if the news api request succeed.
    if response['status'] == 'ok':

        # Check for documents are present or not
        # If present, delete old docs and insert new docs.
        if collection.count_documents({}) > 0:

            # Delete all the existing documents.
            # Our moto is to only show latest 100 news.
            # and also to avoid duplicates.
            collection.delete_many({})

            # Insert news articles to the db collection
            collection.insert_many(response['articles'])

        # If docs are not found, just insert new docs.
        else:
            collection.insert_many(response['articles'])


update_top_headlines()
