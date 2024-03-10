from bardapi import SESSION_HEADERS
from bardapi import Bard
import requests

token = "g.a000gAiiHOL30OH5KPd6hsrCa1UalhP3BCfnx3Ef4f8fIFsz-b3Paz_x_8l3AWWFCGW73OuQ_QACgYKAZYSAQASFQHGX2MiX5SuWqXgRke_5QYoYGVAGBoVAUF8yKohBnf7Nq8reBjVmNu0WSYD0076."

session = requests.Session()
session.max_redirects = 40
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)
session.cookies.set(
    "__Secure-1PSIDTS", "sidts-CjIBYfD7ZxKRp4ZqNHQ2_OxBkXr9H2QT_L6DkXgBo2rs0la_kA1xbGeMB0LMpdmyvS73JRAA")
session.cookies.set(
    "__Secure-1PSIDCC", "ABTWhQElHFL4FZJqvS3zV-4imIA6ZZXGRkpcGRi2A4s75z-iCDFWDr5hrj8CgXv5YE56c1_7yw")

bard = Bard(token=token, session=session)

output = bard.get_answer(str("What is your name"))['content']
print(output)
