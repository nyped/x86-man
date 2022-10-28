DESTDIR ?= /usr

.PHONY: scrap populate install

scrap:
	./x86-man/x86-man --scrap

populate:
	./x86-man/x86-man www.felixcloutier.com/x86

install:
	install -vDm0644 man7/* -t "$(DESTDIR)"/share/man/man7/
