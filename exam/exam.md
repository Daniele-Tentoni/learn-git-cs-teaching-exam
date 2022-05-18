<!--
SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com>

SPDX-License-Identifier: CC0-1.0
-->

---

title: Lezione Tool Git
author: Daniele Tentoni
date: 17/05/2022

---

Esame di Didattica dell'Informatica, A.A. 2021/2022

<!--
# Changelog (se necessario)

Se questa relazione è stata già consegnata in precedenza, indicare qui

* i cambiamenti più sificativi
* dove trovare un eventuale diff (se ritenuto necessario)
* risposte a eventuali domande/commenti fatti dai docenti sulle versioni precedenti
-->

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

<!-- TODO: Controllare i documenti ministeriali e/o alla Proposta CINI -->

L'attività è rivolta specialmente al triennio di un istituto tecnico con indirizzo informatico, da svolgere durante le ore di Informatica o discipline annesse (Sistemi e Reti o Gestione di Progetto).

In generale, potendo tramite Git tracciare qualunque prodotto in grado di essere memorizzato su supporto informatico, l'attività può essere riadattata per poter insegnare Git ad un qualunque pubblico di studenti delle scuole superiori a cui si vuole proporre uno strumento di memorizzazione o versionamento alternativo ai classici storage fisici (pennette usb, supporti ottici ...) o cloud (Onedrive, Google Drive ...).

## Motivazione e Finalità

<!--
Perché avete scelto di realizzare questa specifica attività

Una sua brevissima descrizione generale
-->

Ho scelto di realizzare questa attività per due principali motivi:

1. La proporrei principalmente a studenti che hanno scelto il mio stesso percorso di studi alle scuole superiori, dove mi piacerebbe andare ad insegnare e dove penso che questa attività possa servire maggiormente, preparando gli studenti ad utilizzare uno dei più diffusi tools per il versionamento del codice;
2. Avendo già avuto esperienza lavorativa ho notato che gli studenti usciti da tali percorsi di studi non sono preparati abbastanza per entrare con tranquillità e rapidità dentro al mondo del lavoro. Molti non possiedono le competenze da me ritenute minime per poter lavorare in modo collaborativo neanche a piccoli progetti software interni alla mia azienda attuale.

Per tali motivi, penso che proporre agli studenti quelle che secondo me sono le competenze minime da acquisire durante il proprio percorso scolastico in tema di Versioning Control Systems e sviluppo collaborativo alla scrittura del codice sia un esercizio utile in preparazione alle future lezioni a studenti delle scuole e neo assunti interni alla mia azienda.

## Innovatività

<!--
Perché questa proposta è innovativa? Cosa è già presente su questo tema nella ricerca in Didattica dell'Informatica o nelle risorse disponibili online?
-->

Moltissime attività disponibili in rete che ho cercato non coprono gli stessi argomenti di questa. L'insieme delle competenze che vengono proposte nel seguente materiale è la scrematura di tutte quelle che io abbia mai usato nel mio ambito lavorativo fino adesso (questo è il 5 anno di lavoro in un'azienda software cesenate di una ventina di dipendenti) e che penso sia assolutamente irrinunciabili per una persona neo-diplomata che voglia affacciarsi sul mondo del lavoro in ambito informatico.

Alcune delle risorse disponibili online attualmente sono:

