from random import *


### Burlot Brice, Hales Nadhir

class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """

    def __init__(self, height, width, empty):
        """
        Constructeur d'un labyrinthe de height cellules de haut
        et de width cellules de large
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height = height
        self.width = width
        self.neighbors = {(i, j): set() for i in range(height)
                          for j in range(width)}
        if empty:
            for i in range(self.height):
                for j in range(self.width):
                    if (i + 1) < self.height and 0 <= j < self.width and (i + 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i + 1, j)]:
                        self.neighbors[(i, j)].add((i+1, j))
                        self.neighbors[(i+1, j)].add((i, j))

                    if (j + 1) < self.width and 0 <= i < self.height and (i, j + 1) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i, j + 1)]:
                        self.neighbors[(i, j+1)].add((i, j))
                        self.neighbors[(i, j)].add((i, j+1))

                    if (i - 1) >= 0 and 0 <= j < self.width and (i - 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i - 1, j)]:
                        self.neighbors[(i, j)].add((i - 1, j))
                        self.neighbors[(i - 1, j)].add((i, j))

                    if (j - 1) >= 0 and 0 <= i < self.height and (i, j - 1) not in self.neighbors[(i, j)] and (i, j)not in self.neighbors[(i, j - 1)]:
                        self.neighbors[(i, j - 1)].add((i, j))
                        self.neighbors[(i, j)].add((i, j - 1))

    def info(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = "**Informations sur le labyrinthe**\n"
        txt += f"- Dimensions de la grille : {self.height} x {self.width}\n"
        txt += "- Voisinages :\n"
        txt += str(self.neighbors) + "\n"
        valid = True
        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"
        return txt

    def __str__(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += "   ┃" if (0, j +
                              1) not in self.neighbors[(0, j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1,
                                  j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width -
                                1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i + 1, j +
                                  1) not in self.neighbors[(i + 1, j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def overlay(self, content=None):
        """
        Rendu en mode texte, sur la sortie standard, \
        d'un labyrinthe avec du contenu dans les cellules
        Argument:
            content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
        Retour:
            string
        """
        if content is None:
            content = {(i,j):' ' for i in range(self.height) for j in range(self.width)}
        else:
        # Python >=3.9
        #content = content | {(i, j): ' ' for i in range(
        #    self.height) for j in range(self.width) if (i,j) not in content}
        # Python <3.9
            new_content = {(i, j): ' ' for i in range(self.height) for j in range(self.width) if (i,j) not in content}
            content = {**content, **new_content}
        txt = r""
        # Première ligne
        txt += "┏"
        for j in range(self.width-1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width-1):
            txt += " "+content[(0,j)]+" ┃" if (0,j+1) not in self.neighbors[(0,j)] else " "+content[(0,j)]+"  "
        txt += " "+content[(0,self.width-1)]+" ┃\n"
        # Lignes normales
        for i in range(self.height-1):
            txt += "┣"
            for j in range(self.width-1):
                txt += "━━━╋" if (i+1,j) not in self.neighbors[(i,j)] else "   ╋"
            txt += "━━━┫\n" if (i+1,self.width-1) not in self.neighbors[(i,self.width-1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += " "+content[(i+1,j)]+" ┃" if (i+1,j+1) not in self.neighbors[(i+1,j)] else " "+content[(i+1,j)]+"  "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width-1):
            txt += "━━━┻"
        txt += "━━━┛\n"
        return txt



####################################################


#PARTIE 4



        
    def add_wall(self, c1 :tuple , c2 : tuple)-> None:
        """
        methode

        Parameters
        ----------
        c1 : tuple
            1ere coordonnée visée par l'ajout de mur.
        c2 : TYPE
            2e coordonnée visée.

        Uses
        -------
        ajout de mur entres deux cellules.

        """
        
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire


    def remove_wall(self,c1 : tuple ,c2 : tuple)-> None:
        """
        methode 
        
        Parameters
        ----------
        c1 : tuple
            1ere coordonnée visée par la suppression de mur.
        c2 : TYPE
            2e coordonnée visée.

        Returns
        -------
        Supprime un mur entres deux cellules.

        """
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de la suppression d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        if c1 not in self.neighbors[c2]:
            self.neighbors[c2].add(c1)
        if c2 not in self.neighbors[c1]:
            self.neighbors[c1].add(c2)
            

    def get_walls(self)-> list:
        """
        methode

        Returns
        -------
        l : list
        
            liste contenant l'ensemble des murs dans le labyrinthe visé par le self.

        """
        l=[]
        for i in range(self.height):
            for j in range(self.width):
                if (i + 1) < self.height and (i + 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i + 1, j)] and [(i+1,j),(i,j)] not in l :
                    l.append([(i,j),(i+1,j)])
                    
                if (j + 1) < self.width and (i, j + 1) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i, j + 1)] and [(i,j+1),(i,j)] not in l :
                    l.append([(i, j), (i, j+1)])
        
                if (i - 1) >= 0 and 0<=j<self.width and (i - 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i - 1, j)] and [(i-1,j),(i,j)] not in l :
                    l.append([(i,j),(i-1,j)])
                    
                if (j - 1) >= 0 and 0<=i<self.height and (i, j - 1) not in self.neighbors[(i, j)] and (i, j)not in self.neighbors[(i, j - 1)] and [(i,j-1),(i,j)] not in l :
                    l.append([(i, j), (i, j-1)])

        return l



    def fill(self):
        """
        methode

        Uses
        -------
        remplit le labyrinthe visé par le self de murs.

        """
        for i in range(self.height):
            for j in range(self.width):
                    if (i + 1) < self.height and 0<=j<self.width and (i + 1, j)  in self.neighbors[(i, j)] and (i, j)  in self.neighbors[(i + 1, j)] :
                        self.add_wall((i,j), (i+1,j))
                        
                    if (j + 1) < self.width and 0<=i<self.height and (i, j + 1)  in self.neighbors[(i, j)] and (i, j)  in self.neighbors[(i, j + 1)] :
                        self.add_wall((i,j), (i,j+1))
                        
                    if (i - 1) >= 0 and 0<=j<self.width and (i - 1, j)  in self.neighbors[(i, j)] and (i, j)  in self.neighbors[(i - 1, j)] :
                        self.add_wall((i-1,j), (i,j))
                        
                    if (j - 1) >= 0 and 0<=i<self.height and (i, j - 1)  in self.neighbors[(i, j)] and (i, j) in self.neighbors[(i, j - 1)] :
                        self.add_wall((i,j), (i,j-1))
                        
                        
        
    def empty(self):
        """
        methode

        Uses
        -------
        Vide le labyrinthe de ses murs

        """
        for i in range(self.height):
            for j in range(self.width):
                    if (i + 1) < self.height and 0<=j<self.width and (i + 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i + 1, j)] :
                        self.neighbors[(i,j)].add((i+1,j))
                        self.neighbors[(i+1, j)].add((i, j))
                        
                    if (j + 1) < self.width and 0<=i<self.height and (i, j + 1) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i, j + 1)] :
                        self.neighbors[(i, j+1)].add((i, j))
                        self.neighbors[(i, j)].add((i, j+1))
                        
                    if (i - 1) >= 0 and 0<=j<self.width and (i - 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i - 1, j)] :
                        self.neighbors[(i, j)].add((i - 1, j))
                        self.neighbors[(i - 1, j)].add((i, j))
                        
                    if (j - 1) >= 0 and 0<=i<self.height and (i, j - 1) not in self.neighbors[(i, j)] and (i, j)not in self.neighbors[(i, j - 1)] :
                        self.neighbors[(i, j - 1)].add((i, j))
                        self.neighbors[(i, j)].add((i, j - 1))

    
    def get_contiguous_cells(self,c) : 
        """
        methode

        Parameters
        ----------
        c : TYPE
            une cellule du labyrinthe visé par le self.

        Returns
        -------
        l : TYPE
            la liste des cellules contigues.

        """
        
        assert 0 <= c[0] < self.height and \
               0 <= c[1] < self.width and \
               0 <= c[0] < self.height and \
               0 <= c[1] < self.width, \
            f"Erreur lors de la recuperations des cellules contigues de {c}  : les coordonnées de la cellule ne sont pas compatibles avec les dimensions du labyrinthe"
        l=[]
        for i in range(c[0]-1,c[0]+2):
            for j in range(c[1]-1,c[1]+2):
                if self.height>i>=0 and self.width>j>=0 and ((i,j)!=(c[0]-1,c[1]-1) and (i,j)!=(c[0]-1,c[1]+1) and (i,j)!=(c[0]+1,c[1]-1) and (i,j)!=(c[0]+1,c[1]+1)) and (i,j)!=(c[0],c[1]):
                    l.append((i,j))        
        return l
    

            
    def get_reachable_cells(self,c):
        """
        methode

        Parameters
        ----------
        c : TYPE
            une cellule du labyrinthe visé par le self.

        Returns
        -------
        l : TYPE
            la liste des cellules contigues atteignables.

        """
        assert type(c)==tuple and \
            type(c[0])==type(c[1])==int ,\
                f"erreur dans le type la cellule : {c[1]} ou {c[0]} n'est pas un entier ou {c} n'est pas un un tuple "
        l=self.get_contiguous_cells(c)
        idx = 0
        while idx < len(l):
            voisin = l[idx]
            if voisin not in self.neighbors[c]:
                l.remove(voisin)
                idx -= 1
            idx += 1


        return l
    
    
    
