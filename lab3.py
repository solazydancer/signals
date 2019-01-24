import csv
import numpy as np
import math
import matplotlib.pyplot as plt


def run():
    amp_sig = 1.0
    snr = 13.0
    x = np.linspace(0, 0.1, 10000)
    signal = np.array([])
    noise = np.array([])

    # read csv with signal
    with open('14_signal.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            signal = np.append(signal, float(row[0]))

    # read csv with noise
    with open('14_noise.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            noise = np.append(noise, float(row[0]))

    # SNR = 20*log10(Amp_signal / Amp_noise)
    summ = 0
    for i in signal:
        summ += pow(i, 2)
    amp_sig = math.sqrt(summ/len(signal))


    summ = 0
    for i in noise:
        summ += pow(i, 2)
    amp_noise_csv = math.sqrt(summ / len(noise))

    amp_noise = amp_sig / (10 ** (snr / 20))
    k = amp_noise / amp_noise_csv

    print k

    # get signal+noise*k data
    sig_and_noise = signal + noise * k

    # plot
    plt.figure(figsize=(15, 10), dpi=300)
    plt.plot(x[::10], sig_and_noise[::10], color='g', linewidth=0.5)
    plt.title('Noise (10%)')
    plt.ylabel('Amplitude, V')
    plt.xlabel('Time, sec')
    plt.savefig('3.png')
    plt.clf()

    np.savetxt('14_sn.csv', sig_and_noise, delimiter=',')
    plt.clf()


if __name__ == "__main__":
    run()
