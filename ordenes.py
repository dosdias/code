# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import pandas as pd

# <markdowncell>

# read csv into dataframe

# <codecell>

bfp = '/home/uber/code/sdbox/payment.csv'
hfp = '/home/uber/code/sdbox/hedges.csv'

# <codecell>

dfb = pd.read_csv(bfp)
dfh = pd.read_csv(hfp)


# <codecell>

inner = dfb.merge(dfh,on='order_id')

# <codecell>

print inner

# <codecell>


