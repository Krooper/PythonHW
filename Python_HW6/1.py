info_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        line = line.split(' - - ')
        remote_addr = line[0]
        line[1] = line[1].split(' ')
        request_type = line[1][2].replace('"', '')
        requested_resource = line[1][3]
        info_tuple = (remote_addr, request_type, requested_resource)
        info_list.append(info_tuple)
    for info in info_list:
        print(info)
