import datetime
import json
import os

import requests

from weixin.contact.token import Weixin
import logging


class TestDepartment:
    @classmethod
    def setup_class(cls):
        print("setup class")
        Weixin.get_token()
        print(Weixin._token)

    def setup(self):
        print("setup")

    def test_create_depth(self):
        parentid = 1

        for i in range(15):
            data = {
                "name": "第十期_seveniruby_" + str(parentid)+ str(datetime.datetime.now().timestamp()),
                "parentid": parentid,
            }

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": Weixin.get_token()},
                              json=data,
                              # proxies={"https": "http://127.0.0.1:8080",
                              #          "http": "http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            logging.debug(r)
            parentid = r["id"]

    def test_create_name(self):
        data = {
            "name": "第十期_seveniruby",
            "parentid": 1,
        }

        logging.debug(data)
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": Weixin.get_token()},
                          json=data
                          ).json()
        logging.debug(r)

    def test_create_order(self):
        data = {
            "name": "广州研发中心",
            "parentid": 1,
            "order": 1,
        }

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": Weixin.get_token()},
                          json=data
                          ).json()
        logging.debug(r)

    def test_get(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": Weixin.get_token()}
                         ).json()

        logging.info(json.dumps(r, indent=2))
