def proteins(strand):
    codon = ""
    protein_list = []
    stop_codons = ['UAA', 'UAG', 'UGA']
    translation_list = {'Methionine': ['AUG'],
                        'Phenylalanine': ['UUU', 'UUC'],
                        'Leucine': ['UUA', 'UUG'],
                        'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
                        'Tyrosine': ['UAU', 'UAC'],
                        'Cysteine': ['UGU', 'UGC'],
                        'Tryptophan': ['UGG'],
                        }
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if codon in stop_codons:
            return protein_list
        else:
            for key, value in translation_list.items():
                for c in value:
                    if c == codon:
                        protein_list.append(key)
    return protein_list
