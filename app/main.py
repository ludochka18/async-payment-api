from fastapi import FastAPI

app = FastAPI(
    title="Async Payment API",
    description="REST API for users, accounts, payments and webhook processing",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"status": "ok"}
