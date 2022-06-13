#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    keys = []
    vals = []

    for line in sys.stdin:

        keys.append(line.split("\t")[0])
        vals.append(int(line.split("\t")[1]))
    
    final_order = zip(keys, vals)
    
    final_order_2 = sorted(final_order, key=lambda tup: tup[1]) 

    for key, val in final_order_2:
        sys.stdout.write("{},{}\n".format(key, val))