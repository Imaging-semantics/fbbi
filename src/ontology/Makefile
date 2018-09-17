
# This Makefile is for use by the fbbi Release Manager.
#
# requirements: Oort (http://code.google.com/p/owltools/wiki/OortIntro)
#
# To make a release, type 'make release' in this directory

OBO = http://purl.obolibrary.org/obo

initial-build: fbbi.obo
build: fbbi.obo minidiff
release: fbbi.obo diff

# all release files are derived from the editors version.
# we use the default Oort setup (hermit as reasoner)

fbbi_pre.owl: fbbi-edit.obo fbbi-ext.ofn
	robot merge --input fbbi-edit.obo --input fbbi-ext.ofn -o $@

fbbi.obo: fbbi_pre.owl
	ontology-release-runner $< --allow-overwrite --asserted --simple

# ----------------------------------------
# Diffs
# ----------------------------------------

# 
diff: fbbi.obo
	cd diffs && touch fbbi-diff && rm fbbi-*diff* && make

# Minidiff: intra-release differences
minidiff: fbbi.obo
	cd diffs  && touch fbbi-diff && rm fbbi-*diff* && make TGTS='html txt' SRC=../fbbi.obo && mail -s fbbi-diffs RELEASE-MANAGER@FOO.BAR < fbbi-combined-diff.txt

