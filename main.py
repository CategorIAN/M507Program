from gekko import GEKKO
import numpy as np

def f():
    cov = np.vectorize(lambda x: round(-50 + 100 * x, 2))(np.random.rand(4, 4))
    print(cov)
    r_vec = np.array([2, 4, 6, 8])
    r = 5
    m = GEKKO()
    w = m.Array(m.Var, 4)
    m.Equation(np.sum(w) == 1)
    m.Equation(np.sum([r_vec[i] * w[i] for i in range(4)]) == r)
    m.Equations([w[0]>=0, w[1]>=0, w[2]>=0, w[3]>=0])
    m.Obj(np.sum([np.sum([w[i] * cov[i][j] * w[j] for j in range(4)]) for i in range(4)]))
    m.solve()
    print(w)




if __name__ == '__main__':
    f()



