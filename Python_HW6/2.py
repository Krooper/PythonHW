request_counter = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        line = line.split(' - - ')
        remote_addr = line[0]
        if remote_addr in request_counter.keys():
            request_counter[remote_addr] += 1
        else:
            request_counter[remote_addr] = 1

    max_value = 0
    max_key = ''
    for key, value in request_counter.items():
        if value > max_value:
            max_value = value
            max_key = key
    print(max_key, max_value)
