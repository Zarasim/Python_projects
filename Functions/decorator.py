def decor(func):

    def wrap(text):
        print("============")
        func(text)
        print("============")

    return wrap


@decor
def print_text(string):
    print(string)


#decorated = decor(print_text,'Hi')
#lentxt = decorated()
print_text('Hi all !')
