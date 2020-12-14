# **Dependency Practical - 04**

## **Results**
### **Command**
#### I used the following commands to train, parse, and inspect my model. 

```
./udpipe/src/udpipe --tokenizer none --tagger none --train es.udpipe < UD_Spanish-GSD/es_gsd-ud-train.conllu

udpipe --parse es.udpipe < UD_Spanish-GSD/es_gsd-ud-test.conllu > TESTINGOUT.conllu

python3 conll17_ud_eval.py --verbose UD_Spanish-GSD/es_gsd-ud-test.conllu TESTINGOUT.conllu
```

### **Results of Conllu Evaluation**

```
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
```



## **1st Error - sent_id = es-dev-003-s421**
### *Caudete, con gran desarrollo industrial, cuenta con empresas importantes del sector del vidrio o los transportes.*

```
1       Caudete caudete PROPN   _       _       5       nsubj   _       SpaceAfter=No
2       ,       ,       PUNCT   _       _       5       punct   _       _
3       con     con     ADP     _       _       5       case    _       _
4       gran    gran    ADJ     _       Number=Sing     5       amod    _       _
5       desarrollo      desarrollo      NOUN    _       Gender=Masc|Number=Sing 0       root    _       _
6       industrial      industrial      ADJ     _       Number=Sing     5       amod    _       SpaceAfter=No
7       ,       ,       PUNCT   _       _       8       punct   _       _
8       cuenta  contar  NOUN    _       Number=Sing     5       appos   _       _
9       con     con     ADP     _       _       10      case    _       _
10      empresas        empresa NOUN    _       Gender=Fem|Number=Plur  8       nmod    _       _
11      importantes     importante      ADJ     _       Number=Plur     10      amod    _       _
12-13   del     _       _       _       _       _       _       _       _
12      de      de      ADP     _       _       14      case    _       _
13      el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       14      det     _       _
14      sector  sector  NOUN    _       Gender=Masc|Number=Sing 10      nmod    _       _
15-16   del     _       _       _       _       _       _       _       _
15      de      de      ADP     _       _       17      case    _       _
16      el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       17      det     _       _
17      vidrio  vidrio  NOUN    _       Gender=Masc|Number=Sing 14      nmod    _       _
18      o       o       CCONJ   _       _       20      cc      _       _
19      los     el      DET     _       Definite=Def|Gender=Masc|Number=Plur|PronType=Art       20      det     _       _
20      transportes     transporte      NOUN    _       Gender=Masc|Number=Plur 14      conj    _       SpaceAfter=No
21      .       .       PUNCT   _       _       5       punct   _       _
```

#### This sentence does not contain a verb due to an incorrect labelling of *cuenta* as a noun. Here, this should be a verb. Because of that, it should not be considered as an appos to *Caudete*, but rather a root. It should also be given the head ID number of 0, instead of *desarrollo*.




## **2nd error - sent_id = es-dev-003-s417**
### *Su actuación recibió buenas reseñas, al igual que el filme.*

```
1       Su      su      DET     _       Number=Sing|Person=3|Poss=Yes|PronType=Prs      2       det     _       _
2       actuación       actuación       NOUN    _       Gender=Fem|Number=Sing  3       nsubj   _       _
3       recibió recibir VERB    _       Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin   0       root    _       _
4       buenas  buen    ADJ     _       Gender=Fem|Number=Plur  5       amod    _       _
5       reseñas reseño  NOUN    _       Gender=Fem|Number=Plur  3       obj     _       SpaceAfter=No
6       ,       ,       PUNCT   _       _       3       punct   _       _
7-8     al      _       _       _       _       _       _       _       _
7       a       a       ADP     _       _       12      case    _       _
8       el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       9       det     _       _
9       igual   igual   ADJ     _       Number=Sing     7       fixed   _       _
10      que     que     CCONJ   _       _       7       fixed   _       _
11      el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       12      det     _       _
12      filme   filme   NOUN    _       Gender=Masc|Number=Sing 3       nmod    _       SpaceAfter=No
13      .       .       PUNCT   _       _       3       punct   _       _
```

#### In this sentence, the wrong noun is attributed to the verb *recibio*. The principal noun of the phrase should  be *actuacion*. Instead, the dependency tree has labeled the noun *filme* as the main noun. 




