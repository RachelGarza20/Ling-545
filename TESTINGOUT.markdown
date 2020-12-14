`#`**Dependency Practical - 04**

`##`**Results**
`###`**Command**
`####` I used the following commands to train, parse, and inspect my model.

```./udpipe/src/udpipe --tokenizer none --tagger none --train es.udpipe < UD_Spanish-GSD/es_gsd-ud-train.conllu

```udpipe --parse es.udpipe < UD_Spanish-GSD/es_gsd-ud-test.conllu > TESTINGOUT.conllu

```python3 conll17_ud_eval.py --verbose UD_Spanish-GSD/es_gsd-ud-test.conllu TESTINGOUT.conllu

`###`*Results of Conllu Evaluation*

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     85.67 |     85.67 |     85.67 |     85.67
LAS        |     82.38 |     82.38 |     82.38 |     82.38
