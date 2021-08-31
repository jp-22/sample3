class jay:
    father = "manojkumar"
    mother = "dakshaben"

print(hasattr(jay,'father'))
print(getattr(jay,'father'))
setattr(jay,'father',"manojkumar patel")
print(getattr(jay,'father'))
print(getattr(jay,'mother'))
delattr(jay,'mother')
print(getattr(jay,'mother'))