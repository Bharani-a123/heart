import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Load the dataset
df = pd.read_csv('heart_cleveland_upload.csv')

# Print the column names for confirmation
print("✅ Columns in dataset:")
print(df.columns)

# Binary target: convert all values > 0 to 1
df['condition'] = df['condition'].apply(lambda x: 1 if x > 0 else 0)

# Features and label
X = df.drop('condition', axis=1)
y = df['condition']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
dump(model, 'heart_model.joblib')

print("✅ Model trained and saved as heart_model.joblib")
