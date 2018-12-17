import os, glob, time, csv

# folders of each dataset
folders = ['SED', 'EIMM', 'USED']


def get_files():
    '''
    :return: the sub folders with all the images.
    '''
    subs = {}
    for folder in folders:
        if folder != 'EIMM':
            subs[folder] = glob.glob(folder+"/*/*/*.jpg")
        else:
            subs[folder] = glob.glob(folder + "/*/*/*/*.jpg")
    return subs


def dict2usefull(d):
    '''
    :param d: directories of the files
    :return: a dict with all the available information of the datast
    '''
    table = {
        'ID': [],
        'name': [],
        'format': [],
        'data': [],
        'location': [],
        'event': [],
        'sub-event': [],
        'person': [],
        'datasetID': []
    }
    id = 0
    for key, item in d.items():
        if key == 'SED':
            for img in item:
                m = len(img)
                table['location'].append('ND')
                table['data'].append(0)
                if img[m-12:m-4] == 'noPeople':
                    table['person'].append('No')
                else:
                    table['person'].append('Yes')
                table['datasetID'].append(key)
                table['ID'].append(id)
                id += 1
                table['format'].append('JPEG')
                if img[4] == 'i':
                    table['event'].append('Social')
                    table['sub-event'].append('Indignados')
                    if img[m-12:m-4] == 'noPeople':
                        table['name'].append(img[m-23:m-13])
                    else:
                        table['name'].append(img[m - 21:m - 11])
                elif img[4] == 't':
                    table['event'].append('Social')
                    table['sub-event'].append('Technical')
                    if img[m-12:m-4] == 'noPeople':
                        table['name'].append(img[m-23:m-13])
                    else:
                        table['name'].append(img[m - 21:m - 11])
                else:
                    table['event'].append('Sport')
                    table['sub-event'].append('Soccer')
                    if img[m-12:m-4] == 'noPeople':
                        table['name'].append(img[m-23:m-13])
                    else:
                        table['name'].append(img[m - 21:m - 11])
        elif key == 'EIMM':
        # EIMM
            for img in item:
                m = len(img)
                table['location'].append('ND')
                table['data'].append(0)
                if img[m-12:m-4] == 'noPeople':
                    table['person'].append('No')
                else:
                    table['person'].append('Yes')
                table['datasetID'].append(key)
                table['ID'].append(id)
                id += 1
                table['format'].append('JPEG')
                if img[6] == 'o':
                    table['event'].append('Social')
                    sub = img[12:15]
                    if sub == 'pic':
                        table['sub-event'].append('Pic-Nic')
                    elif sub == 'wed':
                        table['sub-event'].append('Wedding')
                    elif sub == 'con':
                        table['sub-event'].append('Concert')
                    elif sub == 'gra':
                        table['sub-event'].append('Graduation')
                    elif sub == 'mee':
                        table['sub-event'].append('Meeting')
                    elif sub == 'mou':
                        table['sub-event'].append('Mountain')
                    elif sub == 'sea':
                        table['sub-event'].append('Sea-holiday')
                    else:
                        table['sub-event'].append('Ski-holiday')
                    if img[m-12:m-4] == 'noPeople':
                        table['name'].append(img[m-21:m-13])
                    else:
                        table['name'].append(img[m - 19:m - 11])
                elif img[6] == 'p':
                    table['event'].append('Sport')
                    sub = img[11:15]
                    if sub == 'rowi':
                        table['sub-event'].append('Rowing')
                    elif sub == 'bask':
                        table['sub-event'].append('Basket')
                    elif sub == 'swim':
                        table['sub-event'].append('Swimming')
                    elif sub == 'base':
                        table['sub-event'].append('Baseball')
                    elif sub == 'skat':
                        table['sub-event'].append('Skating')
                    elif sub == 'bike':
                        table['sub-event'].append('Bike')
                    elif sub == 'f1_1':
                        table['sub-event'].append('F1')
                    elif sub == 'cycl':
                        table['sub-event'].append('Cycling')
                    elif sub == 'hock':
                        table['sub-event'].append('Hockey')
                    else:
                        table['sub-event'].append('Golf')

                    if img[m-12:m-4] == 'noPeople':
                        table['name'].append(img[m-21:m-13])
                    else:
                        table['name'].append(img[m - 19:m - 11])
        else:
        # USED
            for img in item:
                m = len(img)
                table['location'].append('ND')
                table['data'].append(0)
                if img[m - 12:m - 4] == 'noPeople':
                    table['person'].append('No')
                else:
                    table['person'].append('Yes')
                table['datasetID'].append(key)
                table['ID'].append(id)
                id += 1
                table['format'].append('JPEG')
                sub = img[5:8]
                #print(sub)
                if sub == 'sea':
                    table['event'].append('Social')
                    table['sub-event'].append('Sea-holiday')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[30:53])
                    else:
                        table['name'].append(img[28:51])
                elif sub == 'gra':
                    table['event'].append('Social')
                    table['sub-event'].append('Graduation')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[30:53])
                    else:
                        table['name'].append(img[27:51])
                elif sub == 'pic':
                    table['event'].append('Social')
                    table['sub-event'].append('Pic-nic')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[25:53])
                    else:
                        table['name'].append(img[23:51])
                elif sub == 'ski':
                    table['event'].append('Social')
                    table['sub-event'].append('Ski-holiday')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[30:])
                    else:
                        table['name'].append(img[28:])
                elif sub == 'mou':
                    table['event'].append('Social')
                    table['sub-event'].append('Mountain-trip')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[31:])
                    else:
                        table['name'].append(img[29:])
                elif sub == 'con':
                    table['event'].append('Social')
                    table['sub-event'].append('Concert')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[26:])
                    else:
                        table['name'].append(img[24:])
                elif sub == 'mee':
                    table['event'].append('Social')
                    table['sub-event'].append('Meeting')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[26:])
                    else:
                        table['name'].append(img[24:])
                else:
                    table['event'].append('Social')
                    table['sub-event'].append('Wedding')
                    if img[m - 12:m - 4] == 'noPeople':
                        table['name'].append(img[26:])
                    else:
                        table['name'].append(img[24:])
    return table


if __name__ == '__main__':
    # get lists of directories
    s = get_files()
    # get dataset dicts
    table = dict2usefull(s)
    # number of items in the dict
    nums = len(table['ID'])
    # here the information are merged
    with open('merged.csv', 'w') as f:
        # open a csv writer
        writer = csv.writer(f, table.keys())
        head = ['ID', 'name', 'format', 'data', 'location', 'event', 'sub-event', 'person', 'datasetID']
        # write head
        writer.writerow(head)
        # write items in order
        for n in range(nums):
            file = []
            for key, item in table.items():
                file.append(item[n])
            writer.writerow(file)




