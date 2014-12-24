all: dogecode-whitepaper.html dogecode-whitepaper.pdf

dogecode-whitepaper.pdf: dogecode-whitepaper.markdown
	pandoc dogecode-whitepaper.markdown -o dogecode-whitepaper.pdf

dogecode-whitepaper.html: dogecode-whitepaper.markdown
	pandoc dogecode-whitepaper.markdown -o dogecode-whitepaper.html

clean:
	rm -f dogecode-whitepaper.html dogecode-whitepaper.pdf
