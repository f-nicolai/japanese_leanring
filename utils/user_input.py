from pathlib import Path
import pandas as pd
from matplotlib.pyplot import close

all_units = pd.read_csv(Path(__file__).parent.parent/'data/words.csv',sep=';')[['section','unit']].drop_duplicates()
all_units = (all_units['section'].astype(str)+'_'+all_units['unit'].astype(str))

def is_user_input_valid(user_input:str):
    if user_input=='all':
        return True
    elif len(user_input.split(',')) > 0:
        return all([check_section_unit_format(x) for x in user_input.split(',')])
    else:
        return False

def check_section_unit_format(format:str)-> bool:
    inputs = format.split('_')
    if len(inputs) != 2:
        return False
    else:
        return inputs[0].isdigit() and inputs[1].isdigit()

def parse_input(user_input:str)->list[str]:
    if user_input == 'all' :
        return all_units.to_list()
    return user_input.split(',')
