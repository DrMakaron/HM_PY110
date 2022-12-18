def to_upper_case(string):
    words = string.split()
    capitalized_words = list(map(str.capitalize, words))
    return ' '.join(capitalized_words)


if __name__ == '__main__':
    assert to_upper_case("How can mirrors be real if our eyes aren't real") == \
           "How Can Mirrors Be Real If Our Eyes Aren't Real"
