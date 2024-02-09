row_names = ["A","B", "C","D","E","F","G","H","I","J"]
row_names_dict = {"A":0,"B":1, "C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}

def charToDigit(row):
    return row_names_dict[row]

def digitToChar(row):
    return row_names[row - 1]