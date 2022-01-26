from data import facts
#Memória de trabalho inicializada

work_memory = {
"TEA":False,
"TDAH":False,
"TDDH":False,
"Hiperatividade":False,
"dislexia":False,

"sobrecarga sensorial": False,
'hiperfoco':False,
'dificuldade de leitura': False,
'desconforto ao toque': False,
'dificuldade de fala': False,
'dificuldade motora':False,
'dificuldade de comunicação':False,
'dificuldade de interação social': False,
'euforia recorrente': False,
'dificuldade de foco':False,
'Esteriotipia':False,
'deprimido recorrentemente': False
}
#TEA(Transtorno do Espectro Autista)
#Transtorno disruptivo da desregulação do humor

for fact in facts:
  work_memory[fact] = facts[fact]

for i in range(len(work_memory)):
  if work_memory["dificuldade de leitura"] == True and work_memory["dificuldade de fala"] == True and work_memory["dificuldade motora"] == True and work_memory["dislexia"] == False :
    work_memory["dislexia"] = True

  elif work_memory["desconforto ao toque"] == True and work_memory["dificuldade motora"] == True and work_memory["dificuldade de interação social"] == True and work_memory['sobrecarga sensorial'] == False:
    work_memory['sobrecarga sensorial'] = True

  elif work_memory['sobrecarga sensorial'] == True and work_memory['hiperfoco'] == False:
    work_memory['hiperfoco'] = True

  elif work_memory['hiperfoco'] == True and work_memory['TEA'] == False:
    work_memory['TEA'] = True
    print("alta possibilidade de criança com TEA")

  elif work_memory['euforia recorrente'] == True and work_memory['dificuldade de foco'] == True and work_memory['deprimido recorrentemente'] == False and work_memory['TDAH'] == False:
    work_memory['TDAH'] = True
    print('alta possibilidade de criança com TDAH')

  elif work_memory['euforia recorrente'] == True and work_memory['deprimido recorrentemente'] == True and work_memory['TDDH'] == False:
    work_memory['TDDH'] = True
    print('alta possibilidade de criança com TDDH')


