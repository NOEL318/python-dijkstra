import heapq
from flask import Flask, request
from flask_cors import CORS


# Initializing flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mapa_udlap={    "Ignacio Bernal": {"HU": 3, "José Gaos": 10, "Ray Lindley": 12,"Ciencias de La Salud": 14,"Cafetería":12 , "Recursos Humanos": 10, "Auditorio": 8, "CN": 7, "Biblioteca": 11, "Cain Murray": 12, "Gimnasio Moe": 18, "Alberca Universitaria": 19, "Gimnasio Pesas": 20, "Negocios":11},
	"HU": { "Ignacio Bernal": 3, "José Gaos": 14, "Ray Lindley": 11, "Ciencias de La Salud": 12, "Cafetería": 9, "Recursos Humanos": 13, "Auditorio": 8, "CN": 4, "Biblioteca": 8, "Cain Murray": 9, "Gimnasio Moe": 17, "Alberca Universitaria": 18, "Gimnasio Pesas": 19, "Negocios": 8},
	"CN": { "HU": 4, "Ignacio Bernal": 7, "José Gaos": 11, "Ray Lindley": 9, "Ciencias de La Salud": 11, "Cafetería": 6, "Recursos Humanos": 9, "Auditorio": 3, "Biblioteca": 4, "Cain Murray": 5, "Gimnasio Moe": 13, "Alberca Universitaria": 14, "Gimnasio Pesas": 15, "Negocios": 5 },
	"Auditorio": { "HU": 4, "Ignacio Bernal": 7, "José Gaos": 11, "Ray Lindley": 9, "Ciencias de La Salud": 11, "Cafetería": 6, "Recursos Humanos": 9, "Auditorio": 3, "CN": 7, "Biblioteca": 4, "Cain Murray": 5, "Gimnasio Moe": 13, "Alberca Universitaria": 14, "Gimnasio Pesas": 15, "Negocios": 3 },
	"Biblioteca": { "HU": 8, "Ignacio Bernal": 11, "José Gaos": 7, "Ray Lindley": 5, "Ciencias de La Salud": 7, "Cafetería": 2, "Recursos Humanos": 10, "Auditorio": 5, "CN": 4, "Cain Murray": 1, "Gimnasio Moe": 9, "Alberca Universitaria": 10, "Gimnasio Pesas": 11, "Negocios": 5 },
	"Negocios": { "HU": 8, "Ignacio Bernal": 11, "José Gaos": 7, "Ray Lindley": 5, "Ciencias de La Salud": 7, "Cafetería": 2, "Recursos Humanos": 13, "Auditorio": 2, "CN": 3, "Cain Murray": 5, "Gimnasio Moe": 9, "Alberca Universitaria": 10, "Gimnasio Pesas": 11, "Biblioteca": 4 },
	"José Gaos": { "HU": 13, "Ignacio Bernal": 10, "Ray Lindley": 6, "Ciencias de La Salud": 8, "Cafetería": 6, "Recursos Humanos": 16, "Auditorio": 19, "CN": 13, "Biblioteca": 9, "Cain Murray": 10, "Gimnasio Moe": 10, "Alberca Universitaria": 11, "Gimnasio Pesas": 12, "Negocios": 5 },
  "Ray Lindley": {
    "Ignacio Bernal": 12,
    "HU": 11,
    "José Gaos": 6,
    "Ciencias de La Salud": 5,
    "Cafetería": 4,
    "Recursos Humanos": 8,
    "Auditorio": 9,
    "CN": 9,
    "Biblioteca": 5,
    "Cain Murray": 6,
    "Gimnasio Moe": 11,
    "Alberca Universitaria": 12,
    "Gimnasio Pesas": 13,
    "Negocios": 5
  },
  "Ciencias de La Salud": {
    "Ignacio Bernal": 14,
    "HU": 12,
    "José Gaos": 8,
    "Ray Lindley": 5,
    "Cafetería": 5,
    "Recursos Humanos": 6,
    "Auditorio": 11,
    "CN": 11,
    "Biblioteca": 7,
    "Cain Murray": 8,
    "Gimnasio Moe": 2,
    "Alberca Universitaria": 3,
    "Gimnasio Pesas": 4,
    "Negocios": 7
  },
  "Cafetería": {
    "Ignacio Bernal": 13,
    "HU": 10,
    "José Gaos": 6,
    "Ray Lindley": 4,
    "Ciencias de La Salud": 5,
    "Recursos Humanos": 5,
    "Auditorio": 6,
    "CN": 6,
    "Biblioteca": 2,
    "Cain Murray": 3,
    "Gimnasio Moe": 7,
    "Alberca Universitaria": 8,
    "Gimnasio Pesas": 9,
    "Negocios": 2
  },
  "Recursos Humanos": {
    "Ignacio Bernal": 10,
    "HU": 13,
    "José Gaos": 16,
    "Ray Lindley": 8,
    "Ciencias de La Salud": 6,
    "Cafetería": 5,
    "Auditorio": 9,
    "CN": 9,
    "Biblioteca": 10,
    "Cain Murray": 11,
    "Gimnasio Moe": 14,
    "Alberca Universitaria": 15,
    "Gimnasio Pesas": 16,
    "Negocios": 13
  },
  "Cain Murray": {
    "Ignacio Bernal": 12,
    "HU": 9,
    "José Gaos": 10,
    "Ray Lindley": 6,
    "Ciencias de La Salud": 8,
    "Cafetería": 3,
    "Recursos Humanos": 11,
    "Auditorio": 5,
    "CN": 5,
    "Biblioteca": 1,
    "Gimnasio Moe": 7,
    "Alberca Universitaria": 8,
    "Gimnasio Pesas": 9,
    "Negocios": 5
  },
  "Gimnasio Moe": {
    "Ignacio Bernal": 18,
    "HU": 17,
    "José Gaos": 10,
    "Ray Lindley": 11,
    "Ciencias de La Salud": 2,
    "Cafetería": 7,
    "Recursos Humanos": 14,
    "Auditorio": 13,
    "CN": 13,
    "Biblioteca": 9,
    "Cain Murray": 7,
    "Alberca Universitaria": 2,
    "Gimnasio Pesas": 3,
    "Negocios": 9
  },
  "Alberca Universitaria": {
    "Ignacio Bernal": 19,
    "HU": 18,
    "José Gaos": 11,
    "Ray Lindley": 12,
    "Ciencias de La Salud": 3,
    "Cafetería": 8,
    "Recursos Humanos": 15,
    "Auditorio": 14,
    "CN": 14,
    "Biblioteca": 10,
    "Cain Murray": 8,
    "Gimnasio Moe": 2,
    "Gimnasio Pesas": 1,
    "Negocios": 10
  },
  "Gimnasio Pesas": {
    "Ignacio Bernal": 20,
    "HU": 19,
    "José Gaos": 12,
    "Ray Lindley": 13,
    "Ciencias de La Salud": 4,
    "Cafetería": 9,
    "Recursos Humanos": 16,
    "Auditorio": 15,
    "CN": 15,
    "Biblioteca": 11,
    "Cain Murray": 9,
    "Gimnasio Moe": 3,
    "Alberca Universitaria": 1,
    "Negocios": 11
  }
}

@app.route('/data', methods=['POST'])
def dijkstra():
    datos = request.json
    inicio = datos.get('inicio')
    fin = datos.get('fin')
    print(datos)
    heap = [(0, inicio)]  
    distancias = {nodo: float('inf') for nodo in mapa_udlap}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in mapa_udlap}
    while heap:
        distancia_actual, nodo_actual = heapq.heappop(heap)
        if nodo_actual == fin:
            break
        for vecino, peso in mapa_udlap[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                padres[vecino] = nodo_actual
                heapq.heappush(heap, (distancia, vecino))
    camino = []
    nodo = fin
    while nodo:
        camino.insert(0, nodo)
        nodo = padres[nodo]
		
    return [camino, distancias[fin]]

	# return{inicio, fin, camino, distancia_total}


# camino, distancia_total = dijkstra(mapa_udlap, inicio, fin)
# print(f"La ruta más corta de {inicio} a {fin} es: {camino} con una distancia total de {distancia_total}")


if __name__ == '__main__':
    app.run(debug=True)



