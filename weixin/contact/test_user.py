import logging
import time

import pystache

from weixin.contact.user import User
from weixin.contact.utils import Utils


class TestUser:
    depart_id = 65

    @classmethod
    def setup_class(cls):
        # todo: create depart
        cls.user = User()

    def test_create(self):
        uid = "seveniruby_" + str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid + "@testerhome.com"

        }
        r = self.user.create(data)
        logging.debug(r)
        assert r['errcode'] == 0

    def test_create_by_real(self):
        uid = "seveniruby_" + str(time.time())
        mobile = str(time.time()).replace(".", "")[0:11]
        data = str(Utils.parse("user_create.json", {
            "name": uid,
            "title": "校长",
            "email": mobile + "@qq.com",
            "mobile": mobile
        }))
        data = data.encode("UTF-8")

        r = self.user.create(data=data)
        logging.debug(r)
        assert r['errcode'] == 0

    def test_list(self):
        r = self.user.list()
        logging.debug(r)

        r = self.user.list(department_id=65)
        logging.debug(r)