########################################################################


## PARTIE 5


###    5.1

    def gen_btree(h : int , w : int):
        """
        

        Parameters
        ----------
        h : int
            hauteur du labyrinthe.
        w : int
            largeur du labyrinthe.

        Returns
        -------
        Maze
            labyrinthe de la classe maze avec génération aléatoire de chemins.

        """
        assert type(h)==type(w)==int , \
            f"erreur de type de donnée : {h} ou {w} n'est pas un entier"        
        
        laby = Maze(h, w, False)

        for i in range(laby.height):
            for j in range(laby.width):

                aleatoire = randint(0, 1)
                if aleatoire and j+1 < laby.width:
                    laby.remove_wall((i, j), (i, j+1))
                if not aleatoire and i+1 < laby.height:
                    laby.remove_wall((i, j), (i+1, j))

        return laby
    
    
###    5.2 
    
    def gen_sidewinder(h : int, w : int):
        """
        

        Parameters
        ----------
        h : int
            hauteur du labyrinthe.
        w : int
            largeur du labyrinthe.

        Returns
        -------
        Maze
            Génère un labyrinthe choisissant aléatoirement entre casser
            le mur EST ou le mur SUD
        """
        assert type(h)==type(w)==int , \
            f"erreur de type de donnée : {h} ou {w} n'est pas un entier"
            
        lab = Maze(h, w, empty = False)
        for i in range(h-1):
            lst = []
            for j in range(w-1):
                lst.append((i,j))
                valAl = randint(0,1)
                derCell = (i,j)
                #Si valAl = 0 on retire le mur EST
                if valAl == 0:
                    lab.neighbors[(i, j)].add((i, j+1))
                    lab.neighbors[(i, j+1)].add((i, j))
                #Sinon on retire le mur SUD
                else:
                    (x,y) = lst[randint(0,len(lst)-1)]
                    lab.neighbors[(x, y)].add((x+1, y))
                    lab.neighbors[(x+1, y)].add((x, y))
                    lst = []
            lst.append(derCell)
            (x,y) = lst[randint(0,len(lst)-1)]
            lab.neighbors[(x, y)].add((x+1, y))
            lab.neighbors[(x+1, y)].add((x, y))
        for k in range(w-1):
            lab.neighbors[(h-1, k)].add((h-1, k+1))
            lab.neighbors[(h-1, k+1)].add((h-1, k))
        return lab
    
