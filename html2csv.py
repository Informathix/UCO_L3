#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:58:17 2018

@author: moi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# une page wikipedia avec des tableaux
url = 'http://fr.wikipedia.org/wiki/Coupe_du_monde_de_rugby_%C3%A0_XV_2011'

# on selectionne les tableaux de la page qui contiennentt le champs "Joués"
t = pd.read_html(url, match='Joués', header=0)

# on transforme en tableau numpy dont chaque ligne est [Pays, Points]
tf = np.concatenate([df.filter(items=['Nation', 'PM']).to_records(index=False) for df in t])

# on extrait le tableau 1d des pays et celui des points
pays = [r[0] for r in tf]
points = [r[1] for r in tf]

# on trace un histogramme
plt.pie(points,labels=pays)
plt.show()
