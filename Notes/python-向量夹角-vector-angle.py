## new
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import logging as log
import numpy as np
import math


# %%
# 输出精确度
np.set_printoptions(precision=3)

# 抑制科学计数法
np.set_printoptions(suppress=True)


# %%
def degree_to_vector(degree):
    """
    将度数转化为迪卡尔坐标系下的相应度数的向量
    以x轴正向为0,逆时针为正
    degree 范围为正负无穷皆可,会归到-360~360的范围内
    """
    if degree > 360:
        degree %= 360
    elif degree < -360:
        degree %= -360

    xsign = 1
    ysign = 1
    tanv = math.tan(math.radians(degree))

    x = math.sqrt(1 / (1 + tanv ** 2))
    y = x * tanv

    if 90 < abs(degree) < 270:
        xsign = -1
        ysign = -1

    # if 180 < degree:
    #     ysign = -1
    return (xsign * x, ysign * y)


# %%
for degree in [
    0,
    45,
    90,
    135,
    180,
    225,
    270,
    315,
    360,
    -45,
    -90,
    -135,
    -180,
    -225,
    -270,
    -315,
    -360,
]:
    print((degree, tuple(map(lambda x: round(x, 3), (degree_to_vector(degree))))))


# %%
yheight = 600


def vector2position(vec, yheight):
    return (vec[0], yheight - vec[1])


# %%
vector2position((200, 100), 600)


# %%
def degree_between_tan(v1, v2):
    return np.degrees(np.arctan2(v2[1], v2[0])) - np.degrees(np.arctan2(v1[1], v1[0]))


# %%
for vec in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
    print(vec, degree_between_tan((1, 0), vec))

# %% [markdown]
# 这个函数并非返回绝对度量的值呢

# %%
def vector_degree_tan(v1):
    return np.degrees(np.arctan2(v1[1], v1[0]))


# %%
for vec in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
    print(vec, vector_degree_tan(vec))


# %%
def vector_degree_cos(v1, v2):
    return np.degrees(
        np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    )


# %%
for vec in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
    print(vec, vector_degree_cos((1, 0), vec))


# %%
def vector_degree_tan_abs(v1):
    o_degree = np.degrees(np.arctan2(v1[1], v1[0]))
    abs_degree = o_degree if o_degree >= 0 else 360 + o_degree
    return abs_degree


# %%
for vec in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
    print(vec, vector_degree_tan_abs(vec))


# %%
for vec in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
    print(vec, np.degrees(np.arctan2(vec[1], vec[0])))


# %%
import itertools


# %%
for vec in itertools.combinations(
    [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], r=2
):
    print(vec, degree_between_tan(vec[0], vec[1]))


# %%
def degree_between_tan_abs(v1, v2):
    """"""
    v1_degree = vector_degree_tan_abs(v1)
    v2_degree = vector_degree_tan_abs(v2)

    return v2_degree - v1_degree


# %%
for vec in itertools.combinations(
    [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], r=2
):
    print(vec, degree_between_tan_abs(vec[0], vec[1]))


# %%
def degree_between_tan_abs_min(v1, v2):
    """"""
    v1_degree = vector_degree_tan_abs(v1)
    v2_degree = vector_degree_tan_abs(v2)

    diff_degree = v2_degree - v1_degree

    if -180 < diff_degree < 180:
        return diff_degree
    else:
        return diff_degree - 360 if diff_degree > 0 else 360 + diff_degree


# %%
for vec in itertools.combinations(
    [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], r=2
):
    print(vec, degree_between_tan_abs_min(vec[0], vec[1]))


# %%


## old
def vector_degree_cos(v1, v2):
    return np.degrees(
        np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    )


def vector_degree_tan(v1):
    return np.degrees(np.arctan2(v1[1], v1[0]))


def degree_between_tan(v1, v2):
    return np.degrees(np.arctan2(v2[1], v2[0])) - np.degrees(np.arctan2(v1[1], v1[0]))


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """Returns the angle in radians between vectors 'v1' and 'v2'::"""
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)

    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def direction_between(v1, v2):
    """Returns the angle in radians between vectors 'v1' and 'v2'::"""
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)

    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def vector_diff_degree_clock(v1, v2):
    return np.degrees(angle_between(v1, v2))


def mouse_change_degree(v2):
    v1 = (0, 1)  # y axies
    if v2[0] <= 0:
        return np.degrees(angle_between(v1, v2))
    else:
        return 360 - np.degrees(angle_between(v1, v2))
