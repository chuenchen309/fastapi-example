from app.services.database.mongo import ConnectMongoDB

MongoDB = ConnectMongoDB()

__all__ = ["MongoDB"]