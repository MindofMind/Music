#Understanding the data:
#Under this section, we will explore the dataset and understand it in detail.
#converting 2D array into 1D array

notes_ = [element for note_ in notes_array for element in note_]

#No. of unique notes
unique_notes = list(set(notes_))
print(len(unique_notes))
