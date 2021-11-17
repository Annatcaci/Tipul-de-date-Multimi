A=set(map(str,input("Introduceti cifrele in multimea A= ").split()))
for e in A:
    if (e.isupper()): 
        a=True 
if a==True:   
    B=set(map(str,input("Itroduceti cifrele in multimea B= ").split()))  
    for e in B:
        if (e.isupper()): 
            b=True
if b==True:
    print("Intersectia multimilor:",A.intersection(B))
    print("Reuniunea multimilor:",A.union(B))
    print("Diferenta multimii A de B:",A.difference(B))
    print("Diferenta multimii B de A:",B.difference(A))


            
            
