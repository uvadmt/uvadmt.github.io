+++ 
author="Amro Aljundi" 
title = "Typesetting using Overleaf and LaTeX" 
date = "2025-02-16" 
slug = "latex" 
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

{{< figure src="render.png" title="Simple render" alt="A render of LaTeX code" >}}



## Macros

A macro in LaTeX is something that begins with `\`. This includes math
commands like `\times` or non-math commands like `\textbf`. A macro can take zero or more parameters. Macros are analogous to functions in programming languages (but different from mathematical functions as we have discussed). An example of a macro with one input is `\textbf{Bold}` which will render as bold text. 

The inputs to a macro follow the macro and each input is surrounded by curly braces (`{}`). If you don't use curly braces around inputs, the command will only apply to the first
character after the command. Curly braces act as a grouping method to ensure commands apply to a sequence of
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
{{< figure src="paragraph.png" alt=" Text is separated into paragraphs using two end-line characters." >}}

You can also use the `\\` command to start a new line without starting a new paragraph:

```
Sentence 1, paragraph 1.\\
Sentence 2, paragraph 1.\\Sentence, paragraph 1.

New paragraph.
```
{{< figure src="linebreak.png" alt="Breaking lines in a paragraph" >}}

<details>
<summary>Why ignore new lines?</summary>
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
</details>

## Environments

An environment in LaTeX is a block of code between a `\begin` and an `\end`
command pair. An environment has its own formatting rules. For example, in an
`enumerate` environment, the `\item` command will create a new item in a numbered
list. In an 'itemize' environment, the `\item` command creates a new item but in a bulleted (or some other symbol) list.

In an `equation` environment, code is automatically interpreted in math
mode. 

```
\begin{itemize}
   \item Text in this environment is formatted as a bulleted list.
   \item For cosemetic reasons, a list should always have at least two items, unlike a set which can be empty.
\end{itemize}
\begin{equation*}
f(x) = 2x+5
\end{equation*}
```

Because the math environment is so common, there are several different ways to denote it. The most compact is to use `$` &mdash; text between two `$` will be rendered as math. 

# Numbered lists

As we saw in class, a good way to write proofs is to separate your steps into
a numbered list. Rather than numbering your items and numbering them manually,
LaTeX comes with a neat tool for doing this dirty work for you.

## Writing numbered lists

When writing a proof that uses multiple steps, you can use the `enumerate`
environment in LaTeX.  
```
Text before the enumerated list.
\begin{enumerate}
   \item The item command signals starting a new step. 
   Just like other parts of latex, an end-line character doesn't create a 
   new paragraph.
   
   You can write multiple paragraphs in a single item.
   \item Second step.
\end{enumerate}
Text after the enumerated list.
```

{{< figure src="enum_list_1.png" alt="Simple enumerated list" >}}

## Nested lists (sublists)

Lists can be nested. Simply start a new `enumerate` environment at the point
where you want the sublist to be created.

```
\begin{enumerate}
   \item first step
   \item second step. Includes the following substeps: 
   \begin{enumerate}
      \item substep 1.
      \item substep 2.
   \end{enumerate}
   still in the second step.
   \item substep 3.

\end{enumerate}
```
{{< figure src="enum_sublist.png" alt="Sublists" >}}

## Referencing items in lists
If you want to reference an item in a list, you must give the item a label. This is done using the `\label{}` command:
```
   \item this step will be labeled "step-one"\label{step-one}
```
Now, you can refer to this item anywhere in your text using the `\ref{}` command
 by passing that item's label.

```
\begin{enumerate}
   \item first step.\label{step-one}   
   \item second step. Includes the following 
   substeps: 
   \begin{enumerate}
      \item substep 1.\label{proof1:s1:ss1}
   \end{enumerate}

\end{enumerate}
References to items outside the list work, e.g. 
a reference to step \ref{step-one} or step 
\ref{proof1:s1:ss1}.
```
{{< figure src="enum_sublist_ref.png" alt="Sublists references" >}}

# Math in latex
Math in latex is one of its strongest features. There are two modes for math in
LaTeX: __inline math mode__, or __display math mode__. Inline math is when a
mathematical equation is within a text paragraph, display math is when an
equation is on its own line.

## Inline math mode
You can add a mathematical equation to a paragraph in LaTeX by surrounding the
equation with `$` symbols.

```
This equation $x^2+5 = y$ is rendered 
in the middle of the paragraph.
```
{{< figure src="inline_math.png" alt="Inline math" >}}

## Display math mode
If you want your equation to be prominent and take up the whole line, you can
use display math mode. You can trigger display math using many environments. The
simplest is the `equation*` environment.

```
The following equation will take up its own line
\begin{equation*}
   f(x) = x^{x}