###    5.3
    
    def gen_fusion(h : int , w : int):
        """
        

        Parameters
        ----------
        h : int
            hauteur du labyrinthe.
        w : int
            largeur du labyrinthe.

        Returns
        -------
        Maze
            Un object de la classe Maze avec un chemin aléatoire généré via la fusion.

        """
        assert type(h)==type(w)==int , \
            f"erreur de type de donnée : {h} ou {w} n'est pas un entier"
        
        laby = Maze(h, w, False)
        compt = 0
        compt2=0
        marquage = {}
        murs = laby.get_walls()
        shuffle(murs)
        
        for i in range(h):
            for j in range(w):
                marquage[(i, j)] = compt
                compt += 1
                
        for k in range(len(murs)):
        
            if marquage[murs[k][0]] != marquage[murs[k][1]] and compt2 <((h*w)-1):
                compt2+=1
                temp=marquage[murs[k][0]] 
                laby.remove_wall(murs[k][1], murs[k][0])
                
                for i in marquage:
                    
                   if marquage[i]==temp:
                       marquage[i] = marquage[murs[k][1]]
                               
        return laby
    
###    5.4
    
    
    def gen_exploration(h : int ,w :int ):
        """
        

        Parameters
        ----------
        h : int
            hauteur du labyrinthe.
        w : int
            largeur du labyrinthe.

        Returns
        -------
        Maze
            Génère un labyrinthe cassant les murs à mesure qu'on avance et
            à la manière d'un parcours en profondeur.

        """
        assert type(h)==type(w)==int , \
            f"erreur de type de donnée : {h} ou {w} n'est pas un entier"
            
        lab = Maze(h, w, empty = False)
        lstVisitee = []
        pile = []
        XcellRand = randint(0,h-1)
        YcellRand = randint(0,w-1)
        lstVisitee.append((XcellRand, YcellRand))
        pile.append((XcellRand, YcellRand))
        while pile:
            cell = pile.pop()
            voisins = lab.get_contiguous_cells(cell)
            #recherche de voisin  non visité
            toutVisitee = True
            idx = 0
            while toutVisitee and idx < len(voisins):
                if voisins[idx] not in lstVisitee:
                    toutVisitee = False
                idx += 1
            if not toutVisitee:
                pile.append(cell)
                #suppresion des voisins visitée
                idx = 0
                while idx < len(voisins):
                    if voisins[idx] in lstVisitee:
                        del voisins[idx]
                        idx -= 1
                    idx += 1
                cellSuiv = voisins[randint(0,len(voisins)-1)]
                lab.remove_wall(cell, cellSuiv)
                lstVisitee.append(cellSuiv)
                pile.append(cellSuiv)
        return lab
    
    
