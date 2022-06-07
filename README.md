<!--
SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com>

SPDX-License-Identifier: GPL-3.0-only
-->

# Learn Git

[![REUSE status](https://api.reuse.software/badge/git.fsfe.org/reuse/api)](https://api.reuse.software/info/git.fsfe.org/reuse/api)
[![Check Reuse Compliance](https://github.com/Daniele-Tentoni/learn-git-cs-teaching-exam/actions/workflows/lint.yml/badge.svg)](https://github.com/Daniele-Tentoni/learn-git-cs-teaching-exam/actions/workflows/lint.yml)
[![Produce Pandoc website](https://github.com/Daniele-Tentoni/learn-git-cs-teaching-exam/actions/workflows/pandoc.yml/badge.svg)](https://github.com/Daniele-Tentoni/learn-git-cs-teaching-exam/actions/workflows/pandoc.yml)
[![pages-build-deployment](https://github.com/Daniele-Tentoni/learn-git-cs-teaching-exam/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Daniele-Tentoni/learn-git-cs-teaching-exam/actions/workflows/pages/pages-build-deployment)

Materiale per attività didattica per l'insegnamento dell'utilizzo del tool git presso istituti tecnici industriali con indirizzo informatico per esame di Didattica dell'Informatica aa. 2021/2022 Unibo.

Puoi vedere il risultato pubblicato [qui](https://daniele-tentoni.github.io/learn-git-cs-teaching-exam/).

## Licenza

Il materiale di questo repository è protetto, salvo se diversamente specificato, da licenza GPL 3.0 disponibile [qui](/LICENSES/GPL-3.0-only.txt).

Il contenuto di questo repository è basato sul template [cs-teaching-exam-template](https://github.com/Daniele-Tentoni/cs-teaching-exam-template).

### [Reuse](https://reuse.software/)

Reuse è un progetto che aiuta a mantenere le license software e renderle chiare e accessibili per umani e computers. Puoi ottenere maggiori informazioni sul [sito ufficiale](https://reuse.software/) del progetto.

Ogni volta che verrà effettuata una push o verrà aperta una pull request verso il branch principale, verrà controllato se ogni file dentro al progetto è correttamente licenziato o meno. Per ulteriori informazioni a riguardo, leggi [qui](https://github.com/marketplace/actions/reuse-compliance-check).

In ogni momento puoi controllare che il tuo lavoro sia conforme alle [specifiche](https://reuse.software/spec/) tramite l'uso del [tool dedicato](https://github.com/fsfe/reuse-tool):

    reuse lint

Il tool permette anche di aggiungere gli headers specifici per ogni tipo di file tramite dei comandi appositi:

    reuse addheader --copyright=<your_name> --license=<desired_license> file
