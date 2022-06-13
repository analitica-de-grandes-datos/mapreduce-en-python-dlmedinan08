#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    keys = []
    dates = []
    vals = []

    for line in sys.stdin:

        keys.append(line.split("\t")[0])
        dates.append((line.split("\t")[1]))
        vals.append(int(line.split("\t")[2]))
    
    final_order = zip(keys, dates, vals)
    
    final_order_2 = sorted(final_order, key=lambda tup: tup[2]) 

    final_order_3 = final_order_2[0:6]

    for key, date, val in final_order_3:
        sys.stdout.write("{}   {}   {}\n".format(key, date, val))