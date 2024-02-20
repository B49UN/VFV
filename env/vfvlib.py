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
    #count = 0
    #number_of_sts = df.shape[0]
    #for i in range(number_of_sts):
    #    if df.iloc[7, 5] == '':
    #        count += 1

    if num == 1:
        # print(f'<Information>\n\tTotal {number_of_sts} sentences, {number_of_sts - count} sentences POS-analyzed')
        return df.iloc[:, 0]

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
             "content": "You are an English teacher who teaches Korean students who are not good at English. Let me "
                        "choose the format of your answers. 1. The answers are made up of several lines. 2. The first "
                        "line contains the English sentences to be analyzed in <>. 3. Write a line per commentary for "
                        "one word in the original sentence from the second line. The format is the original words - "
                        "sentence components(subject, object, etc.) - Part of Speech - Korean interpretation. 4. The "
                        "last line is the Korean"
                        "interpretation for the whole sentence."},
            {"role": "user", "content": "Analyze sentence:" + sentence}
        ]
    )
    return completion.choices[0].message.content