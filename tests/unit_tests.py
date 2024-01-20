import os.path
import pandas as pd

from test2.data import generate_data
from test2.plotting import plot_analysis
from test2.analysis import analyse_data

TEST_DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", 'tests', 'test_data')
)

def test_data_generator() -> None:
    original_data = pd.read_parquet(os.path.join(TEST_DATA_DIR, "raw_data.parquet"))
    new_data = generate_data()
    assert original_data.equals(new_data)

def test_analyse_data() -> None:
    original_fit_result = pd.read_parquet(os.path.join(TEST_DATA_DIR, "fit_results.parquet"))
    original_data = pd.read_parquet(os.path.join(TEST_DATA_DIR, "raw_data.parquet"))
    new_results = analyse_data(original_data)
    assert original_fit_result.equals(new_results)

def test_full_analysis() -> None:
    raw_data = generate_data()
    fit_results = analyse_data(raw_data)
    plot_analysis(raw_data = raw_data,
                  fit_results = fit_results)
    