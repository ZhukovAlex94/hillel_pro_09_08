list_orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def f_order(list_orders):
    return list(map(lambda item:
                    (item[0], round(item[2] * item[3] + 10, 2) if item[2] * item[3] < 100 else item[2] * item[3]),
                    list_orders))


if __name__ == "__main__":
    print(f_order(list_orders))
