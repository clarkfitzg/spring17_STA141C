Tue May  9 16:49:23 PDT 2017

The way you express a computation in math may be different than the way you
write the code.

## Hard! Too big

(A + eeT).dot(x)
array([ 78.63633141,   1.52012141,   1.52012141])

eeT

1.,  1.,  1.],
1.,  1.,  1.],
1.,  1.,  1.]])

## Can do

A.dot(x)
array([ 77.11621,   0.     ,   0.     ])

## These are the same

eeT.dot(x)
array([ 1.52012141,  1.52012141,  1.52012141])

x.sum() * np.ones(len(x))

1.5201214136555972

# Algebra:

(A + eeT)x = Ax + eeTx
