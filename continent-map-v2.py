import geopandas as gpd
import matplotlib.pyplot as plt

# 下载世界各国的边界数据（自然地球数据）
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# 读取各洲的边界数据
continents = world.dissolve(by='continent')

# 绘制地图
fig, ax = plt.subplots(figsize=(15, 10))

# 使用不同颜色填充各洲
continents.plot(ax=ax, edgecolor='black', linewidth=1, legend=True, categorical=True, cmap='tab20')

# 添加标签
for idx, row in continents.iterrows():
    ax.annotate(text=row.name, xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                horizontalalignment='center', fontsize=12, color='darkred')

# 设置图标题
plt.title('World Continents Boundary Map', fontsize=15)

# 显示地图
plt.show()


