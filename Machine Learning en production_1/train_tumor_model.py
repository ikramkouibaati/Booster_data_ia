import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("tumor_two_vars.csv")
X = df[['size', 'p53_concentration']]
y = df['is_cancerous']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

joblib.dump(model, "cancer_model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("✅ Modèle et scaler sauvegardés avec succès.")
