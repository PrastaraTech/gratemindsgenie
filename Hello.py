# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from bardapi import Bard
import os
import requests
os.environ['_BARD_API_KEY'] = 'bwg9X4yXD1vxejZw4ckJf8HRlRHhiZ3XDmPjJ4u_iQKigoEAl7Gc-uyjZqFQZ2gy0x_AEQ.'
token='bwg9X4yXD1vxejZw4ckJf8HRlRHhiZ3XDmPjJ4u_iQKigoEAl7Gc-uyjZqFQZ2gy0x_AEQ.'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# session.cookies.set("__Secure-1PSID", token) 

bard = Bard(token=token, session=session, timeout=30)
bard.get_answer("When can I expect Apple 15 Pro Max delivery?")['content']

# Continued conversation without set new session
bard.get_answer("What is my last prompt??")['content']


