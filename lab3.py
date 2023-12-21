import pandas as pd

df = pd.read_csv('datasets/3.csv')

shypo = ['0'] * (length := df.iloc[:, :-1].shape[1])
ghypo = [['?'] * length]

def update_hypothesis(shypo, ghypo, row):
    for i in range(len(shypo)):
        if row.iloc[-1] == 1:
            if shypo[i] != str(row.iloc[i]):
                shypo[i] = '?' if shypo[i] != '0' else str(row.iloc[i])
            ghypo_copy = ghypo.copy()
            for g in ghypo_copy:
                if g[i] != '?' and shypo[i] == '?':
                    ghypo.remove(g)
        elif row.iloc[-1] == 0:
            for i in range(len(shypo)):
                if str(row.iloc[i]) != shypo[i] and shypo[i] != '?':
                    temp_list = ['?'] * i + [shypo[i]] + ['?'] * (len(shypo) - i - 1)
                    if temp_list not in ghypo:
                        ghypo.append(temp_list)

for _, row in df.iterrows():
    update_hypothesis(shypo, ghypo, row)

print("Final Specific Hypothesis:", shypo)
print("Final General Hypothesis:", ghypo)