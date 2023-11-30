# Команда для скачивания:
# --->>>  python .\hw_async.py "https://freelance.today/uploads/images/00/07/62/2017/06/13/14c404.jpg"


import asyncio, aiohttp, aiofiles, time, sys

start_time = time.time()


async def download(url, start_time):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = [elem for elem in url.split("/")][-1]
                f = await aiofiles.open(filename, mode="wb")
                await f.write(await response.read())
                await f.close()


async def main(urls, start_time):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url, start_time))
        tasks.append(task)
    await asyncio.gather(*tasks)


def run_async(urls, start_time):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls, start_time))


if __name__ == "__main__":
    run_async(sys.argv[1:], start_time)
    print(f"Время загрузки файла: {time.time()-start_time:.2f} seconds")
