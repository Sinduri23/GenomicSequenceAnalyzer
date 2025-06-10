#!/usr/bin/env python
# coding: utf-8

# ## to run a loop in a fasta file we need to open fasta files using biopython that is through bioseqio

# In[70]:


import Bio.SeqIO


# In[41]:


sequences=Bio.SeqIO.parse("C:\\Users\\sindu\\Downloads\\genes.fa",'fasta')


# In[43]:


count_gcbc = 0
for record in sequences:
    sequence = str(record.seq).upper()
    
    # Check if the sequence contains the substring "GCGC"
    if "GCGC" in sequence:
        count_gcbc += 1


# In[44]:


print(count_gcbc)


# ## question2
# we have to go through each seq and classify them as med small or high

# In[56]:


output_file='C:\\Users\\sindu\\OneDrive\\Desktop\\researxh internship\\genelenasg2'


# In[59]:


with open(output_file, "w") as out_file:
    # Step 3: Parse sequences
    for record in Bio.SeqIO.parse("C:\\Users\\sindu\\Downloads\\genes.fa",'fasta'):
        gene_id = record.id
        seq_length = len(record.seq)

        # Step 4: Classify based on length
        if seq_length < 300:
            classification = "Short"
        elif 300 <= seq_length <= 1000:
            classification = "Medium"
        else:
            classification = "Long"

        # Step 5: Write to output file
        out_file.write(f"{gene_id}\t{classification}\n")

print("Classification complete! Output saved to genes_length_classification.txt")

    


# ## for q3 we need to find out the no of seq and also the longest seq

# In[73]:


# Initialize
total_count = 0
longest_length = 0
longest_gene = ""

# Loop through all sequences
for recor in Bio.SeqIO.parse("C:\\Users\\sindu\\Downloads\\genes.fa", "fasta"):
    total_count += 1
    seq_length = len(recor.seq)

    if seq_length > longest_length:
        longest_length = seq_length
        longest_gene = recor.id

# Output results
print(f"Total number of sequences: {total_count}")
print(f"Longest gene: {longest_gene} ({longest_length} bases)")


# ## q4 make a dict using gene id and length of that seq

# In[74]:


import Bio.SeqIO


# In[85]:


dict_seq=dict()


# In[88]:


for x in Bio.SeqIO.parse("C:\\Users\\sindu\\Downloads\\genes.fa", "fasta"):
    seq_name=x.id
    len_seq=len(x.seq)
    dict_seq[seq_name]=len_seq


# In[89]:


dict_seq


# ## now we need to also print the gene id which has the shortest seq

# In[95]:


short=min(dict_seq,key=dict_seq.get)
short


# In[94]:


dict_seq[short]


# ## question5

# In[109]:


import Bio.SeqIO
from Bio.SeqUtils import gc_fraction


# In[110]:


file="C:\\Users\\sindu\\Downloads\\genes.fa"


# In[113]:


def find_gc_content(file):
    for record in Bio.SeqIO.parse(file, "fasta"):
        seq=record.seq
        name=record.id
        print(f'{gc_fraction(seq)} and its name is :{name}')
    
    
find_gc_content(file) 


# In[120]:


from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def find_high_gc(file):
    highest_gc = 0
    highest_gene = ""

    for record in SeqIO.parse(file, "fasta"):
        gc = gc_fraction(record.seq)
        name = record.id

        if gc > highest_gc:
            highest_gc = gc
            highest_gene = name

    print(f"The gene with the highest GC content is: {highest_gene} → {highest_gc:.2f}%")

# Call the function
find_high_gc(file)


# In[ ]:





# In[ ]:




