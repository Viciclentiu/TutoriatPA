cuvinte = ["exemplul", "usor", "este","lista", "vida"]

#rez cu set
#ldc = [cuv for cuv in cuvinte if len(cuv) == len(set(cuv))]

#rez cu count
ldc = [cuv for cuv in cuvinte if ("".join(lit for lit in cuv if cuv.count(lit, 0, len(cuv) + 1) == 1) == cuv)]
print(ldc)
