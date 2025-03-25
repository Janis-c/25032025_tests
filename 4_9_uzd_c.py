# Programma pieprasa divus masīvus (pirmajā ir N veseli skaitļi, bet otrajā - M veseli skaitļi), un izvada uz ekrāna šādu informāciju

# c kurā masīvā starpība starp vislielāko un vismazāko vērtību ir lielāka
m = int(input("Cik skaitļu pirmajā masīvā? > "))
n = int(input("Cik skaitļu otrajā masīvā? > "))
skaitli_m = []
skaitli_n = []
for i in range(m):
    skaitli_m.append(int(input("Ievadiet skaitli 1. masīvā > ")))
for i in range(n):
    skaitli_n.append(int(input("Ievadiet skaitli 2. masīvā > ")))

max_m = max(skaitli_m)
min_m = min(skaitli_m)
max_n = max(skaitli_n)
min_n = min(skaitli_n)

if (max_m - min_m) > (max_n - min_n):
    print("Pirmajā masīvā starpība starp vislielāko un vismazāko vērtību ir lielāka")
else:
    print("Otrajā masīvā starpība starp vislielāko un vismazāko vērtību ir lielāka")
