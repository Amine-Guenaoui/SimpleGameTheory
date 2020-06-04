from random import randrange

print('Petit programme qui concerne tp 1 Theorie des jeux:')
print("Dans ce TP nous allons appliquer toutes les notions vues en cours")
print("en stratégies pures dans un jeu à 2 joueurs et plus, à savoir la détermination d’une")
print("stratégie strictement dominante, stratégie faiblement dominante, équilibres par")
print("élimination successives des stratégies fortement dominantes et faiblement")
print("dominantes, équilibres de Nash et profils Pareto dominants et Niveau de sécurité")
print("d’une stratégie ainsi que d’un joueur")
print("pour commencer")


#functions 
def choix():
    print("les operations : ")
    print("1 : determiner la stratégie strictement dominante ")
    print("2 : determiner la stratégie faiblement dominante ")
    print("3 : equilibres d'élimination successives des stratégies fortement dominantes ")
    print("4 : equilibres d'élimination successives des stratégies faiblement dominantes ")
    print("5 : équilibres de Nash")
    print("6 : profil de pareto ")
    print("7 : niveau de securite ")
    print()

# #recursive manually fill the matrix
def fill_matrix(dims, callback, n=0, indices=[]):
  dim = dims[n]
  result = []
  for i in range(dim):
    new_indices = indices + [i]
    if n + 1 < len(dims):
      result.append(fill_matrix(dims, callback, n + 1, new_indices))
    else:
        el = []
        for x in range(len(dims)):
            el.append(int(input("gain de joueur"+str(x+1))))
        result.append(callback(el))

  return result

#recursive auto fill
def auto_fill_matrix(dims, callback, n=0, indices=[]):
  dim = dims[n]
  result = []
  for i in range(dim):
    new_indices = indices + [i]
    if n + 1 < len(dims):
      result.append(auto_fill_matrix(dims, callback, n + 1, new_indices))
    else:
        el = []
        for x in range(len(dims)):
            print("gain de joueur"+str(x+1))
            el.append(randrange(10))
        result.append(callback(el))

  return result

#recursive explorer
def explore(l,i,nj):
    
    if(i<nj):
        for index,s in enumerate(l):
            #print(index)
            if type(s)==list: 
              explore(s,i+1,nj)
    else:
      print(l)

def getIndexes(l,index = []):
    for i,subl in enumerate(l):
      if type(subl)==list :
        yield from getIndexes(subl,index+[i])
      else:
        yield [index+[i],subl] # or just yield (index+[i]) for the index only  

def showIndexes(l,comb):
    for index in getIndexes(l):
      comb.append(index)
      print(index)

def getStrategyValues(player,strategy,comb):
    c = []
    print("player " +str(player+1)+" payoffs of strategy "+str(strategy+1))
    for l in comb:
      if  l[0][player] == strategy :
          if l[0][len(l[0])-1] == player :
            c.append(l[1]) # value (payoff ) of the current index
            print(l[1])
        #  print("------")
    return c

def compareStrictDomianaitingStrategy(str1,str2):
    i = 0
    print("-------------------------------------")
    while i < len(str1):
     print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
     if str1[i] < str2[i]: # if strategy 1 is dominante
          break;
     i+=1
   # print("------")
    if i >= len(str1):
       return True
    return False

def compareWeakDominaitingStrategy(str1,str2):
    i = 0
    while i < len(str1):
     print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
     if str1[i] <= str2[i]: # if strategy 1 is dominante
          break;
     i+=1
    if i == len(str1):
       return True
    return False
def compareStrictDominaitedStrategy(str1,str2):
    i = 0
    while i < len(str1):
      print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
      if str1[i] > str2[i]: # if strategy 1 is strictly dominaited
          break;
      i+=1
    if i == len(str1):
        return True
    return False

def compareWeakDominaitedStrategy(str1,str2):
    i = 0
    while i < len(str1):
      print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
      if str1[i] >= str2[i]: # if strategy 1 is weakly dominaited
          break;
      i+=1
    if i == len(str1):
        return True
    return False


