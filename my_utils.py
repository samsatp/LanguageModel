import pandas as pd
import os

"""
    Read a file providing general Finnish names
"""
df = pd.read_excel(os.path.join('data','etunimitilasto-2022-08-04-dvv.xlsx'), sheet_name='Miehet ens')

"""
    Create a list of all possible characters
"""
names = list(df.Etunimi.str.lower())
chars = set(''.join(names))

"""
    Create look-up dictionaries:
    - c2i: to map a character to an index
    - i2c: to map the other way
"""
c2i = {c:i for i, c in enumerate(chars, start=1)}
c2i['<s>'] = 0
c2i['<e>'] = len(c2i)
i2c = {i:c for c, i in c2i.items()}