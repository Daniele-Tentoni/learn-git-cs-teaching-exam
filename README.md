<!--
SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com>

SPDX-License-Identifier: GPL-3.0-only
-->

# Modello relazione d'esame

[![REUSE status](https://api.reuse.software/badge/git.fsfe.org/reuse/api)](https://api.reuse.software/info/git.fsfe.org/reuse/api)
[![Check Reuse Compliance](https://github.com/Daniele-Tentoni/cs-teaching-exam-template/actions/workflows/lint.yml/badge.svg)](https://github.com/Daniele-Tentoni/cs-teaching-exam-template/actions/workflows/lint.yml)
[![Produce Pandoc website](https://github.com/Daniele-Tentoni/cs-teaching-exam-template/actions/workflows/pandoc.yml/badge.svg)](https://github.com/Daniele-Tentoni/cs-teaching-exam-template/actions/workflows/pandoc.yml)
[![pages-build-deployment](https://github.com/Daniele-Tentoni/cs-teaching-exam-template/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Daniele-Tentoni/cs-teaching-exam-template/actions/workflows/pages/pages-build-deployment)

Questo modello di relazione d'esame di Didattica dell'Informatica è stato utilizzato come base da Daniele Tentoni. Può essere modificato come meglio si crede seguendo la licenza GPL.

Puoi vedere il risultato pubblicato [qui](https://daniele-tentoni.github.io/cs-teaching-exam-template/).

**Tabella dei contenuti**:

- [Compilare la relazione](#compilare-la-relazione)
- [Licenza](#licenza)
  - [Reuse](#reuse)
- [Contribuitre](#contribuire)

## Compilare la relazione

Compila la relazione in Markdown utilizzando [pandoc](https://pandoc.org):

```
sudo apt install pandoc
curl 'https://raw.githubusercontent.com/ryangrose/easy-pandoc-templates/master/html/elegant_bootstrap_menu.html' > .pandoc/templates/elegant_bootstrap_menu.html
mkdir dist
pandoc esame/esame.md --from=markdown --to=html --output=dist/index.html --toc --template=elegant_bootstrap_menu.html --data-dir=.pandoc
```

Per effettuare il deploy automatico su un sito su Github Pages, hai bisogno di creare un token segreto per permettere alla Github Actions di accedere con permessi di scrittura al repository di destinazione sul branch _gh-pages_. Per fare questo, puoi seguire i seguenti passi:

1. Andare nelle impostazioni del proprio profilo: `Avatar` -> `Impostazioni` -> `Opzioni Sviluppatore` -> `Personal Access Token`
2. Creare un nuovo Personal Access Token con i diritti repo_admin **da non condividere con nessuno** (chiunque possederà questo codice potrà scrivere qualunque cosa sul vostro repository)
3. Andare sul proprio repository appena creato, `Impostazioni` -> `Secrets` -> `Actions`
4. Creare un nuovo segreto dal nome `GH_TOKEN`, incollare il token generato e salvare

Ogni volta che verrà effettuata una push sul branch principale verrà effettuato un deploy tutto in automatico.

## Licenza

Il materiale di questo repository è protetto, salvo se diversamente specificato, da licenza GPL 3.0 disponibile [qui](/LICENSES/GPL-3.0-only.txt).

La relazione d'esame d'esempio proposta in `esame/esame.md` è la stessa proposta dal prof. Michael Lodi per il relativo corso [qui](https://github.com/CSEd-unibo/CSEd-unibo.github.io/blob/master/modello_esame.md) di pubblico dominio.

### [Reuse](https://reuse.software/)

Reuse è un progetto che aiuta a mantenere le license software e renderle chiare e accessibili per umani e computers. Puoi ottenere maggiori informazioni sul [sito ufficiale](https://reuse.software/) del progetto.

Ogni volta che verrà effettuata una push o verrà aperta una pull request verso il branch principale, verrà controllato se ogni file dentro al progetto è correttamente licenziato o meno. Per ulteriori informazioni a riguardo, leggi [qui](https://github.com/marketplace/actions/reuse-compliance-check).

In ogni momento puoi controllare che il tuo lavoro sia conforme alle [specifiche](https://reuse.software/spec/) tramite l'uso del [tool dedicato](https://github.com/fsfe/reuse-tool):

    reuse lint

Il tool permette anche di aggiungere gli headers specifici per ogni tipo di file tramite dei comandi appositi:

    reuse addheader --copyright=<your_name> --license=<desired_license> file

## Contribuire

Puoi contribuire a questo repository template aprendo issues o pull requests.

Come contributi interessanti da portare avanti ci sarebbero quello di creare un Makefile per semplificare le operazioni più ripetitive oppure quello di aggiungere il supporto almeno per Latex nel caso qualche altro studente ne avesse bisogno. Io ho usato il Markdown.

E ovviamente traducendo in Inglese questo file.
