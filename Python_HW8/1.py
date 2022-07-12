import re


def email_parse(email_address):
    result = re.compile(r'\w+@\w+\.\w+')
    if result.match(email_address):
        user_and_domain = re.split(r'@', email_address)
        email_dict = dict(username=user_and_domain[0], domain=user_and_domain[1])
        print(email_dict)
    else:
        raise ValueError(f'wrong email: {email_address}')


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
