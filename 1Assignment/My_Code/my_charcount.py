import os                                       # Manipulate path of my PC
import argparse                                 # Make --help description
import logging                                  # Make Debug and Warning 
import time                                     # Misure time of process
import book_features
logging.basicConfig(level=logging.INFO)         # Definisce il livello di log

_description = 'Measure the releative frequencies of letters in a text file'

def process(file_path,inst,sk,stats):
    """Main processing method.
    """
    start = time.time()                         # Start measuring time

    ##################
    #  Sanity check  #
    ##################
    assert file_path.endswith('.txt'), "Not a txt file"
    assert os.path.isfile(file_path), "Wrong path"
    test_inst = (inst == "y" or inst == "n")            # 3 test per i parametri 
    test_sk = (sk == "y" or sk == "n")                  #   che richiedono
    test_stats = (stats == "y" or stats == "n")         #       y/n
    assert  test_inst and test_sk and test_stats, "Can insert only y/n"

    ###############
    #  Open File  #
    ###############
    data = book_features.extract(file_path,sk)

    ############################
    #  Prepare the dictionary  #
    ############################
    letters = 'abcdefghijklmnopqrstuvwxyz'      # Lettere da analizzare
    freq_dict = {}                              # Dizionario
    for ch in letters:                          # Inizializzo a zero tutto
        freq_dict[ch] = 0

    for ch in data.lower():                     # Lower mette tutto minuscolo
        if ch in letters:                       # Metto frequenze non normalizzate
            freq_dict[ch] += 1                  # nel dizionario.

    num_chars = float(sum(freq_dict.values()))  # Normalizzo solo su lettere conteggiate
    for ch in letters:                          # Applico normalizzazione al dizionario
        freq_dict[ch] /= num_chars

    #######################
    #  Print the results  #
    #######################
    book_features.print_freq(freq_dict)         # Print Result with ascii istogram
    book_features.print_stats(data,stats)       # Print the stats of the book
    end = time.time()                           # Stop measuring time
    book_features.istogram(inst,freq_dict)      # Print Instrogram from matplotlib
    logging.info('Elapsed Time: %f sec', end-start)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input file')
    parser.add_argument('--inst', type=str , default='n', help='Add matplot istogram [y/n]')
    parser.add_argument('--skip', type=str , default='n', help='Skip preamble and license [y/n]')
    parser.add_argument('--stats', type=str , default='n', help='Print basic book stats [y/n]')
    args = parser.parse_args()
    process(args.infile,args.inst,args.skip,args.stats)
