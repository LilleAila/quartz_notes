---
id: 20250829T0909-bygge-maskin-fra-krav
aliases:
  - Bygge maskin fra krav
tags: []
date: "2025-08-29"
title: Bygge maskin fra krav
---

#it1 [[20250829T0902-it1|it1]]

# Bygge maskin fra krav

https://docs.google.com/spreadsheets/d/1IkJdNcG4pA8d27XaaYJ_OvuFtg6bv3bmQx5_aTPGDcU/edit?gid=0#gid=0

Denne maskinen er bygget for å støtte videoredigering av 4K videoer. Denne maskinen er optimalisert for redigering av 4K-videoer.

Da dette er en bedrift har jeg regnet med priser ekskludert MVA.

- CPU
  Jeg har valgt en ryzen 9 (altså AMDs toppmodell) fra en tidligere generasjon. Denne har 12 kjerner som vil være mer enn bra nok for videoredigering.
- GPU
  Helst skulle jeg valgt et grafikkort fra AMD her, men jeg har valgt en RTX 5070 grunnet kompatibilitet. NVidia sine grafikkort er generelt kjent for å være bedre støttet enn AMD sine grafikkort for videoredigering. Dette gjelder spesielt i davinci resolve, men gjelder trolig også premiere pro.
- RAM
  Jeg har valgt 64GB (2x32GB) fordi dette skal være godt nok til 4K redigering. For at dette skal være raskest mulig, har jeg brukt DDR5-6000 og ikke noe tregere som DDR-4800 selv om dette er billigere.
  Å bruke to ramm-pinner er optimalt fordi dette blir raskere enn 4x16GB da det er færre kanaler å bytte mellom.
- Strømforsyning
  Alle komponentene bruker totalt like under 600W. Derfor velger jeg en 750W strømforsyning fordi strømforsyninger alltid jobber mest effektivt med opptil 80% ytelse, i tillegg til at dette gir litt rom for fremtidige oppgraderinger.
- Lagring
  Kingston NV3 er ikke kjent for å være den beste SSD-en, men den er ganske grei og ikke veldig dårlig.
  Legger til 4TB med HDD lagring for ferdige prosjekter. Dette går litt over budsjettet.
- Nettverk
  Hovedkortet jeg valgte har integrert wifi, men det vil være optimalt om bedriften bruker kablet internett, spesielt hvis de skal jobbe på en NAS.

Generelt har jeg prøvd å unngå mindre kjente merker, i tillegg til merker som Gigabyte, da de i det siste ikke har fått veldig bra kritikk.

---

Ting som ikke er tatt med i prisen:

- Lisenser
  Helst skulle de brukt linux med davinci resolve i stedet for å bruke premiere pro. Dersom det virkelig er nødvendig blir de nødt til å kjøpe lisenser til windows og adobe premiere, samt annen programvare de kan ønske å bruke.
- Skjerm
  Da de skal holde på med videoredigering bør de investere i en skjerm med god fargegjengivelse og høy oppløsning. Noe av det beste an kan få til dette blir en 4K OLED-skjerm som for eksempel https://www.proshop.no/Skjerm/27-ASUS-ROG-Swift-OLED-PG27UCDM-3840x2160-4k-UHD-240Hz-QD-OLED-90W-USB-C/3346959. Dette koster 13995 kr, eller 11196 ekskludert MVA
  Hvis man skal gå for noe litt billigere, ville jeg heller brukt en ASUS ProArt: https://www.proshop.no/Skjerm/27-ASUS-ProArt-PA279CV-3840x2160-4k-UHD-IPS-65W-USB-C-HDR10/2884317?utm_source=prisjakt&utm_medium=cpc&utm_campaign=pricesite som koster 4959 / 3967 kr.
- Tastatur, mus, kabler etc.
  Dette forventer jeg at de har fra før, og trenger ikke å kjøpes inn

Mulige forbedringer:

- Lagringsplass
  2+4TB kan være lite når man skal håndtere 4K-videoer, og det kunne vært lurt å oppgradere dette til mer lagring. Med en NAS som beskrevet lengre nede, vil ikke dette være like nødvendig, da ikke alle trenger å ha filer fra tidligere prosjekter lagret lokalt.
- GPU
  Det kan hende noen av NVidia sine workstation-grafikkort hadde vært bedre egnet til videoredigering enn GeForce-kortene deres som er mer rettet mot gaming. Dette har jeg ikke undersøkt videre.

## Alternativ prebuilt mac

Mac mini M4 pro, base-modell

- 24GB RAM
- 512GB SSD
- Pris: 16 000 ekskl. MVA

Dette vil være langt fra like mye minne og lagring som i den jeg bygget, men vil likevel kunne håndtere mye av videoredigering relativt bra.

### Benchmarks for å sammenligne GPU:

Det var vanskelig å finne kilder som hadde testet begge to på samme måte, men her er det noe:
https://www.notebookcheck.net/Apple-M4-Pro-20-core-GPU-Benchmarks-and-Specs.915517.0.html
https://www.notebookcheck.net/NVIDIA-GeForce-RTX-5070-Benchmarks-and-Specs.935682.0.html

