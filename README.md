# Genomic Sequence Analyzer 🧬

This project analyzes gene sequences from a FASTA file using Biopython. It was built as a bioinformatics mini-tool to perform:

- ✅ Motif search: Counts how many sequences contain the `"GCGC"` pattern
- ✅ Sequence length classification: Labels each gene as Short, Medium, or Long
- ✅ Sequence summary: Counts total genes and finds longest and shortest
- ✅ GC content analysis: Finds the gene with the highest GC content

## 📁 Input
A FASTA file containing gene sequences (e.g., `genes.fa`)

## 💻 Output
Text file with:
- Total and longest gene summary
- also gives output of the count of GCGC,counts the total genes and gives shortest and longest and also does gc_content analysis

## 🧪 Built With
- Python 3
- Biopython

## 🔄 Run This
```bash
python analyzer.py
