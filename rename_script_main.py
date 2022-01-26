import os
from pickle import dump

list_dir = os.listdir()
new_name = ''

for i in list_dir:
    new_name = i
    if i.__contains__('FusionBD.Com'):
        new_name = new_name.replace('FusionBD.Com','')
    if i.__contains__('Bhoot_FM-'):
        new_name = new_name.replace('Bhoot_FM-', '')
    if i.__contains__('Bhoot-FM-'):
        new_name = new_name.replace('Bhoot-FM-', '')
    new_name = new_name.replace('_','-')
    if not new_name.__contains__('-.mp3'):
        new_name = new_name.replace('.mp3', '-.mp3')
    
    name_split = new_name.split('-')
    if name_split[2].__contains__('20') and name_split.__len__() == 4:
        set_name = ''
        for j in [2,1,0,-1]:
            set_name += name_split[j]
            if name_split[j] != '.mp3':
                set_name += '_'

        os.rename(i, set_name)



    #print(new_name)
    