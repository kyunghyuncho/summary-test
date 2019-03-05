import numpy
import time


def main():
    numpy.random.seed(int(time.time()))

    idx = numpy.random.randint(100000)
    name = input('Please state your name (no space): ')
    name = name.replace(" ", "_")

    fname = 'record-{}-{}.txt'.format(name, idx)
    fout = open(fname, 'w')
    print('article id, system a, system b, answer', file=fout)
    #print('article id, system a, system b, answer')

    # load files
    articles = [l for l in open('data-dontlook/in')]
    ours_in = [l for l in open('data-dontlook/ours_in')]
    ours_out = [l for l in open('data-dontlook/ours_out')]
    wl = [l for l in open('data-dontlook/wl')]
    systems = [ours_in, ours_out, wl]

    n_lines = len(articles)

    indices = numpy.random.permutation(n_lines)

    for ii in indices:
        try:
            print('Article')
            print(articles[ii])
            print('')

            sysids = numpy.random.choice(numpy.arange(3), 2, replace=False)
            sysa, sysb = sysids[0], sysids[1]

            print('(a)', systems[sysa][ii])
            print('(b)', systems[sysb][ii])

            ans = -1

            while True:
                preferred = input('Which do you prefer? Type a or b: ')
                preferred = preferred.strip().lower()

                if preferred == 'a':
                    ans = sysa
                elif preferred == 'b':
                    ans = sysb
                else:
                    continue
                break

            print('{},{},{},{}'.format(ii, sysa, sysb, ans), file=fout)
            #print('{},{},{},{}'.format(ii, sysa, sysb, ans))

        except KeyboardInterrupt:
            break

    print('Thank you. Please send {} to kyunghyun.cho@nyu.edu.'.format(fname))

if __name__ == '__main__':
    main()