def str_dom_str(comb,nbr_stra,n_players):
    print("calcule de strategie Strictement dominante")
     
    for player in range(n_players):
      print("checking dominant strategy for player "+ str(player+1))
      # Right side
      dom_straR = -1 # supposedly that the first strategy of the current player is the dominante one
      strategy = 0
      str1 = getStrategyValues(player,strategy,comb) # current strategy values
      strategy2 = strategy+1
      while strategy2 < nbr_stra[player]:
        str2 = getStrategyValues(player,strategy2,comb)
        if  compareStrictDomianaitingStrategy(str2,str1) :
            dom_straR = strategy2
            print("dom stra R = " + str(dom_straR))
            str1 = str2
        elif compareStrictDomianaitingStrategy(str1,str2):
            dom_straR = strategy
            print("dom stra R = " + str(dom_straR))
          
        strategy2+=1
      #Left side
      # left side
      dom_straL = -1 # supposedly that the last strategy of the current player is the dominante one
      strategy = nbr_stra[player]-1
      str1 = getStrategyValues(player,strategy,comb) # current strategy values
      strategy2 = 0
      while strategy2 < strategy:
        str2 = getStrategyValues(player,strategy2,comb)
        if  compareStrictDomianaitingStrategy(str2,str1) :
            dom_straL = strategy2
            print("dom stra L = " + str(dom_straL))
            str1 = str2
        elif compareStrictDomianaitingStrategy(str1,str2):
            dom_straL = strategy
            print("dom stra L = " + str(dom_straL))

        strategy2+=1
    
      
      if dom_straR >= 0 or dom_straL >= 0 :
        if dom_straR >= 0 and dom_straL != dom_straR:
          print("la strategie Strictement dominante pour le joueur "+str(player+1)+" est "+str(dom_straR+1))
        if dom_straL >= 0 and dom_straL != dom_straR:
          print("la strategie Strictement dominante pour le joueur "+str(player+1)+" est "+str(dom_straL+1))
      else:
        print("pas de strategie Strictement dominante pour le joueur " + str(player+1))



def fbl_dom_str(comb,nbr_stra,n_players):
    print("calcule de strategie faiblement dominante")
     
    for player in range(n_players):
      print("checking weakly dominant strategy for player "+ str(player+1))
      # Right side
      dom_straR = -1 # supposedly that the first strategy of the current player is the dominante one
      strategy = 0
      str1 = getStrategyValues(player,strategy,comb) # current strategy values
      strategy2 = strategy+1
      while strategy2 < nbr_stra[player]:
        str2 = getStrategyValues(player,strategy2,comb)
        if  compareWeakDominaitingStrategy(str2,str1) :
            dom_straR = strategy2
            print("dom stra R = " + str(dom_straR))
            str1 = str2
        elif compareWeakDominaitingStrategy(str1,str2):
            dom_straR = strategy
            print("dom stra R = " + str(dom_straR))
          
        strategy2+=1
      #Left side
      # left side
      dom_straL = -1 # supposedly that the last strategy of the current player is the dominante one
      strategy = nbr_stra[player]-1
      str1 = getStrategyValues(player,strategy,comb) # current strategy values
      strategy2 = 0
      while strategy2 < strategy:
        str2 = getStrategyValues(player,strategy2,comb)
        if  compareWeakDominaitingStrategy(str2,str1) :
            dom_straL = strategy2
            print("dom stra L = " + str(dom_straL))
            str1 = str2
        elif compareWeakDominaitingStrategy(str1,str2):
            dom_straL = strategy
            print("dom stra L = " + str(dom_straL))

        strategy2+=1
    
      
      if dom_straR >= 0 or dom_straL >= 0 :
        if dom_straR >= 0 and dom_straL != dom_straR:
          print("la strategie Faiblement dominante pour le joueur "+str(player+1)+" est "+str(dom_straR+1))
        if dom_straL >= 0 and dom_straL != dom_straR:
          print("la strategie Faiblement dominante pour le joueur "+str(player+1)+" est "+str(dom_straL+1))
      else:
        print("pas de strategie Faiblement dominante pour le joueur " + str(player+1))


