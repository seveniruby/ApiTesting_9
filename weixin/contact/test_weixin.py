from unittest import TestCase

from weixin.contact.token import Weixin


class TestWeixin(TestCase):
    def test_get_token(self):
        print(Weixin.get_token())
        assert Weixin.get_token() !=""

