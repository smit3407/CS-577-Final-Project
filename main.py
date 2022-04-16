# Normal Python Imports
import pandas as pd
import requests

# Import Datasets
import hub

apikey = 'AIzaSyC43adj1EzlXMRgvTfxi9fVymZ00eWSf3s'

# Driver Code
if __name__ == '__main__':
    # TODO
    # 1. Import Datasets as Dataframes
    covid_train = pd.read_csv('data/covid19_twitter_train.csv')
    print (covid_train)
    covid_validate = pd.read_csv('data/covid19_twitter_validate.csv')
    print (covid_validate)
    # liar_train = list(hub.load('hub://activeloop/liar-train')['id'])
    # print (liar_train)
    # liar_validate = hub.load('hub://activeloop/liar-val').pytorch(num_workers=0, batch_size=4, shuffle=False)
    # print (liar_validate)

    # 2. Run Datasets through GFCA
    # 3. Connect Google Fact Check API
    responses = []

    for item in covid_train:
        print (item)
    
    parameters = {
        query,
        languageCode,
        reviewPublisherSiteFilter,
        maxAgeDays,
        pageSize,
        pageToken,
        offset,
    }
    response = requests.get('https://factchecktools.googleapis.com/v1alpha1/claims:search')


    # 4. Output - Precision, Recall, F1-Score, False Neg

    quit()