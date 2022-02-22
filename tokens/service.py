import gevent


def request_to_third_party_api(token: str, ip_address: str, text: str) -> (str, str, str):
    gevent.sleep(5)  # here is request to third party api
    return token, ip_address, text
