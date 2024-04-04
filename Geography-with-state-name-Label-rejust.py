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
fig, ax = plt.subplots(1, 1)
usa_with_covid.plot(column='Cases', legend=True, cmap=orange_cmap, scheme='NaturalBreaks', k=5,
                    edgecolor='black', linewidth=0.5, ax=ax)

# 需要东移的州的列表
east_shift_states = ['New York', 'New Jersey', 'Connecticut', 'New Hampshire']
# 需要南移的州和地区的列表
south_shift_states = ['District of Columbia', 'Rhode Island', 'Alabama']

# 标示出州的名称，对特定州进行位置调整
for idx, row in usa_with_covid.iterrows():
    x_offset = 0
    y_offset = 0
    
    # 对需要南移的州和地区进行南移0.5度处理
    if idx in south_shift_states:
        y_offset = -0.5
    
    # 对'New York', 'New Jersey', 'Connecticut'进行东移3度处理
    if idx in east_shift_states:
        x_offset = 3
    
    plt.text(s=idx, x=row.geometry.centroid.x + x_offset, y=row.geometry.centroid.y + y_offset, 
             horizontalalignment='center', fontsize=6, verticalalignment='center')

# 设置地图的经度显示范围从-130到-50
plt.xlim(-180, -50)

plt.title('COVID-19 Cases Distribution in the USA')
plt.show()
