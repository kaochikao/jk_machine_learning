
logs = open('nb_daily_log.txt', 'r').read().splitlines()

# logs = [
#     '2020-03-23:2',
#     '2020-03-29:8'
# ]

log_d = {}

for l in logs:
    if len(l) < 1:
        continue
    k = l.split(':')[0]
    v = l.split(':')[1]
    log_d[k] = int(v)


# -------------

import numpy as np
import matplotlib.pyplot as plt


start = '2020-03-20'
today = str(np.datetime64('today') + np.timedelta64(1, 'D'))
date_series = np.arange(start, today, dtype='datetime64[D]')
val_series = []

    
count = 0
for date in date_series:
    date = str(date)
    if log_d.get(date):
        count = log_d[date]
    
    val_series.append(count)

# -------------

plt.rcParams['axes.facecolor'] = 'grey'
plt.plot(date_series, val_series, color='orangered')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.ylim(0, 50)
plt.fill_between(
    date_series,
    val_series, 
    color="orange", 
    alpha=0.8)

plt.grid(True)

plt.savefig('progress.png')