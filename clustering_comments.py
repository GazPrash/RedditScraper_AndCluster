import pandas as pd
from LanguageBiasesInReddit import DADDBias_ICWSM



# loading the training data for a particular subreddit
train_data = pd.read_csv("data/askredd.csv")




DADDBias_ICWSM.TrainModel(
    "LanguageBiasesInReddit/Datasets/toy_1000_trp.csv",  # csv file with reddit (or other platform's) comments
    "Comment",  # column with the comments
    outputname="DADDBiasResModel_askmen",  # output model filename
    window=4,  # window
    minf=10,  # minimum frequency (words less frequent than threshold will be ignored)
    epochs=1,  # training epochs
    ndim=200,  # embedding dimensions
    verbose=False,  # verbose
)