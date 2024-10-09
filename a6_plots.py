
def plot_q1():
  import matplotlib.pyplot as plt
  plt.figure(figsize=(10, 6))
  plt.plot(range(time_steps), grass_amounts, label='Grass')
  plt.title('Grass Growth Over Time')
  plt.xlabel('Time Steps')
  plt.ylabel('Grass Amount')
  plt.legend()
  plt.grid(True)
  plt.show()
