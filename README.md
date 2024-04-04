# Geography
要在地图上使用其他颜色来绘制国界，你需要分别设置地理数据的填充颜色和边界颜色。在你的代码中，你已经通过cmap参数设置了填充颜色。要设置边界颜色，你可以使用edgecolor参数。此外，使用linewidth参数可以调整边界线的宽度，以使国界更为显眼。  

以下是如何在你的代码中设置国界颜色的示例，这里假设我们想要将国界绘制为黑色：  

```
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify
from matplotlib.colors import LinearSegmentedColormap

# 读取CSV文件，假设文件名为'covid_data.csv'
covid_data = pd.read_csv('covid_data.csv', header=None, names=['State', 'Cases'])

# 加载美国各州的地理信息，确保你有一个包含州边界的GeoJSON文件
usa = gpd.read_file('gz_2010_us_040_00_500k.json')

# 将新冠数据合并到地理数据中，这里假设GeoJSON文件中州名的列名为'NAME'
usa_with_covid = usa.set_index('NAME').join(covid_data.set_index('State'))

# 创建一个自定义的橙色渐变颜色映射
orange_cmap = LinearSegmentedColormap.from_list("mycmap", ["#ffffcc", "#ff8000"])

# 绘制地图，使用自定义的橙色渐变颜色映射，根据病例数变化颜色明暗  
# 设置国界颜色为黑色，边界线宽度为0.5  
usa_with_covid.plot(column='Cases', legend=True, cmap=orange_cmap, scheme='NaturalBreaks', k=5,
                    edgecolor='black', linewidth=0.5)

# 设置地图的经度显示范围从-130到-50
plt.xlim(-130, -50)

plt.title('COVID-19 Cases Distribution in the USA')
plt.show()


```
![figure 1](Figure_1.png)  

在这个示例中，edgecolor='black'设置了边界颜色为黑色，linewidth=0.5设置了边界线的宽度。你可以根据需要调整这些值，比如改变edgecolor为其他颜色代码以使用不同的颜色绘制国界。  
