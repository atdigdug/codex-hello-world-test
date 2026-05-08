from hello import greet, greet_loud


def test_greet_default():
    assert greet() == "Hello, world!"


def test_greet_name():
    assert greet("Codex") == "Hello, Codex!"


def test_greet_loud_default():
    assert greet_loud() == "HELLO, WORLD!"


def test_greet_loud_name():
    assert greet_loud("Codex") == "HELLO, CODEX!"
