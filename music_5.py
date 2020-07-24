#Output: 167

#As you can see here, no. of frequently occurring notes is around 170.  
#Now, let us prepare new musical files which contain only the top frequent notes



new_music=[]

for notes in notes_array:
    temp=[]
    for note_ in notes:
        if note_ in frequent_notes:
            temp.append(note_)            
    new_music.append(temp)
    
new_music = np.array(new_music)
