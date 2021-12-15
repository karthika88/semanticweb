import joblib
import numpy as np
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import nltk

def remove_stopword(text):
    stopword=nltk.corpus.stopwords.words('english')
    stopword.remove('not')
    a=[w for w in nltk.word_tokenize(text) if w not in stopword]
    return ' '.join(a)

remove_special=lambda s:''.join([i for i in str(s) if i.isalnum() or i==' '])

def make_prediction(input_data):

    model = joblib.load('model.pkl')

    encoder = preprocessing.LabelEncoder()
    encoder.classes_ = np.load('classes.npy', allow_pickle=True)
    
    input_data=remove_special(input_data)
    input_data=remove_stopword(input_data)
    input_array=np.array([input_data])

    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl", "rb")))
    input_vec = transformer.fit_transform(loaded_vec.fit_transform(input_array))

    prediction = encoder.inverse_transform(model.predict(input_vec))

    return prediction[0]
