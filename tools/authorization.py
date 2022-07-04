import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException

"""
jwt 校验和生成
"""


class JwtToken(object):
    _salt = "w1rwi=d3q4l=ie=g-u$s8jevmj*zgg2h"
    _expired_message = dict(code=400, msg="token失效")
    _unknown_error_message = dict(code=401, msg="token解析失效")

    @classmethod
    def generate_token(cls, payload: dict) -> str:
        """
        :param payload: 传递加密的数据 exp是过期时间 其他随意
        :return:
        """
        headers = dict(typ="jwt", alg="HS256")
        result = jwt.encode(
            payload=payload, key=cls._salt, algorithm="HS256", headers=headers
        )
        return result

    @classmethod
    def parse_token(cls, token1: str) -> tuple:
        print("*" * 30)
        print("token", token1)
        print("*" * 30)

        verify_status = False
        try:
            payload_data = jwt.decode(token1, cls._salt, algorithms=["HS256"])
            verify_status = True
        except jwt.ExpiredSignatureError:
            payload_data = cls._expired_message
            raise HTTPException(status_code=400, detail="token过期")
        except Exception as _err:
            payload_data = cls._unknown_error_message
            raise HTTPException(status_code=400, detail="token错误")
        return verify_status, payload_data


if __name__ == "__main__":
    # 设置一秒过期  过期时间务必选择UTC时间
    test_data = dict(name="zaks", exp=datetime.utcnow() + timedelta(days=11))
    token = JwtToken.generate_token(test_data)

    res = JwtToken.parse_token(token)
    print(res)
