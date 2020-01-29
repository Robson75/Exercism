def to_rna(dna_strand):
    in_nucleotides = "ACGT"
    out_nucleotides = "UGCA"
    tran_table = str.maketrans(in_nucleotides, out_nucleotides)
    rna_strand = dna_strand.translate(tran_table)
    return rna_strand
