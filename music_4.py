#importing library
from collections import Counter

#computing frequency of each note
freq = dict(Counter(notes_))

#library for visualiation
import matplotlib.pyplot as plt

#consider only the frequencies
no=[count for _,count in freq.items()]

#set the figure size
plt.figure(figsize=(5,5))

#plot
plt.hist(no)

#From the above plot, we can infer that most of the notes have a very low frequency. 
#So, let us keep the top frequent notes and ignore the low-frequency ones. 
#Here, I am defining the threshold as 50. Nevertheless, the parameter can be changed.

frequent_notes = [note_ for note_, count in freq.items() if count>=50]
print(len(frequent_notes))
