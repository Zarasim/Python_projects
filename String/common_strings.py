# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'


def solution(sentence1, sentence2):

    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    #res = list(set1.symmetric_difference(set2))
    #res += list(set1.intersection(set2))

    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))


print(solution(sentence1, sentence2))
