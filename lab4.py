from numpy.fft import fft, fftfreq, rfft
import csv
from numpy import abs as np_abs, argmax, square, sqrt, array, arange, sum
from math import log10
import matplotlib.pyplot as plt


def run():

    N = 10000
    FD = 100000
    f0 = 28076.17188
    n = 8192
    k = f0 * n / FD

    frequencies = [l * FD / n for l in range(0, n, 1)]

    print(k)

    # noise
    filename = '14_noise.csv'
    array_noise = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            array_noise.append(float(row[0]))
    fft_noise = fft(array_noise[:n])
    plt.figure(figsize=(25, 10))
    plt.plot(frequencies[1:], np_abs(fft_noise[1:]) / n)
    plt.xlabel(u'Frequency, Hz')
    plt.ylabel(u'Voltage, V')
    plt.title(u'Noise spectrum')
    plt.grid(True)
    plt.savefig('noise.png', dpi=250, format='png')
    plt.clf()

    # signal
    filename = '14_signal.csv'
    array_signal = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            array_signal.append(float(row[0]))
    fft_sig = fft(array_signal[:n])
    plt.figure(figsize=(25, 10))
    plt.plot(frequencies[1:int(n/2)], np_abs(fft_sig[1:int(len(fft_sig)/2)]) / n)
    plt.xlabel(u'Frequency, Hz')
    plt.ylabel(u'Voltage, V')
    plt.title(u'Spectrum of useful signal')
    plt.grid(True)
    plt.savefig('signal.png', dpi=250, format='png')
    plt.clf()

    # plot
    index_max_s = argmax(fft_sig[1:int(len(fft_sig) / 2)])
    print(index_max_s)
    n0 = int(n / 20)
    plt.figure(figsize=(25, 10))
    plt.plot(frequencies[index_max_s - n0:index_max_s + n0],
             np_abs(fft_sig)[index_max_s - int(len(fft_sig)/20):index_max_s + int(len(fft_sig)/20)] / n)
    plt.xlabel(u'Frequency, Hz')
    plt.ylabel(u'Voltage, V')
    plt.title(u'Fragment of the useful signal spectrum')
    plt.grid(True)
    plt.savefig('fragmentSignal.png', dpi=250, format='png')
    plt.clf()
    # mixture
    filename = '14_sn.csv'
    array_sig_with_noise = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            array_sig_with_noise.append(float(row[0]))

    # bpf mixture
    fft_sig_with_noise = fft(array_sig_with_noise[:n])

    plt.figure(figsize=(25, 10))
    # plt.plot(frequencies[1:int(n/2)], np_abs(fft_sig_with_noise[1:int(len(fft_sig_with_noise)/2)]) / n)
    plt.plot(frequencies[1:int(n/2)], np_abs(fft_sig_with_noise[1:int(len(fft_sig_with_noise)/2)]) / n)

    plt.xlabel(u'Frequency, Hz')
    plt.ylabel(u'Voltage, V')
    plt.title(u'The spectrum of a mixture of useful signal and noise')
    plt.grid(True)
    plt.savefig('sig_and_noise.png', dpi=250, format='png')
    plt.clf()
    #
    #
    index_max_sn = argmax(np_abs(fft_sig_with_noise[1:int(len(fft_sig_with_noise) / 2)])) + 2
    #
    plt.figure(figsize=(25, 10))
    plt.plot(frequencies[index_max_sn - n0:index_max_sn + n0],
             np_abs(fft_sig_with_noise[
                    index_max_sn - int(len(fft_sig_with_noise)/20):index_max_sn + int(len(fft_sig_with_noise)/20)]) / n)
    plt.xlabel(u'Frequency, Hz')
    plt.ylabel(u'Voltage, V')
    plt.title(u'Fragment of the spectrum of a mixture of useful signal and noise')
    plt.grid(True)
    plt.savefig('partSigAndNoise.png', dpi=250, format='png')
    plt.clf()

    array_signal = array_signal[1:]
    array_sig_with_noise = array_sig_with_noise[1:]
    #
    array_noise_snr = array(array_sig_with_noise) - array(array_signal)

    Anoise = sum(square(array_noise_snr))
    Asignal = sum(square(array_signal))

    print('Asignal', Asignal)
    print('Anoise', Anoise)
    print('SNR', 10 * log10(Asignal / Anoise))


if __name__ == "__main__":
    run()
