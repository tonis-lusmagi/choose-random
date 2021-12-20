#!/usr/bin/env python3

import argparse
import random
from pathlib import Path


class ParseInputFiles():

    def __init__(self, participantsFile, prizeFile):
        self.participantsList = []
        self.prizeList = []
        self._parse_participantsfile(participantsFile)
        self._parse_prizefile(prizeFile)
        self._match(self.participantsList, self.prizeList)


    def _parse_participantsfile(self, participantsFile):
        with participantsFile.open() as f:
            for rawLine in self._yield_lines(f.readlines()):
                line = rawLine
                self.participantsList.append(line)
            random.shuffle(self.participantsList)


    def _parse_prizefile(self, prizeFile):
        with prizeFile.open() as f:
            for rawLine in self._yield_lines(f.readlines()):
                line = rawLine
                self.prizeList.append(line)
            random.shuffle(self.prizeList)


    def _yield_lines(self, iterable):
        currentLine = []
        for rawLine in iterable:
            string = rawLine.strip()
            currentLine.append(string)
            if not string.endswith("\\"):
                yield "\n".join(currentLine)
                currentLine = [] 


    def _match(self, participantsList, prizeList):
        for i in range(len(participantsList)):
            random.shuffle(participantsList)
            random.shuffle(prizeList)
            resultPair = (participantsList.pop(), prizeList.pop())
            print("{}:    \t{}".format(resultPair[0], resultPair[1]))


def generate(args):
    participantsFile = Path(args.participantsfile)
    prizeFile = Path(args.prizefile)
    ParseInputFiles(participantsFile, prizeFile)


def parseargs():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    generate_parser = subparser.add_parser('generate', help='Generate the results')
    generate_parser.add_argument('--participantsfile')
    generate_parser.add_argument('--prizefile')
    generate_parser.set_defaults(func=generate)

    return parser.parse_args()


def main():
    args = parseargs()

    if hasattr(args, "func"):
        args.func(args)
    else:
        print("Command not defined in argparser")
        exit(1)


if __name__ == "__main__":
    main()