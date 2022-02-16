#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("age_gender.csv")
df1= pd.DataFrame(df)
plt.xlabel = 'Gender (1= Female, 0-Male)'
plt.figure(figsize=(10,7))
ax=df1.gender.value_counts().plot.bar(x='Gender (1= Female, 0-Male)', y='Count', title='Gender', legend = (1,0, ('Female', 'Male')))
plt.figure(figsize=(10,7))
labels =['White','Black','Indian','Asian','Hispanic']
ax=df1.ethnicity.value_counts().plot.bar()
ax.set_xticklabels(labels)
ax.set_title('Ethinicity')
## Converting pixels into numpy array
df1['pixels'] = df1['pixels'].apply(lambda x:  np.reshape(np.array(x.split(), dtype="float32"), (48,48)))
df1.head()
def plot_data(rows, cols, lower_value, upper_value):
    fig = plt.figure(figsize=(cols*3,rows*4))
    for i in range(1, cols*rows + 1):
        k = np.random.randint(lower_value,upper_value)
        fig.add_subplot(rows, cols, i) # adding sub plot
        gender = gender_values_to_labels[df.gender[k]]
        ethnicity = eth_values_to_labels[df.ethnicity[k]]
        age = df.age[k]
        im = df.pixels[k]
        plt.imshow(im, cmap='gray')
        plt.axis('off')
        plt.title(f'Gender:{gender}nAge:{age}nEthnicity:{ethnicity}')
        plt.tight_layout()
        plt.show()
plot_data(rows=1, cols=7, lower_value=0, upper_value=len(df))