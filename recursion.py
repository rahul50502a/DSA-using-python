# def printN(n):
#     if n > 0:
#         print(n)
#         printN(n-1)
#
#
# printN(10)


# ----------------------- Question No 2----------------------------------------

# def sumfirstnNnaturalNumbers(n):
#     if n==1:
#         return n
#     s = n + sumfirstnNnaturalNumbers(n-1)
#     return s
#
# print(sumfirstnNnaturalNumbers(3))

# ------------------------------------Question 3-------------------------------

# def sumNOdd(n):
#     if n == 1:
#         return n
#     return 2*n - 1 + sumNOdd(n-1)
# print(sumNOdd(10))

# ----------------------------Question 4-------------------------------------

# def sumNebeven(n):
#     if n == 1:
#         return 2
#     return 2*n + sumNebeven(n-1)
#
# print(sumNebeven(10))
# ----------------------------Question 5------------------------------
# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
#
# print(factorial(10))
# ------------------------------Question 6-------------------------------

# def squares(n):
#     if n == 1:
#         return 1
#     return n**2 + squares(n-1)
# print(squares(10))