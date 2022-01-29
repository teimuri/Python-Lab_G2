import numpy as np
a="kins"
b="sitin"
d=np.zeros((len(a)+1,len(b)+1))
d[0]=np.array(list(range(len(d[0]))))
d[:,0]=np.array(list(range(len(d[:,0]))))
for j in range(1,len(b)+1):
    for i in range(1,len(a)+1):
      if a[i-1] == b[j-1]:
        temp = 0
      else:
        temp = 1

      d[i, j] = min(d[i-1, j] + 1,
                         d[i, j-1] + 1,
                         d[i-1, j-1] + temp)
print(int(d[len(a),len(b)]))
