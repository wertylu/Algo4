from typing import List

from write_read_helper.read_file import read_csv
from write_read_helper.write import create_write_to_file
from algo_word_chain.algo import find_max_chain


def main(word_list: List[str]) -> int:
    word_list.sort(key=lambda x: len(x))
    words_dictionary = {}
    return find_max_chain(word_list, words_dictionary)


if __name__ == '__main__':
    file = 'input.csv'
    create_write_to_file(main(read_csv(file)))
    print(main(read_csv(file)))
