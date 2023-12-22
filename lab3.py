import pandas as pd

df = pd.read_csv('datasets/3.csv')

shypo = ['0'] * len(df.columns[:-1])
ghypo = [['?'] * len(shypo)]

for _, row in df.iterrows():
    for i, value in enumerate(row[:-1]):
        if row.iloc[-1] == 1:
            if shypo[i] != str(value):
                shypo[i] = '?' if shypo[i] != '0' else str(value)
                ghypo = [g for g in ghypo if g[i] == '?' or shypo[i] == '?']
        elif row.iloc[-1] == 0 and str(value) != shypo[i] and shypo[i] != '?':
            temp_list = ['?'] * i + [shypo[i]] + ['?'] * (len(shypo) - i - 1)
            if temp_list not in ghypo:
                ghypo.append(temp_list)

print("Final Specific Hypothesis:", shypo)
print("Final General Hypothesis:", ghypo)