def getStrictWeakestStrategy(tempComb,player,nbr_stra):
    print("checking dominated strategy for player "+ str(player+1))
    print("checking strictly dominantated strategy for player "+ str(player+1))
    dom_stra = -1
    # Right side
    dom_straR = -1 # supposedly that the first strategy of the current player is the dominante one
    strategy = 0
    str1 = getStrategyValues(player,strategy,tempComb) # current strategy values
    if len(str1) > 0 :
      strategy2 = strategy+1
      while strategy2 < nbr_stra[player]:
        str2 = getStrategyValues(player,strategy2,tempComb)
        if len(str2) > 0 :
          if  compareStrictDominaitedStrategy(str2,str1) :
              dom_straR = strategy2
              #print("dom stra R = " + str(dom_straR))
              str1 = str2
          elif compareStrictDominaitedStrategy(str1,str2):
              dom_straR = strategy
              #print("dom stra R = " + str(dom_straR))
        else :
          print("strategy " +str(strategy2) +" was eliminated ")    
        strategy2+=1
    else :
      print("strategy " +str(strategy) +" was eliminated ")    
    #Left side
    # left side
    dom_straL = -1 # supposedly that the last strategy of the current player is the dominante one
    strategy = nbr_stra[player]-1
    str1 = getStrategyValues(player,strategy,tempComb) # current strategy values
    if len(str1) > 0 :
      strategy2 = 0
      while strategy2 < strategy:
        str2 = getStrategyValues(player,strategy2,tempComb)
        if len(str2) > 0: 
          if  compareStrictDominaitedStrategy(str2,str1) :
              dom_straL = strategy2
              #print("dom stra L = " + str(dom_straL))
              str1 = str2
          elif compareStrictDominaitedStrategy(str1,str2):
              dom_straL = strategy
              #print("dom stra L = " + str(dom_straL))
        else :
          print("strategy " +str(strategy2) +" was eliminated ") 
        strategy2+=1
    else :
      print("strategy " +str(strategy) +" was eliminated ") 
  
    
    if dom_straR >= 0 or dom_straL >= 0 :
      if dom_straR >= 0 and dom_straL != dom_straR:
        print("la strategie Strictement dominee pour le joueur "+str(player+1)+" est "+str(dom_straR+1))
        dom_stra = dom_straR
      if dom_straL >= 0 and dom_straL != dom_straR:
        print("la strategie Strictement dominee pour le joueur "+str(player+1)+" est "+str(dom_straL+1))
        dom_stra = dom_straL
    else:
      print("pas de strategie Strictement dominee pour le joueur " + str(player+1))

    return dom_stra

def getWeakWeakestStrategy(tempComb,player,nbr_stra):
    print("checking dominated strategy for player "+ str(player+1))
    print("checking strictly dominantated strategy for player "+ str(player+1))
    dom_stra = -1
    # Right side
    dom_straR = -1 # supposedly that the first strategy of the current player is the dominante one
    strategy = 0
    str1 = getStrategyValues(player,strategy,tempComb) # current strategy values
    if len(str1) > 0 :
      strategy2 = strategy+1
      while strategy2 < nbr_stra[player]:
        str2 = getStrategyValues(player,strategy2,tempComb)
        if len(str2) > 0 :
          if  compareWeakDominaitedStrategy(str2,str1) :
              dom_straR = strategy2
              #print("dom stra R = " + str(dom_straR))
              str1 = str2
          elif compareWeakDominaitedStrategy(str1,str2):
              dom_straR = strategy
              #print("dom stra R = " + str(dom_straR))
        else :
          print("strategy " +str(strategy2) +" was eliminated ")    
        strategy2+=1
    else :
      print("strategy " +str(strategy) +" was eliminated ")    
    #Left side
    # left side
    dom_straL = -1 # supposedly that the last strategy of the current player is the dominante one
    strategy = nbr_stra[player]-1
    str1 = getStrategyValues(player,strategy,tempComb) # current strategy values
    if len(str1) > 0 :
      strategy2 = 0
      while strategy2 < strategy:
        str2 = getStrategyValues(player,strategy2,tempComb)
        if len(str2) > 0: 
          if  compareWeakDominaitedStrategy(str2,str1) :
              dom_straL = strategy2
              #print("dom stra L = " + str(dom_straL))
              str1 = str2
          elif compareWeakDominaitedStrategy(str1,str2):
              dom_straL = strategy
              #print("dom stra L = " + str(dom_straL))
        else :
          print("strategy " +str(strategy2) +" was eliminated ") 
        strategy2+=1
    else :
      print("strategy " +str(strategy) +" was eliminated ") 
  
    
    if dom_straR >= 0 or dom_straL >= 0 :
      if dom_straR >= 0 and dom_straL != dom_straR:
        print("la strategie Faiblement dominee pour le joueur "+str(player+1)+" est "+str(dom_straR+1))
        dom_stra = dom_straR
      if dom_straL >= 0 and dom_straL != dom_straR:
        print("la strategie Faiblement dominee pour le joueur "+str(player+1)+" est "+str(dom_straL+1))
        dom_stra = dom_straL
    else:
      print("pas de strategie Faiblement dominee pour le joueur " + str(player+1))

    return dom_stra


