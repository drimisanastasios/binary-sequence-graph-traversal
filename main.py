import argparse

parser = argparse.ArgumentParser()
parser.add_argument("s", type = int, help="simvola 0")
parser.add_argument("t", type = int, help="simvola 1")
parser.add_argument("mode", choices=["graph", "dfs", "bts"])
parser.add_argument("start", nargs = "?", type = int, default = None)

args = parser.parse_args()
s = args.s
t = args.t
mode = args.mode
start = args.start

##gia zitoumeno bts
def psakseRblock(node):
    previous = False
    let = None
    j1 = 0
    for i, char in enumerate(node):
        if char == '0':
            previous = True
        elif char == '-':               
            if previous:
                let = i - 1
                previous = False
            elif i>1 and node[i-1] == '-':
                let = i - 2
                j1 = 2
            previous = False
    return let, j1


def psakseLblock(node):
    previous1 = False
    previous2 = False
    let = None
    j = None
    for i, char in enumerate(node):
        if char == '+':
            previous1 = True
            previous2 = False
        elif char == '-':
            if previous1:
                previous2 = True
        else:
            if previous1 and previous2:
                let = i - 2
                j = 2
                previous1 = False
                previous2 = False
            elif previous1:
                let = i - 1
                previous1 = False
                j = 1
    return let, j 


def psakseProsimo(node, block):
    for i in range(block + 1, len(node)):
        if node[i] == '+':
            node[i] = '-'
            break
        elif node[i] == '-':
            node[i] = '+'
            break
    return node


def dimiourgiaDiadoxou(node):
    node = list(node)
    generated_nodes = []
    rBlock, j1 = psakseRblock(node)
    lBlock, j = psakseLblock(node)
    while rBlock is not None or lBlock is not None:
        if rBlock is not None and (lBlock is None or rBlock > lBlock):
            if j1 == 2:
                node[rBlock] = '-'
                node[rBlock + 2] = '0'
            else:
                node[rBlock] = '-'
                node[rBlock + 1] = '0'
            node = psakseProsimo(node, rBlock)
        else:
            node[lBlock] = '0'
            node[lBlock + 1] = '+'
            node = psakseProsimo(node, lBlock + 1)
            if j == 2:
                node[lBlock + 2] = '+'
                node = psakseProsimo(node, lBlock + 2)
        generated_nodes.append(''.join(node))
        rBlock, j1 = psakseRblock(node)
        lBlock, j = psakseLblock(node)
    return ''.join(node), generated_nodes

def metatropi_se_dyadiko(metatheseis_midenika):
    dyadikoi = []
    for node in metatheseis_midenika:
        node=list(node)
        for i, char in enumerate(node):
            if node[i] == '+' or node[i] == '-':
                node[i] = '0'
            else:
                node[i] = '1'
        dyadikoi.append(''.join(node))
    return dyadikoi

def metatropi_se_anaparastasi_deiktwn(metatheseis_dyadiko):
    diktes = []
    for node in metatheseis_dyadiko:
        node=list(node)
        apotelesma = []
        for i, char in enumerate(node):
            if node[i] == '1':
                apotelesma.append(str((len(node)-1) - i))
        diktes.append(''.join(apotelesma))
    return diktes

def dimiourgia_node(s, t):
    midenikasinplin = []
    for j in range(0, 2**(s - 1)):
        dyadikoj = format(j, f'0{s-1}b')
        new_num = '0' * t + '-'
        for bit in dyadikoj:
            if bit == '1':
                new_num += '-'
            else:
                new_num += '+'
        midenikasinplin.append(new_num)
    return midenikasinplin

def metatropi_se_dekadikous(metatheseis_dyadiko):
    metatheseis_dekadiko = []
    for node in metatheseis_dyadiko:
        node=list(node)
        num = 0
        for i, char in enumerate(node):
            if node[i] == '1':
                num = num + 2**(len(node)-1-i)
        metatheseis_dekadiko.append(num)
    return metatheseis_dekadiko

