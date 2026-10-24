import pandas as pd
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr.size)
print(arr.min())
print(arr.max())
print(arr.ndim)

class Main:
    def __init__(self):
        pass

    def data(self):
        data = pd.DataFrame(arr)
        print(data)

main = Main()
main.data()
