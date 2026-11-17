n = 14
m = 6
sol = [0] * (m + 1)
rez = []

def verif(sol, m):
    ok = True

    # sa nu fie consecutive nr in solutie
    for i in range(1, m):
        for j in range(i + 1, m + 1):
            if sol[j] - sol[i] == 1:
                ok = False
                break

    nr_par = 0
    nr_impar = 0

    for i in range(1, m + 1):
        if sol[i] % 2 == 0:
            nr_par += 1
        else:
            nr_impar += 1

    if nr_impar == m or nr_par == m:
        ok = False

    return ok


def bkt(pas):
    global n, sol, m, rez

    for v in range(sol[pas - 1] + 1, n + 1):
        sol[pas] = v

        if pas == m:
            if verif(sol, m) == True and 13 in sol:
                for i in range(1, m + 1):
                    print(sol[i], end=" ")
                print()
        else:
            bkt(pas + 1)

bkt(1)

