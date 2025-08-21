# Makefile (paper)
# Requires latexmk + xelatex + biber installed on the system
# Usage: make    (build)
#        make clean

MAIN=main

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
\tlatexmk -xelatex -quiet -interaction=nonstopmode $(MAIN).tex
\tbiber $(MAIN)
\tlatexmk -xelatex -quiet -interaction=nonstopmode $(MAIN).tex
\tlatexmk -xelatex -quiet -interaction=nonstopmode $(MAIN).tex

clean:
\tlatexmk -C
\trm -f $(MAIN).pdf
