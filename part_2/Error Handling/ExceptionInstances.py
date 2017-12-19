#Write a statement that attempts to convert an empty string to an integer, and wrap it in a try/except block.


try:
    int("")
except Exception as exc:
    print(exc)
    print("----")
    print(str(exc))
    print("----")
    print(type(exc))
