import matplotlib.pyplot as plt
import pprint


move_counts = []
p1_scores = []
p2_scores = []
results = []
p1_jumps = []
p2_jumps = []
p1_starts = []
p2_starts = []


with open(".data.txt", "r") as f:
  for line in f.readlines():
    lst = line.split(",")

    move_counts.append(int(lst[1]))
    p1_scores.append(int(lst[2]))
    p2_scores.append(int(lst[3]))
    results.append(lst[4])
    p1_jumps.append(int(lst[5]))
    p2_jumps.append(int(lst[6]))

    starts = f"{lst[7].strip()},{lst[8].strip()},{lst[9].strip()}"
    p1_starts.append(starts)

    starts = f"{lst[10].strip()},{lst[11].strip()},{lst[12].strip()}"
    p2_starts.append(starts)



def move_counts_graph():
  plt.hist(move_counts, 20, (0, 200), color="green", histtype="bar", rwidth=0.8)
  plt.xlabel("# of Moves")
  plt.ylabel("Frequency")
  plt.show()


def wins():
  win_percentage = round((results.count("Win") / len(results)) * 100, 2)
  print(f"{win_percentage}%")


def jumps_on_win():
  total_jumps = 0

  for i in range(len(results)):
    if results[i] == "Win":
      total_jumps += p1_jumps[i]
    elif results[i] == "Loss":
      total_jumps += p2_jumps[i]
    else:
      total_jumps += (p1_jumps[i] + p2_jumps[i]) / 2

  print(f"{round(total_jumps * 200 / sum(move_counts), 2)}%")


def placements_on_win():
  placements = {}

  for i in range(len(results)):
    if results[i] == "Win":
      for tile in p1_starts[i].split(","):
        if not tile in placements:
          placements[tile] = 1
        else:
          placements[tile] += 1
    elif results[i] == "Loss":
      for tile in p2_starts[i].split(","):
        if not tile in placements:
          placements[tile] = 1
        else:
          placements[tile] += 1

  pprint.pprint({k: v for k, v in sorted(placements.items(), key=lambda item: item[1])})

# move_counts_graph()
# wins()
# jumps_on_win()
placements_on_win()
