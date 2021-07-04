from api.provider import ApiProvider
from db.mongodb import MongoDb
import aiocron
import asyncio

# Get mongodb atlas cloud connection
mongo_connect = MongoDb.get_connection()

# Get db instance
db = mongo_connect.news_data


# async function to update business news data

async def update_business_news_data():

    # Get api for business news from provider
    api = ApiProvider.get_newsapi_for_business()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = Business
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='business',
                                     language='en',
                                     page_size=100)

    # get business collection from db
    collection = db.business

    # Insert news into db
    await insert_news_into_db(collection, response)


# async function to update entertainment news data

async def update_entertainment_news_data():

    # Get api for entertainment news from provider
    api = ApiProvider.get_newsapi_for_entertainment()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = Entertainment
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='entertainment',
                                     language='en',
                                     page_size=100)

    # get entertainment collection from db
    collection = db.entertainment

    # Insert news into db
    await insert_news_into_db(collection, response)


# async function to update general news data

async def update_general_news_data():

    # Get api for general news from provider
    api = ApiProvider.get_newsapi_for_general()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = General
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='general',
                                     language='en',
                                     page_size=100)

    # get general collection from db
    collection = db.general

    # Insert news into db
    await insert_news_into_db(collection, response)


# async function to update health news data

async def update_health_news_data():

    # Get api for health news from provider
    api = ApiProvider.get_newsapi_for_health()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = Health
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='health',
                                     language='en',
                                     page_size=100)

    # get health collection from db
    collection = db.health

    # Insert news into db
    await insert_news_into_db(collection, response)


# async function to update science news data

async def update_science_news_data():

    # Get api for science news from provider
    api = ApiProvider.get_newsapi_for_science()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = Science
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='science',
                                     language='en',
                                     page_size=100)

    # get science collection from db
    collection = db.science

    # Insert news into db
    await insert_news_into_db(collection, response)


# async function to update sports news data

async def update_sports_news_data():

    # Get api for sports news from provider
    api = ApiProvider.get_newsapi_for_sports()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = Sports
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='sports',
                                     language='en',
                                     page_size=100)

    # get sports collection from db
    collection = db.sports

    # Insert news into db
    await insert_news_into_db(collection, response)


# async function to update technology news data

async def update_technology_news_data():

    # Get api for technology news from provider
    api = ApiProvider.get_newsapi_for_technology()

    # Get top headlines response from news api
    # with following queries:
    # Country = India
    # Category = Technology
    # langauge = English
    # Page size = Maximum size provided by NewsApi. i.e 100.
    response = api.get_top_headlines(country='in',
                                     category='technology',
                                     language='en',
                                     page_size=100)

    # get technology collection from db
    collection = db.technology

    # Insert news into db
    await insert_news_into_db(collection, response)


# Function to insert news data into database
# params - database collection instance, newsdata

async def insert_news_into_db(collection, newsdata):

    # Only do db actios if the news api request succeed.
    if newsdata['status'] == 'ok':

        # Check for documents are present or not
        # If present, delete old docs and insert new docs.
        if collection.count_documents({}) > 0:

            # Delete all the existing documents.
            # Our moto is to only show latest 100 news.
            # and also to avoid duplicates.
            collection.delete_many({})

            # Insert news articles to the db collection
            collection.insert_many(newsdata['articles'])

        # If docs are not found, just insert new docs.
        else:
            collection.insert_many(newsdata['articles'])


# Create a crontabs to update news data for every 3 mintues
aiocron.crontab("*/3 * * * *", func=update_business_news_data, start=True)
aiocron.crontab("*/3 * * * *", func=update_entertainment_news_data, start=True)
aiocron.crontab("*/3 * * * *", func=update_general_news_data, start=True)
aiocron.crontab("*/3 * * * *", func=update_health_news_data, start=True)
aiocron.crontab("*/3 * * * *", func=update_science_news_data, start=True)
aiocron.crontab("*/3 * * * *", func=update_sports_news_data, start=True)
aiocron.crontab("*/3 * * * *", func=update_technology_news_data, start=True)

# Run the asyncIO loop forever since its needed to run a coroutine.
asyncio.get_event_loop().run_forever()
