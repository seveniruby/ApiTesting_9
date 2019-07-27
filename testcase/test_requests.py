import requests
import logging
import pytest
import json
import jsonpath
from hamcrest import *

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
        assert r.json()["data"]["category"] == 2
        assert r.json()["data"]["stocks"][0]["name"] == "华宝中短债债券C"
        assert jsonpath.jsonpath(r.json(),
                                 "$.data.stocks[?(@.symbol == 'F006947')].name")[0]=="华宝中短债债券A"
        assert_that(jsonpath.jsonpath(r.json(),"$.data.stocks[?(@.symbol == 'F006947')].name")[0],
                    equal_to("华宝中短债债券B"), "比较上市代码与名字")

    def test_hamcrest(self):
        assert_that(0.1 * 0.1, close_to(0.01, 0.000000000000001))
        #assert_that(0.1 * 0.1, close_to(0.01, 0.000000000000000001))
        assert_that(
            ["a", "b", "c"],
            all_of(
                has_items("c", "d"),
                has_items("c", "a")
            )
        )