def eliminateStrategy(tempComb,player,wstr):
    newComb = []
    print("eliminating "+str(wstr)+" of player "+str(player))
    for sub in tempComb:
        if sub[0][player] != wstr:
            newComb.append(sub) #remove the strategy from comb 
    return newComb

def elim_succ_str_frt(comb,nbr_stra,n_players):
   print("elimination des strategies strictement dominnes")
   tempComb = comb #tempo pour appliquer le traitement 
   nbra_stra_temp = nbr_stra
   print("up up ")
   print(tempComb)
    
   while len(tempComb) > n_players:
    player = 0
    dom_stra_exist = False
    print("up")
    print(tempComb)
    while player < n_players:
      wstr = getStrictWeakestStrategy(tempComb,player,nbra_stra_temp)

      if wstr != -1 :
        print("eliminating strategy "+ str(wstr+1) +" of player " + str(player+1))
        tempComb = eliminateStrategy(tempComb,player,wstr)
        print("down")
        print(tempComb)
        dom_stra_exist = True
        break

      player+=1

    if not dom_stra_exist :
      print("ya pas  de strategies dominante")
      break
    cone = input(" proceed ...")
    
   print(tempComb)
   
def elim_succ_fbl_frt(comb,nbr_stra,n_players):
   print("elimination des strategies faiblement dominnes")
   tempComb = comb #tempo pour appliquer le traitement 
   nbra_stra_temp = nbr_stra
   print("up up ")
   print(tempComb)
    
   while len(tempComb) > n_players:
    player = 0
    dom_stra_exist = False
    print("up")
    print(tempComb)
    while player < n_players:
      wstr = getWeakWeakestStrategy(tempComb,player,nbra_stra_temp)

      if wstr != -1 :
        print("eliminating strategy "+ str(wstr+1) +" of player " + str(player+1))
        tempComb = eliminateStrategy(tempComb,player,wstr)
        print("down")
        print(tempComb)
        dom_stra_exist = True
        break

      player+=1

    if not dom_stra_exist :
      print("ya pas  de strategies dominante")
      break
    cone = input(" proceed ...")
    
   print(tempComb)

def get_val_all_str(player,comb):
    print("getting all values of all strategies of player " + str(player))
    player_comb = []
    for subc in comb:
      if subc[0][len(subc[0])-1] == player :
        player_comb.append(subc)
    return player_comb

def get_max_str(player,strp,player_comb):
  max_vstr = player_comb[0]
  for subc in player_comb:
    if strp == subc[0][player]:
      if subc[1] > max_vstr[1] :
        max_vstr = subc
        
  max_str = max_vstr[0].copy()
  max_str.pop()
  return max_str #comb of max value of strategy strp
  

def get_max_all_str(player,player_comb,nbr_stra):
  all_str_max = []
  for strp in range(nbr_stra[player]):
      str_max = get_max_str(player,strp,player_comb)
      #print("max value of strategy "+str(strp)+ " of player "+ str(player) + " is " + str(str_max[1]))
      all_str_max.append(str_max)
  return all_str_max

