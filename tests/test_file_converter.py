import os
import pandas as pd
import pytest
import json
from src.file_converter import (
    csv_to_excel,
    excel_to_csv,
    csv_to_json,
    json_to_csv,
    txt_to_csv,
    csv_to_txt
)


def test_csv_to_excel(tmp_path):
    """
    Test the csv_to_excel function with a simple CSV file.
    """
    csv_data = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': [30, 25]
    })
    csv_path = tmp_path / "test.csv"
    excel_path = tmp_path / "test.xlsx"
    csv_data.to_csv(csv_path, index=False)
    csv_to_excel(str(csv_path), str(excel_path))
    assert excel_path.exists()
    df_excel = pd.read_excel(excel_path)
    pd.testing.assert_frame_equal(csv_data, df_excel)

def test_excel_to_csv(tmp_path):
    """
    Test the excel_to_csv function with a simple Excel file.
    """
    excel_data = pd.DataFrame({
        'city': ['Rome', 'Milan'],
        'population': [2873000, 1372000]
    })
    excel_path = tmp_path / "test.xlsx"
    csv_path = tmp_path / "test.csv"
    excel_data.to_excel(excel_path, index=False)
    excel_to_csv(str(excel_path), str(csv_path))
    assert csv_path.exists()
    df_csv = pd.read_csv(csv_path)
    pd.testing.assert_frame_equal(excel_data, df_csv)

def test_csv_to_json(tmp_path):
    """
    Test the csv_to_json function with a simple CSV file.
    """
    csv_data = pd.DataFrame({
        'product': ['Book', 'Pen'],
        'price': [12.5, 1.2]
    })
    csv_path = tmp_path / "test.csv"
    json_path = tmp_path / "test.json"
    csv_data.to_csv(csv_path, index=False)
    csv_to_json(str(csv_path), str(json_path))
    assert json_path.exists()
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df_json = pd.DataFrame(data)
    pd.testing.assert_frame_equal(csv_data, df_json)

def test_json_to_csv(tmp_path):
    """
    Test the json_to_csv function with a simple JSON file.
    """
    json_data = [
        {"animal": "Dog", "legs": 4},
        {"animal": "Bird", "legs": 2}
    ]
    json_path = tmp_path / "test.json"
    csv_path = tmp_path / "test.csv"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    json_to_csv(str(json_path), str(csv_path))
    assert csv_path.exists()
    df_csv = pd.read_csv(csv_path)
    df_expected = pd.DataFrame(json_data)
    pd.testing.assert_frame_equal(df_expected, df_csv)

def test_txt_to_csv(tmp_path):
    """
    Test the txt_to_csv function with a simple TXT file (tab delimited).
    """
    txt_content = "fruit\tcolor\nApple\tRed\nBanana\tYellow\n"
    txt_path = tmp_path / "test.txt"
    csv_path = tmp_path / "test.csv"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(txt_content)
    txt_to_csv(str(txt_path), str(csv_path), delimiter='\t')
    assert csv_path.exists()
    df_csv = pd.read_csv(csv_path)
    df_expected = pd.DataFrame({
        'fruit': ['Apple', 'Banana'],
        'color': ['Red', 'Yellow']
    })
    pd.testing.assert_frame_equal(df_expected, df_csv)

def test_csv_to_txt(tmp_path):
    """
    Test the csv_to_txt function with a simple CSV file (semicolon delimited TXT output).
    """
    csv_data = pd.DataFrame({
        'brand': ['Fiat', 'Tesla'],
        'year': [2020, 2022]
    })
    csv_path = tmp_path / "test.csv"
    txt_path = tmp_path / "test.txt"
    csv_data.to_csv(csv_path, index=False)
    csv_to_txt(str(csv_path), str(txt_path), delimiter=';')
    assert txt_path.exists()
    df_txt = pd.read_csv(txt_path, delimiter=';')
    pd.testing.assert_frame_equal(csv_data, df_txt) 