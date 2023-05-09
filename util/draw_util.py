import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

stopwords = set(STOPWORDS)
with open('..\\util\\stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords.update([line.strip() for line in f])


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


def draw_count_pie(data, title):
    grouped_data = {}
    for item in data:
        entity = item[0]
        if entity not in grouped_data:
            grouped_data[entity] = {}
        grouped_data[entity][item[1]] = item[2]

    fig, axes = plt.subplots(nrows=1, ncols=len(grouped_data), figsize=(15, 7))
    if len(grouped_data) == 1:
        axes = [axes]

    for i, (entity, data) in enumerate(grouped_data.items()):
        labels = list(data.keys())
        values = list(data.values())

        axes[i].pie(values, labels=labels, autopct="%1.1f%%", radius=1)
        axes[i].set_title(f"{entity.capitalize()}")
        _, y = axes[i].get_ylim()
        axes[i].title.set_position([0.5, y + 10.1])
    plt.suptitle(title, fontsize=16)
    plt.subplots_adjust(wspace=0.2)
    plt.show()


def draw_score_box(data, title, x_label):
    data = {"name": [row[0] for row in data], "score": [row[1] for row in data]}
    sns.set(style='ticks')
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.boxplot(data=data, x='name', y='score', ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel('Score')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.tick_params(axis='x', labelsize=8)
    sns.despine(trim=True)
    plt.tight_layout()
    plt.show()


def draw_word_cloud(data):
    text = " ".join(review[0] for review in data)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
