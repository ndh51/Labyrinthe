from random import randint


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
        self.neighbors = {(i, j): set() for i in range(height) for j in range(width)}
        if empty:
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
            txt += "   ┃" if (0, j + 1) not in self.neighbors[(0, j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def gen_sidewinder(h, w):
        lab = Maze(h, w, empty=False)
        for i in range(h - 1):
            lst = []
            for j in range(w - 1):
                lst.append((i, j))
                valAl = randint(0, 1)
                derCell = (i, j)
                # Si valAl = 0 on retire le mur EST
                if valAl == 0:
                    lab.neighbors[(i, j)].add((i, j + 1))
                    lab.neighbors[(i, j + 1)].add((i, j))
                # Sinon on retire le mur SUD
                else:
                    (x, y) = lst[randint(0, len(lst) - 1)]
                    lab.neighbors[(x, y)].add((x + 1, y))
                    lab.neighbors[(x + 1, y)].add((x, y))
                    lst = []
            lst.append(derCell)
            (x, y) = lst[randint(0, len(lst) - 1)]
            lab.neighbors[(x, y)].add((x + 1, y))
            lab.neighbors[(x + 1, y)].add((x, y))
        for k in range(w - 1):
            lab.neighbors[(h - 1, k)].add((h - 1, k + 1))
            lab.neighbors[(h - 1, k + 1)].add((h - 1, k))
        return lab

    def gen_exploration(h, w):
        lab = Maze(h, w, empty=False)
        # Initialisation :
        XcellAl = rand(0, h - 1)
        YcellAl = rand(0, w - 1)
        tabVisite = []
        for i in range(h):
            lst = [False] * w
            tab.append(lst)
        tabVisite[XcellAl, YcellAl] = True
        pile = []
        pile.append((XcellAl, YcellAl))

        while len(pile) > 0:
            cell = pile[len(pile) - 1]
            del pile[len(pile) - 1]
            #voisin = # get_contiguous_cells(cell)
            nonVisite = False
            for i in range(len(voisin)):
                (x, y) = voisin[i]
                if tabVisite[x, y] == False:
                    pile.append(cell)
                # suppression des voisins déjà visité
                if tabVisite[x, y] != False:
                    del voisin[i]
            # choix aléatoir d'une cellule non visitée
            newCell = voisin[randint(0, len(voisin) - 1)]
            (x1, y1) = newCell
            (x2, y2) = cell
            lab.neighbors[(x1, y1)].add((x2, y2))
            lab.neighbors[(x2, y2)].add((x1, y1))
            tabVisite[x1, y1] = True
            pile.append(newCell)
        return lab


####################################################


    def add_wall(self, c1, c2):
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


    def remove_wall(self,c1,c2):
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

    def get_walls(self):
        l=[]
        for i in range(self.height):
            for j in range(self.width):
                if (i + 1) < self.height and 0<=j<self.width and (i + 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i + 1, j)] :
                    l.append([(i,j),(i+1,j)])
                else:
                    if (j + 1) < self.width and 0<=i<self.height and (i, j + 1) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i, j + 1)] :
                        l.append([(i, j), (i, j+1)])
                    else:
                        if (i - 1) >= 0 and 0<=j<self.width and (i - 1, j) not in self.neighbors[(i, j)] and (i, j) not in self.neighbors[(i - 1, j)] :
                                l.append([(i,j),(i-1,j)])
                        else :
                                if (j - 1) >= 0 and 0<=i<self.height and (i, j - 1) not in self.neighbors[(i, j)] and (i, j)not in self.neighbors[(i, j - 1)] :
                                    l.append([(i, j), (i, j-1)])
        return l



    def fill(self):
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
         l=self.get_contiguous_cells(c)
         for i in l:
             if i not in self.neighbors[i]:
                 l.remove(i)
         return l
  
             
laby = Maze(4, 4,False)
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

laby.neighbors[(1,3)].remove((2,3))
laby.neighbors[(2,3)].remove((1,3))
print(laby)

laby.neighbors[(1, 3)].add((2, 3))
laby.neighbors[(2, 3)].add((1, 3))
print(laby)



laby = Maze(5, 5, empty = True)
laby.fill()
print(laby)

laby.remove_wall((0, 0), (0, 1))
print(laby)

laby.empty()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))

print(laby)

print(laby.get_walls())

print(laby.get_contiguous_cells((0,1))," contigue")

print(laby.get_reachable_cells((0,1)))
