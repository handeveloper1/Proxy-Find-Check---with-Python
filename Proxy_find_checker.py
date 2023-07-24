import requests
import concurrent.futures


test_url = 'http://oguzhanyazman.weebly.com/'


def test_proxy(proxy):
    try:
        response = requests.get(test_url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f'Successful proxy: {proxy}')


    except:
        pass

def find_and_test_proxies():
    proxy_list_url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'  # Proxy listesi alabileceğiniz bir siteyi buraya girin


    response = requests.get(proxy_list_url)
    proxies = response.text.split('\n')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(test_proxy, proxies)

find_and_test_proxies()