import json
import pandas as pd
from LanguageBiasesInReddit import DADDBias_ICWSM



# path of the training data for a particular subreddit
train_path = "data/askredd.csv"
model_path = "DADDBiasResModel_askredd"

DADDBias_ICWSM.TrainModel(
    train_path,  # csv file with reddit (or other platform's) comments
    "Comment",  # column with the comments
    outputname=model_path,  # output model filename
    window=4,  # window
    minf=10,  # minimum frequency (words less frequent than threshold will be ignored)
    epochs=1,  # training epochs
    ndim=200,  # embedding dimensions
    verbose=False,  # verbose
)

ts1 = ["sister" , "female" , "woman" , "girl" , "daughter" , "she" , "hers" , "her"]
ts2   = ["brother" , "male" , "man" , "boy" , "son" , "he" , "his" , "him"]  


# Getting biased wordd
b1,b2 = DADDBias_ICWSM.GetTopMostBiasedWords(
    model_path,                         
    300,                               
    ts1,                               
    ts2,                               
    ['JJ','JJR','JJS'],                
    True)                              

# Making clusters
cl1,cl2 = DADDBias_ICWSM.Cluster(
  b1,                                
  b2,                                
  0.15,                              
  100                                
)

word_clusts1 = {}
for i, cluster in enumerate((cl1)):
    # biased words towards women
    word_clusts1[i] = [x["word"] for x in cluster]

word_clusts2 = {}
for i, cluster in enumerate(cl2):
    # biased words towards women
    word_clusts2[i] = [x["word"] for x in cluster]


# alternatively if cl1 and cl2 are of same size then we can do
# word_clusts1 = {}
# word_clusts2 = {}
# for i, cluster1, cluster2 in enumerate(zip(cl1, cl2)):
#     # biased words towards women
#     word_clusts21[i] = [x["word"] for x in cluster1]
#     word_clusts2[i] = [x["word"] for x in cluster2]


with open("data/cl2.json", "w") as f:
    json.dump(word_clusts2, f)



