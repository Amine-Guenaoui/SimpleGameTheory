#TP 1 m THJ 
import numpy as np

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

def search_dominating_stra(matrix,player,f):
    comment = "strictement"
    if (f) :
        comment = "faiblement"

    tmp_matrix = matrix
    i = 0
    doms = 0
    str_dom = False
    while i < len(tmp_matrix) and str_dom == False :
        # on va comparer la strategie i avec tous les autres strategies
        k = 0 
        l_dom = -1
        left = False
        while k < i and left == False: # verify left side 
            #print("comparing line "+str(i)+" with "+str(k))
            if(str_dom_str_l(tmp_matrix[i],tmp_matrix[k],player - 1 ,f) == False):
                k+=1
            else:
                l_dom = k
                left = True
                #print("line "+str(i)+" dominates "+str(k))
        
        j = i + 1
        r_dom = -1 
        right = False
        while j < len(tmp_matrix) and right == False:
            #print("comparing line "+str(i)+" with "+str(j))
            if(str_dom_str_l(tmp_matrix[i],tmp_matrix[j],player - 1,f) == False):
                j+=1 
            else:
                r_dom = i
                right = True
                #print("line "+str(i)+" dominates"+str(j))
        if (left == True and right == True):
            str_dom = True
            doms = r_dom
        elif left == True and right == False : 
             str_dom = True
             doms = l_dom
        elif left == False and right == True : 
             str_dom = True
             doms = r_dom
        i+=1
    if(str_dom):
        print("la strategie "+comment+" dominante de joueur "+str(player)+" est " + str(i))
    else:
        print("pas de strategie "+comment+" dominante pour joueur "+str(player)+" ")
    print_matrix(tmp_matrix)
    return i-1

def search_dominated_stra(matrix,player,f):
    comment = "strictement"
    if (f) :
        comment = "faiblement"

    tmp_matrix = matrix
    i = 0
    doms = 0
    str_dom = False
    while i < len(tmp_matrix) and str_dom == False :
        # on va comparer la strategie i avec tous les autres strategies
        k = 0 
        l_dom = -1
        left = False
        while k < i and left == False: # verify left side 
            #print("comparing line "+str(i)+" with "+str(k))
            if(str_dom_str_l(tmp_matrix[k],tmp_matrix[i],player - 1 ,f) == False):
                k+=1
            else:
                l_dom = k
                left = True
                #print("line "+str(i)+" dominates "+str(k))
        
        j = i + 1
        r_dom = -1 
        right = False
        while j < len(tmp_matrix) and right == False:
            #print("comparing line "+str(i)+" with "+str(j))
            if(str_dom_str_l(tmp_matrix[j],tmp_matrix[i],player - 1,f) == False):
                j+=1 
            else:
                r_dom = i
                right = True
                #print("line "+str(i)+" dominates"+str(j))
        if (left == True and right == True):
            str_dom = True
            doms = r_dom
        elif left == True and right == False : 
             str_dom = True
             doms = l_dom
        elif left == False and right == True : 
             str_dom = True
             doms = r_dom
        i+=1
    if(str_dom):
        print("la strategie "+comment+" dominée de joueur "+str(player)+" est " + str(i))
    else:
        print("pas de strategie "+comment+" dominée pour joueur "+str(player)+" ")
        i=0
    #print_matrix(tmp_matrix)
    return i-1

def min_el(line,player):
    i = 1
    minimum = line[0][player]
    while i < len(line) : 
        if line[i][player] < minimum :
            minimum = line[i][player]
        i+=1 
    return minimum

def pareto(matrix, i , j):
    
    pareto = []
    #upper left elements 
    k = 0
    while k < i :
        l = 0
        while l < j :
            el = []
            if matrix[k][l][0] >= matrix[i][j][0] and matrix[k][l][1] >= matrix[i][j][1] :
                el.append(k)
                el.append(l)
                pareto.append(el)
            l+=1
        k+=1
    #down right elements
    k = i+1
    while k < len(matrix) :
        l = j+1
        while l < len(matrix[k]) :
            el = []
            if matrix[k][l][0] >= matrix[i][j][0] and matrix[k][l][1] >= matrix[i][j][1] :
                el.append(k)
                el.append(l)
                pareto.append(el)
            l+=1
        k+=1
    
    return pareto


