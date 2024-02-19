def ipt_gsheet(num):
    """
        connect google sheet and import sentence data

        :return:
        1. number of sentences, number of POS analyzed sentences, etc.
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

    # Check how many sentences are POS-analyzed(menu 1)
    count = 0
    number_of_sts = df.shape[0]
    for i in range(number_of_sts):
        if df.iloc[7, 5] == '':
            count += 1

    if num == 1:
        print(f'<Information>\n\tTotal {number_of_sts} sentences, {number_of_sts - count} sentences POS-analyzed')

