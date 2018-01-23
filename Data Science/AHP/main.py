import numpy as np


def matrix_classification(comparison_matrix):
    num_elements = comparison_matrix.shape[0]

    # Calculate Eigen Vector
    sum_array = sum(comparison_matrix)
    norm_array = comparison_matrix / sum_array
    temp_array = [sum(norm_array[y]) for y in range(num_elements)]
    priority_vector = np.array(temp_array) / num_elements

    # Calculate Principal Eigen Value
    p_eigen_value = np.dot(priority_vector, sum_array)

    return p_eigen_value, priority_vector

def consistency_index(eigen_max, n_elements):
    """Consistency index calc"""

    return (eigen_max - n_elements) / (n_elements - 1)

def consistency_ratio(consist_index, rand_consist_index):
    """Consistency ration between calculated consistency and random sample"""

    return consist_index / rand_consist_index


ri_table = {
    1: .0,
    2: .0,
    3: .58,
    4: .9,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.41,
    9: 1.45,
    10: 1.49
}

l1_matrix = np.array(
    [
        [1.0, 3.0, 7.0, 9.0],
        [.33, 1.0, 5.0, 7.0],
        [.14, .20, 1.0, 3.0],
        [.11, .14, .33, 1.0]
    ]
)

l1_eigen_max, p_vector_l1 = matrix_classification(l1_matrix)
ci_l1 = consistency_index(l1_eigen_max, l1_matrix.shape[0])
cr_l1 = consistency_ratio(ci_l1, ri_table[l1_matrix.shape[0]])

l2_matrix_a = np.array(
    [
        [1.0, 1.0, 7.0],
        [1.0, 1.0, 3.0],
        [.14, .33, 1.0],
    ]
)

l2_eigen_max_a, p_vector_l2a = matrix_classification(l2_matrix_a)
ci_l2_a = consistency_index(l2_eigen_max_a, l2_matrix_a.shape[0])
cr_l2_b = consistency_ratio(ci_l2_a, ri_table[l2_matrix_a.shape[0]])

l2_matrix_b = np.array(
    [
        [1.0, .2, .5],
        [5.0, 1.0, 5.0],
        [2.0, .2, 1.0],
    ]
)

l2_eigen_max_b, p_vector_l2b = matrix_classification(l2_matrix_b)
ci_l2_b = consistency_index(l2_eigen_max_b, l2_matrix_b.shape[0])
cr_l2_b = consistency_ratio(ci_l2_b, ri_table[l2_matrix_b.shape[0]])

adjusted_weights = np.array(
    [
        p_vector_l1[0] / (p_vector_l1[0] + p_vector_l1[1]),
        p_vector_l1[1] / (p_vector_l1[0] + p_vector_l1[1])
    ]
)

x_priority = np.array([p_vector_l2a[0], p_vector_l2b[0]])
y_priority = np.array([p_vector_l2a[1], p_vector_l2b[1]])
z_priority = np.array([p_vector_l2a[2], p_vector_l2b[2]])

# Composite wheights vector
cw = np.array(
    [
        np.dot(x_priority, adjusted_weights),
        np.dot(y_priority, adjusted_weights),
        np.dot(z_priority, adjusted_weights)
    ]
)

ext_adjusted_wights = np.append(np.array([1.0]), adjusted_weights)

decision_ci = np.array([ci_l1, ci_l2_a, ci_l2_b])
decision_ri = np.array(
    [
        ri_table[l1_matrix.shape[0]],
        ri_table[l2_matrix_a.shape[0]],
        ri_table[l2_matrix_b.shape[0]]
    ]
)

ci_acum = np.dot(decision_ci, ext_adjusted_wights)
ri_acum = np.dot(decision_ri, ext_adjusted_wights)

decision_cr = (ci_acum / ri_acum)

print(decision_cr)