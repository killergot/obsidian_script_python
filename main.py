from src.FileClasses.FileSetter import FileSetter
from src.FileClasses.Searcher import SearcherAllFiles
from src.lexicon.lexicon import LEXICON_RU

from pathlib import Path
import logging

import argparse

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,  #(DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
               '%(lineno)d - %(name)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description=LEXICON_RU['/help'])
    parser.add_argument('source_file',
                        help=LEXICON_RU['source_file'])

    # folder in this project
    default_output = Path(__file__).resolve().parent.joinpath('output')
    log.debug(default_output)

    parser.add_argument('-o', '--output',
                        help=LEXICON_RU['--output'],
                        default=default_output)
    parser.add_argument('--delete',
                        help=LEXICON_RU['--delete'], action='store_true')
    parser.add_argument('--folder',
                        help=LEXICON_RU['--folder'], action='store_true')
    parser.add_argument('--verbose',
                        help=LEXICON_RU['--verbose'], action='store_true')
    args = parser.parse_args()

    searcher = SearcherAllFiles()
    links = searcher.searchIn(args.source_file)
    if args.verbose:
        log.debug(links)
    FileSetter.file_transfer(links,
                             args.output,
                             del_flag=args.delete,
                             folder_flag=args.folder)