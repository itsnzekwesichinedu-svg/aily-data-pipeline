# Iris Data Cleaning Pipeline

A beginner-friendly Python project that downloads a public dataset, cleans it with pandas, checks the result, and saves a processed CSV. It demonstrates an end-to-end data workflow: **download → clean → validate → export**.

## Dataset

The pipeline uses the [Iris CSV from the Seaborn data repository](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv). It contains four flower measurements and a species label. The script reads the CSV directly from its public raw URL, so an internet connection is needed each time you run it. See the source repository for dataset details and reuse terms.

## What the script does

1. Downloads the CSV into a pandas DataFrame.
2. Standardizes column names, converts the four measurements to numbers, and tidies the species labels.
3. Drops rows with missing required values and removes exact duplicate rows.
4. Checks the expected columns, missing values, measurement types and values, and species labels. The script stops with an error if a check fails.
5. Saves the cleaned data to `data/processed/iris_clean.csv` and prints row counts, species counts, and measurement statistics.

In the latest run, the source contained 150 rows. Cleaning removed one duplicate, leaving 149 rows and five columns. The generated CSV is ignored by Git; run the script to recreate it.

## Requirements

- Python 3.9 or newer
- Internet access to download the source CSV
- Dependencies listed in `requirements.txt` (currently pandas)

## Run on Windows with PowerShell

Open a terminal in the project folder, or move into it with `cd`:

```powershell
cd "path\to\GITHUB\aily-data-pipeline"
```

Create and activate a virtual environment, then install the dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the pipeline:

```powershell
python scripts/process_data.py
```

The cleaned CSV appears at `data\processed\iris_clean.csv`. The terminal prints the validation summary and descriptive statistics. In a new terminal, activate the environment again before running the script.

If PowerShell blocks activation, allow scripts for this terminal session and try activation again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Project structure

```text
aily-data-pipeline/
|-- data/
|   |-- .gitkeep
|   `-- processed/             generated CSV (ignored by Git)
|-- scripts/
|   `-- process_data.py
|-- .gitignore
|-- README.md
`-- requirements.txt
```

## Publish this folder to GitHub

Create a repository named `aily-data-pipeline` on GitHub. From the project folder, these commands initialize Git, create a commit, connect to the repository, and push the `main` branch. Replace `<your-username>` with your GitHub username. If the repository already has an initial commit, fetch and merge it before pushing.

```powershell
git init -b main
git add .
git status
git commit -m "Add Iris data cleaning pipeline"
git remote add origin https://github.com/<your-username>/aily-data-pipeline.git
git push -u origin main
```

Review `git status` before committing. `.venv` and the generated CSV are excluded by `.gitignore`; the script, README, dependency list, and folder marker are included. GitHub may ask you to sign in during the push.