## **3rd error - sent_id = es-dev-003-s425**
### *Su ciudad capital es la ciudad de Dodoma, que es la capital del país.*

```
1       Su      su      DET     _       Number=Sing|Person=3|Poss=Yes|PronType=Prs      2       det     _       _
2       ciudad  ciudad  NOUN    _       Gender=Fem|Number=Sing  6       nsubj   _       _
3       capital capital NOUN    _       Number=Sing     2       appos   _       _
4       es      ser     AUX     _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   6       cop     _       _
5       la      el      DET     _       Definite=Def|Gender=Fem|Number=Sing|PronType=Art        6       det     _       _
6       ciudad  ciudad  NOUN    _       Gender=Fem|Number=Sing  0       root    _       _
7       de      de      ADP     _       _       8       case    _       _
8       Dodoma  dodoma  PROPN   _       _       6       nmod    _       SpaceAfter=No
9       ,       ,       PUNCT   _       _       13      punct   _       _
10      que     que     SCONJ   _       _       13      mark    _       _
11      es      ser     AUX     _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   13      cop     _       _
12      la      el      DET     _       Definite=Def|Gender=Fem|Number=Sing|PronType=Art        13      det     _       _
13      capital capital NOUN    _       Gender=Fem|Number=Sing  6       acl:relcl       _       _
14-15   del     _       _       _       _       _       _       _       _
14      de      de      ADP     _       _       16      case    _       _
15      el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       16      det     _       _
16      país    país    NOUN    _       Gender=Masc|Number=Sing 13      nmod    _       SpaceAfter=No
17      .       .       PUNCT   _       _       6       punct   _       _
```

#### In this sentence, capital is listed as a noun and later tagged as an appositional modifier to the noun, *ciudad*. Grammatically, however, the word *capital* can exist as a noun (as it does in the second phrase of this sentence) or as an adjective. I believe this should have been tagged as amod for adjectival modifier in this case.





## **4th error - sent_id = es-dev-003-s435**
### *La densidad de población era de 41,76 hab. / km².*

```
1       La      el      DET     _       Definite=Def|Gender=Fem|Number=Sing|PronType=Art        2       det     _       _
2       densidad        densidad        NOUN    _       Gender=Fem|Number=Sing  5       nsubj   _       _
3       de      de      ADP     _       _       4       case    _       _
4       población       población       NOUN    _       Gender=Fem|Number=Sing  2       nmod    _       _
5       era     ser     VERB    _       Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin    0       root    _       _
6       de      de      ADP     _       _       8       case    _       _
7       41,76   41,76   NUM     _       NumType=Card    8       nummod  _       _
8       hab     hab     NOUN    _       _       5       obl     _       SpaceAfter=No
9       .       .       PUNCT   _       _       8       punct   _       _
10      /       /       PUNCT   _       _       8       punct   _       _
11      km      km      SYM     _       _       8       dep     _       SpaceAfter=No
12      ²       ²       SYM     _       _       11      dep     _       SpaceAfter=No
13      .       .       PUNCT   _       _       5       punct   _       _
```

#### In this sentence, there was a limitation in the parser in that it did not know how to tag km², and tagged dep by default. 





## **5th error - sent_id = es-dev-003-s449**
### *Además se acuso a las burocracias medicas y el gobierno de encubrimiento.*

```
1       Además  además  ADV     _       _       3       advmod  _       _
2       se      él      PRON    _       Case=Acc,Dat|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes      3       iobj    _       _
3       acuso   aconer  VERB    _       Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin   0       root    _       _
4       a       a       ADP     _       _       6       case    _       _
5       las     el      DET     _       Definite=Def|Gender=Fem|Number=Plur|PronType=Art        6       det     _       _
6       burocracias     burocracia      NOUN    _       Gender=Fem|Number=Plur  3       obl     _       _
7       medicas medico  ADJ     _       Gender=Fem|Number=Plur  6       amod    _       _
8       y       y       CCONJ   _       _       10      cc      _       _
9       el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       10      det     _       _
10      gobierno        gobierno        NOUN    _       Gender=Masc|Number=Sing 3       conj    _       _
11      de      de      ADP     _       _       12      case    _       _
12      encubrimiento   encubrimiento   NOUN    _       Gender=Masc|Number=Sing 10      nmod    _       SpaceAfter=No
13      .       .       PUNCT   _       _       3       punct   _       _
```

