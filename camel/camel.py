def camtosnake(s):
    cam = ""
    for c in s:
        if c.islower():
            cam += c
        else:
            cam += "_" + c.lower()
    return cam

print("snake_case: ",camtosnake(input("camelCase: ")))
