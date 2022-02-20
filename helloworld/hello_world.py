def return_hello_world() -> str:
    hello_world: str = 'Hello, world!'
    return hello_world


def print_hello_world() -> None:
    hello_world: str = return_hello_world()
    print(hello_world)


if __name__ == '__main__':
    print_hello_world()
