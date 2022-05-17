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

## Compilare la relazione

Compila la relazione in Markdown utilizzando [pandoc](https://pandoc.org):

```
sudo apt install pandoc
curl 'https://raw.githubusercontent.com/ryangrose/easy-pandoc-templates/master/html/elegant_bootstrap_menu.html' > .pandoc/templates/elegant_bootstrap_menu.html
mkdir dist
pandoc esame/esame.md --from=markdown --to=html --output=dist/index.html --toc --template=elegant_bootstrap_menu.html --data-dir=.pandoc
```

## Contribuire

Puoi contribuire a questo repository template aprendo issues o pull requests.

Come contributi interessanti da portare avanti ci sarebbero quello di creare un Makefile per semplificare le operazioni più ripetitive oppure quello di aggiungere il supporto almeno per Latex nel caso qualche altro studente ne avesse bisogno. Io ho usato il Markdown.

E ovviamente traducendo in Inglese questo file.

La relazione d'esame d'esempio proposta in `esame/esame.md` è la stessa proposta dal prof. Michael Lodi per il relativo corso [qui](https://github.com/CSEd-unibo/CSEd-unibo.github.io/blob/master/modello_esame.md).
