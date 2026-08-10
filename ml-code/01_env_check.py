"""
01 — Environment check.
Run:  python ml-code/01_env_check.py
Goal : confirm python + ML libraries are installed.
"""
import sys

print("Python:", sys.version)

try:
    import numpy, pandas, matplotlib, sklearn, seaborn, joblib
    print("numpy       ", numpy.__version__)
    print("pandas      ", pandas.__version__)
    print("sklearn     ", sklearn.__version__)
    print("seaborn     ", seaborn.__version__)
    print("All good! Run ml-code/02 next.")
except ImportError as e:
    print("MISSING package:", e)
    print("Fix with: pip install numpy pandas matplotlib scikit-learn seaborn joblib")