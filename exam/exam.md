<!--
SPDX-FileCopyrightText: 2022 Michael Lodi <michael.lodi@unibo.it>
SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni2@studio.unibo.it>

SPDX-License-Identifier: CC0-1.0
-->

---

title: Lezione Tool Git
author: Daniele Tentoni
date: 17/05/2022
bibliography: exam/exam.bib

---

Esame di Didattica dell'Informatica, A.A. 2021/2022

# Changelog (se necessario)

<!--
Se questa relazione è stata già consegnata in precedenza, indicare qui

* i cambiamenti più sificativi
* dove trovare un eventuale diff (se ritenuto necessario)
* risposte a eventuali domande/commenti fatti dai docenti sulle versioni precedenti
-->

## Post esame 21/06

- incluso riferimento a gioco oh-my-git

# Inquadramento del lavoro

## Livello di scuola, classe/i, indirizzo

<!--
A chi è rivolta questa attività?

In quale specifica disciplina scolastica (o le discipline, ovviamente
l'informatica deve essere la disciplina prevalente) si colloca
l'attività?

- Per la scuola dell'infanzia / primaria / scuole \"medie\" si può fare riferimento a una delle discipline nelle Indicazioni Nazionali, nei Nuovi Scenari, e/o alla disciplina Informatica dalla Proposta CINI
- Per le scuole secondarie di secondo grado (superiori), fare riferimento ai documenti ministeriali e/o alla Proposta CINI.

Può essere---adattata---rivolta a studenti di diverse età e indirizzi?
-->

L'attività è rivolta specialmente al triennio di un istituto tecnico con indirizzo informatico, da svolgere durante le ore di Informatica o discipline annesse (Sistemi e Reti o Gestione di Progetto).

In generale, potendo tramite Git tracciare qualunque prodotto in grado di essere memorizzato su supporto informatico, l'attività può essere riadattata per poter insegnare Git ad un qualunque pubblico di studenti delle scuole superiori a cui si vuole proporre uno strumento di memorizzazione o versionamento alternativo ai classici storage fisici (pennette usb, supporti ottici ...) o cloud (Onedrive, Google Drive ...).

## Motivazione e Finalità

<!--
Perché avete scelto di realizzare questa specifica attività

Una sua brevissima descrizione generale
-->

Ho scelto di realizzare questa attività per due principali motivi:

1. La proporrei principalmente a studenti che hanno scelto il mio stesso percorso di studi alle scuole superiori, dove mi piacerebbe andare ad insegnare e dove penso che questa attività possa servire maggiormente, preparando gli studenti ad utilizzare uno dei più diffusi tools per il versionamento del codice;

2. Avendo già avuto esperienza lavorativa ho notato che gli studenti usciti da tali percorsi di studi non sono preparati abbastanza per entrare con tranquillità e rapidità dentro al mondo del lavoro. Molti non possiedono le competenze da me ritenute minime per poter lavorare in modo collaborativo neanche a piccoli progetti software interni alla mia realtà aziendale attuale.

Per tali motivi, penso che proporre agli studenti quelle che secondo me sono le competenze minime da acquisire durante il proprio percorso scolastico in tema di Versioning Control Systems e sviluppo collaborativo alla scrittura del codice sia un esercizio utile in preparazione alle future lezioni a studenti delle scuole e neo assunti interni alla mia azienda.

## Innovatività

<!--
Perché questa proposta è innovativa? Cosa è già presente su questo tema nella ricerca in Didattica dell'Informatica o nelle risorse disponibili online?
-->

Moltissime attività disponibili in rete che ho cercato non coprono gli stessi argomenti di questa. L'insieme delle competenze che vengono proposte nel seguente materiale è la scrematura di tutte quelle che io abbia mai usato nel mio ambito lavorativo fino adesso (al 2022 è il 5 anno di lavoro in un'azienda software cesenate di una ventina di dipendenti) e che penso siano assolutamente irrinunciabili per una persona neo-diplomata che voglia affacciarsi sul mondo del lavoro in ambito informatico.

Alcune delle risorse disponibili online attualmente che permettono di apprendere gli stessi concetti espressi in questo materiale didattico (e anche di più) sono:

