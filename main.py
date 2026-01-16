
from fastapi import FastAPI
from routes.items import router as items_router
from routes.users import router as users_router

app = FastAPI()

# Include routers with prefixes and tags
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(items_router, prefix="/items", tags=["Items"])


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}