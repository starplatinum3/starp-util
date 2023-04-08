import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv("job_skills.csv")

# 职业名称作为节点
nodes = data['job_title']

# 技能、工作经验和教育背景作为特征向量
X = data.drop(['job_title'], axis=1).values

# 计算余弦相似性
similarity = np.dot(X, X.T) / np.linalg.norm(X, axis=1)[:, np.newaxis] / np.linalg.norm(X, axis=1)

# 构建图
G = nx.Graph()
G.add_nodes_from(nodes)

# 添加边
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        if similarity[i][j] > 0.5:
            G.add_edge(nodes[i], nodes[j], weight=similarity[i][j])

# 绘制图形
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='Arial')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,'weight'), font_size=10)
plt.axis('off')
plt.show()
