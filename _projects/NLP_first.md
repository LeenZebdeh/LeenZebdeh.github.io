---
layout: page
title: Data CLeaning Task
description: "We explore the use of regular expressions to clean input text in support of a downstream task."
importance: 5
category: CMPUT 461 - Introduction to Natural Language Processing (NLP)
---

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/NLP-Data-Cleaning-Task)

We explore the use of regular expressions to clean input text in support of a downstream task found [here](https://leenzebdeh.github.io/projects/NLP_third/).

## Data
Input data: [Child Language Data Exchange System (CHILDES Talkbank)](https://childes.talkbank.org/)

The data contains transcripts from oral language that represent the language that young children are exposed to in everyday settings. The data is stored in .cha files.
```
NLP-Data-Cleaning-Task/
├─ Data/
│  ├─ Bates
│  │  ├─ Free20
│  │  │  ├─ amy.cha
│  │  │  ├─ betty.cha
│  │  │  ├─ (more files)
│  │  ├─ (more directories)
│  ├─ (more directories)
```

## Tasks

<h3> Task 1: clean the files: </h3>
   - Convert the files to raw text and remove both the header and extraneous information. Extraneous information is any information that is not needed to support the downstream task.
<h3> Task 2:  transform the files: </h3>
   - You will transform the data so that it uses ArpaBET to represent the sounds that the text maps to. We use[ CMU's Pronunciation Dictionary](https://www.google.com/url?q=http://www.speech.cs.cmu.edu/cgi-bin/cmudict&sa=D&source=docs&ust=1703650680785817&usg=AOvVaw2B2-NioT8l2i6wmOWx3Cwk) to inform this transformation.

# Report 
Further details and justifications can be found [here](https://github.com/Leen-Alzebdeh/NLP-Data-Cleaning-Task/blob/main/REPORT.md).

# Contributors

Leen Alzebdeh  @Leen-Alzebdeh

Sukhnoor Khehra @Sukhnoor-K

# Resources Consulted

[https://www.w3schools.com/python/python_regex.asp](https://www.w3schools.com/python/python_regex.asp)

Jurafsky, D., &amp; Martin, J. H. (2009). Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition. Pearson Prentice Hall.

[CMU’s Pronunciation Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=Hello#phones)

[ARPABET](https://en.wikipedia.org/wiki/ARPABET)

[Child Language Data Exchange System (CHILDES Talkbank)](https://childes.talkbank.org/)

[https://stackoverflow.com/questions/16510017/how-to-use-regular-expressions-do-reverse-search](https://stackoverflow.com/questions/16510017/how-to-use-regular-expressions-do-reverse-search)

[https://stackoverflow.com/questions/3114252/one-liner-to-check-whether-an-iterator-yields-at-least-one-element](https://stackoverflow.com/questions/3114252/one-liner-to-check-whether-an-iterator-yields-at-least-one-element)

GitHub Copilot

### Libraries

We run this project using standard Python libraries re (regex), random, and os.

# Instructions to execute code


To run this project:
1. Ensure Python is installed, as well as the Python Standard Library. 
2. Clone the repository.
3. Ensure you have CHILDES input data in the format outlined above and in a directory 'Data/' 
4. Run the main.py file (no parameters needed).
   Run this command
   ```bash
   python3 src/main.py
   ```

Clean files can be found within the `clean/` directory found in root.

Transformed files can be found within the `transformed/` directory found in root.

