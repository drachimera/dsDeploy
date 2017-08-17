from sklearn.externals import joblib
from sklearn.pipeline import make_pipeline

def readmit_proba(prior_util_6m_ip_count=0, index_los=0, ch_index=0, icu_flag='n', lab_crea_resultn=0.0):
    
    X = locals()
    X = X.values()
    if X[3] == 'n':
        X[3] = 0
    else:
        X[3] = 1
    
    gbm = joblib.load('simplifiedSNF_gbm.pkl')
    
    return gbm.predict_proba(X)[0][1]

def readmit(prior_util_6m_ip_count=0, index_los=0, ch_index=0, icu_flag='n', lab_crea_resultn=0.0):
    
    X = locals()
    X = X.values()
    if X[3] == 'n':
        X[3] = 0
    else:
        X[3] = 1
    
    gbm = joblib.load('simplifiedSNF_gbm.pkl')
    
    return gbm.predict(X)[0]