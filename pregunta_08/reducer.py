#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    sum = 0
    total = 0

    for line in sys.stdin:

        key, val, index = line.split("\t")
        val = float(val)
        index = float(index)

        if key == curkey:
            sum += val
            total += index
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, sum/total))

            curkey = key
            sum = val
            total = index

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, sum/total))