from src.hello_world import greeting

def test_greeting():
    assert greeting("Dev") == "Hello World! I am in Dev!"
