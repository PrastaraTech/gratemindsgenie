import requests
from bardapi import SESSION_HEADERS
from bardapi import Bard
from flask import Flask

app = Flask(__name__)


@app.route('/academics/<prompt>')  # Access using /hello/<name>
def academics(prompt):

    token = "egiiHHGDc6tztvQXIvS6uL5Jio_hRw3TuwB61hc2-GiZ0Uk_hAFkoaFnh27Lzl3yAPfm_g."

    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set(
        "__Secure-1PSIDTS", "sidts-CjIBPVxjSkpDYjmTNbOIYWwn45KkW80G-yvIHOCcg43JVNxlBDZ3y9cjhF5B6rhHqKxrLxAA")
    session.cookies.set(
        "__Secure-1PSIDCC", "ABTWhQF9l02bzP2JHgsZ6Uk6pmtyc_s-pRe83vJJ_ivMcMUjAgkc2jdpni6zPNQ7S4SqlZhMBw")

    bard = Bard(token=token, session=session)

    output = bard.get_answer(str(prompt))['content']
    print(output)

    return output


@app.route('/aiSelfAccount/<prompt>')  # Access using /hello/<name>
def aiSelfAccount(prompt):
    bard = Bard(token_from_browser=True)
    res = bard.get_answer("Do you like cookies?")
    return res['content']


if __name__ == '__main__':
    app.run(host='127.0.1.1', port=5000)  # Adjust host and port if needed
