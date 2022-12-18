from string import ascii_lowercase, ascii_uppercase


def encryptor(key, string):
    if not string:
        return ''

    buffer = []

    def insert_element(symbol_set, index_):
        if index_ + key > len(symbol_set):
            buffer.append(symbol_set[index_ + key - len(symbol_set)])
        else:
            buffer.append(symbol_set[index_ + key])

    for position, char in enumerate(list(string)):
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            insert_element(ascii_lowercase, index)
        elif char in ascii_uppercase:
            index = ascii_uppercase.index(char)
            insert_element(ascii_uppercase, index)
        else:
            buffer.insert(position, char)

    return ''.join(buffer)


if __name__ == '__main__':
    assert encryptor(13, '') == ''
    assert encryptor(13, 'Caesar Cipher') == 'Pnrfne Pvcure'
    assert encryptor(-5, 'Hello World!') == 'Czggj Rjmgy!'
    assert encryptor(27, 'Whoopi Goldberg') == 'Xippqj Hpmecfsh'
