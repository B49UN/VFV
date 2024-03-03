import vfvlib
import json

# list of sentences to be created to jsonl file
sts = vfvlib.ipt_gsheet(1).iloc[13:21]
# instruction
sys_ctnt = vfvlib.instruction


def const_assis_cont(num):
    cnk = vfvlib.ipt_gsheet(2, 'chunk').iloc[num]
    ana = vfvlib.ipt_gsheet(2, 'analysis').iloc[num]
    n = 0
    txt = ''
    while cnk.iloc[n] != '':
        txt += cnk.iloc[n] + '\n'
        txt += ana.iloc[n] + '\n'
        n += 1
    return txt


with open("first_tune_val.jsonl", encoding="utf-8", mode="w") as file:
    for i in range(13, 21):
        assis_cont = const_assis_cont(i)
        sent_dict = {
            "messages": [
                {"role": "system",
                 "content": sys_ctnt},
                {"role": "user",
                 "content": "Analyze sentence: " + sts[i]},
                {"role": "assistant",
                 "content": assis_cont}
            ]
        }
        file.write(json.dumps(sent_dict) + "\n")
