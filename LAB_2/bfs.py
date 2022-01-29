# ---------- define 'Graph' class
class Graph:
	def __init__(self, V: set, E: set) -> None:
		self.V, self.E = V, E

	def adj(self, v) -> set:
		adjacents = set({})
		for i in range(len(self.adj_mat()[v])):
			if self.adj_mat()[v][i] == 1:
				adjacents.add(i)
		return adjacents

	def adj_mat(self) -> list:
		A = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
		for v in self.V:
			for e in self.E:
				if v in e:
					A[e[0]][e[1]] = 1
					A[e[1]][e[0]] = 1
		return A
	
	def bfs(self, s, colors, target_color) -> int:
		# let 'q' be a queue
		q = []

		# label 's' as explored (enqueue 's')
		q.reverse()
		q.append(s)
		q.reverse()

		while len(q) > 0:
			v = q.pop()
			if colors[v] == target_color:
					return v
			for node in self.adj(v):
				# label adjacents as explored
				if not node in q:
					q.reverse()
					q.append(node)
					q.reverse()

# ---------- define problem: find the red node of this graph using BFS algorithm (answer: node 1)
V = {0, 1, 2, 3, 4, 5, 6}
E = {(0, 3), (0, 4), (0, 5), (0, 6), (1, 2), (1, 3), (1, 6)}
colors = {
	0: "green",
	1: "red",
	2: "green",
	3: "green",
	4: "green",
	5: "green",
	6: "green"
}
s = 0
target_color = "red"

# ---------- solve problem
G = Graph(V, E)

print(G.bfs(s, colors, target_color))