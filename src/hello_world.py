

def greeting(env: str = "Dev") -> str: 
    return f"Hello World! I am in {env}"


if __name__ == "__main__": 
    print(greeting())