\end{equation*}
```

{{< figure src="display_math.png" title="Display math" alt="Display math" >}}
Display math equations can also be added in the middle of an enumerated list.

```
\begin{enumerate}
   \item definitions.
   \item some case\begin{enumerate}
         \item a display math equation
         \begin{equation*}
            f(x|y) = xy-2
         \end{equation*}
      \end{enumerate}
\end{enumerate}
```
{{< figure src="display_math_enum.png" alt="Display math in an enumerated list" >}}

## Splitting equations over multiple lines
Sometimes you want to show multiple steps of a derivation, or your equation is
too long to fit in a single line. In such cases, you can use the `align*`
enviornment. Inside this environment, you can separate lines using `\\`, which
you add to every line except the last one. By default, consequent lines will be
right-aligned.

```
\begin{align*}
   y = 3 + 2 - 3 +4 - 2\\
   + 4 +11 \\
   = 19
\end{align*}
```
{{< figure src="align_no_sep.png" alt="Seperating an equation into multiple lines" >}}

## Splitting equations over lines and align them
You can align the lines of a multi-line equation around certain points in a
line. This is especially useful when simplifying an equation or moving things
around an inequality. This is done using the `align*` environment. Inside the
environment, split lines using `\\` and specify where the symbols should align
using the `&` symbol. You can think of `&` as a separator of columns in a table,
where each `&` character within a line represents the beginning of a new column.



```
\begin{align*}
   y &= 3 + 2 - 3 
   +4 - 2\\ % Note that lines 1 and 2 are rendered 
   %as a single line
   & + 4 +11 \\
   & = 19
\end{align*}
\begin{align*}
   3+y &\geq x\\
   3 & \geq x-y
\end{align*}
\begin{align*}
   2x + 3 &= 11 \\
   2x &= 8 \\
   x &= 4
\end{align*}
```
{{< figure src="align.png"  alt="Aligning equations" >}}

## Numbering and referencing equations
Sometimes, it is useful to number equations and reference them in your proof. This works for display math equations. To make your equations numbered, simply remove the `*` from the environment name. 
```
\begin{equation}
x= y
\end{equation}
\begin{align}
x = 3y + z \\
+ 5v
\end{align}
```
{{< figure src="number.png" title="Numbering equations" alt="Numbering equations" >}}

You can give numbered equations a label and then reference them in your text.
This is done through the `\label{}` and `\ref{}` commands. To reference an
equation, add a `\label{}` command to the end of the equation (or the line for a
multi-line equation) with your desired label, and then use `\ref{}` to refer to
that equation. 

Note: for multi-line equations using `align`, you can add `\nonumber` to lines
in the equation that you don't want to number, e.g., those that are a part of
longer equations.

```
\begin{enumerate}
   \item definitions.
   \item some case\begin{enumerate}
         \item a display math equation
         \begin{equation}
            f(x|y) = xy-2\label{proof2:eq}
         \end{equation}
         \item two lines with different numbers 
         \begin{align}
            x &= 3y+5z+\sum_1^{10} v \nonumber\\
            & +(2\times 3)y \label{proof2:eq:start}\\
            x &= 1.5\times 2 \times y \label{proof2:eq:interm}
         \end{align}
      \end{enumerate}
   \item From equations \ref{proof2:eq} and \ref{proof2:eq:interm} we conclude ...
