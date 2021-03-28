---
Title: EDA
Date: 2021-01-15
Modified: 2020-01-15
Tags: blog, penserbjorne
Keywords: blog, penserbjorne
Category: eda, linux
Author: penserbjorne
Summary: EDA
Lang: es-MX
Translation: false
Status: draft
---

#   Referencia

-   https://camilotejeiro.github.io/2016/05/03/open-tools-for-circuit-design-learning-qucs-kicad-and-freecad.html

#   Simulaciones

Instalar:

** Hacer notar los componentes de Qucs y Qucs-S para ver como se relacionan los simuladores**
    -   Revisar https://qucs-s-help.readthedocs.io/en/latest/Intro.html#qucs-0-0-18-structure

```
Provide Qucs users with a choice of simulation engine selected from qucsator, Ngspice, Xyce and SPICE OPUS. By selecting Ngspice, Xyce or SPICE OPUS as the Qucs simulation engine users may capitalise on all the features offered by the extensive SPICE developments which have taken place over the last forty years. Both Ngspice, Xyce and SPICE OPUS offer improved transient simulation convergence and speed, particularly for large non-linear circuits. Xyce brings an alternative implementation of single tone Harmonic Balance simulation to Qucs which offers much improved convergence properties for both linear and non linear components and devices. The latest version of Xyce, 6.5 at the time of writing, also offers multi-tone Harmonic Balance simulation. SPICE OPUS adds transient shooting methods for the steady state analysis of large signal AC simulation and optimization.
```

-   Ngspice
    -   http://ngspice.sourceforge.net/download.html
        -   La versión más reciente es la 33, los repositorios de Ubuntu tienen hasta la 31
-   SPICE OPUS
    -   http://fides.fe.uni-lj.si/spice/download/downloadl.html
-   Xyce
    -   https://xyce.sandia.gov/
        -   Requiere registro


-   Qucs
    -   http://qucs.sourceforge.net/install.html#install_ubuntu
        -   Funciona en Ubuntu 20.04
    -   
-   Qucs-S
    -   https://ra3xdh.github.io/
    -   https://download.opensuse.org/repositories/home:/ra3xdh/
        -   Se puede utilizar el .deb de Debian
        -   He utilizado el .deb de Debian 10 para Ubuntu 20.04

##  Documentación para comenzar

-   Qucs
    -   http://qucs.sourceforge.net/docs.html
    -   http://qucs.sourceforge.net/docs/tutorial/getstarted.pdf

-   Qucs-s
    -   https://ra3xdh.github.io/#docs
    -   https://qucs-s-help.readthedocs.io/en/latest/Intro.html#
