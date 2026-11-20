#  Pentru un student se cunosc următoarele informații: numele, grupa și o listă cu
# creditele obținute la toate examenele din anul respectiv.
# a) Scrieți o funcție care să primească numele unui fișier de tip CSV care conține
# informații despre mai mulți studenți (i.e., informațiile despre un student se găsesc
# pe o linie și sunt despărțite între ele prin câte o virgulă) și furnizează o listă
# conținând informațiile despre studenți sub forma unei liste de tupluri (i.e.,
# informațiile despre un student se vor păstra într-un tuplu de forma (nume, grupa,
# (nota_1, nota_2, ..., nota_n))).
# b) Considerând o listă de studenți, scrieți o funcție care să adauge la informațiile
# despre un student situația sa școlară: promovat (True) sau nepromovat (False).
# Pentru a fi considerat promovat, un student trebuie să nu aibă nici un examen
# nepromovat (adică o valoare egală cu 0 în lista creditelor), iar suma creditelor
# obținute să fie mai mare sau egală decât un număr minim de credite dat.
# c) Scrieți câte o funcție care să furnizeze cheia necesară sortării listei cu informații
# despre studenți în raport de fiecare dintre următoarele criterii:
# • crescător după grupă și în fiecare grupă în ordine alfabetică;
# • întâi studenții promovați, apoi cei nepromovați și în fiecare categorie în ordine
# alfabetică;
#  descrescător după suma creditelor, iar în cazul unor sume egale în ordinea
# crescătoare a grupei și în ordine alfabetică în cadrul grupei;
# • în ordinea crescătoare a grupelor, în cadrul fiecărei grupe mai întâi studenții
# promovați, iar apoi cei nepromovați, în fiecare categorie
# (promovat/nepromovat) în ordinea descrescătoare a sumei creditelor și, în
# cazul unor sume egale, în ordine alfabetică.


def citireInformatiiStudent(fisier) :
    fin = open(fisier)

    studenti = []

    for linie in fin :
        student = linie.strip().split(',')

        nume = student[0]
        grupa = int(student[1])
        note = tuple(int(x) for x in student[2:])

        studenti.append((nume, grupa, note))

    fin.close()

    return studenti

def promovare(studenti, min_credite = 32) :
    for i in range(len(studenti)):
        if 0 not in studenti[i][2] and sum(studenti[i][2]) >= min_credite :
            studenti[i] += (True,)
        else:
            studenti[i] += (False,)

studenti = citireInformatiiStudent('ex1.txt')
promovare(studenti, 20)
print(*studenti, sep = '\n')

def criteriu_1(t):
    return t[1], t[0]

def criteriu_2(t):
    return -t[3], t[0]

def criteriu_3(t):
    return -sum(t[2]), t[1], t[0]

def criteriu_4(t):
    return t[1], -t[3], -sum(t[2]), t[0]