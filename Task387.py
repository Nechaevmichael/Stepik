# Исправьте код с предыдущего задания так, чтобы на экран вывело bye и hello
# Код с предыдущего задания:

# Sample Input:

# Sample Output:

# bye
# hello

def outer() -> None:

    def say_bye() -> None:
        print('bye')

    def say_hello() -> None:
        print('hello')

    say_bye()
    say_hello()
outer()