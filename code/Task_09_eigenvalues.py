import numpy as np

A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

nodes = ["A", "B", "C", "D"]

eigenvalues, eigenvectors = np.linalg.eig(A)
index = np.argmax(eigenvalues.real)

dominant_value = eigenvalues[index].real
v = eigenvectors[:, index].real
centrality = np.abs(v)
centrality /= centrality.sum()

print("BIT 2118 - Task 9: Eigenvalues")
print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")

for node, score in zip(nodes, centrality):
    print(f"Node {node}: {score:.4f}")

print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))

# Parameter change: add a connection between A and D
A_changed = A.copy()
A_changed[0, 3] = 1
A_changed[3, 0] = 1

values2, vectors2 = np.linalg.eig(A_changed)
idx2 = np.argmax(values2.real)
scores2 = np.abs(vectors2[:, idx2].real)
scores2 /= scores2.sum()

print("\nAfter adding the A-D connection:")
for node, score in zip(nodes, scores2):
    print(f"Node {node}: {score:.4f}")