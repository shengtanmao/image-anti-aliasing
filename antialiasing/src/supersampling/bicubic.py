import numpy as np

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33


def bicub_val(m):
    """
    computation for bicubic interpolation

    :m: 4 by 4 matrix
    :type file: ndarray

    :return: 4 by 4 matrix
    :rtype: ndarray
    """
    f00 = m[1][1]
    f01 = m[1][2]
    f10 = m[2][1]
    f11 = m[2][2]
    fx00 = (m[1][2] - m[1][0])/2
    fx01 = (m[2][2] - m[2][0])/2
    fx10 = (m[1][3] - m[1][1])/2
    fx11 = (m[2][3] - m[2][1])/2
    fy00 = (m[2][1] - m[0][1])/2
    fy01 = (m[3][1] - m[1][1])/2
    fy10 = (m[2][2] - m[0][2])/2
    fy11 = (m[3][2] - m[1][2])/2
    fxy00 = (fx01 - (m[0][2]-m[0][0])/2)/2
    fxy01 = ((m[3][2]-m[3][0])/2 - fx00)/2
    fxy10 = (fx11 - (m[0][3]-m[0][1])/2)/2
    fxy11 = ((m[3][3] - m[3][1])/2 - fx10)/2
    return np.array([[f00, f01, fy00, fy01], [f10, f11, fy10, fy11],
                     [fx00, fx01, fxy00, fxy01], [fx10, fx11, fxy10, fxy11]])


def compute_coeff(col):
    """
    computes coefficients for bicubic interpolation

    :col: a numpy array representing a single color
    :type file: ndarray

    :return: a dictionary storing every set of coefficients
    :rtype: dict
    """
    m_dict = {}
    m1 = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [-3, 3, -2, -1], [2, -2, 1, 1]])
    m2 = np.array([[1, 0, -3, 2], [0, 0, 3, -2], [0, 1, -2, 1], [0, 0, -1, 1]])
    for i in range(col.shape[0]-3):
        for j in range(col.shape[1]-3):
            m = bicub_val(col[i:i+4, j:j+4])
            m_dict[(i, j)] = np.matmul(np.matmul(m1, m), m2)
    return m_dict


def bicub_inter(array, factor):
    """
    Scales an image by a factor using bicubic interpolation

    :param array: a numpy array representing the image
    :type file: ndarray

    :return: a numpy array representing the scaled image
    :rtype: ndarray
    """
    old_shape = array.shape
    new_arr = np.zeros(
        (round(old_shape[0] * factor), round(old_shape[1] * factor), 3),
        np.uint8)
    new_shape = new_arr.shape
    coeffs = []
    coeffs.append(compute_coeff(array[:, :, 0]))
    coeffs.append(compute_coeff(array[:, :, 1]))
    coeffs.append(compute_coeff(array[:, :, 2]))

    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            x = i / factor
            y = j / factor
            adjx = min(max(0, round(x-1.5)), old_shape[0]-4)
            adjy = min(max(0, round(y-1.5)), old_shape[1]-4)
            key = (adjx, adjy)
            x -= (adjx + 1)
            y -= (adjy + 1)
            for k in range(3):
                a = coeffs[k][key]
                new_arr[i][j][k] = min(max(0, round(np.matmul(np.matmul(
                    np.array([1, x, x**2, x**3]).T, a),
                    np.array([1, y, y**2, y**3])))), 255)
    return new_arr
