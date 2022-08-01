import json


class JIM:
    """
    JIM base class
    """

    @classmethod
    def pack(cls, dict_msg):
        """
        Создание сообщения, пригодного для отправки через TCP
        :param dict_msg: dict
        :return: str
        """
        str_msg = json.dumps(dict_msg)
        return str_msg.encode("utf8")

    @classmethod
    def unpack(cls, bt_str):
        """
        Распаковка полученного сообщения
        :param bt_str: str
        :return: dict
        """
        str_decoded = bt_str.decode('utf-8')
        return json.loads(str_decoded)


class JimMessage(JIM):
    """
    class JimMessage
    """

    pass


class JimResponse(JIM):
    """
    class JimResponse
    """

    @classmethod
    def status_200(cls):
        """
        Message for status 200
        :return:
        """

        msg = {
            "response": 200,
            "alert": "Необязательное сообщение/уведомление"
        }
        return cls.pack(msg)

    @classmethod
    def status_402(cls):
        """
        Message for status 402
        :return:
        """

        msg = {
            "response": 402,
            "error": "This could be wrong password or no account with that name"
        }
        return cls.pack(msg)

    @classmethod
    def status_409(cls):
        """
        Message for status 409
        :return:
        """

        msg = {
            "response": 409,
            "alert": "Someone is already connected with the given user name"
        }
        return cls.pack(msg)