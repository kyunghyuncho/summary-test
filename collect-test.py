import numpy
import glob



def main():

    fnames = glob.glob('./record*.txt')

    sysnames = ['ours-in', 'ours-out', 'wl']
    counts = numpy.zeros((len(sysnames), len(sysnames)))

    for fn in fnames:
        with open(fn, 'r') as f:
            f.readline() # throw away the heading
            for line in f:
                if len(line) < 2:
                    continue
                cols = [int(c.strip()) for c in line.split(',')]
                sysa, sysb = cols[1], cols[2]
                winner = cols[3]
                if winner == sysa:
                    counts[sysa, sysb] = counts[sysa, sysb] + 1
                else:
                    counts[sysb, sysa] = counts[sysb, sysa] + 1

    print("\t\t".join(["    "]+sysnames))
    for ci, cname in enumerate(sysnames):
        print("{}\t\t{}".format(cname, '\t\t'.join([str(fi) for fi in list(counts[ci,:])])))

if __name__ == '__main__':
    main()