def intersect(tab1,tab2):
    equi = []
    i = 0
    while i < len(tab1) :
        j = 0
        while j < len(tab2) :
            if tab1[i][0] == tab2[j][0] and tab1[i][1] == tab2[j][1] :
                el = []
                el.append(tab1[i][0])  
                el.append(tab1[i][1])
                equi.append(el)
            j+=1
        i+=1  
    return equi
    

def Best_response_col_for_line(line,player):
    br = 0
    i=0
    max_g = line[0][player] 
    while i < len(line) :
        if line[i][player] > max_g:
            max_g = line[i][player]
            br = i
        i+=1
    return br
    


def transpose(lst): #manulellement car j'utilise list de list de list
    newlist = []
    i = 0
    while i < len(lst):
        j = 0
        colvec = []
        while j < len(lst):
            colvec.append(lst[j][i])
            j = j + 1
        newlist.append(colvec)
        i = i + 1
    return newlist

def str_dom_str_l(str1 , str2 ,player,f): # function to compare two strategies for player 1
    dominating = True
    i=0
    if(f == False):
        while i< len(str1) and dominating :
            if(str1[i][player] < str2[i][player]):
                dominating = False
            i+=1
    else : 
        while i< len(str1) and dominating :
            if(str1[i][player] <= str2[i][player]):
                dominating = False
            i+=1
    
    return dominating


def  str_dom_str(matrice):
    print("strategies strictement dominantes")
    
    print("pour joueur 1 ")
    search_dominating_stra(matrice,1,False) # la matrice , le joeur , faiblement ou pas 

    print("pour joueur 2 ") # if we transpose the matrice ,. we can calculate using same functions for player 2
    tmp_matrix = transpose(matrice)
    search_dominating_stra(tmp_matrix,2,False)


def  fbl_dom_str(matrice):
    print("strategie faiblement dominante")
    print("pour joueur 1 ")
    search_dominating_stra(matrice,1,True) # la matrice , le joeur , faiblement ou pas 

    print("pour joueur 2 ") # if we transpose the matrice ,. we can calculate using same functions for player 2
    tmp_matrix = transpose(matrice)
    search_dominating_stra(tmp_matrix,2,True)

def  elim_succ_str_frt(matrice):
    print("elimination successive des strategies dominantes")
    tmp_matrix = matrice
    joueur1 = True  
    x = 2
    while len(tmp_matrix) > 1 :
        if x == 1 : 
            x = 2
        elif x == 2 :
            x = 1
        i = search_dominated_stra(tmp_matrix,x,False)
        print(i)
        if i != -1 :
            tmp_matrix.pop(i)
        tmp_matrix = transpose(tmp_matrix)
        
    if x == 2:
        tmp_matrix = transpose(tmp_matrix)
    print_matrix(tmp_matrix)



def  elim_succ_fbl_frt(matrice):
    print("elimination successive des strategies dominantes")
    tmp_matrix = matrice
    joueur1 = True  
    x = 2
    while len(tmp_matrix) > 1 :
        if x == 1 : 
            x = 2
        elif x == 2 :
            x = 1
        i = search_dominated_stra(tmp_matrix,x,True)
        print(i)
        if i != -1 :
            tmp_matrix.pop(i)
        tmp_matrix = transpose(tmp_matrix)
        
    if x == 2:
        tmp_matrix = transpose(tmp_matrix)
    print_matrix(tmp_matrix)

