from data import facts
#Memória de trabalho inicializada

work_memory = {
  'dor_de_cabeça': False,
  'garganta_inflamada': False,
  'Tosse': False,
  'cansaço':False,
  'tontura':False,
  'nauseas':False,
  'dificuldade_de_respirar':False,
  "Dor_no_peito":False,
  'desmaio':False
}

for fact in facts:
  work_memory[fact] = facts[fact]

for i in range(len(work_memory)):
  if work_memory["garganta_inflamada"] == True and work_memory["dificuldade_de_respirar"] == True:
    work_memory["covid"] = True
    print("diagnostico de covid")



