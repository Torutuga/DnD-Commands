from random import randint as rni
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter as _gl
import os

def nameGen(x, sht):
    if x == '!name':
        _rn = (1, 117)
        name = []
        general = rni(1,100)
        if general >= 1:
            syl = rni(_rn[0], _rn[1])
            name.append(sht['A'+str(syl)].value)
        if general > 11:
            syl = rni(_rn[0], _rn[1])
            name.append(sht['A'+str(syl)].value)
        if general > 70:
            syl = rni(_rn[0], _rn[1])
            name.append(sht['A'+str(syl)].value)
        if len(name) == 1:
            print(name[0])
        if len(name) == 2:
            print(name[0]+name[1].lower())
        if len(name) == 3:
            print(name[0]+name[1].lower() + '-'+ name[2])
