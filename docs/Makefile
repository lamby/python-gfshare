SPHINXOPTS    =
SPHINXBUILD   = python3 -msphinx
SPHINXPROJ    = python-gfshare
SOURCEDIR     = .
BUILDDIR      = _build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

push:
	git checkout master
	cd .. && ./setup.py clean && ./setup.py build
	$(MAKE) clean html
	git checkout gh-pages
	rsync -av _build/html/* ..
	cd .. && rm -rf ../docs/ ../.eggs/ && git add -A .
	git commit -m "Update docs"
	git push origin gh-pages
	git checkout master