\end{enumerate}
```
{{< figure src="ref_equation.png" alt="Referencing equations" >}}

## Common math commands and operations
Writing math in inline or display math modes works very similarly. This section
shows some of the operations you will need to use.
### Common operators
Here is a list of commonly used operators in proofs
| LaTeX Code | <div style="text-align: center;">Rendered Result</div> | Description |
|------------|----------------|-------------|
| `$\implies$` | <div style="text-align: center;">\\(\implies\\)</div> | Implies |
| `$\iff$` |<div style="text-align: center;"> \\(\iff\\)</div> | If and only if (logical equivalence) |
| `$\neg$` | <div style="text-align: center;">\\(\neg\\)</div> | Logical NOT |
| `$\land$` | <div style="text-align: center;">\\(\land\\)</div> | Logical AND |
| `$\lor$` | <div style="text-align: center;">\\(\lor\\)</div> | Logical OR |
| `$\in$` | <div style="text-align: center;">\\(\in\\)</div> | Element of (set membership) |
| `$\notin$` | <div style="text-align: center;">\\(\notin\\)</div> | Not element of |
| `$\subseteq$` | <div style="text-align: center;">\\(\subseteq\\)</div> | Subset (subset or equal to) |
| `$\subset$` | <div style="text-align: center;">\\(\subset\\)</div> | Proper subset (strict subset) |
| `$\cup$` | <div style="text-align: center;">\\(\cup\\)</div> | Set union |
| `$\cap$` | <div style="text-align: center;">\\(\cap\\)</div> | Set intersection |
| `$\emptyset$` | <div style="text-align: center;">\\(\emptyset\\)</div> | Empty set |
| `$\mathbb{N}$` | <div style="text-align: center;">\\(\mathbb{N}\\)</div> | Natural numbers |
| `$\mathbb{Z}$` | <div style="text-align: center;">\\(\mathbb{Z}\\)</div> | Integers |
| `$\mathbb{Q}$` | <div style="text-align: center;">\\(\mathbb{Q}\\)</div> | Rational numbers |
| `$\mathbb{R}$` | <div style="text-align: center;">\\(\mathbb{R}\\)</div> | Real numbers |
| `$\mid$` | <div style="text-align: center;">\\(\mid\\)</div> | Such that (vertical bar in set comprehension notation) |
| `$\forall$` | <div style="text-align: center;">\\(\forall\\)</div> | For all (universal quantifier) |
| `$\exists$` | <div style="text-align: center;">\\(\exists\\)</div> | There exists (existential quantifier) |
| `$\equiv$` | <div style="text-align: center;">\\(\equiv\\)</div> | Equivalent to |
| `$\neq$` | <div style="text-align: center;">\\(\neq\\)</div> | Not equal to |
| `$\infty$` | <div style="text-align: center;">\\(\infty\\)</div> | Infinity |

Here are some examples:

```
\begin{equation*}
\{x \in \mathbb{R} \mid x > 0\}    % set notation
\end{equation*}
\begin{equation*}
\forall x \in \mathbb{N} \exists y  % quantifiers
\end{equation*}
\begin{equation*}
A \subseteq B \implies A \cap C \subseteq B \cap C  % set logic
\end{equation*}
```
$$
\{x \in \mathbb{R} \mid x > 0\}  % set notation
$$
$$
\forall x \in \mathbb{N} \exists y  % quantifiers
$$
$$
A \subseteq B \implies A \cap C \subseteq B \cap C  % set logic
$$

### Subscript and Superscript

Subscripts and superscripts (exponents) are done using the `_` and `^` operators. Each operator makes the group that follows the operator a subscript or a superscript.
Remember to always place the expression you want to make the subscript or
superscript in curly braces.
```
$$
x_{2}, x_{2+1}, x^{2}, x^{2+1}
$$
```
$$
x_{2}, x_{2+1}, x^{2}, x^{2+1}
$$

### Fractions
Fractions can be written using the `\frac{}{}` command which takes two inputs,
the numerator and the denominator, respectively.
```
$\frac{p}{q}$
```

$$
\frac{p}{q}
$$

Nested fractions are possible, but pay attention to the braces.
```
\begin{equation*}
\frac{1}{\frac{2}{3}}
\end{equation*}
```
$$
\frac{1}{\frac{2}{3}}
$$

### Brackets
You can add brackets to your equations directly, except for curly braces, as
those require an escape character.

```
\begin{equation*}
(a+1)
\end{equation*}
\begin{equation*}
[0,1]
\end{equation*}
\begin{equation*}
\{n\in\{1,2,3\} \mid n > 1\}
\end{equation*}
```
$$
(a+1)
$$
$$
[0,1]
$$
$$
\\{n\in\{1,2,3\} \mid n > 1\\}
$$


### Bracket resizing 
Brackets are generally added using a single size regardless of their contents.

```
\begin{equation*}
(\frac{\frac{\frac{a}{b}}{c}}{d})
\end{equation*}
```
$$
(\frac{\frac{\frac{a}{b}}{c}}{d})
$$

To instruct LaTeX to resize brackets, use `\left` and `\right` when adding brackets.

```
\begin{equation*}
\left(\frac{\frac{\frac{a}{b}}{c}}{d}\right)
\end{equation*}
\begin{equation*}
\left(\sum_{i=1}^{10}\frac{i}{i/2}\right)
\end{equation*}
```
$$
\left(\frac{\frac{\frac{a}{b}}{c}}{d}\right)
$$
$$
\left(\sum_{i=1}^{10}\frac{i}{i/2}\right)
$$

### Spaces
LaTeX takes care of adding spaces between characters in equations; you can't add
spaces in the rendering of an equation by adding extra spaces to the code

```
\begin{equation*}
a    =    b
\end{equation*}
\begin{equation*}
a=b 
\end{equation*}
\begin{equation*}
x y 
\end{equation*}
```
$$
a    =    b
$$
$$
a=b 
$$
$$
x y 
$$

If you wish to manually add spaces, you need to use special commands.

```
\begin{equation*}
x \; y\\        % medium space
\end{equation*}
\begin{equation*}
x \: y\\        % thin space
\end{equation*}
\begin{equation*}
x \! y\\        % negative thin space
\end{equation*}
```
{{< figure src="space.png" alt="Changing space in math mode" >}}


# Example proofs
Here are fully written proofs as examples.

## Example 1

```
Prove that for sets $A$, $B$, and $C$, if $A \subseteq B$ then 
$(A \cap C) \subseteq (B \cap C)$

