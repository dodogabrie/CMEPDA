import os                                       # Manipulate path of my PC
import argparse                                 # Make --help description
import logging                                  # Make Debug and Warning 
import time                                     # Misure time of process
import my_features
logging.basicConfig(level=logging.INFO)         # Definisce il livello di log


_description = 'Measure the releative frequencies of letters in a text file'

def process(file_path,inst,sk,stats):
    """Main processing method.
    """
    start = time.time()                         # Start measuring time
    # Basic sanity check: make sure that the file_argument points to an
    # existing text file.
    assert file_path.endswith('.txt'), "Not a txt file"
    assert os.path.isfile(file_path), "Wrong path"
    test_inst = (inst == "y" or inst == "n")
    test_sk = (sk == "y" or sk == "n")
    test_stats = (stats == "y" or stats == "n")
    assert  test_inst and test_sk and test_stats, "Can insert only y/n"

    # Open the input file (note that we are taking advantage of context
    # management, using a with statement).
    data = my_features.extract(file_path,sk)

    # Prepare a dictionary to hold the letter frequencies, and initialize
    # all the counts to zero.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    freq_dict = {}                              # Tabella Hash
    for ch in letters:                          # Inizializzo a zero tutto
        freq_dict[ch] = 0

    # Loop over the input data (note the call to the lower() string method
    # that is casting everything in lower case).
    for ch in data.lower():                     # Lower mette tutto minuscolo
        if ch in letters:
            freq_dict[ch] += 1

    # One last loop over the letters to normalize the occurrences to 1.
    num_chars = float(sum(freq_dict.values()))
    for ch in letters:
        freq_dict[ch] /= num_chars

    # We're done---print the glorious output. (And here it is appropriate to
    # use print() instead of logging.)
    my_features.print_freq(freq_dict)                        # Print Result with ascii istogram
    end = time.time()                           # Stop measuring time
    my_features.istogram(inst,freq_dict)                      # Print Instrogram from matplotlib
    logging.info('Elapsed Time: %f sec', end-start)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input file')
    parser.add_argument('--inst', type=str , default='n', help='Add matplot istogram [y/n]')
    parser.add_argument('--skip', type=str , default='n', help='Skip preamble and license [y/n]')
    parser.add_argument('--stats', type=str , default='n', help='Print basic book stats [y/n]')
    args = parser.parse_args()
    process(args.infile,args.inst,args.skip,args.stats)
