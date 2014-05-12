#!/usr/bin/env jython -J-Xmx8000m
from uk.ac.ebi.brain.error import BrainException
from uk.ac.ebi.brain.core import Brain
# from owltools.graph import OWLGraphWrapper
# import sys

# baseURI = sys.argv[1]
# filePath = sys.argv[2]

# ont = Brain()
# ont.learn(URL)
# onto = ont.getOntology()
# ogw = OWLGraphWrapper(onto)

def add_long_label_to_branch(ont, parent_class, prefix, postfix):
	clist = [] 
	clist.extend(ont.getSubClasses(parent_class, 0))
	for c in clist:
		label = ont.getLabel(c)
		ont.annotation(c, 'IAO_0000589', prefix + label + postfix) #

		#ont.save(filePath)
		#ont.sleep()
