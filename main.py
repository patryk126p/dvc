import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

if __name__ == "__main__":
    data = pd.read_csv(
        "data/iris.data",
        header=None,
        names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
    )
    x = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = data.species

    model = DecisionTreeClassifier(max_depth=3, random_state=1)
    model.fit(x, y)
    joblib.dump(model, "models/model.joblib")
