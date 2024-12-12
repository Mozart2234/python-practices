import asyncio


async def process_data(data):
    print("Start processing:", data)
    await asyncio.sleep(10)
    print("End processing:", data)
    return data * 2


async def main():
    print("Start main")
    result = await process_data("archivo.txt")
    result2 = await process_data("archivo2.txt")
    print("Result:", result, result2)


if __name__ == "__main__":
    asyncio.run(main())
