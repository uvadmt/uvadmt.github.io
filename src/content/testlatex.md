+++ 
author="Amro Aljundi" 
title = "Typesetting using Overleaf and LaTeX" 
date = "2025-02-16" 
slug = "testlatex" 
description = "A focused introduction to LaTeX for typesetting in discrete math" 
enableMathNotation = true 
+++

# Overleaf and LaTex

Overleaf is a web application for collaboratively editing documents typeset using LaTeX.

LaTeX is a powerful and extensible typesetting language that allows you to produce beautiful, complex documents from structured text input. The philosophy of LaTex is for you to write without worrying about how things will look.

LaTeX was developed by Leslie Lamport (who won the 2013 Turing Award for work on distributed computing) as a set of macros built on TeX to make it easier to produce documents. TeX was developed by Donald Knuth (who won the 1974 Turing Award and was among the first people to formally analyze algorithms), because he was unsatisfied with the typesetting tools available for writing _The Art of Computer Programming_ (which he started writing in 1962, but is still unfinished). 

# Basics
## "source" and "rendering"
We will refer to LaTeX that we write as "source", and we will refer to the result
of compiling some LaTeX code as its "rendering". In other words, this LaTeX source:

```
$P :=$ Latex is great
```
Is rendered as:

