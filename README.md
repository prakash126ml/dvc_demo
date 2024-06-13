# ml-pipelines-using-dvc

Code of how to build a ml-pipeline using DVC

dvc repro

dvc dag

dvc stage add -n model_evaluation -d src/model_evaluation.py -d model.pkl  --metrics  metrics.json python src/model_evaluation.py

dvc metrics show
