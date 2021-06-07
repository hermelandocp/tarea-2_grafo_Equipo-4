class Vertice:

    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()
        self.distancia = 9999
        self.color = 'white'
        self.pred = -1
        self.nodo = 0

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    def __init__(self):
        self.vertices = dict()
    def agregarVertices(self, vertices):
        for v in vertices:
            n = Vertice(v)
            self.agregarVertice(n)

    def agregarAristas(self, aristas):
        for arista in aristas:
            self.agregarArista(arista[0], arista[1])

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False

    def bfs(self, vert):
        vert = self.vertices[vert]
        vert.distancia = 0
        vert.color = 'gray'
        vert.pred = -1
        q = list()

        q.append(vert.nombre)

        while len(q) > 0:

            u = q.pop()
            node_u  = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gray'
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    q.append(v)
            self.vertices[u].color = 'black'        

    def imprimeGrafo (self):
        for key in sorted(list(self.vertices.keys())):
            print ("Vertice " + key + " sus vecinos son "+ str(self.vertices[key].vecinos) )
            print("La distancia de A a " + key + " es: "+ str(self.vertices[key].distancia))
            print()
    def modificar (self):
      print(aristas)
      posicion=len (aristas)
      while posicion >= len (aristas):
        posicion = int(input("inserta la posicion "))
        valornuevo=(input("ingrese nuevo valor"))
        aristas[posicion] = valornuevo
        print(aristas)
    def eliminarnodo (self):
        nodo = input("Ingrese el nodo que desea eliminar: ")
        l=[]
        for i in aristas:
          if nodo in i:
            print (i)
          else: l.append(i)
        print (l)

vertices = [chr(i) for i in range(ord('A'), ord('H'))]
aristas=[]

numeronodos = int(input("inserta el numero de nodos: "))
for x in range(numeronodos):
    valor=(input("INGRESE UNA PAREJA DE  VERTICES:"))
    aristas.append(valor)
   
print(aristas)
grafo = Grafo()
grafo.agregarVertices(vertices)
grafo.agregarAristas(aristas)
grafo.bfs('A')
print("Resultado del Grafo")
grafo.imprimeGrafo()
print("Modificar el  Grafo")
grafo.modificar()
print("Eliminar nodo del  Grafo")
grafo.eliminarnodo()