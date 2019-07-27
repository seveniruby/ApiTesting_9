import logging
import time

import pystache
import requests

from weixin.contact.token import Weixin


class TestUser:
    depart_id = 65

    @classmethod
    def setup_class(cls):
        # todo: create depart
        pass

    def test_create(self):
        uid = "seveniruby_" + str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid + "@testerhome.com"

        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=data,

                          ).json()
        logging.debug(r)
        assert r['errcode'] == 0

    def test_create_by_template(self):
        uid = "seveniruby_" + str(time.time())
        mobile=str(time.time()).replace(".", "")[0:11]
        data=str(self.get_user({
            "name": uid,
            "title": "校长",
            "email": "1@1.com",
            "mobile": mobile
        }))
        data=data.encode("UTF-8")

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          data=data,
                          headers={"content-type": "application/json; charset=UTF-8"}
                          ).json()
        logging.debug(r)
        assert r['errcode'] == 0


    def test_list(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={"access_token": Weixin.get_token(),
                                 "department_id": 1,
                                 "fetch_child": 0}
                         ).json()

        logging.debug(r)


    def get_user(self, dict):
        template="".join(open("user_create.json").readlines())
        return pystache.render(template, dict)
    def test_get_user(self):
        logging.debug(self.get_user({ "name": "seveniruby", "title": "校长", "email": "1@1.com"}))
