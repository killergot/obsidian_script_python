import os

from src.FileClasses.FileSetter import FileSetter
from src.FileClasses.Searcher import SearcherAllFiles
from src.lexicon.lexicon import LEXICON_RU
from src.logger.logger import init_log

from pathlib import Path
import logging

import argparse

if __name__ == '__main__':
    os.makedirs('./output', exist_ok=True)
    parser = argparse.ArgumentParser(description=LEXICON_RU['/help'])
    parser.add_argument('source_file',
                        help=LEXICON_RU['source_file'])

    # folder in this project
    default_output = Path(__file__).resolve().parent.joinpath('output')

    parser.add_argument('-o', '--output',
                        help=LEXICON_RU['--output'],
                        default=default_output)
    parser.add_argument('--delete',
                        help=LEXICON_RU['--delete'], action='store_true')
    parser.add_argument('--folder',
                        help=LEXICON_RU['--folder'], action='store_true')
    parser.add_argument('--verbose',
                        help=LEXICON_RU['--verbose'], action='store_true')
    parser.add_argument('--main_path',
                        help=LEXICON_RU['--main_path'], default=None)
    args = parser.parse_args()



    searcher = SearcherAllFiles()
    links = searcher.searchIn(Path(args.source_file))
    if args.verbose:
        init_log(logging.DEBUG)
    else:
        init_log(logging.INFO)

    log = logging.getLogger(__name__)

    log.debug(default_output)
    log.debug(links)
    FileSetter.file_transfer(links,
                             args.output,
                             del_flag=args.delete,
                             folder_flag=args.folder)