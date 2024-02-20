duljina = int(input())
shir = int(input())
visochina = int(input())
procent = float(input()) /100  # 17 input means => 0.17 == 17%

obem_akvarium = duljina * shir * visochina
obem_litri = obem_akvarium * 0.001
nujni_litri = obem_litri * (1 - procent)
#print(obem_akvarium)
#print(obem_litri)
print(nujni_litri)