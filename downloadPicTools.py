import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}


def download(file_path, url):
    if url.startswith('http') or url.startswith('https'):
        name = file_path + url.split('/')[-1]
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            with open(name, 'wb') as f:
                f.write(res.content)
