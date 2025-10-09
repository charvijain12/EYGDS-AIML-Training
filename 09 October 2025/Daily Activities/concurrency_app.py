from fastapi import FastAPI
import asyncio
import time

app=FastAPI()

#----SYNC ENDPOINT-----
@app.get("/sync_task")
def sync_task():
    time.sleep(10) #--blocking
    return {"message":"Sync task completed after 5 seconds"}

#----ASYNC ENDPOINT----
@app.get("/async_task")
async def async_task():
    await asyncio.sleep(10) #-non blocking
    return {"message":"Async task completed after 5 seconds"}