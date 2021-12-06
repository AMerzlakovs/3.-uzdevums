
n=int(input("Ievadiet rindkopu skaitu: " )) # тут по условию вводиться количество строк в тексте
saraksts=set()
for _ in range(n):
    teksts=input().split()
    for x in teksts:
        saraksts.add(x) 
print(len(saraksts))