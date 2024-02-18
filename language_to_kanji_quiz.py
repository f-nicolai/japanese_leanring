import pandas as pd
from pathlib import Path
from utils.plot import display_kanji_and_wait
from utils.user_input import is_user_input_valid, parse_input

data = kanji = pd.read_csv(Path(__file__).parent/'data/words.csv',sep=';')
data['filter'] = data['section'].astype(str)+'_'+data['unit'].astype(str)

user_input = input("Please select a unit or list of units (format : section_unit) or all\n")
while not is_user_input_valid(user_input):
    user_input = input("Please select a unit or list of units (format : section_unit) or all\n")

section_unit = parse_input(user_input)

counter = 1
while True :
    sample = data.loc[data['filter'].isin(section_unit)].sample(replace=True,n=1).to_dict(orient='records')[0]
    print(f"Draw the kanji for: {sample['english']}")
    display_kanji_and_wait(word=sample['english'])

    print(f"Pronunciation: {sample['hiragana']} - {sample['romanji']}")

    display_kanji_and_wait(kanji=sample['kanji'], hiragana=sample['hiragana'], romanji=sample['romanji'])

    print("\n=========================\n")
    counter += 1
