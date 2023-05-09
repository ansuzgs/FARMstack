from motor.motor_asyncio import AsyncIOMotorClient #type: ignore
from model import Todo

client = AsyncIOMotorClient('mongodb://localhost:27017/')
#client = AsyncIOMotorClient('mongodb+srv://ansuzgs:<password>@cluster0.n8srebp.mongodb.net/?retryWrites=true&w=majority')
database = client.TodoList
collection = database.todo

async def fetch_one_todo(title: str):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo: str):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title: str, desc: str):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title: str):
    await collection.delete_one({"title": title})
    return True