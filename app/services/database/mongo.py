from pymongo import MongoClient
from app.config import configs as p
from app.utils.logger import logger

class ConnectMongoDB(object):
    instance = None
    init_flag = False

    # 單例模式
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if ConnectMongoDB.init_flag:
            return

        try:
            mongodb_client = MongoClient(
                p.MONGODB_URL,
                username=p.MONGODB_USERNAME,
                password=p.MONGODB_PASSWORD,
                authSource=p.MONGODB_AUTH_SOURCE,
                authMechanism=p.MONGODB_AUTHMECHANISM,
            )
            # mongodb_client = MongoProxy(
            #     MongoClient(
            #         p.MONGODB_URL,
            #         username=p.MONGODB_USERNAME,
            #         password=p.MONGODB_PASSWORD,
            #         authSource=p.MONGODB_AUTH_SOURCE,
            #         authMechanism=p.MONGODB_AUTHMECHANISM,
            #     )
            # )

            self.DATABASE = mongodb_client[p.MONGODB_DATABASE]
            ConnectMongoDB.init_flag = True
            logger.debug(f"[MongoDB] Connect mongo success: {p.MONGODB_DATABASE}.")
        except Exception as e:
            logger.error(f"[MongoDB] Connect mongo error: {str(e)}.")

    def get_one(self, collection, filter):
        col = self.DATABASE[collection]
        result = col.find_one(filter)
        return result

    def get_many(self, collection, pipeline):
        col = self.DATABASE[collection]
        result = col.aggregate(pipeline)
        return list(result)

    def insert_one(self, collection, document):
        col = self.DATABASE[collection]
        x = col.insert_one(document)
        return x.inserted_id

    def insert_many(self, collection, document):
        col = self.DATABASE[collection]
        col.insertMany(document)

    def update_one(self, collection, filter, document):
        col = self.DATABASE[collection]
        update = self.check_update(document)
        col.update_one(filter, update)

    def update_many(self, collection, filter, document):
        col = self.DATABASE[collection]
        update = self.check_update(document)
        col.update_many(filter, update)

    def upsert_one(self, collection, filter, document):
        col = self.DATABASE[collection]
        update = self.check_update(document)
        col.update_one(filter, update, upsert=True)

    def upsert_many(self, collection, operations):
        col = self.DATABASE[collection]
        col.bulk_write(operations)

    def delete_one(self, collection, document):
        col = self.DATABASE[collection]
        col.delete_one(document)

    def delete_many(self, collection, document):
        col = self.DATABASE[collection]
        result = col.delete_many(document)
        return result

    def find_one_and_delete(self, collection, dictRequest):
        col = self.DATABASE[collection]
        result = col.find_one_and_delete(dictRequest)
        return result

    def delete_collection(self, collection):
        col = self.DATABASE[collection]
        col.delete_many({})

    def check_update(self, document):
        return document if "$set" in document else {"$set": document}

    def get_one_sort(self, collection, dictRequest, sort=[("createdAt", -1)]):
        col = self.DATABASE[collection]
        result = col.find_one(dictRequest, sort=sort)
        return result

    def get_many_sort(self, collection, dictRequest, sort=[("createdAt", -1)], limit=None):
        col = self.DATABASE[collection]
        result = col.find(dictRequest, sort=sort)
        if limit:
            result = result.limit(limit)
        return list(result)