- Geekbench 6.4 - Geekbench 6.4 GPU OpenCL
  - Mac: 69665.5 (median)
  - RTX: 189865

Benchmarks sier ikke alt, men ut fra dette kan man se at det er ganske stor forskjell i ytelsen mellom de to grafikkkortene. Dette skyldes blant annet at M4 pro er egentlig ment som en laptop-gpu og er integrert grafikk i prossessoren, mens RTX 5070 er et dedikert grafikkort. Dermed vil det være bedre på nesten alle måter å bygge en egen maskin slik som beskrevet over.

### CPU benchmarks

https://www.cpubenchmark.net/compare/5027vs6346/AMD-Ryzen-9-7900X-vs-Apple-M4-Pro-12-Core

Her ser man at også for CPU-en er r9 7900X en god del raskere enn M4 pro, men her er ikke forskjellene like store. Det er også verdt å nevne at M4 er basert på ARM-platformen som er mye mer energieffektiv, i tillegg til at programmer skrevet for mac ofte er bedre optimalisert for den platformen og ytelsen kan derfor være en del høyere enn det tallene sier. Likevel er det så stor forskjell, spesielt i GPU-en. Derfor ville jeg gått for den jeg har bygget.

## Lagring / NAS

For å jobbe sammen og å dele filer, i tillegg til å håndtere sikkerhetskopier av data, ville jeg bygget en NAS (network-attached storage). Det finnes ferdige løsninger fra for eksempel synology, eller man kan bygge en server selv.

I en NAS vil man som regel bruke flere disker satt opp i en RAID array.

### Ferdig løsning

NAS: https://www.proshop.no/NAS-Server/Synology-DX525-NAS-Server/3371321 (5672 / 4537 kr)
Denne har 5 brønner til harddisker. Her ville jeg brukt alle de ledige brønnene og satt dem opp i en RAIDZ2 (kalt RAID-6 på ikke-ZFS filsystemer) array. Det vil si at man i praksis bruker to av diskene til redundans slik at om en eller to skulle bli ødelagt, vil man ikke miste dataen.

Jeg vil bruke 5x 16TB harddisker. Toshiba sin N300 er generelt kjent for å være gode NAS-harddisker, og skriver med CMR (conventional magnetic recording) som er bedre egnet for slik bruk. https://www.proshop.no/Harddisk/Toshiba-N300-16TB-Harddisk-HDWG51GUZSVA-SATA-600-35/3342900 (3884 / 3107 kr)

5x 16TB lagring vil bli 80TB plass. To av disse brukes til redundans, slik at man vil få 48TB med ledig plass. Dette vil være nok til samarbeid på prosjekter og til å arkivere tidligere prosjekter.

### Selvbygget

Man kan også bygge en enkel NAS selv. Til dette ville jeg ikke trengt en spesielt kraftig CPU, og jeg vil ha et hovedkort som har nok SATA-porter til alle diskene. Med en selvbygget vil jeg også ha muligheten til å utvide RAID-arrayen i fremtiden hvis det er ønskelig.

Her hadde jeg brukt ZFS med programvarenivå RAID. Jeg ville startet med et ZPOOL med kun en VDEV der denne er en RAIDZ2-pool bestående av 5 disker som beskrevet tidligere. I fremtiden vil man kunne legge til enda en lik VDEV i samme ZPOOL for å doble den tilgjengelige lagringen enkelt.

Å bruke RAID gjør at hvis en (eller to med RAIDZ2) av diskene slutter å virke, vil man fortsatt ha tilgang til dataen sin.

Serveren ville kjørt NixOS slik at konfigurasjonen er enkelt reproduserbar og alt blir enklere å konfigurere. Den vil også måtte kjøre en filserver slik at de ulike maskinene kan få tilgang til filene de trenger.

---

I tillegg til å ha en egen NAS på bygget, er det viktig å lage backups av dette. Her er det lurt å lage fysiske backups på eksterne harddisker av alt innholdet i NAS-en, i tillegg til å bruke skylagringstjenester som google drive.

## Må hver person ha sin egen maskin?

I stedet for at hver person som jobber må ha sin egen maskin, kan man ha en sentral server med mange ressurser. I denne ville jeg brukt en AMD Threadripper (eller intel sin ekvivalent xeon) som CPUen, da denne er velegnet for servere og har mange kjerner. På denne maskinen man man koble til flere grafikkort og slikt, og kjøre proxmox eller noe lignende. Da vil man kunne fordele de fysiske ressursene på flere virtuelle maskiner slik at hver av de som redigerer videoer ikke trenger en fysisk maskin. Dette vil gjøre det mulig å raskt legge til flere og å gi alle de ressursene de trenger - for eksempel kan flere personer dele på samme grafikkort hvis de ikke har like krevende arbeid, eller en person kan få mer minne og prossessorkraft enn andre hvis det trengs.

## Kilder

Proshop for priser av produktene
Produsentens nettsider for å finne blant annet krav for strøm for ulike komponenter
Egen kunnskap (jeg byttet fag så jeg kom inn dagen oppgaven skulle leveres og gjorde egentlig hele oppgaven ut fra det jeg kan fra før)
