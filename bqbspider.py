import requests, time
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

def Data(url):
    try:
        data = requests.get(url=url)
    except:
        print('error')
        return
    try:
        soup = BeautifulSoup(data.text, 'html.parser')
        photo = soup.find_all(name='img', class_='ui image lazy')
    except:
        print('error')
        return
    for i in photo:
        path = i['alt']
        url = i['data-original']
        if url[-3:] == 'gif':
            path += '.gif'
        elif url[-3:] == 'jpg':
            path += '.jpg'
        else:
            path += '.png'
        download(path, url)
    return


def download(path, url):
    try:
        photodata = requests.get(url).content
        with open(r'bqb\%s' % path, 'wb') as w:
            w.write(photodata)
        print(path + '下载完成')
        return
    except:
        print(path + "下载错误！")
        return

if __name__ == "__main__":
    start = time.time()
    urllist = ['https://www.fabiaoqing.com/biaoqing/lists/page/%d.html' % i for i in range(1, 5)]
    pool = ThreadPoolExecutor(4)
    while len(urllist):
        pool.submit(Data,urllist[0])
        pool.join(2)
        urllist.pop(0)
    print("耗时:",time.time()-start)


