---
Title: Hack-The-Box (0001) > Starting Point
Date: 2020-08-06
Modified: 2021-04-04
Tags: init, cybersecurity, htb, pentest, writeup
Keywords: cybersecurity, htb, pentest, hacking, writeup, archetype
Category: htb
Author: Penserbjorne
Summary: Anotaciones sobre la sección "Starting point" de Hack-The-Box
Lang: es-MX
Translation: false
Status: published
---

# This is not the intro :)

Ola k ase.

Para este exacto momento en el que escribo esta linea de texto han pasado 146
días desde que comenzó la pandemia del COVID-19 y pareciera que el tiempo se
detuvo y que no ha pasado nada pero que a la vez que han pasado tantas cosas.

Como sea, este blog esta en la misma situación, un tiempo suspendido.

Dependiendo de cual futuro o universo paralelo leas esto puede que el blog
ni siquiera este terminado de configurar, que aún tenga el template de `Pelican`
y que no tenga nada de contenido o que ya sea un pequeño blog que se ve hermoso
y tiene un par de entradas útiles para la humanidad haha en todo caso, si en
estos dos párrafos no te haz aburrido o retirado, mandame un tuit a
[@_penserbjorne](https://twitter.com/_penserbjorne)
con una captura de pantalla de como se ve el blog y a cambio te invito unos
taquitos :)

---

Personas hermosas que han reclamado sus tacos:

- [Brendita](https://twitter.com/brendorts/status/1291595727693651969), aunque elimino esa cuenta.

---

Ahora sí, arranquemos.

# Hack-The-Box: Starting point

## ¿Qué es esto?

Estos textos serán anotaciones sobre la sección **Starting point** de
**Hack-The-Box**.

Nos apoyaremos en los walk-throughs que ya vienen incorporados en la sección
*Starting point* e iremos explicando los comandos utilizados.

## Hack-The-Box (HTB)

Bueno, para hablar de [**Hack-The-Box** (HTB)](https://www.hackthebox.eu) y
presentar lo qué realmente es este proyecto seria bueno dedicar una entrada
específicamente a eso, por lo cual solo diré que es una plataforma para
practicar o probar tus habilidades de pentesting trabajando sobre maquinas
virtuales que están diseñadas y preparadas para esto.

En resumen, hay maquinas virtuales con cierto software instalado y ciertas
configuraciones que permiten que esta maquina pueda ser vulnerada de alguna
manera. ¿Quieres practicar temas de pentesting? Esta es una de las plataformas
recomendadas.

## Starting Point

Para las personas que van comenzando en este ámbito puede que HTB sea una
plataforma con un nivel de complejidad bastante alto y no necesariamente la
primera opción para arrancar.

Para solucionar esto HTB ha habilitado una sección llamada
[**Starting Point**](https://www.hackthebox.eu/home/start)
en la cual se encuentran una serie de maquinas con un nivel *básico*
acompañadas de sus [walk-throughs](https://www.wordnik.com/words/walk-through)
para que puedas resolverlas y familiarizarte con los pasos usuales del proceso
de pentesting.

**Nota**: El pentesting no es una receta, estos recursos son solo para
comenzar, pero conforme se avanza es necesario refinar tus habilidades y hacer
uso el conocimiento que vas desarrollando o acumulando :)

## Elementos del pentesting

Si bien el pentesting no es una receta, existen diferentes metodologías o
frameworks que nos ayudan a guiarnos para realizar esta actividad de manera
ordenada y limpia.

Si quieres saber más puedes buscar los siguientes términos en Internet:

- Cyber security framework
- Cyber security kill chain
- MITRE Framework
- OWASP Framework

Listo, ahora que haz ignorado lo anterior o haz regresado de buscar, en el caso
de la sección de **Starting Point** de HTB podemos encontrar de manera general
los siguiente elementos:

- Reconocimiento (Reconnaissance)
- Enumeración (Enumeration)
- Punto de partida (Foothold)
- Movimiento lateral (Lateral Movement)
- Explotación (Explotation)
- Escalada de privilegios (Privilege Escalation)
- Explotación posterior (Post Explotation)

Si bien no todas las máquinas necesitan todos los pasos mencionados, es bueno
tenerlos presentes para tratar de trabajar de manera ordenada.

Te recomendamos resolver cada maquina con su walk-through y a la par ir leyendo
esta serie de textos.

## Anotaciones de Starting point

Para ir tomando nota iremos creando una sección por cada maquina e iremos
desarrollando los comando que solicita su walk-through correspondiente y le
daremos contexto al comando o a la acción.

Debido a que no sé cual va a ser la longitud de cada maquina lo mejor será
dedicar una entrada a cada una por lo que te invito pases a la siguiente entrada
en la cual comenzaremos con la maquina
[**Archetype**]({filename}./htb-02-starting-point-archetype.md).

`#HappyHacking`
