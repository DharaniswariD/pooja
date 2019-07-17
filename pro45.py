d=input()
if d==d[::-1]:
    print("yes")
else:
    value=d.strip("0")
    if value==value[::-1]:
        print("yes")
    else:
        value=d.lstrip("0")
        if value==value[::-1]:
            print("yes")
        else:
print("no")
