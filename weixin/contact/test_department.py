import datetime
import json
import os

import pytest
import requests

from weixin.contact.token import Weixin
import logging

from weixin.contact.utils import Utils

class TestDepartment:
    def test_create_depth(self, token):
        parentid = 1

        for i in range(14):
            data = {
                "name": "第十期_seveniruby_" + str(parentid)+ str(datetime.datetime.now().timestamp()),
                "parentid": parentid,
            }

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": token},
                              json=data,
                              # proxies={"https": "http://127.0.0.1:8080",
                              #          "http": "http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            logging.debug(r)
            parentid = r["id"]
            assert r["errcode"]==0

    def test_create_name(self, token):
        data = {
            "name": "第十期_seveniruby",
            "parentid": 1,
        }

        logging.debug(data)
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()
        logging.debug(r)

    @pytest.mark.parametrize("name", [
        "广州研发中心",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    def test_create_order(self, name, token):
        data = {
            "name": name+Utils.udid(),
            "parentid": 1,
            "order": 1,
        }

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()

        #解密
        logging.debug(r)
        assert r["errcode"]==0

    def test_get(self, token):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": token }
                         ).json()

        logging.info(json.dumps(r, indent=2))
