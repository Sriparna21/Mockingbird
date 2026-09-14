import pandas as pd
from sqlalchemy import create_engine, text
from database.queries import (get_prediction_query)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix



def load_prediction_data():
    engine = create_engine('postgresql://sriparnaghoshchaudhuri:sriparnaghoshchaudhuri@localhost:5432/project_db')

    data = pd.read_sql(text(get_prediction_query),engine)

    return data

def prepare_training_data(data):

    train_df = data[data['poutcome'].isin(['success','failure'])].copy()

    X = train_df.drop(columns='poutcome')
    y = train_df['poutcome']

    X_train, X_test, y_train , y_test = train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)

    return X_train, X_test, y_train , y_test 
    


# prediction_df = data[data['poutcome'].isin(['unknown','other'])].copy()

def build_processor():
    categorical_features = ['job','marital','education','housing','loan','deposit']
    numerical_features = ['age','campaign','pdays','balance']

    preprocessor = ColumnTransformer(
        transformers=[
        ('categorical',OneHotEncoder(handle_unknown='ignore'),categorical_features),
        ('numeric',StandardScaler(),numerical_features)
        ]
        )   

    return preprocessor


def process_training_data(X_train,X_test,preprocessor):
    X_train_processed = preprocessor.fit_transform(X_train)

    X_test_processed = preprocessor.transform(X_test)

    return X_train_processed, X_test_processed


def train_model(X_train_processed, y_train):
    model = LogisticRegression()
    return model.fit(X_train_processed,y_train)


def evaluate_model(model,X_test_processed,y_test):
    y_pred = model.predict(X_test_processed)

    accuracy = accuracy_score(y_test,y_pred)
    classification_report_result = classification_report(y_test,y_pred)
    confusion_matrix_result = confusion_matrix(y_test,y_pred)

    return y_pred, accuracy,classification_report_result,confusion_matrix_result

def predict_customer(customer,preprocessor,model):
    cust = pd.DataFrame([customer])
    cust_transformed = preprocessor.transform(cust)
    predicted = model.predict(cust_transformed)
    probabilities = model.predict_proba(cust_transformed)

    result={'prediction':predicted[0],
        'failure_probability': float(probabilities[0][0]),
        'success_probability': float(probabilities[0][1])}

    return result


data = load_prediction_data()

X_train, X_test, y_train , y_test = prepare_training_data(data)

preprocessor = build_processor()

X_train_processed, X_test_processed = process_training_data(X_train,X_test,preprocessor)

model = train_model(X_train_processed , y_train)

y_pred, accuracy,classification_report_result,confusion_matrix_result = evaluate_model(model,X_test_processed,y_test)

# print(accuracy)
# print(confusion_matrix_result)
# print(classification_report_result)

customer = {
    "age": 42,
    "job": "management",
    "marital": "married",
    "education": "tertiary",
    "housing": "yes",
    "loan": "no",
    "campaign": 2,
    "pdays": 180,
    "deposit": "yes",
    "balance": 3500
}

result = predict_customer(customer,preprocessor,model)

print(result)