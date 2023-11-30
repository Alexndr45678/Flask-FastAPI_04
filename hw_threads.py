# Команда для скачивания:
# --->>>  python .\hw_threads.py "https://freelance.today/uploads/images/00/07/62/2017/06/13/14c404.jpg"


import requests, threading, time, sys


def download(url, start_time):
    response = requests.get(url)
    filename = [elem for elem in url.split("/")][-1]
    print(f"Время загрузки файла {filename} : {time.time() - start_time:.2f} seconds")
    with open(filename, "wb") as f:
        f.write(response.content)


def run_threading(urls, start_time):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url, start_time])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


start_time = time.time()
if __name__ == "__main__":
    run_threading(sys.argv[1:], start_time)
