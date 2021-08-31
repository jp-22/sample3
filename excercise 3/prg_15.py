import pickle

variable1 = "jp bhai"

with open("my_variables.data","wb") as f:
    pickle.dump(variable1, f)



