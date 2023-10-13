import pandas as pd
# Sample dataset
data = {'Length': [5.1, 4.9, 4.7, 4.6, 5.0],'Width': [3.5, 3.0, 3.2, 3.1, 3.6],'Height': [1.4, 1.4, 1.3, 1.5, 1.4]}
df = pd.DataFrame(data)
df['Volume'] = df['Length'] * df['Width'] * df['Height']
print(df)
