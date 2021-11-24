import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pattern = re.compile(r'^.{1,4}.+(?=\s[-]\s[-])')
        remote_addr = re.search(pattern, line).group()
        pattern = re.compile(r'\d{1,2}/.+(?=])')
        request_datetime = re.search(pattern, line).group()
        pattern = re.compile(r'GET|HEAD')
        request_type = re.search(pattern, line).group()
        pattern = re.compile(r'/downloads/product_\d')
        requested_resource = re.search(pattern, line).group()
        pattern = re.compile(r'\d{1,3}(?=\s\d{1,3})')
        response_code = re.search(pattern, line).group()
        pattern = re.compile(r'\d{1,3}(?=\s["])')
        response_size = re.search(pattern, line).group()
        parsed_raw = (remote_addr, request_datetime, request_type,
                      requested_resource, response_code,
                      response_size)
        print(parsed_raw)
