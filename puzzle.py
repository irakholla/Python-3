schema = {1: ['а', 'б', 'в'],
          2: ['г', 'д', 'е'],
          3: ['ж', 'з', 'и', 'й'],
          4: ['к', 'л', 'м'],
          5: ['н', 'о', 'п'],
          6: ['р', 'с', 'т'],
          7: ['у', 'ф', 'х', 'ц'],
          8: ['ч', 'ш', 'щ'],
          9: ['ь', 'ы', 'ь'],
          0: ['э', 'ю', 'я']}
data = '52331266510'
dict_count = 0
result = {}
result_list = []
for letters_number_in_data in range(len(data)):
    len_result = len(result)
    if letters_number_in_data == 0:
        for letter in schema.get(int(data[letters_number_in_data])):
            result[dict_count] = [letter]
            dict_count += 1
    else:
        for letter in schema.get(int(data[letters_number_in_data])):
            for element in range(len_result):
                result[dict_count] = [result.get(element)]
                result.get(dict_count).append(letter)
                dict_count += 1
f = open('result.txt', 'w')
for l in range(len(result)):
    f.write(("".join(map(str,result[l]))).replace('[', '').replace('\'', '').replace(']', '').replace(',', '').replace(' ', '') + '\n')
f.close()
