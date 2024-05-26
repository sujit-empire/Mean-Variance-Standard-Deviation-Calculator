import numpy as np

def calculate(list):
    if len(list) != 9:
        print("List must contain nine numbers.")
    else:
        arr = np.array(list)
        arr2 = arr.reshape(3,3)
        Mean = []
        M = arr2.mean(axis=0)
        Mean.append(M)
        M0 = arr2.mean(axis=1)
        Mean.append(M0)
        M1 = arr2.mean()
        Mean.append(M1)
        Var = []
        V = arr2.var(axis=0)
        Var.append(V)
        V0 = arr2.var(axis=1)
        Var.append(V0)
        V1 = arr2.var()
        Var.append(V1)
        STD = []
        std = arr2.std(axis=0)
        STD.append(std)
        std0 = arr2.std(axis=1)
        STD.append(std0)
        std1 = arr2.std()
        STD.append(std1)
        MAX = []
        ma = arr2.max(axis=0)
        MAX.append(ma)
        ma0 = arr2.max(axis=1)
        MAX.append(ma0)
        ma1 = arr2.max()
        MAX.append(ma1)
        MIN = []
        mi = arr2.min(axis=0)
        MIN.append(mi)
        mi0 = arr2.min(axis=1)
        MIN.append(mi0)
        mi1 = arr2.min()
        MIN.append(mi1)
        SUM = []
        s = arr2.sum(axis=0)
        SUM.append(s)
        s0 = arr2.sum(axis=1)
        SUM.append(s0)
        s1 = arr2.sum()
        SUM.append(s1)
        calculations = {"mean":Mean,
                        "variance":Var,
                        'standard deviation': STD,
                        'max': MAX,
                        'min': MIN,
                        'sum':SUM}
        return calculations
