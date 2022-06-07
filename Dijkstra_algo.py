# Reading .txt files 
city_name = open("city_name.txt",'r')
city = city_name.read().splitlines()
city_dist = open("distance.txt",'r')
# Making adjacent list of distances
distance = []
for row in city_dist:
    row = row.split(" ")
    temp = []
    for num in row:
        if num != "":
            temp.append(int(num))
    distance.append(temp)
code = open("city_code.txt",'r')
city_codes = code.read().splitlines()

Graph = {}
Distances = {}
for i in range(len(city_codes)):
    # Placing empty list as a value against every key of graph
    Graph[city_codes[i]] = []
    # Placing huge number (infinity) as a value against every key of distance
    Distances[city_codes[i]] = 99999999999

# Making directed graph and adding values as given in file
for c_code in range(30):
    for j in range(30):
        value = (city_codes[j], distance[j][c_code])
        Graph[city_codes[c_code]].append(value)

# Dijkstra algorithm
def Dijkstra(Weighted_Graph, vertex):
    bucket = []
    Q = []
    SST = []
    bucket.append(vertex)
    Q.extend(Graph[vertex])
    Q.sort(key=lambda y: y[1])
    Distances[vertex] = 0

    while len(Q) != 0:
        Q.sort(key = lambda y : y[1])
        code_dist = Q.pop(0)
        for vertex in bucket:
            if code_dist[0] not in bucket:
                if code_dist in Graph[vertex]:
                    bucket.append(code_dist[0])
                    Q.extend(Graph[code_dist[0]])
                    Distances[code_dist[0]] = int(Distances[vertex]) + int(code_dist[1])
                    SST.append((vertex, code_dist[0]))
    return Distances

# Calling function
vertex = 'AZ'
print(Dijkstra(Graph, vertex))