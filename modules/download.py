import threading
from tqdm import tqdm
import requests


def dl(urls, save_to):
    for url in urls:
        def dl_thread(url_in_thread):
            with requests.get(url_in_thread, stream=True) as r:
                with open(save_to, "wb") as f:
                    pbar = tqdm(unit="B", unit_scale=True, total=int(r.headers['Content-Length']),
                                position=urls.index(url_in_thread))
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            if pbar.n < pbar.total - 1:
                                pbar.update(len(chunk))
                            f.write(chunk)
            pbar.clear()

        threading.Thread(target=dl_thread, args=(url,)).start()