def common(list1,list2):
  equils = []
  i1 = 0
  while i1 < len(list1):
    i2 = 0
    while i2 < len(list2):
      print ( " list 1  = " + str(list1[i1]))
      print ( " list 2  = " + str(list2[i2]))
      if list1[i1][0] == list2[i2][0] and list1[i1][1] == list2[i2][1] :
        equils.append(list1[i1])

      i2+=1
    i1+=1
  return equils

def verify_equil(equil):
  print(equil)
  nash_equilibrium_list = []
  player1 = 0
  while player1 < len(equil):
    #check right side
    player2 = player1 + 1
    while player2 < len(equil):
      equils = common(equil[player1],equil[player2])
      if len(equils) > 0 : 
        nash_equilibrium_list.append(equils)
       
      player2+=1
    player1+=1

  #print(nash_equilibrium_list)
    
  if len(nash_equilibrium_list) > 0 : 
     print("les profils d'equilibre de nash sont")
     print(nash_equilibrium_list)
  else : 
    print(" pas d'equilibre de nash")

        
    

def nash_equi(comb,nbr_stra,n_players):
    print("nash equilibrium")
    # pour chaque joueur on va choisir la meilleure strategie qu'il trouve meilleur pour lui
    equil = []
    player = 0
    while player < n_players:
      player_comb = get_val_all_str(player,comb)
      print(player_comb)
      str_max =  get_max_all_str(player,player_comb,nbr_stra)
      print(str_max)
      #equil.append(player)
      equil.append(str_max)
      # getBestStrategyAgainstRest(player,comb,nbr_stra,n_players)
      player+=1

    #print(equil)

    nash_list = verify_equil(equil)
      


def init():
  n_players = int(input("entrer le nombre des joueurs"))  # the number of players 
  nbr_stra = n_players * [] #a table that has the number of strategies of each player

  print("entrez le nombre de strategie pour chaque joueur")

  for i in range(n_players):
    
      nbr_stra.append(int(input("nombre strategies pour joureur " + str((i+1)))))

  print(nbr_stra)

  #initialisation
  #matrix = auto_fill_matrix(nbr_stra, lambda coords: coords[:])
  matrix = fill_matrix(nbr_stra, lambda coords: coords[:])
  explore(matrix,0,n_players)

  #store the indexes of each element in comb 

  comb = []
  showIndexes(matrix,comb) # comb contient tous les valeurs de la matrice avec leurs indices which we will use for our treatment

  return comb,nbr_stra,n_players

#main program    
leave = False 
while not leave :

  comb,nbr_stra,n_players = init()

  # for choices 
  choix()



  user_choice = input("que vous voulez fair ? ")
  while int(user_choice) < 0 and int(user_choice) > 7 :
      user_choice = input("vous devez choisir une des 7 operations ")

  x = input("appuyez pour commencer ..")
 #comb,nbr_stra,n_players = init()
  while x != "n" or x!= "non" :
      choice = int(user_choice)
      if x == "oui" or x == "o":
          choix()
          choice = int(input("que voulez vous faire"))
          
      if choice == 1 :
          str_dom_str(comb,nbr_stra,n_players)
      if choice == 2 :
          fbl_dom_str(comb,nbr_stra,n_players)
      if choice == 3 : 
          elim_succ_str_frt(comb,nbr_stra,n_players)
      if choice == 4 :
          elim_succ_fbl_frt(comb,nbr_stra,n_players)
      if choice == 5 :
          nash_equi(comb,nbr_stra,n_players)
      # if choice == 6 :
      #     prof_pareto(matrix)
      # if choice == 7 :
      #     niv_sec(matrix)
      if choice < 0 or choice > 7  :
          print("vous devez choisir entre 1 et 7 ")
      
      x = input("voulez vous faire autre chose ? ")
      if x == "non" or x =="n" :
              break
  r = input ('voulez vous fair ce processus avec autre issue ?')
  if r == "n" or r == "non":
    leave = True
            