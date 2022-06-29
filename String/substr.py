
string = 'ABACDAQA BACDAQA ACDAQAW AQASDSD'
strings = string.split()


def substring_in_string(sub, string):
    return sub in string


def compare_strings(str, text):
    char = ''
    list_subs = []
    for l in str:
        char += l
        if substring_in_string(char, text):
            if str.endswith(l):
                list_subs.append(char)
            continue
        else:
            list_subs.append(char[:-1])
            char = l

    return max(list_subs, key=len)


str = strings[0]
for text in strings[1:]:
    str = compare_strings(str, text)

print(str)
