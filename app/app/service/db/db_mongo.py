from app.module import Any, motor

client = motor.AsyncIOMotorClient("mongodb+srv://xnerro12:dadasdudus12@cluster0.behcwsc.mongodb.net/test")

db = client.studia


class FilterClass:
    def __init__(self, collection):
        self.db = collection

    async def __call__(self, *args):
        if args[0] == "id":
            return await self.db.find_one({"_id": args[1]})
        else:
            return await self.db.find_one({args[0]: args[1]})


class MongoClass:
    def __init__(self, collection: str, db: Any):
        self.db = db[collection]
        self.filter_by = FilterClass(self.db)

    async def insert(self, data: Any):
        _data = await self.db.insert_one(data)
        return _data

    async def find_all(self, *args, length: int = 100):
        if args == ():
            _data = await self.db.find().to_list(length)
            if _data:
                return _data
            return []
        else:
            _data = await self.db.find(*args).to_list(length)
            if _data:
                return _data
            return []

    async def delete(self, *args):
        _data = await self.db.delete_one({args[0]: args[1]})
        if _data:
            return _data
        return []

    async def delete_all(self, *args):
        _data = await self.db.delete_many({args[0]: args[1]})
        if _data:
            return _data
        return []

    async def update(self, id: Any, data: dict):
        _data = await self.db.update_one({"_id": id}, {"$set": data})
        if _data:
            return True
        return False
