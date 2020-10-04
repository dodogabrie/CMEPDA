import os                                       # Manipulate path of my PC
import argparse                                 # Make --help description
import logging                                  # Make Debug and Warning 
logging.basicConfig(level=logging.INFO)         # Definisce il livello di log


_description = 'Measure the releative frequencies of letters in a text file'



def process(file_path):
    """Main processing method.
    """
    # Basic sanity check: make sure that the file_argument points to an
    # existing text file.
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    logging.info('Opening input file "%s"', file_path)
    with open(file_path) as input_file:             # Apre e chiude file  
        data = input_file.read()
    logging.info('Done. %d character(s) found.', len(data))
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
    for ch, freq in freq_dict.items():
        print('{}: {:.3f}%'.format(ch, freq * 100.))




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input file')
    args = parser.parse_args()
    process(args.infile)
