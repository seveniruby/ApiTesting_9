import requests
import logging
import pytest
import json

class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url="https://testerhome.com/api/v3/topics.json?limit=2"
    def test_get(self):
        r=requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))


    def test_post(self):
        r=requests.get(self.url,
                        params={ "a":1 , "b": "string corntent" },
                        headers={"a": "1" , "b": "b2"},
                        proxies={"https": "http://127.0.0.1:7778",
                                 "http": "http://127.0.0.1:7778"},
                        verify=False
                        )
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_cookies(self):
        r=requests.get("http://47.95.238.18:8090/cookies", cookies={"a": "1", "b":"string content"})
        logging.info(r.text)


    def test_xueqiu_quote(self):
        url="https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
        r=requests.get(url,
                     params={ "category": "2"},
                     headers={'User-Agent': 'Xueqiu Android 11.19'},
                     cookies={"u": "3446260779", "xq_a_token":"5806a70c6bc5d5fb2b00978aeb1895532fffe502"}
                     )
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["data"]["category"] == 1




