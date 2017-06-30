MARKDOWN=$(shell find . -iname "*.md" -not -iname "index.md")
INDEX=$(shell find . -name "index.md")
INDEXHTML=$(INDEX:.md=.html)
HTML=$(MARKDOWN:.md=.html)
INDEXDIRS=$(shell find . -type d -not -path './.git*')
SS1=normalize.css
SS2=sakura.css

.PHONY: all notes tar clean indexhtml
all: notes
	$(MAKE) indexhtml

indexhtml: $(INDEXHTML) $(INDEXDIRS)

notes: $(HTML)

tar: $(MARKDOWN)
	tar --exclude=notes.tar.gz --exclude=.git/ -czvf notes.tar.gz ./

clean:
	rm $(HTML)
	rm $(INDEXHTML)

%index.html: %index.md
	pandoc --css /$(SS1) --css /$(SS2) --from markdown --to html $< -o $@

.SECONDEXPANSION:
%index.md: $$(wildcard %)
	echo $@
	zsh gen_index.sh "$@"

%.html: %.md
	pandoc --toc --css /$(SS1) --css /$(SS2) --from markdown --to html $< -o $@
