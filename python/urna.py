candidatos = []
for i in range(3):
    candidato = str(input('digite o nome dos canditados: '))
    candidatos.append(candidato)
   
total_votos = int(input("Digite o número total de votos: "))
votos = [0, 0, 0]
 
print(candidatos)
 
for i in range(total_votos):
   nome_candidato = input("Digite o nome do candidato : ")
   while nome_candidato not in candidatos:
       print("Nome de candidato inválido. Digite novamente.")
       nome_candidato = input("Digite o nome do candidato " + candidatos[0]+", " +candidatos[1]+", "+ candidatos[2]+ ":")
   indice_candidato = candidatos.index(nome_candidato)
   votos[indice_candidato] += 1
 
indice_vencedor = votos.index(max(votos)) 
vencedor = candidatos[indice_vencedor]

if votos[0] == votos[1] or votos[0] == votos[2]:
    print('empate')
elif votos[1] == votos[2]:
    print('empate')
else:    
    print("Resultados da eleição:")
for i in range(len(candidatos)):
   print(f"{candidatos[i]}: {votos[i]} votos")
print(f"Vencedor da eleição: {vencedor}")
 
