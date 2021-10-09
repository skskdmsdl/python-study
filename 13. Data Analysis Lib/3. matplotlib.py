# Matplotlib

# Matplotlib 그래프
# Line plot
fig, ax = plt.subplots()
x = np.arange(15)
y = x ** 2
ax.plot(
  x, y,
  linestyle=":",
  marker="*",
  color="#524FA1" 
)

# Line style
x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x, linestyle="-")
# solid
ax.plot(x, x+2, linestyle="--")
# dashed
ax.plot(x, x+4, linestyle="-.")
# dashdot
ax.plot(x, x+6, linestyle=":")
# dotted

# Line Color
x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x, color="r")
ax.plot(x, x+2, color="green")
ax.plot(x, x+4, color="0.8")
ax.plot(x, x+6, color="#524FA1")

# Marker
x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x, marker=".")
ax.plot(x, x+2, marker="o")
ax.plot(x, x+4, marker="v")
ax.plot(x, x+6, marker="s")
ax.plot(x, x+8, marker="*")

# 축 경계 조정하기
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.set_xlim(-2, 12)
ax.set_ylim(-1.5, 1.5)

# 범례
x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x, label='y=x')
ax.plot(x, x**2, label='y=x^2')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc='upper right', shadow=True, fancybox=True, borderpad=2)

# Bar plot1
# bar
x = np.arange(10)
fig, ax = plt.subplots(figsize=(12, 4))
ax.bar(x, x*2)

# Bar plot2
x = np.random.rand(3)
y = np.random.rand(3)
z = np.random.rand(3)
data = [x, y, z]
fig, ax = plt.subplots()
x_ax = np.arange(3)
for i in x_ax:
  ax.bar(x_ax, data[i],
  bottom=np.sum(data[:i], axis=0))
ax.set_xticks(x_ax)
ax.set_xticklabels(["A", "B", "C"])

# Histogram
fig, ax = plt.subplots()
data = np.random.randn(1000)
ax.hist(data, bins=50)

# Matplotlib with pandas1
df = pd.read_csv("./president_heights.csv")
fig, ax = plt.subplots()
ax.plot(df["order"], df["height(cm)"], label="height")
ax.set_xlabel("order")
ax.set_ylabel("height(cm)")

# Matplotlib with pandas2
df = pd.read_csv("./data/pokemon.csv")
fire = df[(df['Type 1']=='Fire') | ((df['Type 2'])=="Fire")]
water = df[(df['Type 1']=='Water') | ((df['Type 2'])=="Water")]
fig, ax = plt.subplots()
ax.scatter(fire['Attack'], fire['Defense’], color='R', label='Fire', marker="*", s=50)
ax.scatter(water['Attack'], water['Defense’], color='B', label="Water", s=25)
ax.set_xlabel("Attack")
ax.set_ylabel("Defense")
ax.legend(loc="upper right")
