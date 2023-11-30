# Команда для скачивания: 
# --->>>  python .\hw_multiproc.py "https://freelance.today/uploads/images/00/07/62/2017/06/13/14c404.jpg"


import requests, multiprocessing, time, sys


def download(url, start_time):
    response = requests.get(url)
    filename = [elem for elem in url.split("/")][-1]
    print(f"Время загрузки файла {filename} : {time.time() - start_time:.2f} seconds")
    with open(filename, "wb") as f:
        f.write(response.content)


def run_multiprocessing(urls, start_time):
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download, args=(url, start_time))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


start_time = time.time()
if __name__ == "__main__":
    run_multiprocessing(sys.argv[1:], start_time)
