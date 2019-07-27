import requests
import yaml
import logging

class Weixin:
    logging.basicConfig(level=logging.DEBUG)
    _token= ""
    @classmethod
    def get_token(cls):
        if len(cls._token)==0:
            conf=yaml.safe_load(open("weixin.yaml"))
            logging.debug(conf["env"])

            r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": conf["env"]["corpid"],
                                 "corpsecret": conf["env"]["secret"]}
                         ).json()
            cls._token=r["access_token"]

        return cls._token
