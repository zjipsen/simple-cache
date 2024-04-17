from src.uniq import UniqChecker

def test_empty_instantiate():
    checker = UniqChecker()
    assert checker.known == {}

def test_add_one():
    checker = UniqChecker()
    assert checker.handle("a") == "a"
    assert checker.handle("b") == "b"
    assert checker.handle("a") == None

def test_add_two():
    checker = UniqChecker()
    assert checker.handle("a") == "a"
    assert checker.handle("b") == "b"
    assert checker.handle("a") == None
    assert checker.known["a"] == 2
    assert checker.known["b"] == 1

def test_lru():
    checker = UniqChecker()
    assert checker.handle("a") == "a"
    assert checker.handle("b") == "b"
    assert checker.handle("a") == None
    assert checker.lru() == "b"
