
fname=$(patsubst %.tex, %, ${main})

${fname}.pdf: ${fname}.tex 
	xelatex -shell-escape ${fname}.tex
	bibtex ${fname}.aux
	xelatex -shell-escape ${fname}.tex
	xelatex -shell-escape ${fname}.tex
	evince ${fname}.pdf&

view:
	evince ${fname}.pdf&

.PHONY:clean  
clean:
	-rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl *.gz *.snm *.nav
	-rm -rf _minted*

