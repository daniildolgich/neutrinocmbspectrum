% _MScDiss2017_cls.cls Thesis Dissertation class
% Modified by Jim Emerson from Ian Huston from original downloaded from
% http://www.doc.ic.ac.uk/~dwagner/downloads.php

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{_MScDiss2017_cls}
 
\DeclareOption{doublespacing}{\AtBeginDocument{\doublespacing}}
\DeclareOption{onehalfspacing}{\AtBeginDocument{\onehalfspacing}}
\DeclareOption{titlepagenumber=off}{\AtEndOfClass{\renewcommand{\titlepagestyle}{empty}}}
\DeclareOption{titlepagenumber=on}{\AtEndOfClass{\renewcommand{\titlepagestyle}{plain}}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{scrreprt}}

\ExecuteOptions{onehalfspacing,titlepagenumber=off,a4paper,12pt,twoside}

\ProcessOptions\relax

\LoadClass{scrreprt}
\RequirePackage{setspace}
\RequirePackage[left=4.0cm,right=2.0cm,top=3.50cm,bottom=3.0cm]{geometry}% MARGINS
 
\setkomafont{sectioning}{\rmfamily\bfseries}

\newcommand*{\@supervisor}{}
\newcommand*{\supervisor}[1]{\gdef\@supervisor{#1}}

\newcommand*{\@declaration}{}
\newcommand*{\declaration}[1]{\gdef\@declaration{#1}}
 
\newcommand*{\@acknowledgements}{}
\newcommand*{\acknowledgements}[1]{\gdef\@acknowledgements{#1}}

\input{_MScDiss2017_Preambles.cls} % uncomment this to get MSc start stuff

\renewenvironment{abstract}{\chapter*{Abstract}\thispagestyle{plain}}
\clearpage%{\cleardoublepage}

\input{_jnls.cls} % for interpretation of ADS journal abbreviations in Bibliography and bibfile

\endinput
%%
%% End of file `_MScDiss2017_cls.cls'.
