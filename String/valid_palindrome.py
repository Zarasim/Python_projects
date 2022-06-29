# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.
# string are immutable and cannot be modified

s = 'cardrbl'


def solution(s):
    i = 0
    j = len(s) - 1
    tent = 1

    while i < j:
        if s[i] != s[j]:
            if tent == 0:
                return -1
            else:
                tent -= 1

        i += 1
        j -= 1

    return 1


print(solution(s))
