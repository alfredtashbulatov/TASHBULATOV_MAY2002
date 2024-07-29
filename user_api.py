import allure
import requests


class Api():

    def __init__(self, url) -> None:
        self.url = url

    @allure.title("Api. Метод добавления товара в корзину")
    def add_goods(self):
        data = {"idCookie":"360310",
                "idProd":"180",
                "type":"add"
            }
        header = {
            "accept" : "application/json, text/javascript,\
                */*; q=0.01",
            "content-type" : "application/x-www-form-urlencoded;\
                charset=UTF-8",
            "cookie" : "BX_USER_ID=e42b17dc97fd5d3a8ea4a806a2fd0eca;\
                _ym_uid=1721241962222052932; _ym_d=1721241962;\
                    basketor=845543; PHPSESSID=5HJQrX1FbXGwwYHyMorj3VPk9CKV6W0G;\
                        _ym_isad=2; _ym_visorc=w"
        }
        res = str(requests.post(self.url, headers=header, json=data).json)
        return res

    @allure.title("Api. Увелечения количества товара в корзине")
    def goods_basket_plus(self):
        data = {"idCookie":"360310",
                "idProd":"180",
                "type":"plus"
            }
        header = {
            "accept" : "application/json, text/javascript,\
                */*; q=0.01",
            "content-type" : "application/x-www-form-urlencoded;\
                charset=UTF-8",
            "cookie" : "BX_USER_ID=e42b17dc97fd5d3a8ea4a806a2fd0eca;\
                _ym_uid=1721241962222052932; _ym_d=1721241962;\
                    basketor=845543; PHPSESSID=5HJQrX1FbXGwwYHyMorj3VPk9CKV6W0G;\
                    _ym_isad=2; _ym_visorc=w"
        }
        res = str(requests.post(self.url,
                                headers=header,
                                json=data).json)
        return res


    @allure.title("Api. Удаление товара из корзины")
    def delete_goods_basket(self):
        data = {"idCookie":"360310",
                "idProd":"180",
                "type":"delete"
            }
        header = {
            "accept" : "application/json, text/javascript,\
                */*; q=0.01",
            "content-type" : "application/x-www-form-urlencoded;\
                charset=UTF-8",
            "cookie" : "BX_USER_ID=e42b17dc97fd5d3a8ea4a806a2fd0eca;\
                _ym_uid=1721241962222052932; _ym_d=1721241962;\
                    basketor=845543; PHPSESSID=5HJQrX1FbXGwwYHyMorj3VPk9CKV6W0G;\
                        _ym_isad=2; _ym_visorc=w"
        }
        res = str(requests.post(self.url, headers=header, json=data).json)
        return res
