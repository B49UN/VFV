def ipt_gsheet(num):
    """
        connect google sheet and import sentence data

        :return:
        1. store every sentence in variable.
        """

    import gspread
    import pandas as pd
    from oauth2client.service_account import ServiceAccountCredentials

    # Authenticate with Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/bagun/Documents/savvy-folio-413809-90235952e75e.json', scope)
    client = gspread.authorize(creds)

    # Open the spreadsheet and select the worksheet by name
    spreadsheet = client.open('Raw_Sentences')
    worksheet = spreadsheet.worksheet('sentences')
    df = pd.DataFrame(worksheet.get_all_records())

    # Check how many sentences are analyzed
    # count = 0
    # number_of_sts = df.shape[0]
    # for i in range(number_of_sts):
    #    if df.iloc[7, 5] == '':
    #        count += 1

    if num == 1:
        # print(f'<Information>\n\tTotal {number_of_sts} sentences, {number_of_sts - count} sentences POS-analyzed')
        return df.iloc[:, 0]


instruction = "너는 영어를 잘 못하는 한국 학생들을 가르치는 영어 선생님이야. " \
              + "네가 어떻게 답변해야 할지 그 규칙을 알려줄게. " \
              + "1. 첫번째 줄은 분석 대상인 영어 문장을 <>안에 넣어서 보여줘. 첫번째 줄은 볼드체야." \
              + "2. 두번째 줄부터는 문장 성분(주어, 목적어, 동사 등)별로 한 줄을 작성해. " \
              + "3. 그 순서는 해당 영어 구절 - 문장 성분(주어, 목적어, 동사 등) - 한국어 해석 순이야." \
              + "4. 문장이 몇형식인지(1형식, 2형식, 3형식 등)를 알려줘. 5. 가장 마지막 줄에는 문장 전체의 한국어 해석을 적어줘." \
              + "6. 만약 문장에 구 또는 절이 있다면 그것을 규칙 2., 3.에 맞게 따로 분석해서 답변 가장 밑에 작성해. "\
              + "답변은 markdown 형식으로 적어"


def structure_analysis_detail(sentence):
    # prepare to use OpenAI API
    from openai import OpenAI
    import os
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": instruction},
            {"role": "user", "content": "Analyze sentence:" + sentence}
        ]
    )
    return completion.choices[0].message.content
