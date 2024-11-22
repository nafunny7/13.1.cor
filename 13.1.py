import asyncio


async def start_strongman(name: str, power: int):
    print(f"Силач {name} начал соревнования.")
    delay = 1 / power
    for ball in range(1, 6):
        await asyncio.sleep(delay)
        print(f"Силач {name} поднял {ball} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Джагернаут", 2))
    task2 = asyncio.create_task(start_strongman("Арнольд", 6))
    task3 = asyncio.create_task(start_strongman("Пудж", 10))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
