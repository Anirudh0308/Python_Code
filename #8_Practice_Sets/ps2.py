# c/5 = (f-32)/9


def f_to_c(f):
    return 5*(f-32)/9


f = int(input("Enter temprature in F: "))
print(f_to_c(f))