def  nash_equi(matrice):
    print("nash_equi")
    tmp_matrix = matrice
    #def premier ensemble , il sera que des indices ,
    
    br1= []
    
    i = 0 
    while i < len(tmp_matrix) :
        el = []
        el.append(i)
        el.append(Best_response_col_for_line(tmp_matrix[i],0))
        br1.append(el)
        i+=1
    print("pour joueur 2 nous avons les meilleures reponses suivantes")
    print(br1)
    #def 2 eme ensemble ,
    tmp_matrix = transpose(tmp_matrix)
    br2 = []
    i = 0 
    while i < len(tmp_matrix) :
        el = []
        el.append(Best_response_col_for_line(tmp_matrix[i],1))
        el.append(i)
        br2.append(el)
        i+=1
    print("pour joueur 1 nous avons les meilleures reponses suivantes")
    print(br2)
    # si les deux ensembles sont dif . alors pas d'equilibre 
    nash = intersect(br1,br2)
    if len(nash) > 0 :
        print("profil nash est")
        print(nash)
    else:
        print("pas d'equilibre de nash en strategies pures")

def  prof_pareto(matrice):
    print("profil pareto dominant ")
    tmp_matrix = matrice 
    el_par = []
    i = 0
    while i < len(tmp_matrix):
        j = 0
        while j < len(tmp_matrix[i]):
            pareto_l = []
            el = []
            el.append(i)
            el.append(j)
            pareto_l.append(el)
            pareto_l.append(pareto(tmp_matrix, i , j) )
            el_par.append(pareto_l)
            j+=1
        i+=1
    
    print(el_par)

def  niv_sec(matrice):
    print("niveau de securite de chaque joueur ")
    # for each line , cal min 
    print("pour joueur 1")
    tmp_matrix = matrice
    mins_l = []
    i = 0
    while i < len(tmp_matrix) :
        mins_l.append(min_el(tmp_matrix[i],0))
        i+=1
    niv_sec = max(mins_l)
    print("niveau de securite de joueur 1 est "+ str(niv_sec))

    tmp_matrix = transpose(matrice)
    mins_l = []
    i = 0
    while i < len(tmp_matrix) :
        mins_l.append(min_el(tmp_matrix[i],1))
        i+=1
    niv_sec = max(mins_l)
    print("niveau de securite de joueur 2 est "+ str(niv_sec))




def print_matrix(matrix):
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            print( "| " +  str(matrix[i][j][0]) +","+ str(matrix[i][j][1]) +" |"  , end = " ") 
        print() 




# pour commencer il faut saisir le nombre des lignes et colonnes pour qu'on puisse appliquer les notions 
lines = int(input(", entrez le nombre de strategies du joueur 1 : \n"))
print('nbr strategie joueur 1 : ' + str(lines) )
cols = int(input(", entrez le nombre de strategies du joueur 2 : \n"))
print('nbr strategie joueur 2 : ' + str(cols))

#initialisation

matrix = []

for i in range(lines):          # A for loop for row entries 
    a =[]
    for j in range(cols):      # A for loop for column entries 
         x = []
         x.insert(0 ,int(input("\ngain de joueur 1 de la strategie joueur 1 : "+str(i))))
         x.insert(1, int(input("\ngain de joueur 2 : "+str(j)))) 
         a.append(x)
    matrix.append(a) 
  
# For printing the matrix 
print_matrix(matrix)

# for choices 
choix()

user_choice = input("que vous voulez fair ? ")
while int(user_choice) < 0 and int(user_choice) > 7 :
    user_choice = input("vous devez choisir une des 7 operations ")

x = input("appuyez pour commencer ..")

while x != "n" or x!= "non" :
    choice = int(user_choice)
    if x == "oui" or x == "o":
        choix()
        choice = int(input("que voulez vous faire"))
        
    if choice == 1 :
        str_dom_str(matrix)
    if choice == 2 :
        fbl_dom_str(matrix)
    if choice == 3 : 
        elim_succ_str_frt(matrix)
    if choice == 4 :
        elim_succ_fbl_frt(matrix)
    if choice == 5 :
        nash_equi(matrix)
    if choice == 6 :
        prof_pareto(matrix)
    if choice == 7 :
        niv_sec(matrix)
    if choice < 0 or choice > 7  :
        print("vous devez choisir entre 1 et 7 ")
    
    x = input("voulez vous faire autre chose ? ")
    if x == "non" or x =="n" :
            break



