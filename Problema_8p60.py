A=set(map(int,input("Introduceti cifrele in multimea A ").split()))
B=set(map(int,input("Itroduceti cifrele in multimea B ").split()))
    #b=all(isinstance(e, int) for e in B)
    #if b==True:
print("Intersectia multimilor:",A.intersection(B))
print("Reuniunea multimilor:",A.union(B))
print("Diferenta multimii A de B:",A.difference(B))
print("Diferenta multimii B de A:",B.difference(A))
#else:
#    print("Introduceti doar numerele intregi")