###    5.5
    
    def gen_wilson(h :int ,w: int ): 
        """
        

        Parameters
        ----------
        h : int
            hauteur du labyrinthe.
        w : int
            largeur du labyrinthe.

        Returns
        -------
        Maze
            Génère un labyrinthe comme si un serpent avait creusé dans le labyrinthe
            à partir d'un point de dépar aléatoire et jusqu'à un endroit déjà creusé.
        """
        assert type(h)==type(w)==int , \
            f"erreur de type de donnée : {h} ou {w} n'est pas un entier"
        
        lab = Maze(h, w, empty = False)
        #Récupération de toute les coordonnées
        lstNonMarquee = []
        for i in range(h):
            for j in range(w):
                lstNonMarquee.append((i,j))
        #choix d'une cellule aléatoire non marqué
        cellAl = lstNonMarquee[randint(0,len(lstNonMarquee)-1)]
        lstNonMarquee.remove(cellAl)
        voisins = lab.get_contiguous_cells(cellAl)
        cellRaccord = voisins[randint(0,len(voisins)-1)]
        lab.remove_wall(cellAl, cellRaccord)
        
        while len(lstNonMarquee) > 0:
            #initialisation de la première cellule aléatoire
            cellDep = lstNonMarquee[randint(0,len(lstNonMarquee)-1)]
            voisins = lab.get_contiguous_cells(cellDep)
            cellSuiv = voisins[randint(0,len(voisins)-1)]
            cellPrec = cellDep
            #début de la marche
            continu = True
            chemin = [cellDep]
            while cellSuiv in lstNonMarquee:
                #suppression du chemin formant la boucle
                if cellSuiv in chemin:
                    pos = chemin.index(cellSuiv)
                    while len(chemin)-1 > pos:
                        del chemin[len(chemin)-1]
                else:
                    chemin.append(cellSuiv)
                #recherche de voisins
                voisins = lab.get_contiguous_cells(cellSuiv)
                voisins.remove(cellPrec)
                cellPrec = cellSuiv
                cellSuiv = voisins[randint(0,len(voisins)-1)]
            #Si chemin long
            if len(chemin) > 1:
                for i in range(len(chemin)-1):
                    lab.remove_wall(chemin[i], chemin[i+1])
                    lstNonMarquee.remove(chemin[i])
                lab.remove_wall(chemin[len(chemin)-1], cellSuiv)
            #si chemin comportant une seule cellule
            else :
                lab.remove_wall(cellDep, cellSuiv)
                
            lstNonMarquee.remove(chemin[len(chemin)-1])
            
        return lab
    
    
    
