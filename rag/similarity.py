import numpy as np
import matplotlib.pyplot as plt

# Define the points
points = {
    'A': np.array([1, 1]),
    'B': np.array([2, 3]),
    'C': np.array([2, 4])
}

def calculate_euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return np.linalg.norm(p2 - p1)

# Calculate distances
dist_ab = calculate_euclidean_distance(points['A'], points['B'])
dist_ac = calculate_euclidean_distance(points['A'], points['C'])

# Create figure and axis
plt.figure(figsize=(10, 5))
ax = plt.gca()

# Plot points
for label, point in points.items():
    plt.scatter(*point, label=f'Point {label}')
    plt.text(point[0], point[1] + 0.5, f'{label}{tuple(point)}', ha='center')

# Draw lines between points with distance labels
for (p1, p2) in [('A', 'B'), ('A', 'C')]:
    distance = calculate_euclidean_distance(points[p1], points[p2])
    plt.plot([points[p1][0], points[p2][0]], 
             [points[p1][1], points[p2][1]], 
             'r--', alpha=0.5)
    mid_point = (points[p1] + points[p2]) / 2
    plt.text(mid_point[0], mid_point[1], f'd = {distance:.2f}', 
             bbox=dict(facecolor='white', alpha=0.8))

# Add grid and labels
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Euclidean Distance Between Points in 2D Space')
plt.axis('equal')
plt.legend()
plt.tight_layout()

# Print the calculations
print("Euclidean Distances:")
print(f"A to B: √(({points['B'][0]}-{points['A'][0]})² + ({points['B'][1]}-{points['A'][1]})²) = {dist_ab:.2f}")
print(f"A to C: √(({points['C'][0]}-{points['A'][0]})² + ({points['C'][1]}-{points['A'][1]})²) = {dist_ac:.2f}")
print(f"\nAnalysis: Point B is much closer to A ({dist_ab:.2f} units) than Point C is ({dist_ac:.2f} units).")

# Show the plot
plt.show()
