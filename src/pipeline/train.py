import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import top_k_accuracy_score
import mlflow
import mlflow.sklearn
import pathlib

def load_data(path="data/processed/setlists.csv"):
    return pd.read_csv(path)

def build_pipeline():
    cat_cols = ["genero", "tonalidade", "contexto"]
    num_cols = ["bpm", "energia"]
    pre = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ("num", StandardScaler(), num_cols)
    ])
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    pipe = Pipeline([("prep", pre), ("clf", model)])
    return pipe

def main():
    data_path = pathlib.Path("data/processed/setlists.csv")
    if not data_path.exists():
        raise FileNotFoundError("Crie data/processed/setlists.csv com as colunas esperadas")

    df = load_data(data_path)
    X = df[["genero", "tonalidade", "contexto", "bpm", "energia"]]
    y = df["proxima_musica"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    with mlflow.start_run():
        pipe = build_pipeline()
        pipe.fit(X_train, y_train)
        # Exemplo simples de métrica Top-3
        preds = pipe.predict_proba(X_test)
        # top_k_accuracy_score requer rótulos. Aqui usamos 3 como k
        # Em classificadores probabilísticos do sklearn, classes_ define a ordem
        top3 = top_k_accuracy_score(y_test, preds, k=3, labels=pipe.named_steps["clf"].classes_)
        mlflow.log_metric("top3_accuracy", top3)
        mlflow.sklearn.log_model(pipe, artifact_path="model")
        print(f"Top-3 accuracy: {top3:.3f}")

if __name__ == "__main__":
    main()