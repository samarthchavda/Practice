import asyncio
import time 
from fastapi import FastAPI

# async is progoramming to set a multiple task in a same time 

# def task():
#     print("hello")
#     time.sleep(4)
#     print("samarth")

# task()
# task()


# async non blocking code 

# async def task():
#     print("hello")
#     await asyncio.sleep(4)
#     print("samarth")
# async def main():
#     await asyncio.gather(task(), task())
# asyncio.run(main())


# asynce api call

# async def fetch_data():
#     await asyncio.sleep(2)
#     return "data received"

# async def main():
#     result = await fetch_data()
#     print(result)

# asyncio.run(main())

# # multiple api call
# async def api_call(name):
#     await asyncio.sleep(2)
#     print(f"{name} done")

# async def main():
#     await asyncio.gather(
#         api_call("api1"),
#         api_call("api2"),
#         api_call("api3")
#     )
# asyncio.run(main())


# real use in fast api 


app = FastAPI()
@app.get("/")
async def main():
    await asyncio.sleep(4)
    return {"message": "hello"}