\begin{enumerate}
    \item Let $A \subseteq B$ \label{step:subset}
    \item Take any $x \in (A \cap C)$ \label{step:element}
    \item From step \ref{step:element}, we know:
    \begin{enumerate}
        \item $x \in A$ \label{step:inA}
        \item $x \in C$ \label{step:inC}
    \end{enumerate}
    \item From steps \ref{step:subset} and \ref{step:inA}, we can conclude:
    \begin{equation}
        x \in B \label{eq:inB}
    \end{equation}
    \item From equation \ref{eq:inB} and step \ref{step:inC}, we have:
        \[ x \in B \land x \in C \implies x \in (B \cap C) \]
    \item Therefore, $(A \cap C) \subseteq (B \cap C)$
\end{enumerate}
```
{{< figure src="example_1.png" title="First example proof" alt="First example proof" >}}

# Images

It is easy to incorporate images that you create with some other tool (e.g., taking a picture of a hand drawn image or a drawing using digitial ink in PowerPoint) in a LaTeX document. The best way to do this is to just make a PDF file of the image (although this works with most image formats such as PNG or JPG files) and upload the image to your overleaf repository. Then, you can include it in the LaTeX file using `\includegraphics` with the name of the image file as a parameter:

```
\begin{center}
\includegraphics[width=0.8\linewidth]{setdrawing.pdf}
\end{center}
```

The optional `[width=0.8\linewidth]` scales the image to $\frac{8}{10}$ of the width of the column.


# Tables
Create tables using the `tabular` environment. The environment takes an input
which will contain a letter for each column. Letters can be `l`, `r`, or `c`
which make column left-, right-, or center-aligned. 

The following declaration creates a table with three columns, the first two left-aligned
and the last one center-aligned.

```
\begin{tabular}{llc}
%...
\end{tabular}
```

Rows inside a table are separated with `\\` (except the last row), and columns within a row are
separated with `&`. Note that you can use inline math inside a table.

```
\begin{tabular}{llc}
Name & ID & Salary \\
John & 
1234 & 
$9000.00$ \\ 
Doe &
5678 & $1000.00$
\end{tabular}
```
{{< figure src="table.png" alt="Table" >}}

## Adding visual separators
You can add vertical separators using `|` characters defined inside the tabular input braces.

```
\begin{tabular}{||l|l|c}
c1 & c2 & c3
\end{tabular}
```
{{< figure src="table_vertical.png" alt="Vertical table seperators" >}}

You can add horizontal separators using the `\hline` command.
```
\begin{tabular}{||l|l|c}
\hline
Heading 1 & Heading 2 & Heading 3\\
\hline\hline
c1 & c2 & c3
\end{tabular}
```

{{< figure src="table_horizontal.png" alt="Horizontal separators" >}}

Note that you shouldn't ever actually make tables this ugly! A good table has as few horizontal and vertical lines as possible.