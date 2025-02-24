with open('Arquivo.txt', 'rb') as f:
    read_data = f.read()
    print(read_data)
    f.close()