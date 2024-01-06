---
layout: page
title: Language Models
description: "We create n-gram language models that quantify the likelihood of various sound sequences occurring in the English language."
importance: 3
category: CMPUT 461 - Introduction to Natural Language Processing (NLP)
---

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/NLP-LMs)

## Data
Input data: We leverage the transformed data from the [data cleaning task](https://github.com/Leen-Alzebdeh/NLP-Data-Cleaning-Task).

The original data comes from [Child Language Data Exchange System (CHILDES Talkbank)](https://childes.talkbank.org/)

The data contains transcripts from oral language that represent the language that young children are exposed to in everyday settings. The transformed data is stored in .txt files.

```
NLP-LMs/
├─ transformed/
│  ├─ Bates
│  │  ├─ Free20
│  │  │  ├─ amy.txt
│  │  │  ├─ betty.txt
│  │  │  ├─ (more files)
│  │  ├─ (more directories)
│  ├─ (more directories)
```

Example of a sequence: "HH AH L OW W ER L D" (hello world)

### Data Splits
The training and dev sets should be put under `data/.` In other words, two files `data/training.txt` and `data/dev.txt` need to be in the repository.

## Tasks
<h3> Task 1: Training N-gram Models </h3>
  -  We trained n-gram language models: unigram, bigram, and trigram models using the training set described above.
<h3>Task 2: Evaluating N-gram Models</h3>
  - After building the models and implementing the smoothing techniques, we evaluated them by computing the perplexity (PPL) of the dev set.
<h3> Additional Task: KenLM </h3>
  - Use KenLM to train the same bigram and trigram models using the same training data.
    
# Report and Results
Further details and results can be found [here](https://github.com/Leen-Alzebdeh/NLP-LMs/blob/main/REPORT.md)

# Contributors

Leen Alzebdeh @Leen-Alzebdeh

Sukhnoor Khehra @Sukhnoor-K

## Resources Consulted

https://www.semanticscholar.org/paper/KenLM%3A-Faster-and-Smaller-Language-Model-Queries-Heafield/883d1d06d857a85a0e64bb19f0b17d56f2cc9d7b (Understanding KenLM challenges and limitations)

https://stackoverflow.com/questions/38151445/iterate-over-n-successive-elements-of-list-with-overlapping (For understanding overlapping)

GitHub Copilot

## Libraries

We run this project using standard Python libraries: argparse, itertools, os, random, math, sys.

# Instructions to execute code

1. Ensure Python is installed, as well as the Python Standard Library.

2. Ensure you have the transformed CHILDES input data in the format outlined above and in a directory 'Data/'
Example usage:

Use the following commands in the current directory.

For unigram:

`python3 src/main.py unigram data/training.txt data/dev.txt`

For bigram smoothed:

`python3 src/main.py bigram data/training.txt data/dev.txt --laplace`

For bigram unsmoothed:

`python3 src/main.py bigram data/training.txt data/dev.txt`

For trigram smoothed:

`python3 src/main.py trigram data/training.txt data/dev.txt --laplace`

For trigram unsmoothed:

`python3 src/main.py trigram data/training.txt data/dev.txt`

To change the text file to evaluate preplexity on, for example to evaluate on data/training.txt (for unigram):

`python3 src/main.py unigram data/training.txt data/training.txt`
