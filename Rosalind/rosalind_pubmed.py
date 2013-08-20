import Bio
from Bio import Entrez
Entrez.email = "simon.boardman@leedsth.nhs.uk"
handle = Entrez.esearch(db='pubmed', term='"Lopes-Viana S"[Author] AND "2005"[PDAT]')
record = Entrez.read(handle)
print record["IdList"]
