all: dogecode-whitepaper.html dogecode-whitepaper.pdf

dogecode-whitepaper.pdf: dogecode-whitepaper.md
	pandoc dogecode-whitepaper.md -o dogecode-whitepaper.pdf

dogecode-whitepaper.html: dogecode-whitepaper.md
	pandoc dogecode-whitepaper.md -o dogecode-whitepaper.html

clean:
	rm -f dogecode-whitepaper.html dogecode-whitepaper.pdf
