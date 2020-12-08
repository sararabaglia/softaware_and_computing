#!/bin/bash

# make summary tex file to watch
cat <<EOF
\documentclass[landscape]{article}
\usepackage[landscape,a4paper,margin=1cm]{geometry}
\begin{document}
\footnotesize
EOF

while read file
do
    cat <<EOF
\section{$(echo $(basename $file .tex) | sed 's/_/\\_/g')}
\input{$file}
EOF
done

cat <<EOF
\end{document}
EOF

