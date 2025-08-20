import numpy as np, pandas as pd
a = np.arange(6).reshape(2,3) 
print("NumPy ok:", a.sum()) 
print("Pandas ok:", pd.DataFrame({"x":[1,2,3]}).x.mean()) 
