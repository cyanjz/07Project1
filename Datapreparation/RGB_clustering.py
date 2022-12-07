import pandas as pd
from sklearn.cluster import KMeans
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import pickle

# DATA = pd.read_csv('C:\\workplace\\SW_academy\\project1\\Src\\chairDB.csv')


def kmeans_from_db(data, save_path=None, k=5):
    color_table_temp = list()
    for color in data['색상']:
        temp = color.split('/')  # list of hex-decimal
        for t in temp:
            if len(t) < 7:
                print('Corrupted color detected!')
            else:
                color_dump = list()
                for i in range(3):
                    color_hex = t[1 + i * 2: 1 + (i + 1) * 2]
                    color_dec = int(color_hex, 16)
                    color_dump.append(color_dec/255)
                color_table_temp.append(color_dump)

    color_table = pd.DataFrame(color_table_temp)
    km = KMeans(n_clusters=k, max_iter=1000)
    km.fit(color_table)

    km_cent = km.cluster_centers_
    km_cent_sorted = sorted(km_cent, key=lambda x: sum(x), reverse=True)
    color_centroids = np.array(km_cent_sorted).reshape((k, 1, 3))
    io.imshow(color_centroids)
    plt.show()
    if save_path is not None:
        with open(save_path + '\\' + f'{k}cent', 'wb') as fp:
            pickle.dump(color_centroids, fp)
    return km_cent_sorted


# kmeans_from_db(DATA, 'C:\\workplace\\SW_academy\\project1\\RGB_color_tags', k=5)
# kmeans_from_db(DATA, 'C:\\workplace\\SW_academy\\project1\\RGB_color_tags', k=10)
# kmeans_from_db(DATA, 'C:\\workplace\\SW_academy\\project1\\RGB_color_tags', k=15)
# kmeans_from_db(DATA, 'C:\\workplace\\SW_academy\\project1\\RGB_color_tags', k=20)
