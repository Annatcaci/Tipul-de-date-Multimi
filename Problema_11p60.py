def powerset(A):
    LenA=len(A)
    submul=[1 << i for i in range(LenA)]
    for i in range(1 << LenA):
        yield [e for mul, e in zip(submul, A) if i & mul]
print(list(powerset(["A","B","C","D"])))