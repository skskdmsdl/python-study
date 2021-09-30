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
