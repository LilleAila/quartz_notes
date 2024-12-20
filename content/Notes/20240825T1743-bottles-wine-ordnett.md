---
id: 20240825T1743-bottles-wine-ordnett
aliases:
  - bottles wine ordnett
tags: []
title: Bottles wine ordnett
date: 2024-08-25
---

#linux [[20240901T0613-linux|linux]]

# Bottles wine ordnett

![ordnett-wine.png](Assets/ordnett-wine.png)

## Bottle setup

1. Install bottles
2. Lag ny bottle med default application type
3. Trykk run executable inni bottlen og run `.msi` installeren
4. "Add desktop entry" under ... menyen til "OrdnettPluss" for å adde en `.desktop` fil
5. Sett fullmodus som default inni ordnett settings

## Fikse fonts

1. Åpne regedit gjennom bottles
2. Gå til `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\FontSubstitutes`
3. Add en `text`-key med navn `Tahoma` og sett valuen til en font du har installet, for eksempel `DejaVu Sans`. Det blir passet through fra hosten.
4. Åpne bottle settings og sett `dpi` under "advanced display settings" til noe høyere, for eksempel `128`.
