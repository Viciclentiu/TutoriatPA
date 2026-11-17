#prima problema
def nr_max_div(*val):
    L = set()
    for i in val:
        L.add(i)
    def divizori(x):
        div = 0
        for d in range(2,x//'2+1):
            if x % d ==0:
                div += 1
        return div
    L = sorted(L)
    maxim_div =-1
    for nr in L:
        nrdiv = divizori(nr)
        if nrdiv > maxim_div:
            maxim_div = nrdiv
    Q = []
    for nr in L:
        nrdiv = divizori(nr)
        if nrdiv == maxim_div:
            Q.append(nr)
            
    return Q
        

print(nr_max_div(1700,1002,288,2026,101,980,999,288,980))