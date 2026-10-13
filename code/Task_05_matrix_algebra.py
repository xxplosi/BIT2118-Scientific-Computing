import numpy as np

# Four corners of a square
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Rotation and scaling parameters
angle_degrees = 45
scale_x = 2.0
scale_y = 1.5

angle = np.deg2rad(angle_degrees)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

scale = np.diag([scale_x, scale_y])

transformation = rotation @ scale
transformed_points = points @ transformation.T

print("BIT 2118 - Task 5: Matrix Algebra")
print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", np.round(transformed_points, 4))
print("Determinant:", np.linalg.det(transformation))

# Parameter change: double the horizontal scale
scale_x = 4.0
scale = np.diag([scale_x, scale_y])
transformation = rotation @ scale
changed_points = points @ transformation.T

print("\nAfter changing horizontal scale to 4:")
print(np.round(changed_points, 4))