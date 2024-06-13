



# ml-pipelines-using-dvc

Code of how to build a ml-pipeline using DVC

dvc stage add -n model_evaluation -d src/model_evaluation.py -d data/features -o metrics.json python src/model_evaluation.py

dvc repro

dvc dag
