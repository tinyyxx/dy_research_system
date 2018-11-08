"""
重写jwt登陆后的返回json内容
"""


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'code': 101
    }
