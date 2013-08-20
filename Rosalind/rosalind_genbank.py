import Bio
from Bio import Entrez
Entrez.email = ('simon.boardman@leedsth.nhs.uk') #always tell NCBI who you are
handle = Entrez.esearch(db='nucleotide', term='"Laparocerus"[Organism] AND ("2005/01/01 "[Publication Date] : "2009/09/14"[Publication Date])') #search GenBank for term input.
record = Entrez.read(handle) #search!
print record['Count'] #expect '7' to be returned.
