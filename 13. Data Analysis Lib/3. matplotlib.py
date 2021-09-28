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
