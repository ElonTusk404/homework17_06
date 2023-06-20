while True:
    print('Write the text and I will divide it into parts and output the number of repetitions of each word')
    print('To exit write \'q\'')
    word = input('Write: ')
    if word == 'q':
        break
    chars = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in word:
        if char in chars:
            word = word.replace(char, '')
    word = word.lower().split()

    result = {}
    for w in word:
        if w in result:
            result[w] +=1
        else:
            result[w] = 1
    for key, value in result.items():
        print(f'{key} : {value}')