##gia ta ipolipa
def paragontiko(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * paragontiko(x - 1)

def metatheseis_dekadiko(protos_komvos_kanoniki, t, n):
    metath = set()

    def antikatastasi(x, i, j):
        if ((x >> i) & 1) != ((x >> j) & 1):
            x ^= (1 << i)
            x ^= (1 << j)
        return x
    
    def met2(x, k):
        metath.add(x)
        for i in range(k, n - 1):
            for j in range(i + 1, n):
                new_x = antikatastasi(x, i, j)
                if new_x not in metath:
                    met2(new_x, i + 1)
    
    met2(protos_komvos_kanoniki, 0)
    return sorted(metath)

def metatropi_se_diadiko(pinakas, mikos):
    apotelesma = []
    for num in pinakas:
        apotelesma.append(format(num, f'0{mikos}b'))
    return apotelesma

##gia to zitoumeno graph
def dimiourgiagrafou(pinakas_metatheseis_dyadiko):
    grafos = {}
    for node in pinakas_metatheseis_dyadiko:
        node_str = str(node)
        grafos[node_str] = []
    for node in pinakas_metatheseis_dyadiko:
        node_str = str(node)
        for neighbor in pinakas_metatheseis_dyadiko:
            neighbor_str = str(neighbor)
            if node_str != neighbor_str:
                diafores = 0
                for a, b in zip(node_str, neighbor_str):
                    if a != b:
                        diafores += 1
                if diafores == 2:
                    grafos[node_str].append(neighbor_str)

    return grafos


def metatroph_se_arithmous(dyadikos_grafos):
    dekadikos_grafos = {}
    
    for komvos, geitones in dyadikos_grafos.items():
        komvos_arithmos = int(komvos, 2)
        geitones_arithmoi = [int(geitonas, 2) for geitonas in geitones]
        dekadikos_grafos[komvos_arithmos] = geitones_arithmoi
    
    return dekadikos_grafos

def emfanisi_pinaka(dekadikos_grafos): 
    for komvos in sorted(dekadikos_grafos.keys(), reverse=True):
        geitones = sorted(dekadikos_grafos[komvos])
        print(f"{komvos} -> {geitones}")

##gia dfs

def dyadiko_se_anaparastasi_diktwn(binary_str):
    return int(''.join(str(len(binary_str) - 1 - i) for i, bit in enumerate(binary_str) if bit == '1'), 10)

def anaparastasi_diktwn(dyadikos_grafos):
    grafos_anaparastasi_diktwn = {}
    
    for node, neighbors in dyadikos_grafos.items():
        node_positions = dyadiko_se_anaparastasi_diktwn(node)
        neighbors_positions = [dyadiko_se_anaparastasi_diktwn(neighbor) for neighbor in neighbors]
        
        grafos_anaparastasi_diktwn[node_positions] = neighbors_positions
    
    return grafos_anaparastasi_diktwn

def dfs(graph, start, komvoi_grafou):
    stack = [start]
    diadromes = []
    antigrafo = {k: list(v) for k, v in graph.items()}

    while stack:
        node = stack[-1]
        protopsif = False
        best_neighbor = None
        max_common = -1
        defteropsifio = -1
        for neighbor in antigrafo[node]:
            if neighbor not in stack:
                neighbor_str = str(neighbor)
                node_str = str(node)
                if neighbor_str[0] == node_str[0]:
                    protopsif = True
                    j = 0
                    for i in range(1, len(node_str)):
                        if neighbor_str[i] == node_str[i]:
                            j += 1
                        else:
                            break
                    if (defteropsifio == j or j >= max_common) and sum(c1 != c2 for c1, c2 in zip(neighbor_str, node_str)) == 1:
                        max_common = j
                        best_neighbor =  neighbor
                else:
                    for i in range(1, len(node_str)):
                        j = 0
                        if neighbor_str[i] == node_str[i]:
                            j += 1
                        else:
                            break
                    if j >= max_common and sum(c1 != c2 for c1, c2 in zip(neighbor_str, node_str)) == 1 and protopsif == False:
                        max_common = j
                        best_neighbor =  neighbor
                        defteropsifio = j
        if best_neighbor is not None:
            stack.append(best_neighbor)
            antigrafo[node].remove(best_neighbor)
            if len(stack) == komvoi_grafou:
                diadromes.append(list(stack))
                for i in range(komvoi_grafou - 1):
                    stack.pop()
        else:
            antigrafo[node] = list(graph[node])
            stack.pop()
                
    return diadromes

def teleutea(diadromes, n):
    neospinakas = []
    for diadromi in diadromes:
        nea_diadromi = []
        for komvos in diadromi:
            komvos_str = str(komvos)
            neos_komvos = ['0'] * n
            for digit in komvos_str:
                if digit != '[' and digit != ']' and digit != ',':
                    i = int(digit)
                    neos_komvos[n - 1 - i] = '1'
            neos_komvos_str = ''.join(neos_komvos)
            nea_diadromi.append(neos_komvos_str)
        neospinakas.append(nea_diadromi)
    return neospinakas

def teleutea2(pinakas_dyadikos):
    pinakas_dekadikos = []
    for diadromi in pinakas_dyadikos:
        nea_diadromi = []
        for dyadikos in diadromi:
            dekadikos = int(dyadikos, 2)
            nea_diadromi.append(dekadikos)
        pinakas_dekadikos.append(nea_diadromi)
    return pinakas_dekadikos

if mode == 'bts':

    pinakas_midenika = dimiourgia_node(s, t)
    metatheseis_midenika = []
    for node in pinakas_midenika:
        apotelesma, metatheseis = dimiourgiaDiadoxou(node)
        metatheseis.insert(0, node)
        metatheseis_midenika.append(metatheseis)
        metatheseis_dyadiko = metatropi_se_dyadiko(metatheseis)
        metatheseis_midenika.append(metatheseis_dyadiko)
        metatheseis_diktes = metatropi_se_anaparastasi_deiktwn(metatheseis_dyadiko)
        metatheseis_midenika.append(metatheseis_diktes)
        metatheseis_dekadiko = metatropi_se_dekadikous(metatheseis_dyadiko)
        metatheseis_midenika.append(metatheseis_dekadiko)
    print(metatheseis_midenika)
 
elif mode == 'graph':
    if (s >= t):
        komvoi_grafou = paragontiko(s+t) / (paragontiko(t) * paragontiko((s + t) - t))
    else:
        komvoi_grafou = paragontiko(s+t) // (paragontiko(t) * paragontiko(s))
        n = s + t 
        akmes_komvou = (1/2) * (n**2 - (s**2 + t**2))
        akmes_grafou = 2 * akmes_komvou
    protos_komvos_dyadiki = ("0" * s + "1" * t)
    protos_komvos_dekadiki = int(protos_komvos_dyadiki, 2)
    pinakas_metatheseis_dekadiko = metatheseis_dekadiko(protos_komvos_dekadiki, t, n)
    pinakas_metatheseis_dyadiko = metatropi_se_diadiko(pinakas_metatheseis_dekadiko, n)
    dyadikos_grafos = dimiourgiagrafou(pinakas_metatheseis_dyadiko)
    dekadikos_grafos = metatroph_se_arithmous(dyadikos_grafos)
    emfanisi_pinaka(dekadikos_grafos)
    grafos_anaparastasi_diktwn = anaparastasi_diktwn(dyadikos_grafos)

elif mode == 'dfs':
    if (s >= t):
        komvoi_grafou = paragontiko(s+t) / (paragontiko(t) * paragontiko((s + t) - t))
    else:
        komvoi_grafou = paragontiko(s+t) // (paragontiko(t) * paragontiko(s))
        n = s + t 
        akmes_komvou = (1/2) * (n**2 - (s**2 + t**2))
        akmes_grafou = 2 * akmes_komvou
    protos_komvos_dyadiki = ("0" * s + "1" * t)
    protos_komvos_dekadiki = int(protos_komvos_dyadiki, 2)
    pinakas_metatheseis_dekadiko = metatheseis_dekadiko(protos_komvos_dekadiki, t, n)
    pinakas_metatheseis_dyadiko = metatropi_se_diadiko(pinakas_metatheseis_dekadiko, n)
    dyadikos_grafos = dimiourgiagrafou(pinakas_metatheseis_dyadiko)
    grafos_anaparastasi_diktwn = anaparastasi_diktwn(dyadikos_grafos)
    for key in grafos_anaparastasi_diktwn:
        grafos_anaparastasi_diktwn[key].sort(reverse=True)
    grafos_sorted = dict(sorted(grafos_anaparastasi_diktwn.items(), key=lambda x: x[0], reverse=True))
    diadromes = []
    ##print(grafos_anaparastasi_diktwn)
    if start is not None:
        dyadikos = format(start, f'0{n}b')
        str_dyadikos = str(dyadikos)
        apotelesma = []
        for i in range(0, len(str_dyadikos)):
            if str_dyadikos[i] == '1':
                apotelesma.append(str(len(str_dyadikos) - i - 1))
        dekadikos = ''.join(apotelesma)
        dekadikos = int(dekadikos)
        diadromes.extend(dfs(grafos_anaparastasi_diktwn, dekadikos, komvoi_grafou))
        diadromes_dyadiki = teleutea(diadromes, n)
        diadromes_dekadiko = teleutea2(diadromes_dyadiki)
        print(diadromes_dyadiki)
        print(diadromes)
        print(diadromes_dekadiko)
    else: 
        for i in sorted(grafos_anaparastasi_diktwn.keys(), reverse=True):
            diadromes.extend(dfs(grafos_anaparastasi_diktwn, i, komvoi_grafou))
        print(diadromes)
