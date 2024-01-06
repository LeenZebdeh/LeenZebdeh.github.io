---
layout: page
title: POS Taggers
description: "We compare, and contrast two part-of-speech taggers’ (HMM and Brill) performance on in-domain and out-of-domain text samples. "
importance: 2
category: CMPUT 461 - Introduction to Natural Language Processing (NLP)
---

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/NLP-Taggers)

## Data
Input data: POS tagged sentences from [The Georgetown University Multilayer Corpus (GUM)](http://corpling.uis.georgetown.edu/gum/)

  The training and test files have a .txt format. Each line has a word and POS tag and each sentence is separated by an empty line.Below is an example of the structure: 
  ```
  Always	 RB
  wear VB
  ballet NN
  slippers NNS
  . .
  
  Stretch VB
  your PRP$
  ...
  ```
The training data is under `data/train.txt` <br>
The in-domain test data is under `data/test.txt` <br>
The out-of-domain test data is under `data/test_ood.txt` <br>
The POS tags follow the Penn Treebank (PTB) tagging scheme, described [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
## Tasks
### Task 1: Train and Tune the Taggers
  - We trained the HMM and Brill tagger on the training set and tuned each to find the best performance. 

### Task 2: Compare results
  - We measured the performance of the taggers on in-domain and out-of-domain test sets.

### Output
The program’s output file is a .txt file in the same format as the input training file. 

# Report and Results
Further details and results can be found [here](https://github.com/Leen-Alzebdeh/NLP-Taggers/blob/main/REPORT.md)

# Contributors

Leen Alzebdeh  @Leen-Alzebdeh

Sukhnoor Khehra @Sukhnoor-K

# Resources Consulted

- https://gist.github.com/blumonkey/007955ec2f67119e0909
 - https://stats.stackexchange.com/questions/366552/nlp-various-probabilities-estimators-in-nltk
 - https://www.nltk.org/_modules/nltk/tag/hmm.html
 - https://gist.github.com/h-alg/4ec991f90a682c6d0a0b
 - https://www.nltk.org/_modules/nltk/tag/brill.html
 - https://www.nltk.org/api/nltk.tag.brill_trainer.html
 - Github Copilot

## Libraries

* `main.py L:4, 13` used `argparse` for extracting command line args.
* `main.py L:8, 104` used `os` for creating directory of output.
  
# Instructions to execute code

1. Ensure Python is installed, as well as the Python Standard Library. To download Python if it is not already installed, follow the instructions on the following website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Ensure you have training and test input data in the format outlined above and in a directory 'data/'
Example usage: use the following commands in the current directory.

For using the HMM tagger on in-domain data:
`python3 src/main.py --tagger hmm --train data/train.txt --test data/test.txt --output output/test_hmm.txt`

For using the HMM tagger in out-of-domain data:
`python3 src/main.py --tagger hmm --train data/train.txt --test data/test_ood.txt --output output/test_ood_hmm.txt`

For using the Brill tagger on in-domain data:
`python3 src/main.py --tagger brill --train data/train.txt --test data/test.txt --output output/test_brill.txt`

For using the Brill tagger on out-of-domain data:
`python3 src/main.py --tagger brill --train data/train.txt --test data/test_ood.txt --output output/test_ood_brill.txt`

