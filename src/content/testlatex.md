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



## Macros

A macro in LaTeX is something that begins with `\`. This includes math
commands like `\times` or non-math commands like `\textbf`. A macro can take zero or more parameters. Macros are analogous to functions in programming languages (but different from mathematical functions as we have discussed). Some macros only work in math mode, such as the `\frac` in the example below---the `$` is one way to denote math mode.

```
\LaTeX % command with no input

\textbf{Bold} % command with one input

$\frac{a}{b}$ % command with two inputs
```
{{< figure src="commands.png" title="Commands and arguments" alt="Commands and arguments" >}}

The inputs to a macro follow the macro and each input is surrounded by curly braces (`{}`). If you don't use curly braces around inputs, the command will only apply to the first
character after the command.

```
\textbf Bold  % only applies to the character B

$\frac ab cd$ % `a` will be the first input 
              % and `b` the second
```
{{< figure src="commands_bad.png" title="Surround command inputs with curly braces" alt="If you don't surround command inputs with curly braces, only one character is assumed as the input." >}}
Curly braces act as a grouping method to ensure commands apply to a sequence of
characters. 

## Comments

Comments in LaTeX start with the `%` character.  You can comment out longer regions using a conditional (started with `\iffalse` and ended with if backwards `\fi`):

```
% $P :=$ Latex is great

\iffalse
This is a lot of junk that will not show up in the rendering!
\fi
```



# Seperating Lines

One of the philosophies behind the design of LaTeX is that the structure of a document is separated from its presentation. So, most whitespace (including newlines) in the source do not influence the rendering.

To start a new paragraph in LaTeX use two new lines (i.e., a blank line):

```
Paragraph 1.
Second line in paragraph 1.

Paragraph 2. Second sentence in paragraph 2.
Third sentence in paragraph 2.
```
{{< figure src="paragraph.png" title="Paragraph separation" alt=" Text is separated into paragraphs using two end-line characters." >}}

You can also use the `\\` command to start a new line without starting a new paragraph:

```
Sentence 1, paragraph 1.\\
Sentence 2, paragraph 1.\\Sentence, paragraph 1.

New paragraph.
```
{{< figure src="linebreak.png" title="Breaking lines in a paragraph" alt="Breaking lines in a paragraph" >}}


Why ignore new lines?

This might seem annoying at first since it's more natural to separate paragraphs with a single end-line. However, this comes in handy in two respects. First, when writing long paragraphs with equations or links, it might be easier to edit when these big things are separate. For example,
<pre><code>
Given that we know
$a = 2b+c$
and that
$c\in\{0,1\}$, 
then we can conclude that the statement is true.
</code></pre>
might be easier to edit than
<pre><code>
Given that we know $a = 2b+c$ and that $c\in\{0,1\}$, then we can conclude that the statement is true.
</code></pre>
The second reason is version control. If you're keeping track of your document using Git, for example, it's better to separate paragraphs into shorter segments so smaller changes are easy to track.

