
import os

# list 

dirs = {
    'INTRO': 'Intro',
    'CNN': 'CNN',
    'NLP': 'NLP',
    'SEQUENCE': 'Sequence'
}

nb_counts = {}

for k in dirs:
    dir_nb_count = 0
    files = os.listdir("../{}".format(dirs[k]))
    for f in files:
        _, ext = os.path.splitext(f)
        if ext == '.ipynb':
            dir_nb_count += 1

    nb_counts[k] = dir_nb_count



README = '../README.md'

out_lines = []
tf_total = 0

for k in nb_counts:
    tf_total += nb_counts[k]
    out_lines.append("\t- {}: {}".format(k, nb_counts[k]))


out_lines = ["- TF_TOTAL: {}".format(tf_total)] + out_lines

out = open(README, 'w')
journal = open('journal.md', 'r')

for l in out_lines:
    out.write(l + '\n')

out.write('\n-----------------------\n\n')
out.write(journal.read())
out.write('\n-----------------------\n\n')

out.write('![progress chart](/utils/progress.png)')
journal.close()
out.close()

daily_log_f = open('nb_daily_log.txt', 'r')
logs = daily_log_f.read().splitlines()
daily_log_f.close()



log_d = {}
for l in logs:
    date = l.split(':')[0]
    count = l.split(':')[1]
    log_d[date] = count

import datetime 

today = datetime.datetime.today()
today = today.strftime('%Y-%m-%d')

log_d[today] = str(tf_total)

daily_log_f = open('nb_daily_log.txt', 'w')

for k in log_d:
    daily_log_f.write("{}:{}\n".format(k, log_d[k]))

daily_log_f.close()