##############################################################################


##  PARTIE 6



###    6.1    
    
    def solve_dfs(self, start :tuple , stop:tuple )-> list:
        """
        

        Parameters
        ----------
        start : tuple
            coordonnée de depart.
        stop : tuple
            coordonnée d'arrivée.

        Returns
        -------
        list
            Recherche le chemin le plus rapide pour atteindre 'stop' en partant
            de 'start' avec un parcours en profondeur.

        """
        assert type(start[0]) == type(start[1]) == type(stop[0])  == type(stop[1])  ==int  and \
                type(start )== type(stop)==tuple , \
            f"Erreur lors de la verification des types des attributs  : type de donnée non adéquat"
            
        #initialisation
        pile = [start]
        lstMarquee = []
        pred = {start : start}
        continu = True
        cellAMarquee = []
        while len(pile) > 0:
            c = pile.pop(0)
            if c == stop:
                continu = False
            else :
                voisins = self.get_reachable_cells(c)
                for i in range(len(voisins)):
                    if voisins[i] not in lstMarquee and voisins[i] not in pile:
                        lstMarquee.append(voisins[i])
                        pile = [voisins[i]] + pile
                        pred[voisins[i]] = c
        c = stop
        chemin = []
        while c != start:
            chemin.append(c)
            c = pred[c]
        chemin.append(start)
        return chemin

    
    
    
    
    def solve_bfs(self, start, stop):
        """

        Parameters
        ----------
        start : tuple
            coordonnée de depart.
        stop : tuple
            coordonnée d'arrivée.

        Returns
        -------
        list
            Recherche le chemin le plus rapide pour atteindre 'stop' en partant
            de 'start' avec un parcours en largeur.

        """
        assert type(start[0]) == type(start[1]) == type(stop[0])  == type(stop[1])  ==int  and \
                type(start )== type(stop)==tuple , \
            f"Erreur lors de la verification des types des attributs  : type de donnée non adéquat"
            
        #initialisation
        file = [start]
        lstMarquee = []
        pred = {start : start}
        continu = True
        cellAMarquee = []
        while len(file) > 0:
           c = file.pop(0)
           if c == stop:
               continu = False
           else :
               voisins = self.get_reachable_cells(c)
               for i in range(len(voisins)):
                   if voisins[i] not in lstMarquee and voisins[i] not in file:
                       lstMarquee.append(voisins[i])
                       file.append(voisins[i])
                       pred[voisins[i]] = c
                       
        c = stop
        chemin = []
        while c != start:
            chemin.append(c)
            c = pred[c]
        chemin.append(start)
        return chemin

    


###    6.2

    def solve_rhr(start:tuple , stop:tuple) ->list:
        """
        

        Parameters
        ----------
        start : tuple
            coordonnée de depart.
        stop : tuple
            coordonnée d'arrivée.
            
        Returns
        -------
        list
            Recherche le chemin le plus rapide pour atteindre le départ en partant
            de l'arrivée dans un labyrinthe sans murs.
        """
        assert type(start[0]) == type(start[1]) == type(stop[0])  == type(stop[1])  ==int  and \
                type(start )== type(stop)==tuple , \
            f"Erreur lors de la verification des types des attributs  : type de donnée non adéquat"
        
        l=[]
        
        return l







###############################################################################

