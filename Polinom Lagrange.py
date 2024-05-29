import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x_values, y_values, x):
    """
    Menghitung nilai interpolasi Lagrange pada titik x.
    
    Args:
    x_values (numpy array): array dari nilai x yang diketahui
    y_values (numpy array): array dari nilai y yang diketahui
    x (float): nilai x yang ingin diinterpolasi
    
    Returns:
    float: nilai y hasil interpolasi
    """
    n = len(x_values)
    L = np.zeros(n)
    for i in range(n):
        L[i] = 1
        for j in range(n):
            if i != j:
                L[i] *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return np.sum(L * y_values)

# Testing interpolasi pada beberapa titik
test_points = np.linspace(5, 40, 100)
interpolated_values = [lagrange_interpolation(x, y, point) for point in test_points]

# Plotting hasil interpolasi
plt.figure(figsize=(10, 6))
plt.plot(test_points, interpolated_values, label='Interpolasi Lagrange', color='blue')
plt.scatter(x, y, color='red', label='Data asli')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()
