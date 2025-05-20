# **Card Fraud Detection System** 🕵️‍♂️💳

## **🔍 Overview**

This project is a complete **end-to-end machine learning pipeline** for detecting fraudulent credit card transactions using robust preprocessing and classification techniques.

Key components include:

- **SMOTE** for class imbalance correction
- **Multiple classifiers** (XGBoost, RandomForest, etc.)
- **Modular configuration via YAML**
- **Data versioning with DVC**
- **CI/CD readiness** for automated ML workflows

---

## 📈 Exploratory Data Analysis (EDA)

Check out the detailed EDA in the notebook below:

🔗 [EDA Research Notebook](research/EDA.ipynb)

## **📁 Project Structure**

````bash
CardFraud/
│
├── .github/workflows/.gitkeep         # CI workflow placeholder
├── config/
│   └── config.yaml                    # YAML config for paths/artifacts
├── params.yaml                        # Hyperparameters & model settings
├── requirements.txt                   # Python dependencies
├── setup.py                           # Project setup file
├── research/
│   └── trials.ipynb                   # Jupyter notebook for EDA & experiments
└── src/CardFraud/
    ├── __init__.py
    ├── component/
    │   ├── __init__.py
    │   ├── data_ingestion.py         # Ingests and splits data
    │   ├── data_preprocessing.py     # Cleans, balances, scales data
    │   └── data_training.py          # Trains and evaluates models
    ├── config/
    │   └── __init__.py
    ├── constant/
    │   └── __init__.py
    ├── entity/
    │   ├── __init__.py
    │   └── con.py                    # Data classes (configs, entities)
    ├── pipeline/
    │   ├── __init__.py
    │   └── main.py                   # Orchestrates pipeline steps
    └── utils/
        └── __init__.py
## 📄 YAML Configuration Management

We use **YAML** files to decouple code logic from configuration:

- `config.yaml`: Contains path settings, directory names, and artifact locations
- `params.yaml`: Defines hyperparameters for models, test split ratios, and SMOTE settings

### 🔧 Why YAML?
- Easy to edit and tune
- Promotes modularity and reusability
- Keeps experiment setup clean and reproducible

---

## 📦 DVC for Data & Pipeline Versioning

We integrate **DVC (Data Version Control)** to manage:

- Raw and processed datasets
- Tracked versions of training outputs
- Complete ML pipeline with reproducibility

### ✅ DVC Benefits
- Git-like control for large files and models
- Pipeline automation via `dvc.yaml`
- Easy rollback and sharing of datasets/models

### 🔧 Basic DVC Usage

```bash
dvc init
dvc add data/raw.csv
dvc run -n preprocess -d src/... -o data/processed/ ...
dvc repro  # Re-runs updated stages
⚙️ CI/CD Pipeline Ready
This project is CI/CD-ready using GitHub Actions or similar tools:

Triggers pipeline on every push/merge

Installs dependencies

Runs linting/tests/training pipeline

Saves model artifacts

📁 Add .github/workflows/train.yml
yaml
Copy
Edit
name: Model Training

on: [push]

jobs:
  train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run pipeline
        run: python src/CardFraud/pipeline/main.py
## 📊 Model Results Summary

| Model              | Accuracy | Precision | Recall  | F1 Score |
|-------------------|----------|-----------|---------|----------|
| LogisticRegression| 0.9803   | 0.0742    | 0.9072  | 0.1371   |
| RandomForest      | 0.9995   | 0.8804    | 0.8350  | 0.8571   |
| DecisionTree      | 0.9975   | 0.3878    | 0.7835  | 0.5187   |
| XGBoost           | 0.9995   | 0.8586    | 0.8763  | 0.8673   |

🏆 **Best Model**: **XGBoost** with an **F1 Score** of **0.8673**


🚀 How to Run
Clone the repository

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Edit config.yaml and params.yaml as needed

Run the pipeline

bash
Copy
Edit
python src/CardFraud/pipeline/main.py
✍️ Author
Developed by [Your Name]
Feel free to open issues or submit PRs!

📌 Notes
Ensure paths in config.yaml point to the correct folders

Use dvc repro to execute the full pipeline

Focus: Backend ML pipeline only (no UI)
#workflow

1. update the config.yaml
2. update the params.yaml
3. update the entity
4. updata the components
5. update the pipeline
6. update the main.py
7. update the dvc.yaml
````
