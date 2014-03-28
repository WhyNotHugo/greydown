PREFIX = /usr

install:
	install -Dm 755 greydown.py $(DESTDIR)$(PREFIX)/bin/greydown
	install -Dm 644 LICENSE $(DESTDIR)$(PREFIX)/share/licenses/greydown/LICENSE
