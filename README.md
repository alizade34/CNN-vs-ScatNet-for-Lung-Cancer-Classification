# Visual Intelligence Project

MSc in Artificial Intelligence - University of Verona  
Academic Year: 2024/2025  
Student: Emil Alizada (VR510345)

## Project Overview

Binary classification of lung cancer histopathological images using:
- 2D Convolutional Neural Network (CNN)
- Scattering Network (ScatNet)
- DeepLIFT explainability analysis

## Dataset

Kaggle: [Lung Cancer Histopathological Images](https://www.kaggle.com/datasets/rm1000/lung-cancer-histopathological-images)
- Classes: Adenocarcinoma vs Benign
- Task: Binary classification

## Project Structure

```
visual_intelligence_project/
├── notebooks/           # Jupyter notebooks for development and experiments
├── src/                # Python source code (data loading, models, training, utils, explainability)
├── data/               # Dataset and processed data
│   ├── raw/            # Original images (adenocarcinoma, benign)
│   └── processed/      # Preprocessed, train/test splits
├── results/            # Models, figures, outputs, analysis
├── report/             # Final report
└── presentation/       # Final presentation
```

## Setup Instructions

1. **Python version:** 3.9+ recommended
2. **Create virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Download dataset:** Place extracted folders in `data/raw/` as:
   - `data/raw/adenocarcinoma/`
   - `data/raw/benign/`
5. **Initial data setup:**
   - Run or review `notebooks/01_data_analysis/01_dataset_setup.ipynb` for preprocessing and split info.

## Main Components

- **src/data/**: Data loading, preprocessing, augmentation
- **src/models/**: CNN and ScatNet architectures
- **src/training/**: Training loops, k-fold cross-validation
- **src/explainability/**: DeepLIFT, attribution maps, filter analysis
- **notebooks/**: Step-by-step experiments, results, and analysis

## Training & Evaluation

- **CNN Training:**
  - Use `notebooks/02_cnn_implementation/02_cnn_training.ipynb` for standard training
  - Use `03_cnn_kfold.ipynb` for k-fold cross-validation
- **ScatNet Training:**
  - Use `notebooks/03_scatnet_implementation/01_scatnet_training.ipynb`
- **Explainability:**
  - DeepLIFT and attribution: `notebooks/04_explainability/`
- **Results & Analysis:**
  - See `notebooks/05_results_analysis/` and `results/` for figures and summaries

## Reproducibility

- All random seeds are set in notebooks/scripts for reproducibility
- Trained models and outputs are saved in `models/` and `results/`
- Configurations for experiments are in `config.json` and `cnn_config.json`

## Main Dependencies

- torch (PyTorch)
- torchvision
- kymatio (for ScatNet)
- numpy, pandas, matplotlib, scikit-learn
- tqdm

## Requirements

- Minimum 70% accuracy for both models
- K-fold cross validation
- DeepLIFT implementation from scratch
- Filter analysis and comparison
- Attribution maps generation

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/rm1000/lung-cancer-histopathological-images)
- [PyTorch](https://pytorch.org/), [Kymatio](https://www.kymat.io/)
- DeepLIFT: Shrikumar et al., 2017
"# CNN-vs-ScatNet-for-Lung-Cancer-Classification" 
