from numpy.random import uniform, power, poisson, laplace
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

nb_etu = 4000
n_max = 100

devoir = [[np.floor(i) for i in uniform(0, n_max+1, nb_etu)],
          [np.floor(j) for j in n_max*power(5, nb_etu)],
          [np.floor(k) for k in poisson(n_max/2, nb_etu)],
          [np.floor(l) for l in laplace(n_max/2, 1, nb_etu)],
          [np.floor(j) for j in n_max*power(2, nb_etu)],
          [np.floor(j) for j in n_max*power(15, nb_etu)],
          [np.floor(k) for k in poisson(2*n_max/3, nb_etu)]
         ]

n_dev = len(devoir)
n_row = int(np.ceil(n_dev/2))

ax = [plt.subplot2grid((n_row + 1, 2), (i, j)) for i in range(n_row) for j in range(2)]
ax.append(plt.subplot2grid((n_row + 1, 2), (n_row, 0), colspan=2))


for k in range(n_dev):
    ax[k].set_xlim(0, n_max)    
    
for k in range(n_dev):
    ax[k].set_title('Devoir' + str(k))

ax[-1].set_title('Moyennes et ecarts types')

cmap = plt.get_cmap('gnuplot')
couleur = [cmap(i) for i in np.linspace(0, 1, n_dev)]


for k in range(n_dev):
    ax[k].hist(devoir[k], histtype="bar",
             bins=n_max + 1, range=(0, n_max), alpha=0.8, color = couleur[k])



ind = [k for k in range(0, n_max, 5)]
indx = [round(float(u)*n_max/(n_max+1) + n_max/(2*(n_max+1)), 2) for u in ind]
for k in range(n_dev):
    ax[k].set_xticks(indx)
    ax[k].set_xticklabels(ind)



ax[-1].set_xlim(0, 3*n_dev + 1)
means = [np.mean(d) for d in devoir]
stds = [np.std(d) for d in devoir]
ind = np.linspace(1, 3*n_dev, n_dev)
ax[-1].bar(ind, means, 2,
         alpha=0.8, yerr=stds, label='Moyennes', color=couleur)
ax[-1].set_xticks(ind)
ax[-1].set_xticklabels(['Devoir ' + str(k) for k in range(n_dev)])

plt.show()
