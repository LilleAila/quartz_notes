---
id: 20260121T0824-elektrisitet
aliases:
  - elektrisitet
tags: []
date: "2026-01-21"
title: elektrisitet
---

#fysikk [[20250820T0820-fysikk-1|fysikk 1]]

# elektrisitet

> [!NOTE]
> Egentlig bare repetisjon av [[20250825T1400-elektriske-kretser|elektriske kretser]] og [[20250908T1337-koblingsskjema|koblingsskjema]]

Det finnes to typer elektriske ladninger: positiv og negativ. To like ladninger vil frastøte hverandre, og to ulike ladninger vil tiltrekkes hverandre. Positive og negative ladninger er henholdsvis protoner og elektroner. Ladningen er elementærladningen, definert ved $e = 1.60 \cdot 10^{-19} \,\mathrm{C}$ (coulomb). Elektroner har ladningen $q = -e = -1.60*10^{-16} \,\mathrm{C}$ og protoner har ladningen $q = e = 1.60 \cdot 10^{-19} \,\mathrm{C}$.

Et elektrisk felt er et område der det virker elektriske krefter på ladninger.

![[20260121T0824-elektrisitet 2026-01-21 08.28.19.excalidraw.svg]]

## Spenning

Spenning defineres som som arbeidet som gjøres per ladning $q$ når ladningen blir flyttet fra et punkt til et annet. Måles i volt ($\mathrm{V}$).

$$
\begin{align}
    U &= \frac{W}{q} \,\mathrm{V} & \\
    \left[ \mathrm{V} \right] &= \left[ \mathrm{\frac{J}{C}} \right] &
\end{align}
$$

## Strøm

Strøm defineres som ladningen $q$ som passerer et everrsnitt av en leder i løpet av tiden $\Delta t$. Måles i ampere ($\mathrm{A}$)

$$
\begin{align}
  I &= \frac{q}{\Delta t} \,\mathrm{A} &
\end{align}
$$

Strømretningen er definert som det motsatte av retningen elektronene beveger seg. Elektroner beveger seg fra den negative til den positive polen, men strømretningen går fra den positive til den negative polen.

## Resistans

Resistans $R$ er motstand i en leder. Måles i ohm ($\Omega$). Materialer som leder strøm dårlig, har høy resistans. Da vil mye av energien gå tapt. En leder med lav resistans vil lede strøm bedre.

## Ohms lov

$$
\underbrace{U}_{\text{Spenning}} = \underbrace{I}_{\text{Spenning}} \cdot \underbrace{R}_{\text{Resistans}}
$$

Dette gjelder når man har ren konstant resistant. Motstander med konstant resistans og som følger Ohms lov kalles ohmske motstander.

## Kirchoffs 1. lov

I en parallellkobling er summen av alle strømmene inn i et forgreiningspunkt lik summen av alle strømmene ut av forgreiningspunktet.

$$
\sum I_{\text{inn}} = \sum I_{\text{ut}}
$$

## Kirchoffs 2. lov

I en lukket strømkrets er summen av spenningene over komponentene i kretsen lik polspenningen til spenningskildene.

## Seriekobling

Alle komponentene er koblet i serie (som navnet tilsier lol). Motstanden er lik summen av motstandene i seriekoblingen.

$$
R = \sum_{i=0}^{n} R_{i}
$$

## Parallellkobling

Motstanden er gitt ved

$$
R = \left( \sum_{i=0}^{n} R_{i}^{-1} \right)^{-1}
$$

Om en lyspære slutter å lyse i en parallellkobling, vil den andre fortsette å lyse siden den delen av kretsen er fortsatt lukket. Spenningen i alle grenene av en parallellkobling er alltid lik. Strømmen er definert ved kirchoffs 1. lov.
