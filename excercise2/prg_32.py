word = input("enter word : ")
def cheak(st1):
    st2 = st1.capitalize()
    if st1 == st2:
        print("string has first letter capital and all other letters are small")
    else:
        print("false condition")
cheak(word)
