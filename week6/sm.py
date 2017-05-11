class SparseMatrix(dict):
    def __add__(self, other):
        out = self.copy()
        for key in other:
            if key in self:
                out[key] += other[key]
            else:
                out[key] = other[key]
        return out

sm1 = SparseMatrix()
sm2 = SparseMatrix()

sm1[(1, 0)] = 100
sm2[(1, 0)] = 100
sm2[(0, 0)] = 3

sm3 = sm1 + sm2
