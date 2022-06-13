#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    dict_result_4 = {}
    
    for line in sys.stdin:
        numbers, letters = line.split('\t')
        numbers = int(numbers)
        letters = letters.strip()
        letters = letters.split(',')
        for letter in letters:
            if letter in dict_result_4.keys():
                dict_result_4[letter].append(numbers)
            else:
                dict_result_4[letter] = [numbers]
    

    for key in sorted(dict_result_4.keys()):
        result_num = sorted((dict_result_4[key]))
        result_num_2 = ",".join([str(num) for num in result_num])
        sys.stdout.write("{}\t{}\n".format(key, result_num_2))
