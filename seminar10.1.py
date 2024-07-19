# Написать EDA для датасета про пингвинов Необходимо:
# ● ● ● ● ● Использовать 2-3 точечных графика Применить доп измерение 
# в точечных графиках, используя аргументы 
# hue, size, stile Использовать PairGrid с типом графика на ваш выбор 
# Изобразить Heatmap Использовать 2-3 гистограммы Чтобы подключить 
# датасет с пингвинами, воспользуйтесь данным скриптом:
# penguins = sns.load_dataset( penguins.head()
import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt



#1 построить два точечных графика
penguins = sns.load_dataset('penguins')
# sns.scatterplot(data=penguins, x='sex', y='body_mass_g')
# plt.show()
# #2
#sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', size='bill_length_mm', hue='bill_length_mm')
#.scatterplot(data=penguins, x='body_mass_g', y='bill_length_mm', hue='island', style='species')


#3 не работает потому что сергей петух
# data_columns = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# graph = sns.PairGrid__init__(penguins[data_columns],hue='body_mass_g', pallete='deep')
# graph = graph.map_diag(mpl.hist)
# graph = graph.map_offdiag(mpl.scatter)
# #body_mass = {'light': 3000, 'light_heavy': 4000, 'medium': 5000, 'medium_heavy': 5500, 'heavy': 6000}
# graph = graph.add_legend(legend_data=body_mass, title='Масса тушки')
# #plt.show()

#4
# data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
# sns.heatmap(data)
# plt.xlabel('Остров', size=14)
# plt.ylabel('Вид пингвина', size=14)
# plt.show()

#5
sns.displot(data=penguins, x='body_mass_g', kind='hist', col='sex', hue='species')
plt.show()