def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def greet_loud(name: str = "world") -> str:
    return greet(name).upper()


if __name__ == "__main__":
    print(greet())
