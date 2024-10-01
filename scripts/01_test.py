import mlflow

if __name__ == "__main__":
    mlflow.create_experiment(
        name="testing_mlflow2",
        artifact_location="mlflow-artifacts:/2",
        tags={"env":"dev", "version":"1.0.0"}
    )