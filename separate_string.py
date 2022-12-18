import numpy as np


def sep_str(string):
    splitted_string = string.split()
    columns_number = len(splitted_string)
    rows_number = len(max(splitted_string, key=len))

    tmp = []

    for i in range(len(splitted_string)):
        if len(splitted_string[i]) != rows_number:
            a = list(splitted_string[i])
            for j in range(abs(len(splitted_string[i]) - rows_number)):
                a.append('')
            for element in a:
                tmp.append(element)
        else:
            for element in list(splitted_string[i]):
                tmp.append(element)

    array_ = np.array(tmp)
    return array_.reshape(columns_number, rows_number).transpose()


if __name__ == '__main__':
    print(sep_str('Just Live Life Man'))
    print(sep_str('Python the best language ever'))
