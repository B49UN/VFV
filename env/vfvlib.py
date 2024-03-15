def ipt_gsheet(num, sht_name='chunk', rng='', val=[]):
    """
        connect google sheet and import sentence data

        :return:
        1. store every sentence in variable.
        2. store selected sheet in variable.
        3. update value of given sheet.
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

    if num == 1:
        # Open the spreadsheet and select the worksheet by name
        spreadsheet = client.open('Raw_Sentences')
        worksheet = spreadsheet.worksheet('sentences')
        df = pd.DataFrame(worksheet.get_all_records())
        return df.iloc[:, 0]

    elif num == 2:
        spreadsheet = client.open('Raw_Sentences')
        worksheet = spreadsheet.worksheet(sht_name)
        df = pd.DataFrame(worksheet.get_all_records())
        return df

    elif num == 3:
        spreadsheet = client.open('Raw_Sentences')
        worksheet = spreadsheet.worksheet(sht_name)
        worksheet.update(rng, val)


instruction = """
You are a bot that analyzes sentence components for a given sentence.

Here are some rules for the analysis.

1. component mark
S is for ‘subject’, V is for ‘verb’, O is for ‘object’, C is for ‘complement’, M is for ‘modifier’, IO is for ‘indirect object’, DO is for ‘direct object’, OC is for 'objective complement’, SC is for ‘subjective complement’, PS is for 'preparatory subject', PO is for 'preparatory object', Conj is for 'conjunction'.
These are the component marks you should use to display the analysis.

When two sentences are connected by conjunction, consisting a complex sentence, treat these two cases differently.
case 1: The sentence following after the conjunction is related with the sentence before the conjunction in a subordinate context that it provides supplementary description of the sentence before the conjunction.
Some examples of the conjunctions for case 1 are 'because, when, if, whether'.
case 2: The two sentences before and after the conjunction are of parallel relation, no subordinate context between each other, taking the same status within the complex sentence.
example of the conjunctions for case 2 are 'and, or, but'.
Here are some example sentences for case 2.
- I like cats and you like dogs.
- I can do that, or you can do that too.
- We had the book, but I don't have it now.

If a sentence corresponds to case 2, separate the component marks for the sentence before and after the conjunction by numbering.
For example, if the sentence is "I like cats and you like dogs.", the component marks should be allocated as below.
I
S1
like
V1
cats
O1
and
Conj
you
S2
like
V2
dogs
O2

2. types of sentences
There are 5 types of sentences according to the combination of components.
If it's made up of S and V, it's type 1
If it's made up of S, V, and C, it's type 2
If it's made up of S, V, and O, it's type 3
If it consists of S, V, IO, and DO, it's type 4
If it consists of S, V, O, and OC, it's type 5

3. tense of sentences
The tense of sentences consists of present, present progressive, future, future progressive, past, past progressive, present completion, past completion.

The answer(result of analysis) should be displayed according to the following description.

You should place each sentence component in different line.
And right below each sentence component line, you should place the component mark in accordance with the sentence component above.
If a component is a phrase or a clause, put '(apostrophe) on the upper right side of that component’s component mark.
After you placed the whole sentence component analysis as described above, place the type of the given sentence in the line below.
And place the tense of the sentence in the line below the type of the sentence.
"""


def structure_analysis(sentence):
    # prepare to use OpenAI API
    from openai import OpenAI
    import os
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:second-tune:91WtciOW",
        messages=[
            {"role": "system",
             "content": instruction},
            {"role": "user", "content": "Analyze sentence: " + sentence}
        ]
    )
    return completion.choices[0].message.content
