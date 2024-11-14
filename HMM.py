

import random
import argparse
import codecs
import os
import numpy

# Sequence - represents a sequence of hidden states and corresponding
# output variables.

class Sequence:
    def __init__(self, stateseq, outputseq):
        self.stateseq  = stateseq   # sequence of states
        self.outputseq = outputseq  # sequence of outputs
    def __str__(self):
        return ' '.join(self.stateseq)+'\n'+' '.join(self.outputseq)+'\n'
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return len(self.outputseq)

# HMM model
class HMM:
    def __init__(self, transitions={}, emissions={}):
        """creates a model from transition and emission probabilities
        e.g. {'happy': {'silent': '0.2', 'meow': '0.3', 'purr': '0.5'},
              'grumpy': {'silent': '0.5', 'meow': '0.4', 'purr': '0.1'},
              'hungry': {'silent': '0.2', 'meow': '0.6', 'purr': '0.2'}}"""
        self.transitions = transitions
        self.emissions = emissions

    ## part 1 - you do this.
    def load(self, basename):
        """reads HMM structure from transition (basename.trans),
        and emission (basename.emit) files,
        as well as the probabilities."""
        self.transitions = {}
        with open(f"{basename}.trans", "r") as file_trans:
            for line in file_trans:
                parts = line.strip().split()
                if parts[0] not in self.transitions:
                    self.transitions[parts[0]] = {}
                self.transitions[parts[0]][parts[1]] = float(parts[2])

        self.emissions = {}
        with open(f"{basename}.emit", "r") as file_emit:
            for line in file_emit:
                parts = line.strip().split()
                if parts[0] not in self.emissions:
                    self.emissions[parts[0]] = {}
                self.emissions[parts[0]][parts[1]] = float(parts[2])


   ## you do this.
    def generate(self, n):
        """return an n-length Sequence by randomly sampling from this HMM."""
        curr_state = random.choices(list(self.transitions['#'].keys()), weights=list(self.transitions['#'].values()))[0]
        stateseq = [curr_state]
        outputseq = []

        for _ in range(n):
            if curr_state in self.emissions:
                emission = random.choices(list(self.emissions[curr_state].keys()), weights=list(self.emissions[curr_state].values()))[0]
                outputseq.append(emission)

            if curr_state in self.transitions:
                next_state = random.choices(list(self.transitions[curr_state].keys()), weights=list(self.transitions[curr_state].values()))[0]
                stateseq.append(next_state)
                curr_state = next_state
            else:
                break

        return Sequence(stateseq, outputseq)

    def forward(self, sequence):
        pass
    ## you do this: Implement the Viterbi algorithm. Given a Sequence with a list of emissions,
    ## determine the most likely sequence of states.






    def viterbi(self, sequence):
        pass
    ## You do this. Given a sequence with a list of emissions, fill in the most likely
    ## hidden states using the Viterbi algorithm.


def main():
    p = argparse.ArgumentParser()
    p.add_argument("basename", help="HMM file name without the extension")
    p.add_argument("--generate", type=int, help="input length")
    args = p.parse_args()

    h = HMM()
    h.load(args.basename)

    if args.generate:
        sequence = h.generate(args.generate)
        print(sequence)

if __name__ == "__main__":
    main()