- [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
: Ebook scaricabile dal sito ufficiale del progetto Git. Moltissimi argomenti vengono trattati, potrebbe far desistere chi invece cerca un approccio più pragmatico. Include anche un capitolo sullo strumento Github, esattamente come questo materiale didattico. Quindi a mio parere è la scelta più valida possibile per chi volesse approfondire l'argomento autonomamente a casa;

- [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
: Gioco gratuito per imparare nei primi livelli i comandi base e via via avanzando nel gioco concetti più complicati. Possibile allenamento in vista di interrogazioni e compiti in classe per gli studenti;

- [https://ohmygit.org/](https://ohmygit.org/): Altro gioco gratuito e open source scaricabile per quasi tutte le piattaforme desktop per imparare i comandi, diversamente dal precedente non offre agli studenti proprio una console, offrendo una diversa gamification;

- [https://www.atlassian.com/git](https://www.atlassian.com/git)
: Guida a Git curata da Atlassian, uno dei principali attori in gioco in tema di Sistemi di Versionamento del Codice grazie alla loro piattaforma BitBucket. Propone guide ed esercizi per imparare ad usare gli strumenti Git e Bitbucket, similmente a https://lab.github.com/ per Githubò

- [https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
: Elenco dei principali comandi di Git curata dai sopracitati collaboratori di Atlassian. [@github_learning_lab]

Un articolo accademico[^1] consultato è stato [Integrating Git into CS1/2](https://dl.acm.org/doi/10.5555/3381569.3381583)[@integrating_git],  che spiega i risultati dell'insegnamento di Git nei corsi CS 1 e 2 il quale metodo differisce dal mio nei seguenti punti:

1. usa Gitlab come hosting di repository remoti, in esecuzione su di un cluster interno alla rete d'istituto, mentre io userò invece Github, in esecuzione su Github.com, pubblicamente accessibile da chiunque. La loro scelta consente di usare uno strumento *open core*, mentre quello scelto da me invece no[^2]. La mia scelta permette agli studenti di iniziare a comporre un proprio *curriculumn* informatico da mostrare in futuro alle aziende presso cui cercheranno lavoro. Una soluzione che potrebbe risolvere la questione potrebbe essere quella di usare Gitlab.com invece di eseguirlo su un cluster interno oppure per una soluzione completamente open source si potrebbe optare per Gitea, eseguibile anche su una Raspberry Pi oppure direttamente sul loro portale ufficiale.

2. In esso la scoperta del tool git avviene diversamente da questo materiale didattico, in modo progressivo con l'avanzamento del corso, in modo tale che gli studenti vedano in separati momenti i diversi concetti. Attualmente io ho preferito la strada del fornire tutto l'insieme delle conoscenze necessarie ad uno sviluppo di un prodotto informatico con il supporto di Git, in modo tale che gli studenti poi possano toccare con mano i risultati delle loro lezioni ed essere soddisfatti del percorso svolto.

3. In tale articolo inoltre si lamenta l'incremento del carico cognitivo degli alunni nell'imparare, oltre a programmare, anche l'uso di questo strumento. Non ho attualmente strumenti che mi permettano di affermare con certezza che riunire tali insegnamenti in alcune condensate lezioni possa ridurre negli studenti tale carico.

Un altro articolo consultato è [Pushing Git & GitHub in undergraduate computer science classes](https://dl.acm.org/doi/10.5555/3015220.3015251)[@pushing_git]. In tale articolo viene specificato che separando le lezioni su Git usato solamente in locale e su Git usato anche con il repository remoto su Github sia più facile per gli studenti imparare i diversi concetti riducendo la confusione che ne potrebbe derivare.

[^1]: Articoli consigliati dal professor Lodi durante il colloquio aperto a fine corso.

[^2]: O quantomeno rilasciano open source molto software di corollario e secondario, rilasciarlo in toto han dichiarato che potrebbe danneggiare il loro business.

## Prerequisiti

<!--
Elencare i contenuti che si suppone siano già stati svolti e appresi dagli studenti
-->

Gli studenti devono già essere in possesso delle seguenti competenze *minime*:

1. Manipolare files (creare, modificare, eliminare, spostare, copiare)

2. Navigare su siti internet (nello specifico github.com per il secondo modulo)

Le esercitazioni preparate per l'esame e fornite con questo materiale didattico, destinate a studenti di indirizzo informatico richiedono:

1. Sapere cosa sia un algoritmo, un programma, una funzione, una istruzione, un dato

2. Avere padronanza dei construtti semplici di un linguaggio a scelta del professore (in questo materiale didattico viene scelto il linguaggio Python)

    *Sono stati proposti alcuni esercizi per provare i vari comandi git su casi pratici, nel primo viene anche fatto uso degli array e del passaggio dei parametri per riferimento. Questo può essere riadattato per combaciare meglio al secondo esercizio, dove non viene fatto uso di tali strutture dati.*

Le seguenti conoscenze pregresse aiutano gli studenti a capire meglio gli argomenti trattati:

1. Sapere cosa sia un sistema operativo e come vengono memorizzati i files

2. Sapere cosa sia un'interfaccia a riga di comando, eseguire comandi e programmi, eseguire programmi con interfaccia grafica

Nel caso si ritenga superfluo o oneroso l'uso dell'interfaccia a riga di comando di git, possono essere valutati dei programmi ad interfaccia grafica come sostituti, come ad esempio:

* [Git Extensions](https://gitextensions.github.io/) (Linux, Windows, Mac)

* [Ungit](https://github.com/FredrikNoren/ungit) (Linux, Windows, Mac)

* [Github Desktop](https://desktop.github.com/) (Windows, Mac)

* Estensioni per il proprio editor: Per moltissimi editor di testo esistono moltissime estensioni che permettono di aggiungere sezioni con client per git (vscode per esempio ne possiede uno già integrato)

* [Github.com](https://github.com): Creato un repository, premendo `.` si usa un editor web in stile vscode (quindi con integrato un client git)

## Contenuti

<!--
Spiegare brevemente i contenuti. Se si tratta di contenuti banalmente chiari per un informatico, elencarli semplicemente. Se ci sono contenuti particolari o specifici illustrarli brevemente.
-->

Si vuole introdurre gli studenti all'uso dello strumento Git per versionare il loro codice. Si vuole aiutare a comprendere loro il concetto di repository, branch, commit e staging area, visionare la storia dello stesso e le differenze tra i vari commit e l'attuale contenuto dei files nel repository con la loro controparte attualmente versionata dal repository.

## Traguardi e Obiettivi

<!--
Quali traguardi e obiettivi di apprendimento si vuole raggiungere con le attività proposte?
-->

Al termine delle lezioni nell'area `git` lo studente sa:
* distinguere tra sistemi di versionamento centralizzati o distruibuiti
* creare repository
* usare la staging area per gestire le modifiche, l'aggiunta e la rimozione di files
* registrare le modifiche nel repository tramite i commit, assegnare un messaggio utile per lo sviluppo del progetto
* creare un branch, identificare un branch principale, creare branch secondari e spostarsi tra di essi per portare avanti diversi sviluppi del progetto
* consultare la storia del repository essere consapevole di cosa significhi modificarla e come farlo consapevolmente per poter rimediare a degli errori
* gestire i conflitti delle modifiche quando si manifestano

Al termine delle lezioni nell'area `github` lo studente sa:
* distinguere i concetti di repository locale, remoto, versioning centralizzato e distribuito
* creare un repository remoto, collegarlo al suo repository in locale, eseguire download degli aggiornamenti dal repository remote e upload dal repository locale
* usare le issue come richiesta di chiarimenti, segnalazione di un problema o suggerimento di una soluzione
* usare le pull request come offerta di aggiunta di una nuova funzionalità e di una soluzione ad un problema riscontrato

Al termine di tutte le lezioni lo studente ha le competenze di gestire un progetto sofware al quale possano contribuire più persone, sia come spettatore (consultandolo soltanto), come utilizzatore (segnalando eventuali problemi), come contributore (sviluppando nuove funzionalità o correggendo quelle esistenti) e anche come manutentore (assegnando compiti ai contributori e in generale gestendo le relazioni con tutti gli attori del progetto).

| Dimensioni | Base | Intermedio | Avanzato |
| --- | --- | --- | --- |
| Repository locale | Lo studente sa creare il repository e committare dei file in esso. | Lo studente sa scegliere quali file aggiungere alla staging area e rimuoverli. | Lo studente sa aggiungere e rimuovere piccole modifiche tra le varie contenute dentro ad un certo file. Sa scegliere un adeguato commento per il commit. |
| Branches | Lo studente sa creare in locale branch e come riunirli, sa come visualizzare i rami presenti in locale | Lo studente conosce la differenza la differenza tra branch locali e branch remoti e sa come ottenerli o pubblicarli. | Lo studente sa creare rami e gestire flussi più complessi, sa gestire git flow complessi e sa spiegare i vantaggi che essi comportano. |
| Storia e Tags | Lo studente sa visualizzare la storia del repository e i tag presenti. Sa annotare il commit corrente. | Lo studente sa navigare nella storia e annotare i commit passati. | Lo studente sa navigare nella storia e modificarla in modo proprio, sa annotare e assegnare un nome e un messaggio semanticamente ricco di significato ad un commit. |
| Github (contribuzione) | Lo studente sa sviluppare almeno una nuova funzionalità, usando correttamente i branch in locale e in remoto per *far arrivare* la feature sul branch principale su Github. | Lo studente sa aprire una pull request, chiedendo la correzione da parte di almeno un compagno. | Lo studente sa anche discutere con il compagno in merito alla soluzione proposta in modo costruttivo. |
| Github (lavoro in team) | Lo studente sa svolgere i compiti ad esso assegnati. | Lo studente riesce a coordinare il gruppo sapendo assegnare a se stesso/i e agli altri i compiti da svolgere e le funzionalità da sviluppare in modo equo. | Lo studente sa aiutare i compagni, sia tramite discussioni di persona in laboratorio che attraverso lo strumento Issues di Github. Lo/gli studente/i con la predisposizione a coordinare il gruppo sa valorizzare ogni componente. |

Queste lezioni promuovono, secondo le linee guida del Miur[@linee_guida], la conoscenza del ciclo di vita di un prodotto informatico rendendo coscenti gli studenti di uno degli strumenti più diffusi in ambito aziendale e non per il versionamento del codice e assicurazione della qualità. Gli studenti acquisiranno le basi per poter apprendere più facilmente lo sviluppo agile e le pratiche DevOps, oggi giorno sempre più diffuse in ambito aziendale.

## Metodologie didattiche

<!--
Elencare brevemente quali metodologie didattiche si utilizzano.

Da quelle più classiche (es. lezione frontale, dialogata... uno schema [qui](https://www.leonardope.it/pvw/app/default/pvw_img.php?sede_codice=PELS0001&doc=2130858)) a quelle più moderne (unplugged, cooperative learning, pair programming, flipped classroom) discusse o viste a lezione.

Massima libertà di introdurre altre metodologie non spiegate a lezione (es. EAS) con i dovuti riferimenti.

Se si parla di didattica della programmazione, fare anche riferimento ai relativi concetti (macchina concettuale, misconcezioni, visualizzazione, program comprehension) spiegati a lezione.
-->

Vengono proposte due moduli che possono essere suddivisi in una o più lezioni frontali e due attività di laboratorio da proporre agli studenti che dovranno eseguire esercizi singolarmente e in gruppo.

Come metodologia principale si cerca di sfruttare la *Necessity Learning Design* [@necessity], dove il problema irrisolto è conservare in modo efficente ed efficace gli esercizi svolti dagli alunni (sia per l'insegnante che per gli alunni stessi) durante il corso della loro carriera, tenendo conto dei progressi compiuti e delle correzioni apportate, l'insegnamento è imparare ad usare lo strumento Git per salvare le modifiche ai loro artefatti e il "problema risolto" è effettuare le consegne dei futuri elaborati degli alunni tramite la piattaforma Github o un server Git interno alla rete d'istituto.

Nella prima lezione di teoria dei concetti base di Git si cerca di sfruttare una metodologia *unplugged*, spiegando gli hunk, i commit e i branch con l'ausilio di fogli di carta che vengono scritti, ritagliati, scotchati tra loro.

Nella prima lezione laboratorio viene proposto un *esercizio guidato* inizialmente, pensato per essere svolto, seguendo il *workflow* visto a lezione e ripreso nel testo dell'esercizio, abbondantemente al di sotto del tempo previsto per la lezione di laboratorio per permettere agli studenti di sperimentare autonomamente ed approfondire le prove svolte precedentemente. Eventualmente da svolgere in Pair Programming[^pair]. Vedi meglio le indicazioni nella [sezione apposita](#laboratorio-git).

Nella lezione *github* gli studenti possono assumere diversi ruoli [^role_playing] [@strategie_didattiche] a seconda di chi, alla fine di particolari esercizi, possiede la proprietà del repository Github al quale tutti gli altri devono contribuire: il docente può creare diversi repository per ogni gruppo di studenti oppure saranno gli studenti stessi che dovranno creare i repository remoti su Github per poi usarli tra loro, concedendo i necessari diritti di accesso al docente. In queste lezioni, gli studenti sono suddivisi in *Team di sviluppo* cercando di unire studenti con capacità complementari, senza mettere assieme tutti gli studenti migliori come in un "dream team". Tenere conto anche della predisposizione degli studenti a coordinare, farsi coordinare o lavorare in solitaria.

[^role_playing]: gli studenti si immedesimano in programmatori su un unico progetto software, Strategie Didattiche (A. Calvani) pag. 10

## Tempi

<!--
Un'idea generale e indicativa dei tempi richiesti
-->

In totale 2 lezioni frontali da un'ora ciascuna con gli studenti per introdurre gli aspetti teorici di ciascun modulo e 2 lezioni per applicare tali concetti nella pratica, eventualmente con l'ausilio di un laboratorio di due o tre ore ciascuno dove gli studenti possano eseguire gli esercizi e sperimentare autonomamente.

## Spazi

<!--
Classe, laboratorio, cortile...
-->

Le lezioni frontali possono essere svolte in qualunque aula. Gli argomenti teorici possono essere insegnati anche senza l'ausilio di un supporto informatico, in modalità unplugged. Durante le lezioni più pratiche dove gli studenti dovranno svolgere esercizi e laboratori, serve uno spazio dove poter usare il proprio personal computer o dispositivi messi a disposizione dalla scuola.

## Materiali e Strumenti

<!--
Quali materiali e strumenti (hardware e software, di ogni tipo, non solo informatico) sono necessari?
-->

Per la prima parte di spiegazione di concetti teorici sono necessari fogli di carta, forbici e scotch. Per la seconda parte più pratica sono necessari dei computer personali per ciascun studente per eseguire i comandi dello strumento Git. Essendo tale strumento disponibile per i più diffusi sistemi operativi e totalmente gratuito, non esistono impedimenti strutturali che possano impedire ad uno studente di affrontare le lezioni proposte.

Per la consegna degli esercizi di Git può essere usata la rete d'istituto e una cartella condivisa, dopo aver studiato i comandi per la pubblicazione delle proprie modifiche tramite git (push) può essere messo a disposizione un server Git interno alla rete d'istituto in modo temporaneo, per poi usare, dopo l'apposita lezione, Github (o altro servizio di hosting a scelta).

# Sviluppo dei contenuti

<!--
Questa deve essere la parte centrale e più corposa del documento.
Viene lasciata a voi massima libertà su come organizzarla.
Deve contenere almeno:
1. Materiale didattico per studenti
2. Guida per gli insegnanti
    * Consigli su come utilizzare il materiale didattico. E' possibile inframezzarli al materiale didattico per studenti (ma in tal caso chiarire bene cosa è per l'insegnante e cosa viene dato agli studenti)
    * Suggerimenti su come valutare il raggiungimento degli obiettivi di apprendimento da voi individuati (soprattutto valutazione formativa)
-->

## Introduzione al versionamento del codice

Al giorno d'oggi gli standard di qualità dello sviluppo del codice impongono alle aziende e alle università di tenere sempre conto di chi lavora su quali progetti, su quali aree degli stessi e su quali singoli file. I motivi potrebbero essere:

* risalire ai proprietari per l'attribuzione di proprietà intellettuale;

* ricerca e risoluzione di problemi;

* misurazione della retribuzione per l'eventuale lavoro svolto.

In ambito strettamente scolastico, uno studente ha la necessità di ripristinare il proprio esercizio o elaborato ad uno stadio precedente dopo aver svolto una prova o aver continuato per una strada sbagliata, accorgendosi di aver fatto un errore.

Più in generale, chiunque vorrebbe poter aggiungere, modificare, eliminare o manipolare in qualunque modo un prodotto informatico da solo e poter seguire diversi sviluppi differenti, oppure lavorare con un team di persone che hanno bisogno di lavorare sullo stesso prodotto contemporaneamente senza incorrere perennemenete in problemi di aggiornamento della propria versione del prodotto.

Una prima soluzione a tutti questi problemi potremmo averla usando solamente il nostro file system. Facciamo l'esempio del "programmatore solitario":

1. Alla creazione del nuovo progetto, crea una cartella `Prog`

2. Aggiunge files alla cartella `Prog`, come un `main.py`, `dataset.txt` e altri

3. Vuole provare a sviluppare la funzionalità di modifica del dataset in base a certi parametri, quindi crea la cartella `Prog_before_params` dove copia il contenuto attuale della cartella `Prog` come backup nel caso in cui dovesse tornare indietro e inizia a modificarne il contenuto

4. Un cliente gli chiede di iniziare anche a sviluppare una funzionalità per leggere eventuali dataset in un formato differente, quindi crea una copia della cartella `Prog_before_params` e la rinomina in `Prog_nuovo_formato` e inizia a lavorarci

5. Poi il cliente vuole la funzionalità che lo sviluppatore ha iniziato a fare nel punto 3, ma con qualche modifica, quindi lo sviluppatore deve prelevare le modifiche introdotte, capire come modificarle opportunamente e trasferirle nella cartella del cliente

Si nota quindi come per cambiare poche righe di codice in un progetto in corso per ciascuna funzionalità si devono creare diverse copie di file e cartelle. Volendo poi salvare lo stato del progetto durante le varie fasi della sua vita, creando un *backup* per la versione 1, uno per la versione 2 e altre per ogni versione prodotta, si capisce che la quantità di risorse duplicate e spazio occupato superi di gran lunga quella iniziale per il progetto in sé. Magari dobbiamo duplicare centinaia di file per delle modifiche a una manciata di files.

Per questo vengono in nostro aiuto i sistemi odierni di versionamento del codice. Nel corso del tempo sono state adottate varie tecniche e metodologie per gestire le versioni di un qualunque prodotto informatico, in particolare citiamo due diverse e contrapposte modalità:

* la centralizzata: un unico punto di verità (da qui chiamato per semplicità server) contiene tutto il nostro progetto e ogni persona che vuole contribuire ad esso deve chiedere il permesso di modificarne una parte (creare un nuovo file, modificarne uno esistente, eliminarne...) e una volta terminato, notifica al server di aver completato le modifiche e il server si occupa di salvare l'aggiornamento. Questa modalità nel tempo è stata sempre meno utilizzata in favore della successiva, dato che creava problemi quando più persone volevano modificare la stessa porzione del progetto oppure se la fonte centrale del progetto era inaccessibile, non era possibile lavorare;

* la distribuita: ogni sviluppatore possiede l'intera copia del progetto sul quale si sta lavorando e può in ogni momento lavorare su di esso. Quando sarà pronto a pubblicare le proprie implementazioni, allora lui stesso si assume il compito di chiedere agli altri contribuenti di scaricare le modifiche dalla propria versione del progetto o sarà lui ad inviarle agli altri.

Di seguito vedremo solamente la modalità distribuita, ad oggi tra le più utilizzate in ambito scolastico, accademico e lavorativo. Vedremo nel dettaglio lo strumento **Git** per versionare un progetto in ambito locale, sulla propria macchina e gestirne le versioni e lo sviluppo di diverse funzionalità. Vedremo lo strumento **Github** come gestore di progetti versionati salvati in una località remota che ci aiuta anche a gestire la contribuzioni ai progetti dei nostri compagni e colleghi.

## Versionamento del codice (unplugged)

Dimostrazione della modalità di versionamento del codice proposta da *Git* usando fogli di carta, forbici e scotch. Tutte le operazioni in seguito proposte potranno essere riviste in laboratorio tramite comandi Git scritti tra parentesi.

Un repository è un insieme di file e di oggetti (o metadati). La similitudine con un archivio inizialmente vuoto e una scrivania piena di fogli sparsi ci permette di immaginare il concetto. Proporre un foglio con un programma scritto da "archiviare" ci permette di semplificare il concetto rendendolo riproducibile senza l'uso di un elaboratore e ci permette di introdurre i concetti un po' alla volta.

Prendere un foglio e scrivere sopra un programma Python che effettui la divisione di due numeri come nel codice seguente:

```python
"""
Divide two numbers.
"""

first = float(input("First param:"))

second = float(input("Second param:"))

result = first / second

print("The result is " + str(result))
```

Quando il codice è stato scritto, tale foglio è come se fosse ancora sulla scrivania del programmatore. Quando si vuole salvare il lavoro svolto, lo si affida ad un archivista in attesa di essere effettivamente inserito nell'archivio (`add`). Quando siamo pronti per archiviarlo, si dice all'archivista di creare il nostro primo metadato: scrivere su un altro foglio di carta un codice univoco, la data, l'autore,  un commento che spieghi cosa si è svolto e la riga `+ program.py` per indicare che si è aggiunto un file al repository:

```
commit a8tnf
Author: Daniele Tentoni
Date: 2022-06-07 12:48

    Aggiunta divisione tra numeri.

    + program.py
```

Quindi affianco di ogni riga si scrive il relativo codice (`commit`). Per semplicità vengono mostrate solamente le prime righe:

```
"""                                         a8tnf
Make the division between two numbers.      a8tnf
"""                                         a8tnf
```

A questo punto, simulare la modifica di tale codice, aggiungendo ad esempio il seguente codice per il controllo dell'input sul divisore:

```python
if second == 0:
    print("Second param cannot be 0")
    exit()
```

Scriviamo quindi il codice precedente su due strisce di carta ritagliate da un altro foglio. In questo momento stiamo ancora lavorando sulla scrivania del programmatore. Spiegare agli studenti che ogni striscia di carta che produciamo sulla nostra scrivania è chiamata hunk e rappresenta l'unità di base delle modifiche al nostro repository. Adesso vogliamo tornare dall'archivista per far inserire nell'archivio queste nuove righe. Diciamo quindi all'archivista di aggiungere queste righe in mezzo al nostro programma (`add`): ritagliamo il foglio di carta principale nel punto indicato dalle freccie nel punto indicato di seguito:

```
second = float(input("Second param:"))

<-----------> Tagliare qui <------------>

result = first / second
```

Dato che essa sarà una parte aggiunta, attacchiamo con lo scotch le due parti del foglio principale con una striscia per l'aggiunta, in questo modo:

```
second = float(input("Second param:"))

<-----------> Scotch qui <------------>

if second == 0:
    print("Second param cannot be 0")
    exit()

<-----------> Scotch qui <------------>

result = first / second
```

Quindi ora diciamo all'archivista di confermare le modifiche svolte (`commit`). Scriviamo sul foglio dei metadati le seguenti righe e le striscie di carta rimanenti:

```
commit gehe
Author: Daniele Tentoni
Date: 2022-06-07 13:48

    Aggiunta divisione tra numeri.

    <-----------> Incolliamo aggiunte <----------->
    <-----------> Incolliamo rimozioni <----------->
```

Poi scriviamo di lato il codice del nuovo commit (`commit` delle ultime modifiche effettuate), così:

```
...

if second == 0:                             gehe
    print("Second param cannot be 0")       gehe
    exit()                                  gehe

...
```

Il risultato finale visibile sarà quindi il seguente:

```
"""                                         a8tnf
Make the division between two numbers.      a8tnf
"""                                         a8tnf

first = float(input("First param:"))        a8tnf

second = float(input("Second param:"))      a8tnf

if second == 0:                             gehe
    print("Second param cannot be 0")       gehe
    exit()                                  gehe

result = first / second                     a8tnf

print("The result is " + str(result))       a8tnf
```

Questo è il contenuto del repository (il nostro archivio) dopo le operazioni effettuate.

In questo modo abbiamo visto come creare una nuova risorsa, aggiungerla al sistema di controllo di versione, preparare una modifica ad essa ed applicarla.

Non verranno approfondite, ma similmente possono essere spiegati i concetti di:

* storia del repository (`log`): la storia del commit è quella scritta sul foglio dei metadati. Navigarla vuol dire tagliare/scotchare le striscie dal foglio dei metadati nel foglio del nostro programma come abbiamo fatto fino adesso fino al commit nella storia che si vuole navigare. Si introduce l'uso di un post-it per marcare il commit corrente (`HEAD`).

* rami (`branches`): per creare un nuovo branch si scrive il suo nome su una etichetta e la si pone sul commit a cui punta la HEAD del branch. Nel foglio dei metadati ci si annota per ogni commit anche i genitori di esso. Si può far ricostruire agli studenti su un altro foglio di carta l'albero del repository

* tags (`tag`): creare un altro foglio di metadati dove ci si annotano i tag con i relativi commit e messaggi

*Gli studenti possono continuare a sperimentare con aggiunte e modifiche alla risorsa proposta.*

### Laboratorio Git

Vedere l'esercizio proposto nella cartella git.

Proporre tale esercizio supportando gli alunni con maggiori difficoltà nella scelta dei comandi giusti per assolvere i compiti assegnati. Volendo si possono accopiare gli alunni[^pair] durante questo laboratorio. Nel caso in cui si ritenga opportuno, rimuovere il paragrafo inerente al repository remoto (ad esempio nel caso in cui non sia stato trattato a lezione la differenza tra repository locale e remoto e come operare su di essi oppure in assenza di un server git a disposizione).

[^pair]: Prendendo spunto dalla Pair Programming: gli alunni svolgono a coppie gli esercizi proposti per confrontarsi sulle strategie da adottare per risolvere un particolare problema.

### Laboratorio Github

Vedere l'esercizio proposto nella cartella github.

Le indicazioni sono le stesse del precedente esercizio. In questo caso l'esercizio è molto corposo, constringendo molti studenti a dover finire a casa, in altra sede o durante una lezione successiva. Lo sviluppo sullo stesso progetto da remoto è un fondamentale bisogno che viene soddisfatto e difficoltà che viene semplificata proprio dallo strumento in questione, per questo potrebbe essere anche forzato il fatto di dover finire a casa l'esercizio per poter mettere alla prova gli alunni anche sotto questo aspetto.

# Conclusioni

Git e la maggior parte dei programmi, servizi, utility e altri prodotti informatici sopracitati vengono rilasciati con licenze aperte e libere.

Si vuole fare notare in questa istanza che il codice di Github non è completamente Open Source, sebbene loro per primi siano forti promotori di pratiche di software libero (in una conferenza hanno dichiarato che *aprirlo* potrebbe danneggiare il loro business). Un'altra alternativa maggiormente  open source potrebbe essere [Gitlab](https://gitlab.com) (non completamente, si sono dichiarati *open core*) mentre l'alternativa <u>completamente</u> open source (eseguibile anche su una Raspberry Pi) è [Gitea](https://gitea.com/). Tuttavia a differenza dei primi due servizi, Gitea non possiede un motore/servizio di CI integrato (come le Github Actions o Gitlab CI), per questo deve essere usato un servizio esterno.

Dopo queste lezioni, gli studenti possono essere pronti ad ulteriori conseguenze degli argomenti trattati, come ad esempio:

* pratiche DevOps

* contribuzione a progetti Open Source

* esplorazione di ulteriori servizi che permettano hosting di repository (alcuni proposti sopra)

* uso di Github Pages (o i concorrenti Gitlab Pages, Gitea non possiede anche in questo caso un servizio integrato, quindi bisognerebbe adottare una soluzione terza) per la pubblicazione di siti web statici o applicazioni web lato client (con l'uso di JQuery o i più modermi Vue, React o Angular)

# Bibliografia

<!--
Citare le fonti utilizzate (si consiglia ad esempio bibtex o biblatex)
-->

::: {#refs}
:::

# Licenza del documento

<!--
Specificare la licenza del documento.

Sono caldeggiate licenze libere (es. [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/deed.it)), così da poter
condividere (es. pubblicazione sul Wiki) il documento con futuri
colleghi o insegnanti.

NB: non basta specificare una licenza, bisogna anche rispettarla (es. non includere testi o immagini con licenze non compatibili con quella scelta)
-->

Questo documento viene fornito con licenza Creative Commons 1.0 Universal, di cui una copia è disponibile [allegata](/LICENSES/CC0-1.0.txt) al repository dove è contenuto questo file.
