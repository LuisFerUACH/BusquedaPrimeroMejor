def ObtenerCamino(ini,Cerrados):
    resp=[]
    listo=False
    actual=Cerrados[-1].nombre
    while not listo:
        if actual==ini:
            listo=True
            resp.insert(0,actual)
        else:
            for nodo in Cerrados:
                if nodo.nombre==actual:
                    resp.insert(0,actual)
                    actual=nodo.padre
                    break
    return resp

def siguiente(Abiertos):
    fmejor=100
    mejor=None
    donde=0
    cuenta=0
    for nodo in Abiertos:
        if nodo.f < fmejor:
            fmejor=nodo.f
            mejor=nodo
            donde=cuenta
        cuenta=cuenta +1
    del Abiertos[donde]
    return Abiertos,mejor

class Edo:
    def __init__(self,nombre,padre,f):
        self.nombre=nombre
        self.padre=padre
        self.f=f

def expandir(edo,proble,Abiertos,Cerrados):
    hijos=proble[edo.nombre]
    for hijo in hijos:
        fnue=edo.f+hijos[hijo]
        m,p=miembro(hijo,Cerrados)
        if not m :
            m2,p2=miembro(hijo, Abiertos)
            if m2:
                fori = Abiertos[p2].f
                if fnue < fori:
                    Abiertos[p2]=Edo(hijo,edo.nombre,fnue)
            else:
                Abiertos.append(Edo(hijo,edo.nombre,fnue))
    return Abiertos

def miembro(edo ,lista):
    resp = False
    indi = -1
    cuenta =0
    for nodo in lista:
        if edo == nodo.nombre:
            resp = True
            indi = cuenta
            break
        else:
            cuenta=cuenta+1
    return resp,indi

def primMej(ini,meta,proble):
    Abiertos =[Edo(ini,ini,0)]
    Cerrados =[]
    listo = False
    while not listo:
        Abiertos,actual=siguiente(Abiertos)
        if actual.nombre==meta:
            listo=True
            Cerrados.append(actual)
        else:
            Cerrados.append(actual)
            Abiertos=expandir(actual,proble,Abiertos,Cerrados)
    return Cerrados



## Funcion principal
def main(ini ,meta):
    proble ={ 'A':{'B':20,'C':15},
              'B':{'A':20,'C':6,'E':5,'G':30},
              'C':{'A':15,'B':6,'D':5,'F':9},
              'D':{'C':5,'F':7},
              'E':{'B':5,'F':4,'G':25},
              'F':{'D':7,'C':9,'E':4},
              'G':{'B':30,'E':25}}
    cerrados = primMej(ini,meta,proble)
    camino = ObtenerCamino(ini,cerrados)
    print('El mejor camino es:')
    print(camino)

 ## Este es el punto de entrada al programa
if __name__ == '__main__':
    a = input('Inserte el estado inicial: ')
    b = input('Inserte la meta: ')
    main(a,b)