###    PARTIE 7

    def distance_geo(self, c1: tuple , c2 : tuple )-> int:
            """
            

            Parameters
            ----------
            c1 : tuple
                cellule de depart.
            c2 : tuple
                cellule d'arrivée.

            Returns
            -------
            int
                nombre minimale de deplacement necessaire pour atteindre c2 depuis c1 en prenant en compte les murs.

            """
            
            assert type(c1[0]) == type(c1[1]) == type(c2[0])  == type(c2[1])  ==int  and \
                    type(c1 )== type(c2)==tuple , \
                f"Erreur lors de la verification des types des attributs  : type de donnée non adéquat"
            
            chemin = self.solve_dfs(c1, c2)
            return len(chemin)-1






    def distance_man(self, c1:tuple ,c2: tuple )->int :
            """
            

            Parameters
            ----------
            c1 : tuple
                cellule de depart.
            c2 : tuple
                cellule d'arrivée.

            Returns
            -------
            int
                taille du chemin le plus cours sans prendre compte des murs.

            """
            assert type(c1[0]) == type(c1[1]) == type(c2[0])  == type(c2[1])  ==int  and \
                    type(c1 )== type(c2)==tuple , \
                f"Erreur lors de la verification des types des attributs  : type de donnée non adéquat"
            
            return abs(c2[0]-c1[0])+abs(c2[1]-c1[1])
            




###############################################################################


###            PARTIE 8



###     8.1






###     8.2




"""

        TESTs :

"""

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

"""

Permet l'affichage en couleurs

"""

## PARTIE 3

print(color.RED + color.BOLD +'\n Tests Partie 3 \n\n'+ color.END)

laby = Maze(4, 4, False)
print(laby.info())


print(laby)

laby.neighbors = {
    (0, 0): {(1, 0)},
    (0, 1): {(0, 2), (1, 1)},
    (0, 2): {(0, 1), (0, 3)},
    (0, 3): {(0, 2), (1, 3)},
    (1, 0): {(2, 0), (0, 0)},
    (1, 1): {(0, 1), (1, 2)},
    (1, 2): {(1, 1), (2, 2)},
    (1, 3): {(2, 3), (0, 3)},
    (2, 0): {(1, 0), (2, 1), (3, 0)},
    (2, 1): {(2, 0), (2, 2)},
    (2, 2): {(1, 2), (2, 1)},
    (2, 3): {(3, 3), (1, 3)},
    (3, 0): {(3, 1), (2, 0)},
    (3, 1): {(3, 2), (3, 0)},
    (3, 2): {(3, 1)},
    (3, 3): {(2, 3)}
}
print(laby)

laby.neighbors[(1, 3)].remove((2, 3))
laby.neighbors[(2, 3)].remove((1, 3))
print(laby, 'test remove walls')

laby.neighbors[(1, 3)].add((2, 3))
laby.neighbors[(2, 3)].add((1, 3))
print(laby,' test ajoux de voisins \n\n')



## PARTIE 4

print(color.RED + color.BOLD + '\n Tests Partie 4 \n\n' + color.END)

laby = Maze(5, 5, empty=True)
laby.fill()
print(laby, 'laby.fill ')

laby.remove_wall((0, 0), (0, 1))
print(laby,' test remove wall')

laby.empty()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))

print(laby, 'test add wall')

print(laby.get_walls(),'liste des murs')

print(laby.get_contiguous_cells((0, 1)), " cellules contigues")

print(laby.get_reachable_cells((0, 1)),'cellules atteignables \n\n')




## PARTIE 5

print(color.RED + color.BOLD +'\n Tests Partie 5 \n\n'+ color.END)

laby = Maze.gen_btree(4, 4)
print(laby, 'arbre binaire')

laby = Maze.gen_sidewinder(4, 4)
print(laby, 'Sidewinder')

laby = Maze.gen_fusion(4, 4)
print(laby, 'fusion')

laby = Maze.gen_exploration(15,15)
print(laby, 'exploration exhaustive')

laby = Maze.gen_wilson(12, 12)
print(laby,'Wilson \n\n')




## PARTIE 6

print(color.RED + color.BOLD + '\n Tests Partie 6 \n\n' + color.END )

laby = Maze.gen_exploration(15, 15)
solution = laby.solve_dfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'

print(laby.overlay(str_solution), "parcours en profondeur")


solution = laby.solve_bfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution),"parcours en largeur \n\n")




## partie 7

print(color.RED + color.BOLD + '\n Tests Partie 7 \n\n' + color.END)


laby = Maze.gen_exploration(15, 15)
print(laby.distance_geo((0, 0), (14, 14)),'distance géographique')


print(laby.distance_man((0,0),(14,14)),'Manhattan \n\n')


## partie 8 






