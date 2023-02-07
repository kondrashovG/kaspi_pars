import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent
import json


class Kaspi:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'
    }

    def __init__(self) -> None:
        pass

    def get_link(self):
        for i in range(1, 2):
            res = requests.get(
                f'https://kaspi.kz/shop/aktobe/c/boilers/?page={i}', headers=self.headers).content
            soup = BeautifulSoup(res, 'lxml')
            response = soup.find_all(class_='item-card__name')
            for res in response:
                name = res.text
                link = res['href']

                # self.get_prod(link)

                print(name, link)

    def get_prod(self, link):
        cookie = {'session': 'F0543788861AC1BBBA0FA0A974A40727; _ym_uid=1658774411377152374; _hjSessionUser_283363=eyJpZCI6ImE3YmVmZjg4LWJkYTUtNWY5NS05ZjY3LWRmYTdkMGRjM2I2OSIsImNyZWF0ZWQiOjE2NTg3NzQ0MTEyODIsImV4aXN0aW5nIjp0cnVlfQ==; current-action-name=Index; .AspNetCore.Culture=c%3Dru%7Cuic%3Dru; k_stat=0f2bb597-ce54-402b-a837-bab9997a13ff; ks.tg=90; _ALGOLIA=anonymous-d33e8584-4d60-4989-86f6-6d2563d2152d; ssaid=36e0ee10-0c49-11ed-b57d-cdb501e80158; kaspi.storefront.cookie.city=151010000; ks.cc=-1; test.user.group=46; _ga=GA1.2.66144144.1665643382; _gcl_au=1.1.483742933.1673950572; _ga_0R30CM934D=GS1.1.1673950571.1.1.1673950587.44.0.0; amp_6e9c16=UKJ84gE1xkUf8e-1fdbcwP...1gmvjnaj1.1gmvjnaj1.0.0.0; X-Mc-Api-Session-Id=Y6-150e6b84-4952-44a6-9fc3-49893baeddc2; _gcl_aw=GCL.1674021112.Cj0KCQiAq5meBhCyARIsAJrtdr4whOGGm4nIwXEFspKf--kjzWAV-v9MehRsEJg0tSRBlT4C3NBqZbcaAv0PEALw_wcB; _gac_UA-33540388-1=1.1674031053.Cj0KCQiAq5meBhCyARIsAJrtdr4whOGGm4nIwXEFspKf--kjzWAV-v9MehRsEJg0tSRBlT4C3NBqZbcaAv0PEALw_wcB; _ym_d=1674547902; _gid=GA1.2.955899020.1675679625; _ym_isad=1; __tld__=null'}

        # prof_url = 'https://kaspi.kz/shop/p/gornjak-ksvm-20-104921924/?c=151010000'
        res = requests.get(link, headers=self.headers, cookies=cookie).content
        print(res)
        soup = BeautifulSoup(res, 'lxml')
        response = soup.find_all(attrs={'class':'item__price-once'})
        for resp in response:
            print(resp.text)

    def get_salers(self):
        pass


if __name__ == '__main__':
    kas = Kaspi()
    link = 'https://kaspi.kz/shop/p/navien-ace-30k-dymohod-8500141/?c=151010000#!/item'
    kas.get_link()
    
    
    # print(kas.get_prod(link))
