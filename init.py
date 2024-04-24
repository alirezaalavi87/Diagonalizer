import numpy as np

pauli_I = np.array([[1, 0], [0, 1]])
pauli_X = np.array([[0, 1], [1, 0]])
pauli_Y = np.array([[0, -1j], [1j, 0]])
pauli_Z = np.array([[1, 0], [0, -1]])

# pauli_matrices = [pauli_I, pauli_X, pauli_Y, pauli_Z]
pauli_matrices = {
    "Pauli_I": pauli_I,
    "Pauli_X": pauli_X,
    "Pauli_Y": pauli_Y,
    "Pauli_Z": pauli_Z,
}

# Function to diagonalize a matrix


def diagonalize_matrix(matrix):
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    # Calculate diagonal matrix from eigenvalues
    diagonal_matrix = np.diag(eigenvalues)
    # calculate ((eigenvectors^-1).matrix).eigenvectors  which is the diagonalized matrix
    diagonalized_matrix = np.dot(
        np.dot(np.linalg.inv(eigenvectors), matrix), eigenvectors)
    return diagonal_matrix, eigenvectors, diagonalized_matrix


def print_values(matrix_name, matrix, diagonal_matrix, eigenvectors, diagonalized_matrix):
    print(f"matrix name: {matrix_name}")
    print("Original Matrix:")
    print(matrix)

    print("\nDiagonal Matrix:")
    print(diagonal_matrix)

    print("\nEigenvectors:")
    print(eigenvectors)

    print("\nDiagonalized Matrix:")
    print(diagonalized_matrix)

    print("\n================\n")


def main():
    # Loop over Pauli matrices and calculate values for them
    for matrix_name, matrix in pauli_matrices.items():
        diagonal_matrix, eigenvectors, diagonalized_matrix = diagonalize_matrix(
            matrix)
        print_values(matrix_name, matrix, diagonal_matrix,
                     eigenvectors, diagonalized_matrix)


if __name__ == "__main__":
    main()