#### The dependency taggers here are off in that *gobierno* is labeled as a conjunct of *acuso*, but *burocracias* is not labeled as a conjunct along with *gobierno*. 





## **6th error - sent_id = es-dev-003-s468**
### *Esta ciudad producía uranio enriquecido para el programa nuclear soviético.*

```
1       Esta    este    DET     _       Gender=Fem|Number=Sing|PronType=Dem     2       det     _       _
2       ciudad  ciudad  NOUN    _       Gender=Fem|Number=Sing  3       nsubj   _       _
3       producía        producir        VERB    _       Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin    0       root    _       _
4       uranio  uranio  NOUN    _       Gender=Masc|Number=Sing 3       obj     _       _
5       enriquecido     enriquecido     VERB    _       Gender=Masc|Number=Sing|VerbForm=Part   4       acl     _       _
6       para    para    ADP     _       _       8       case    _       _
7       el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       8       det     _       _
8       programa        programa        NOUN    _       Gender=Masc|Number=Sing 5       obl     _       _
9       nuclear nuclear ADJ     _       Number=Sing     8       amod    _       _
10      soviético       soviético       ADJ     _       Gender=Masc|Number=Sing 8       amod    _       SpaceAfter=No
11      .       .       PUNCT   _       _       3       punct   _       _
```

#### In this sentence, *enriquecido* is mislabeled as a verb instead of an adjective. Because of this, it's tagged as being an acl, or a clausal modifier of a noun. Instead, it should be tagged as an adjective to *uranio*, and thus an amod (an adjectival modifier) of *uranio*. 




## **7th error - sent_id = es-dev-004-s2** 
### *Es un queso de pasta no cocida, prensada o no.*

```
1       Es      ser     AUX     _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   3       cop     _       _
2       un      uno     DET     _       Definite=Ind|Gender=Masc|Number=Sing|PronType=Art       3       det     _       _
3       queso   queso   NOUN    _       Gender=Masc|Number=Sing 0       root    _       _
4       de      de      ADP     _       _       5       case    _       _
5       pasta   pasta   NOUN    _       Gender=Fem|Number=Sing  3       nmod    _       _
6       no      no      ADV     _       _       7       advmod  _       _
7       cocida  cocido  ADJ     _       Gender=Fem|Number=Sing|VerbForm=Part    3       amod    _       SpaceAfter=No
8       ,       ,       PUNCT   _       _       9       punct   _       _
9       prensada        prensado        ADJ     _       Gender=Fem|Number=Sing|VerbForm=Part    7       conj    _       _
10      o       o       CCONJ   _       _       11      cc      _       _
11      no      no      ADV     _       _       3       conj    _       SpaceAfter=No
12      .       .       PUNCT   _       _       3       punct   _       _
```

#### *Es* in this sentence is considered to be an auxiliary verb. Thus, *queso* is indicated as having a head ID of 0. Given that *Es* is not appearing imediately before a participle, this should be labeled as verb and have a head ID of 0 instead of *queso*. This would change the structure of the depenency tree. 




## **8th error - sent_id = es-dev-004-s4**
### *Del total de la población el 1.22 % eran hispanos o latinos de cualquier raza.*

```
1       Del     del     ADP     _       _       2       case    _       _
2       total   total   NOUN    _       Gender=Masc|Number=Sing 10      nmod    _       _
3       de      de      ADP     _       _       5       case    _       _
4       la      el      DET     _       Definite=Def|Gender=Fem|Number=Sing|PronType=Art        5       det     _       _
5       población       población       NOUN    _       Gender=Fem|Number=Sing  2       nmod    _       _
6       el      el      DET     _       Definite=Def|Gender=Masc|Number=Sing|PronType=Art       8       det     _       _
7       1.22    1.22    NUM     _       NumType=Card    8       nummod  _       _
8       %       %       SYM     _       _       10      nsubj   _       _
9       eran    ser     AUX     _       Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin    10      cop     _       _
10      hispanos        hispano ADJ     _       Gender=Masc|Number=Plur 0       root    _       _
11      o       o       CCONJ   _       _       12      cc      _       _
12      latinos latino  NOUN    _       Gender=Masc|Number=Plur 10      conj    _       _
13      de      de      ADP     _       _       15      case    _       _
14      cualquier       cualquiera      DET     _       Number=Sing|PronType=Ind        15      det     _       _
15      raza    raza    NOUN    _       Gender=Fem|Number=Sing  10      nmod    _       SpaceAfter=No
16      .       .       PUNCT   _       _       10      punct   _       _
```

