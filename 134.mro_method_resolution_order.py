#MRO - Method Resolution Order

class A:
    num=10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.mro())#To see the order
print(D.num)

#      A
#     / \
#    /   \
#   B     C
#   \     /
#      D