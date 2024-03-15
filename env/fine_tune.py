import vfvlib
import json

# list of sentences to be created to jsonl file
start_number = int(input('start number: ')) - 2
end_number = int(input('end number: ')) - 1
sts = vfvlib.ipt_gsheet(1).iloc[start_number:end_number]
# instruction
sys_ctnt = vfvlib.instruction

all_cnk = vfvlib.ipt_gsheet(2, 'chunk')
all_ana = vfvlib.ipt_gsheet(2, 'analysis')
all_ten = vfvlib.ipt_gsheet(2, 'tense')


def const_assis_cont(num):
    cnk = all_cnk.iloc[num]
    ana = all_ana.iloc[num]
    ten = all_ten.iloc[num]
    n = 0
    txt = ''
    while cnk.iloc[n] != '':
        txt += cnk.iloc[n] + '\n'
        txt += ana.iloc[n] + '\n'
        n += 1
    txt += '<tense>\ntype ' + str(ten.iloc[0]) + '\n' + ten.iloc[1] + '\n'
    return txt


with open("second_tune_val.jsonl", encoding="utf-8", mode="w") as file:
    for i in range(start_number, end_number):
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
