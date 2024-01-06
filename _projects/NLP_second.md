---
layout: page
title: Grammar Checker
description: "We write a grammar and a parser to parse the POS tag sequence."
importance: 4
category: CMPUT 461 - Introduction to Natural Language Processing (NLP)
---

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/NLP-Grammar-Checker)

## Data
Input data: sentences with POS tags
  The input is a tsv (tab-separated values) file like the sample:
  ```
  |id|label|sentence|pos|
  | -|-----|--------|---|
  |73|0|Many thanks in advance for your cooperation .| JJ NNS IN NN IN PRP$ NN .| 74| 1| At that moment we saw the bus to come .|IN DT NN PRP VBD DT NN TO VB .|
  ```
  <br>
The id column is the unique id for each sentence. The label column indicates whether a sentence contains grammar errors (1 means having errors and 0 means error-free). The pos column contains the POS tags for each token in the sentence, also separated by a single space.

The POS tags follow the Penn Treebank (PTB) tagging scheme, described [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
## Tasks

<h3> Task 1: Building a toy grammar</h3>
  <ul>
  <li> We wrote a toy CFG for English in NLTK’s .cfg format. </li>
  </ul>
<h3> Task 2: Constituency parsing</h3>
  - We used the chart parser from NLTK to parse each of the POS sequences in the dataset with the toy grammar we wrote in task 1. We stored results in a TSV  file with three columns:

|Column name|Description|
| --------- | --------- |
|id|The id of the input sentence.|ground_truth|The ground truth label of the input sentence, copied from the dataset. |
|prediction|1 if the sentence has grammar errors, 0 if not. In other words, whether the POS sequence can be parsed successfully with your grammar and parser.|

### Task 3: Evaluation and error analysis
- We evaluate the performance of our grammar checker by calculating its precision and recall on the data available to us. To do that, we compared the prediction of our system on a given sentence and its corresponding label in the dataset. 

# Report and Results
Further details and results can be found [here](https://github.com/Leen-Alzebdeh/NLP-Grammar-Checker/blob/main/REPORT.md)

# Contributors

Leen Alzebdeh  @Leen-Alzebdeh

Sukhnoor Khehra @Sukhnoor-K

# Resources Consulted

[Penn Treebank P.O.S. Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

Jurafsky, D., &amp; Martin, J. H. (2009). Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition. Pearson Prentice Hall.

GitHub Copilot

## Libraries

We run this project using standard Python libraries csv, sys, nltk.

# Instructions to execute code

1. Ensure Python is installed, as well as the Python Standard Library.

2. Ensure the library nltk is installed, it can be installed using the following command: 

`pip install --user -U nltk`

3. Ensure you have input data in the format outlined above and in a file 'data/train.tsv' 


Example usage: use the following command in the current directory.

`python3 src/main.py data/train.tsv grammars/toy.cfg output/train.tsv`


