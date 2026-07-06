"""
Project-wide directory paths.

This module centralizes all file and folder locations used throughout the project.
Import these constants instead of hardcoding paths in notebooks.
"""

from pathlib import Path

# =============================================================================
# Project Root
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =============================================================================
# Main Directories
# =============================================================================

DATA_DIR = PROJECT_ROOT / "data"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
MODELS_DIR = PROJECT_ROOT / "models"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
REPORT_DIR = PROJECT_ROOT / "report"

# =============================================================================
# Output Subdirectories
# =============================================================================

FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"

# =============================================================================
# Dataset Directory
# =============================================================================

AIFB_DIR = DATA_DIR / "aifb-hetero"

# Dataset files
RDF_FILE = AIFB_DIR / "aifbfixed_complete.n3"
TRAIN_FILE = AIFB_DIR / "trainingSet.tsv"
TEST_FILE = AIFB_DIR / "testSet.tsv"
COMPLETE_DATASET_FILE = AIFB_DIR / "completeDataset.tsv"


# =============================================================================
# Create output folders automatically
# =============================================================================

MODELS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)
FIGURES_DIR.mkdir(exist_ok=True)
TABLES_DIR.mkdir(exist_ok=True)


