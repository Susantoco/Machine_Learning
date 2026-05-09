import pandas as pd
import numpy as np
import warnings as wr
from .utils import remove_outliers_iqr
from sklearn.model_selection import train_test_split

wr.filterwarnings('ignore')
pd.set_option('display.float_format', '{:.2f}'.format)

df = pd.read_csv('../features/raw/immo_data.csv')
keep_cols = ["serviceCharge", "picturecount", "pricetrend", "totalRent", "yearConstructed",
             "baseRent", "livingSpace", "noRooms", "floor", "numberOfFloors", "regio1", "heatingType", "newlyConst",
             "balcony", "hasKitchen", "cellar", "condition", "lift", "typeOfFlat", "garden", "regio2",
]
df = df[keep_cols]

num_cols = [
    "serviceCharge", # must float64
    "picturecount", # must int64
    "pricetrend", # must float64
    "totalRent", # must float64
    "yearConstructed", # must int64 -> can be float64 because of missing values
    "baseRent", # must float64
    "livingSpace", # must float64
    "noRooms", # must int64 -> can be float64 because of missing values
    "floor", # must int64 -> can be float64 because of missing values
    "numberOfFloors" # must int64 -> can be float64 because of missing values
]
cat_cols = [
    "regio1","heatingType","condition","typeOfFlat","regio2" # must object
]
bool_cols = [
    "newlyConst","balcony","hasKitchen","cellar","lift","garden" # must bool
]

cols_check_int = ["noRooms","floor","numberOfFloors"]

for col in cols_check_int:
    mask = df[col].notna() & ((df[col] % 1 != 0) | (df[col] < 0) | (df[col] > 1000))
    print(col, df.loc[mask, col].unique()[:10])

mask = df["yearConstructed"].notna() & ((df["yearConstructed"] % 1 != 0) | (df["yearConstructed"] < 1800) | (df["yearConstructed"] > 2024))

df.loc[df["floor"] > df["numberOfFloors"], ["floor","numberOfFloors"]]
df.loc[(df["yearConstructed"] < 1800) | (df["yearConstructed"] > 2025), "yearConstructed"] = np.nan
df.loc[df["noRooms"] <= 0, "noRooms"] = np.nan
df.loc[df["numberOfFloors"] <= 0, "numberOfFloors"] = np.nan
df.loc[df["floor"] < -1, "floor"] = np.nan
mask = (df["floor"] > df["numberOfFloors"]) & df["numberOfFloors"].notna()
df.loc[mask, "floor"] = np.nan
# Check for outliers in numeric columns
for col in num_cols:
    remove_outliers_iqr(df, col)

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Check for missing values in categorical columns
for col in cat_cols:
    df[col] = df[col].str.strip().str.lower()

for col in cat_cols:
    df[col] = df[col].fillna("unknown")

freq = df["regio2"].value_counts(normalize=True)
df["regio2_freq"] = df["regio2"].map(freq)
df = df.drop(columns=["regio2"])
small_cat = ["regio1","heatingType","condition","typeOfFlat"]
df = pd.get_dummies(df, columns=small_cat, drop_first=True)
# Convert boolean columns to integers
df[bool_cols] = df[bool_cols].astype(int)

# Prepare features and target variable
X = df.drop(columns=["totalRent"])
y = df["totalRent"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train,
    test_size=0.2,   
    random_state=42
)
train_df = X_train.copy()
train_df["totalRent"] = y_train

val_df = X_val.copy()
val_df["totalRent"] = y_val

test_df = X_test.copy()
test_df["totalRent"] = y_test

train_df.to_csv("../features/processed/train.csv", index=False)
val_df.to_csv("../features/processed/val.csv", index=False)
test_df.to_csv("../features/processed/test.csv", index=False)