#### Similar to the previous error, I also believe that the use of *ser* as *eran* in this sentence was mislabeled as an auxiliary verb. Because of this, the noun following it, *hispanos* was given the head ID of 0 and labeled as the root. This seems odd, as even if *eran* were an auxiiary verb here, *poblacion* should be the root, not hispanos. So the dependency relations are a bit off in this sentence.




## **9th error - sent_id = es-dev-004-s17**
### *La película consiste en once historias cortas que parten de tomar café y fumar cigarrillos como argumento en común.*

```
1       La      el      DET     _       Definite=Def|Gender=Fem|Number=Sing|PronType=Art        2       det     _       _
2       película        película        NOUN    _       Gender=Fem|Number=Sing  3       nsubj   _       _
3       consiste        consistir       VERB    _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   0       root    _       _
4       en      en      ADP     _       _       6       case    _       _
5       once    once    NUM     _       Number=Plur|NumType=Card        6       nummod  _       _
6       historias       historia        NOUN    _       Gender=Fem|Number=Plur  3       obl     _       _
7       cortas  corta   ADJ     _       Gender=Fem|Number=Plur  6       amod    _       _
8       que     que     SCONJ   _       _       9       mark    _       _
9       parten  partir  VERB    _       Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin   6       acl:relcl       _       _
10      de      de      ADP     _       _       11      mark    _       _
11      tomar   tomar   VERB    _       VerbForm=Inf    9       advcl   _       _
12      café    café    NOUN    _       Gender=Masc|Number=Sing 11      obj     _       _
13      y       y       CCONJ   _       _       14      cc      _       _
14      fumar   fumar   VERB    _       VerbForm=Inf    3       conj    _       _
15      cigarrillos     cigarrillo      NOUN    _       Gender=Masc|Number=Plur 14      obj     _       _
16      como    como    ADP     _       _       17      case    _       _
17      argumento       argumento       NOUN    _       Gender=Masc|Number=Sing 3       obl     _       _
18      en      en      ADP     _       _       19      case    _       _
19      común   común   ADJ     _       Gender=Masc|Number=Sing 3       amod    _       SpaceAfter=No
20      .       .       PUNCT   _       _       3       punct   _       _
```

#### The levels of dependency in this tree in general seem to be off. Several are described as their relation to the main verb, *consiste*, insted of their relation to sub-levels of dependency. For example, *comun* is labeled as an adjectival modifier of *consiste* instead of the noun *argumento*.




## **10th error - sent_id = es-dev-004-s64**
### *Lo que tenéis que hacer es pagar a la gente y no engañar tanto.*

```
1       Lo      él      PRON    _       Case=Acc|Gender=Masc|Number=Sing|Person=3|PrepCase=Npr|PronType=Prs     7       nsubj   _       _
2       que     que     SCONJ   _       _       5       mark    _       _
3       tenéis  tener   AUX     _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   5       aux     _       _
4       que     que     CCONJ   _       _       3       fixed   _       _
5       hacer   hacer   VERB    _       VerbForm=Inf    1       acl:relcl       _       _
6       es      ser     AUX     _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   1       cop     _       _
7       pagar   pagar   VERB    _       VerbForm=Inf    0       root    _       _
8       a       a       ADP     _       _       10      case    _       _
9       la      el      DET     _       Definite=Def|Gender=Fem|Number=Sing|PronType=Art        10      det     _       _
10      gente   gente   NOUN    _       Gender=Fem|Number=Sing  7       obj     _       _
11      y       y       CCONJ   _       _       13      cc      _       _
12      no      no      ADV     _       Polarity=Neg    13      advmod  _       _
13      engañar engañar VERB    _       VerbForm=Inf    7       conj    _       _
14      tanto   tanto   PRON    _       NumType=Card|PronType=Dem       13      obj     _       SpaceAfter=No
15      .       .       PUNCT   _       _       7       punct   _       _
```

#### In this sentence, *pagar* is considered the root, labeled with a head ID of 0. It seems that this is incorrect, considering that *pagar* and *enganar* should be conjuncts of one another, and clausal complements of the verb *hacer*, which should be the root of this sentence.

