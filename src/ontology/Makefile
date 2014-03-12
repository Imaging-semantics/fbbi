
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
fbbi.obo: fbbi-edit.owl
	ontology-release-runner $< --allow-overwrite --asserted --simple

# ----------------------------------------
# Imports
# ----------------------------------------
all_imports: imports/go_import.owl imports/pato_import.owl

imports/%_import.owl: fbbi-edit.owl
	owltools $< $(OBO)/$*.owl --add-imports-from-supports --extract-module -s $(OBO)/$*.owl -c --extract-mingraph  --set-ontology-id $(OBO)/go/extensions/$@ -o $@

# ----------------------------------------
# Diffs
# ----------------------------------------

# 
diff: fbbi.obo
	cd diffs && touch fbbi-diff && rm fbbi-*diff* && make

# Minidiff: intra-release differences
minidiff: fbbi.obo
	cd diffs  && touch fbbi-diff && rm fbbi-*diff* && make TGTS='html txt' SRC=../fbbi.obo && mail -s fbbi-diffs RELEASE-MANAGER@FOO.BAR < fbbi-combined-diff.txt

