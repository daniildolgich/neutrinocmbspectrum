\renewcommand*{\maketitle}{
\begin{titlepage}
 \par
 \clearpage
 \thispagestyle{\titlepagestyle}
 \noindent\begin{minipage}[t]{\textwidth}
  \centering\large
  School of Physics \& Astronomy
  
  Queen Mary University of London
 \end{minipage}
 
 \null\vfill
 \begin{center}
  {\titlefont\huge \@title\par}
  \vskip 3em
  {\Large \lineskip 0.75em
  \begin{tabular}[t]{c}
   \@author
  \end{tabular}\par}
  \vskip 1.5em
%   {\Large \@date \par}
  \vskip \z@ \@plus3fill
  \ifx\@supervisor\@empty \else
  {\Large Supervised by \@supervisor \par}
  \fi
  \vskip 3em
 \end{center}\par
 \noindent\begin{minipage}[b]{\textwidth}
  \centering
 Submitted August 2019 in part fulfilment of the requirements for the degree of\\
 Bachelor in Physics and Particle Physics at Queen Mary University of London  
\end{minipage}

 \ifx\@declaration\@empty\else{
 \clearpage
 %\cleardoublepage
 \chapter*{Declaration}
 \thispagestyle{plain}
 \@declaration
 \par\vspace{3cm}
 \hfill\@author
 \clearpage 
 %\cleardoublepage
}\fi

\ifx\@acknowledgements\@empty\else{
\clearpage %\cleardoublepage
 \chapter*{Acknowledgements}
 \thispagestyle{plain}
 \@acknowledgements
 \par\vspace{3cm}
 \hfill %\clearpage %\cleardoublepage
 }\fi

\end{titlepage}
} 
