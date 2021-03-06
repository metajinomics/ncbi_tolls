import sys 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


genome=SeqIO.read(sys.argv[1], 'genbank')

n = 0
l = []

for record in list(SeqIO.parse(sys.argv[1], 'genbank')):
    org = record.description.replace(' ','_').split(',')[0]
    #org = record.annotations["source"].replace(' ','_')
    genome_name = record.name
    tax = record.annotations['taxonomy'][1]
    for feat in genome.features:
        if feat.type == "rRNA":
            if '16S' in feat.qualifiers['product'][0]:#or '16S ribosomal' for strict match
                start = feat.location.start.position
                end = feat.location.end.position
                pos = [start, end]
                l.append(pos)
                idname = record.id.split('.')
                print '>' + tax + "_" + org + str(n)                
            #            print '>' + sys.argv[1].split('.')[0] + ' 16S rRNA gene ' + str(n) 
                print feat.extract(genome.seq)
                n =+ 1
                break;