[https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
: Ebook scaricabile dal sito ufficiale del progetto Git. Mette a disposizione quindi tutto lo scibile di Git, quindi potrebbe far desistere chi invece cerca un approccio più pragmatico. Resta comunque la scelta più valida possibile per chi volesse approfondire l'argomento autonomamente a casa;

[https://learngitbranching.js.org/](https://learngitbranching.js.org/)
: Gioco gratuito per imparare nei primi livelli i comandi base e via via avanzando nel gioco concetti più complicati. Possibile allenamento in vista di interrogazioni e compiti in classe per gli studenti;

[https://www.atlassian.com/git](https://www.atlassian.com/git)
: Guida a Git curata da Atlassian, uno dei principali attori in gioco in tema di Sistemi di Versionamento del Codice grazie alla loro piattaforma BitBucket;

[https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
: Elenco dei principali comandi di Git curata dai sopracitati collaboratori di Atlassian.

## Prerequisiti

<!--
Elencare i contenuti che si suppone siano già stati svolti e appresi dagli studenti
-->

Gli studenti devono già essere in possesso delle seguenti conoscenze:

1. Sapere cosa sia un sistema operativo e come vengono memorizzati i files
2. Sapere cosa sia un'interfaccia a riga di comando e come eseguire comandi e programmi

Per l'uso di questo materiale didattico in un istituto tecnico non ad indirizzo informatico sono superflue le seguenti conoscenze (richiede il riadattamento di una parte di questo materiale didattico):

1. Sapere cosa sia un algoritmo, un programma, una funzione, una istruzione, un dato
2. Avere padronanza dei construtti semplici di un linguaggio a scelta del professore (in questo materiale didattico viene scelto il linguaggio Python)

## Contenuti

<!--
Spiegare brevemente i contenuti. Se si tratta di contenuti banalmente chiari per un informatico, elencarli semplicemente. Se ci sono contenuti particolari o specifici illustrarli brevemente.
-->

Si vuole introdurre gli studenti all'uso dello strumento Git per versionare il loro codice. Si vuole aiutare a comprendere loro il concetto di repository, branch, commit e staging area, visionare la storia dello stesso e le differenze tra i vari commit e l'attuale contenuto dei files nel repository con la loro controparte attualmente versionata dal repository.

## Traguardi e Obiettivi

<!--
Quali traguardi e obiettivi di apprendimento si vuole raggiungere con le attività proposte?
-->

Al termine delle lezioni nell'area `git`, lo studente deve aver appreso i seguenti concetti:

- repository, locale o remoto
- branch, principale, secondario
- commit, con o senza messaggio
- storia del repository
- staging area

Deve essere entrato in possesso delle seguenti competenze:

- creare un repository locale
- visualizzare lo stato attuale del repository
- creare un branch a partire dal principale e muoversi tra quelli già presenti
- aggiungere/rimuovere files o parte di essi alla staging area ed eseguire commit
- visualizzare la storia del repository e muoversi all'interno di essa
- tornare indietro nella storia nel caso sia stato fatto un errore

Al termine delle lezioni nell'area `github` devono aver appreso i seguenti concetti:

- repository centralizzato
- issue come richiesta di chiarimenti, segnalazione di un problema o suggerimento di una soluzione
- pull request come offerta di aggiunta di una nuova funzionalità e di una soluzione ad un problema riscontrato

Deve essere entrato in possesso delle seguenti competenze:

- creare un repository sul proprio account
- creare branch
- aprire una issue, ispezionarne il contenuto, aggiungere meta-informazioni, rispondere ad issue aperte e chiuderle quando necessario
- aprire una pull request, ispezionarne il contenuto, aggiungere meta-informazioni, collegarne le issue ad essa relative e partecipare al loro ciclo di sviluppo con revisioni del codice, apporto di modifiche, commenti e chiusura

### Collegamento con i documenti ministeriali/proposte

<!--
Indicare quali traguardi/obiettivi presenti nei documenti rilevanti vengono
raggiunti (es. Indicazioni nazionali per il primo ciclo, Nuovi scenari,
Proposta CINI numerata, Indicazioni nazionali / linee guida per scuola
secondaria di secondo grado).
-->

### Obiettivi di apprendimento

<!--
E' obbligatorio scrivere gli obiettivi di apprendimento specifici basandosi su una tassonomia (es. Bloom rivisitata, Guerra-Frabboni-Arrigo, SOLO...)

E' possibile (ma non obbligatorio) organizzarli in termini di
* traguardi di competenze
* obiettivi di conoscenze e abilità
-->

## Metodologie didattiche

<!--
Elencare brevemente quali metodologie didattiche si utilizzano.

Da quelle più classiche (es. lezione frontale, dialogata... uno schema [qui](https://www.leonardope.it/pvw/app/default/pvw_img.php?sede_codice=PELS0001&doc=2130858)) a quelle più moderne (unplugged, cooperative learning, pair programming, flipped classroom) discusse o viste a lezione.

Massima libertà di introdurre altre metodologie non spiegate a lezione (es. EAS) con i dovuti riferimenti.

Se si parla di didattica della programmazione, fare anche riferimento ai relativi concetti (macchina concettuale, misconcezioni, visualizzazione, program comprehension) spiegati a lezione.
-->

Vengono proposte due aree le quali possono essere suddivise in una o più lezioni frontali e due attività di laboratorio da proporre agli studenti che dovranno eseguire esercizi in gruppo.

## Tempi

<!--
Un'idea generale e indicativa dei tempi richiesti
-->

Per la prima parte dell'attività didattica di spiegazione in aula possono essere necessarie dalle due alle tre lezioni da un ora circa ciascuna, mentre per il laboratorio possono essere necessarie da una alle due lezioni di tre ore ciascuna.

## Spazi

<!--
Classe, laboratorio, cortile...
-->

L'attività didattica proposta può essere svolta per la prima parte in un qualunque luogo dove possa essere posizionato un computer con un proiettore, mentre per la seconda parte di laboratorio appunto in un laboratorio che dia la possibilità di usare un computer per ogni studente, sia esso fornito dalla scuola oppure portato da casa da ogni studente.

## Materiali e Strumenti

<!--
Quali materiali e strumenti (hardware e software, di ogni tipo, non solo informatico) sono necessari?
-->

Per la prima parte di spiegazione del funzionamento base dello strumento Git in aula sono necessari fogli di carta, forbici e scotch. Per la seconda parte, sempre in aula, sono necessari un computer e un proiettore per mostrare agli studenti l'esecuzione dei comandi specifici dello strumento Git e il loro risultato sui file all'interno di una cartella contenente un repository e l'analogia con le stesse operazioni però usando solamente i file e le cartelle.

Per la parte in laboratorio, ogni studente deve essersi preparato da casa un proprio account Github ed essere dotato di un computer con installata l'ultima versione dello strumento Git, disponibile per i principali sistemi operativi: Windows, MacOs, Debian, Ubuntu e molte altre distribuzioni Unix-like.

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

# Bibliografia

<!--
Citare le fonti utilizzate (si consiglia ad esempio bibtex o biblatex)
-->

# Licenza del documento

Questo documento viene fornito con licenza Creative Commons 1.0 Universal, di cui una copia è disponibile [allegata](/LICENSES/CC0-1.0.txt) al repository dove è contenuto questo file.

<!--
Specificare la licenza del documento.

Sono caldeggiate licenze libere (es. [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/deed.it)), così da poter
condividere (es. pubblicazione sul Wiki) il documento con futuri
colleghi o insegnanti.

NB: non basta specificare una licenza, bisogna anche rispettarla (es. non includere testi o immagini con licenze non compatibili con quella scelta)
-->
