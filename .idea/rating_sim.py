import random
from pandas import DataFrame
import numpy as np
import pandas as pd


def wtc_generator():
    wtc = []
    for i in range(5):
        wtc.append(np.random.normal(0.5, 0.15, 1))
    return wtc

def atc_generator(): ##ability to create of teachers
    atc = []
    for i in range(5):
        atc.append(np.random.normal(10, 3, 1))
    return atc

def atc_s_generator(): ##ability to create of students
    atcs = []
    for i in range(5):
        atcs.append(np.random.normal(10, 3, 1))
    return atc

# def rating_generator(one_ten): ## better to delet and statrt from 0 rating for all users
#     ratings = []
#     for i in range(5):
#         ratings.append(random.choice(one_ten))
#     return ratings

def distribution(ratings, max_limit):
    if not ratings:
        dist = []
    else:
        dist = []
        for r in ratings:
            if r != min(ratings):
                dist.append(max_limit)
            else:
                dist.append(0)
    return dist

def wtc_change(dist, wtc):
    loc_wtc = []
    if not dist:
        loc_wtc = wtc
    else:
        for key, val in enumerate(dist):
            if val == 0:
                loc_wtc.append(1.0)
            else:
                loc_wtc.append(wtc[key])
    return loc_wtc

def mat_rat_cal(atc, loc_wtc, ratings):
    materials = []

    for key, val in enumerate(loc_wtc):
        num_mat = int(atc[key] * val)
        materials.append(num_mat)
        for i in range(num_mat):
            alfa = np.random.normal(0.5, 0.15, 1)
            beta = np.random.normal(5, 2, 1)
            gamma =  np.random.normal(5, 2, 1)
            if len(ratings)< 5:
                ratings.append(np.round(alfa + beta + gamma, 2))
            else:
                ratings[key] = np.round(ratings[key] + alfa + beta + gamma, 2)
    return materials, ratings


def mat_rat_cal_2(atc, loc_wtc, ratings):
    materials = []

    for key, val in enumerate(loc_wtc):
        num_mat = int(atc[key] * val)
        materials.append(num_mat)
        for i in range(num_mat):
            alfa = np.random.normal(0.5, 0.15, 1)
            beta = np.random.normal(5, 2, 1)
            gamma =  np.random.normal(5, 2, 1)
            if len(ratings)< 5:
                ratings.append(np.round(alfa + beta + gamma, 2))
            else:
                ratings[key] = np.round(alfa + beta + gamma, 2)
    return materials_2, ratings_2


# zero_one = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# one_ten = [1, 2, 3, 4, 5, 6, 7, 8]
# ratings = [1,2,3,4,5]##rating_generator(one_ten)

ratings = []
glob_rating = []
atc = atc_generator()
print('ATC:', atc)
glob_wtc = []

print('rating:', ratings)
glob_materials = []
stud_dist = []
dist = []
num_students = 100
max_limit = 25
glob_num_teachers = 100


for i in range(10):
    dist = distribution(ratings, max_limit)
    stud_dist.append(dist)

    wtc = wtc_generator()
    print('_wtc:', wtc)

    loc_wtc = wtc_change(dist, wtc)
    print('wtc_', loc_wtc)

    glob_wtc.append(loc_wtc)
    materials, ratings = mat_rat_cal(atc, loc_wtc, ratings)
    # print('materials:' ,materials)
    # print('ratings:' ,ratings)
    glob_materials.extend(materials)
    glob_rating.extend(ratings)

    # glob_rating.reshape(10, 5)
    # print(glob_rating)
#     glob_wtc.append(wtc)
# print( 'wtc:', glob_wtc)
# print('Students distribution:', stud_dist)
# print('Teachers rating:', glob_rating)
# print('Number of materials:', glob_materials)

wtc_df = DataFrame(glob_wtc, columns=None)
print('DataFram of WTC')
print(wtc_df)

ratings_df = pd.DataFrame(np.array(glob_rating).reshape(10,5))
print('DataFrame of Ratings')
print (ratings_df)

materials_df = pd.DataFrame(np.array(glob_materials).reshape(10,5))
print('DataFrame of Materials')
print(materials_df)