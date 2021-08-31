with open("test10_file.txt","rb+") as f:

    f.write(b'jay patel')
    s = f.read()
print(s)