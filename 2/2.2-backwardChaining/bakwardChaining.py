from data import facts
from data import hypothesis
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
'deprimido recorrentemente': False}
#TEA(Transtorno do Espectro Autista)
#Transtorno disruptivo da desregulação do humor

global resp

for hip in hypothesis:
  work_memory[hip] = hypothesis[hip]
  resp = hip

dec = 0

for i in range(len(work_memory)):
  if work_memory["dislexia"] == True:
    work_memory["dificuldade de leitura"] = True
    work_memory["dificuldade de fala"] = True 
    work_memory["dificuldade motora"] = True 
    

  if work_memory['sobrecarga sensorial'] == True:
    work_memory["desconforto ao toque"] = True
    work_memory["dificuldade motora"] = True
    work_memory["dificuldade de interação social"] = True
    

  if work_memory['hiperfoco'] == True:
    work_memory['sobrecarga sensorial'] = True 
    

  if work_memory['TEA'] == True:
    work_memory['hiperfoco'] = True 

  if work_memory['TDAH'] == True:
    work_memory['euforia recorrente'] = True
    work_memory['dificuldade de foco'] = True
    work_memory['deprimido recorrentemente'] = False

  if work_memory['TDDH'] == True:
    work_memory['euforia recorrente'] = True
    work_memory['deprimido recorrentemente'] = True

  if dec != 1:
    dec = 0
    for fact in facts:
      if work_memory[fact] != facts[fact]:
        dec = -1
    
    if dec == 0:
      print('alta possibilidade de criança com '+ resp)
      dec = 1



print("\n")
for memory in work_memory:
  print( memory + " " + str(work_memory[memory]))
