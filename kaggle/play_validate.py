import pandas as pd
from sklearn.ensemble import RandomForestRegressor

home_data = pd.read_csv("data/train.csv")
forest_model = RandomForestRegressor(random_state=1)
y = home_data.SalePrice
features = [
    "LotArea",
    "YearBuilt",
    "1stFlrSF",
    "2ndFlrSF",
    "FullBath",
    "BedroomAbvGr",
    "TotRmsAbvGrd",
]

x = home_data[features]
forest_model.fit(x, y)

predict_data = pd.read_csv("data/test.csv")
val_x = predict_data[features]

val_y = forest_model.predict(val_x)

output = pd.DataFrame({"Id": predict_data.Id, "SalePrice": val_y})
output.to_csv("submission.csv", index=False)
