import matplotlib.pyplot as plt


def draw_year_label_bars(data, title):
    years = sorted(list(set([row[0] for row in data])))
    labels = sorted(list(set([row[1] for row in data])))
    counts = [[0 for _ in range(len(labels))] for _ in range(len(years))]
    for row in data:
        year_index = years.index(row[0])
        label_index = labels.index(row[1])
        counts[year_index][label_index] = row[2]

    fig, ax = plt.subplots(figsize=(10, 6))  # 设置画布大小
    fig.set_size_inches(20, 8)
    bar_width = 0.8 / len(labels)  # 计算每个平台的条形宽度
    for i, label in enumerate(labels):
        x = [j + i * bar_width for j in range(len(years))]  # 计算当前平台的x坐标
        ax.bar(x, [count[i] for count in counts], width=bar_width, label=label)  # 绘制当前平台的条形图
    ax.set_xticks([j + (len(labels) - 1) * bar_width / 2 for j in range(len(years))])  # 设置x轴刻度
    ax.set_xticklabels(years)  # 设置x轴标签
    ax.legend()  # 添加图例
    ax.set_xlabel('Year')  # 设置x轴标签
    ax.set_ylabel('Count')  # 设置y轴标签
    ax.set_title(title)  # 设置标题
    plt.show()  # 显示图形


def draw_score_scatter(data, title):
    print(data)
    games = {}
    for datum in data:
        if datum[0] in games:
            games[datum[0]]['metascore'].append(datum[1])
            games[datum[0]]['userscore'].append(datum[2])
        else:
            games[datum[0]] = {'metascore': [datum[1]], 'userscore': [datum[2]]}

    fig, ax = plt.subplots(figsize=(12, 12))
    for i, (name, scores) in enumerate(games.items()):
        metascores = scores['metascore']
        userscores = scores['userscore']
        ax.scatter(metascores, userscores, label=name, alpha=0.7)
    ax.set_xlabel('Metascore')
    ax.set_ylabel('Userscore')
    ax.set_title(title)
    ax.legend()

    plt.show()


def draw_score_date_line(data, title):
    grouped_data = {}
    for datum in data:
        if datum[0] not in grouped_data:
            grouped_data[datum[0]] = {'dates': [], 'metascores': []}
        grouped_data[datum[0]]['metascores'].append(datum[1])
        grouped_data[datum[0]]['dates'].append(datum[2])
    fig, ax = plt.subplots()
    for name, group in grouped_data.items():
        ax.plot(group['dates'], group['metascores'], label=name)
    ax.legend()
    ax.set_title(title)
    fig.set_size_inches(20, 8)
    plt.show()
