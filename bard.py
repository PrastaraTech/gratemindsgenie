from gemini import Gemini


token = 'g.a000gAiiHOL30OH5KPd6hsrCa1UalhP3BCfnx3Ef4f8fIFsz-b3Paz_x_8l3AWWFCGW73OuQ_QACgYKAZYSAQASFQHGX2MiX5SuWqXgRke_5QYoYGVAGBoVAUF8yKohBnf7Nq8reBjVmNu0WSYD0076'
cookies = {
    "__Secure-1PSID": "g.a000gAiiHOL30OH5KPd6hsrCa1UalhP3BCfnx3Ef4f8fIFsz-b3Paz_x_8l3AWWFCGW73OuQ_QACgYKAZYSAQASFQHGX2MiX5SuWqXgRke_5QYoYGVAGBoVAUF8yKohBnf7Nq8reBjVmNu0WSYD0076",
    "__Secure-1PSIDTS": "sidts-CjIBYfD7Z7o4De28Ss90tZBgAbLLZRBVKb1UjScZ5rmwLIiOH2erwC7G5Ne8_K_b8tdKXhAA",
    "__Secure-1PSIDCC": "ABTWhQGxaujUvkmOwW-vSdQD7g6Goq1qq2CcF0crnxKNOi0Tg0yP97IH4Ui76HAHHsbZEyd6-Q",
}


client = Gemini(auto_cookies=True)

prompt = "Hello, Gemini. What's the weather like in Seoul today?"
response = client.generate_content(prompt)
print(response)
