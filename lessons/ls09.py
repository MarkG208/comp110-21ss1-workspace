"""An example function definition."""

def my_max(a: int, b: int) -> int:
    """Returns the largest parameter.""" 
    if a >= b:
        return a
    else:
        return b

def main() -> None:
    """Entrypoint of a program."""
    print(my_max(10,15))

if __name__ == "__main__":
    main()

