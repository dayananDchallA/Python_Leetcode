def get_counter(s='aba'):
    counter = {}
    for c in s:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    print(counter)


def get_counter_defaultdict(s='aba'):
    from collections import defaultdict
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1

    print(counter)


if __name__ == "__main__":
    get_counter()
    get_counter_defaultdict()