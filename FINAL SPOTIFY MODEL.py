#!/usr/bin/env python
# coding: utf-8

# # Final Project (Individual)
# 
# #### Each Each student picks a project assigned at the beginning of the course and will prepare a case study on a chosen topic. There are two tracks for the project. Student, based on personal interest will choose one of the two  tracks. The project output at the end of the course will be a paper describing the case prepared and a presentation to the class.
# 
# #### Business Application Track: In this track, the student plays a role of a business consultant addressing a serious business issue and presents a solution that addresses the issue using Machine Learning. The student will choose one out of three choice business problems given during the beginning of the course. The student will apply the learnings from the course supplemented by research to analyze the problem and provide a recommendation that addresses it using Machine Learning.

# In[1]:


import pandas as pd


# In[2]:


spotifydata = pd.read_excel('\\Users\Angie Menjivar\Downloads\YourLibrary (1).xlsx')


# In[3]:


spotifydata


# In[4]:


spotifydata.columns


# In[5]:


spotlist = list(spotifydata)
print(spotlist)


# In[6]:


spotifydata.count()


# In[7]:


spotifydata.isnull().sum()


# In[8]:


# taking out unnecessary columns
spotdata = spotifydata.drop(columns=['artist.1', 'album.1', 'uri.1','Unnamed: 7','Unnamed: 8', 'Unnamed: 9', 'name',
                            'uri.2','Unnamed: 12', 'Unnamed: 13'])
spotdata.count()


# In[9]:


spotdata


# In[10]:


track = spotdata.track


# In[11]:


track


# In[12]:


import random

# Define a prediction model (in this case, a random shuffle)
def predict_next_song(current_song, track):
    next_song = random.choice(track)
    while next_song == current_song:
        next_song = random.choice(track)
    return next_song

# Shuffle the playlist by predicting the next song
current_song = None
shuffled_playlist = []
for i in range(len(track)):
    next_song = predict_next_song(current_song, track)
    shuffled_playlist.append(next_song)
    current_song = next_song

# Print the shuffled playlist
shuffled_playlist


# In[13]:


# showing list of songs 
shuffled_playlist

