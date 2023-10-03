import kaggle
import difflib
import chardet

def dt_generator(dtname):
    # Detect the encoding of the file
    with open('dd.txt', 'rb') as f:
        result = chardet.detect(f.read())
    # Open the file with the detected encoding
    file = open('dd.txt', 'r', encoding=result['encoding'])
    names = []
    dataset_names = []
    for i in file:
        x = i.split("/")
        dataset_names.append(x[1][:-1].replace("-"," "))
        names.append(x[0])
    name = dtname
    nearest_name = difflib.get_close_matches(name,dataset_names)
    name = nearest_name[0].replace(" ","-")
    dd = dict()

    dataset = kaggle.api.datasets_list(search = name)
    links = []
    n = 0
    for i in dataset:
        n = n + 1
        f = i['ref']
        ind = f.find('/')
        dd[n] = f
        # print(f'{n}. {f[ind+1:]}')
        links.append(f'https://www.kaggle.com/datasets/{f}')

    print(links)














