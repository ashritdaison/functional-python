def evens(n):
    print(list(filter(lambda x: x%2 == 0, range(n))))


def threes(n):
    print(list(filter(lambda x : "3" in str(x), range(n))))


def small_words(text):
    print([word for word in text.split() if len(word) <= 4])


def squares(n):
    print(list(map(lambda x: x**2, range(n+1))))


def lengths(strings):
    print([len(word) for word in strings])
