import re


def email_parser(email):
    res = {}
    pattern = re.compile(r'(\w+)([@])(\w+)([.]\w+)')
    if pattern.findall(email) == []:
        raise ValueError(': wrong email')
    else:
        part = pattern.finditer(email)
        for i in part:
            res['username'] = i.group(1)
            res['domain'] = i.group(3)
            return print(res)


email_parser('lo@lo.com')
