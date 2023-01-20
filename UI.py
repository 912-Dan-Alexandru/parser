from grammar import Grammar
from tree import Tree
from parserr import Parser


class UI:

    def __init__(self):
        self.grammar = None
        self.parser = None

    def run(self):
        self.evaluateG1()

    def readG1(self):
        self.g1 = Grammar.fromFile('g1.txt')
        print('Read g1')


    def readSequence(self, fname):
        sequence = ""
        with open(fname, 'r') as fin:
            for line in fin.readlines():
                sequence += line.strip() + " "
        return sequence.strip()

    def evaluateG1(self):
        self.readG1()
        self.p1 = Parser(self.g1)
        print(self.p1.firstSet)
        print(self.p1.followSet)
        for k in self.p1.table.keys():
            print(k, '->', self.p1.table[k])
        result = self.p1.evaluateSequence(self.readSequence('seq.txt'))
        if result is None:
            print("Sequence not accepted")
        else:
            print(result)
            t = Tree(self.g1)
            t.build(result.strip().split(' '))
            t.print_table()

