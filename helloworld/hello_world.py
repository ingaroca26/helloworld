def return_hello_world() -> str:
    hello: str = 'hello'
    world: str = 'world'
    capitalized_hello: str = hello.capitalize()
    hello_world: str = f'{capitalized_hello}, {world}!'
    return hello_world


def print_hello_world() -> None:
    hello_world: str = return_hello_world()
    print(hello_world)


def hello_world() -> None:
    print_hello_world()


if __name__ == '__main__':
    hello_world()
