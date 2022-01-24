def return_capitalized_hello() -> str:
    hello: str = 'hello'
    capitalized_hello: str = hello.capitalize()
    return capitalized_hello


def return_world() -> str:
    world: str = 'world'
    return world


def print_hello_world() -> None:
    capitalized_hello: str = return_capitalized_hello()
    world: str = return_world()
    hello_world: str = f'{capitalized_hello}, {world}!'
    print(hello_world)


if __name__ == '__main__':
    print_hello_world()
