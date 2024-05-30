def first_algoritmo(G):
    first = {}
    for no_terminal in G:
        first[no_terminal] = set()
    _ = True
    while _:
        _ = False
        for no_terminal, producciones in G.items():
            for produccion in producciones:
                first_produccion = first_de_produccion(produccion, first)
                verificador = len(first[no_terminal])
                first[no_terminal] = first[no_terminal] | first_produccion
                if len(first[no_terminal]) != verificador:
                    _ = True
    return first

def first_de_produccion(produccion, first):
    first_produccion = set()
    for elemento in produccion:
        if elemento in first:
            first_produccion = first_produccion | first[elemento]
            if 'e' not in first[elemento]:
                break
        else:
            first_produccion.add(elemento)
            break
    else:
        first_produccion.add('e')
    return first_produccion

def follow_algoritmo(G, simbolo_inicial):
    first = first_algoritmo(G)
    follow = {}
    for no_terminal in G:
        follow[no_terminal] = set()
    follow[simbolo_inicial].add('$')
    verificador = True
    while verificador:
        verificador = False
        for no_terminal, producciones in G.items():
            for produccion in producciones:
                verificador = verificador or follow_de_produccion(no_terminal, produccion, follow, first)
    return follow

def follow_de_produccion(no_terminal, produccion, follow, first):
    verificador = False
    trailer = follow[no_terminal].copy()
    for simbolo in reversed(produccion):
        if simbolo in follow:
            verificador2 = len(follow[simbolo])
            follow[simbolo] = follow[simbolo] | trailer
            if len(follow[simbolo]) != verificador2:
                verificador = True
            if 'e' in first[simbolo]:
                trailer = trailer | (first[simbolo] - {'e'})
            else:
                trailer = first[simbolo]
        else:
            trailer = {simbolo}
    return verificador

def main():
  c = int(input())
  for _ in range(c):
    n = int(input())
    G = {}
    j = 0
    while j < n:
      l = input()
      l = l.split()
      G[l[0]] = []
      for i in range(1,len(l)):
        G[l[0]].append(l[i])
      j+=1
    i = 0
    first_set = first_algoritmo(G)
    for simbolo in G:
        simbolo_inicial = simbolo
        break
    follow_set =  follow_algoritmo(G, simbolo_inicial)
    for non_terminal, first in first_set.items():
        print(f"First({non_terminal}) = {first}")
    #-----------------------------------
    print("")
    for non_terminal, follow in follow_set.items():
        print(f"Follow({non_terminal}) = {follow}")
main()
