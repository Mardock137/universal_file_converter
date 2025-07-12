"""
file_converter.py

Module for converting files between CSV, Excel, JSON, and TXT formats.
All functions are designed to be simple, safe, and easy to use.
"""

import pandas as pd
import json


def csv_to_excel(csv_path: str, excel_path: str) -> None:
    """
    Convert a CSV file to Excel format (.xlsx).
    Args:
        csv_path (str): Path to the input CSV file.
        excel_path (str): Path to the output Excel file.
    """
    df = pd.read_csv(csv_path)
    df.to_excel(excel_path, index=False)


def excel_to_csv(excel_path: str, csv_path: str) -> None:
    """
    Convert an Excel file (.xlsx) to CSV format.
    Args:
        excel_path (str): Path to the input Excel file.
        csv_path (str): Path to the output CSV file.
    """
    df = pd.read_excel(excel_path)
    df.to_csv(csv_path, index=False)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Convert a CSV file to JSON format.
    Args:
        csv_path (str): Path to the input CSV file.
        json_path (str): Path to the output JSON file.
    """
    df = pd.read_csv(csv_path)
    df.to_json(json_path, orient="records", force_ascii=False, indent=2)


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Convert a JSON file to CSV format.
    Args:
        json_path (str): Path to the input JSON file.
        csv_path (str): Path to the output CSV file.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)


def txt_to_csv(txt_path: str, csv_path: str, delimiter: str = ',') -> None:
    """
    Convert a TXT file (with delimiter) to CSV format.
    Args:
        txt_path (str): Path to the input TXT file.
        csv_path (str): Path to the output CSV file.
        delimiter (str): Delimiter used in the TXT file (default: ',').
    """
    df = pd.read_csv(txt_path, delimiter=delimiter)
    df.to_csv(csv_path, index=False)


def csv_to_txt(csv_path: str, txt_path: str, delimiter: str = ',') -> None:
    """
    Convert a CSV file to TXT format (with delimiter).
    Args:
        csv_path (str): Path to the input CSV file.
        txt_path (str): Path to the output TXT file.
        delimiter (str): Delimiter to use in the TXT file (default: ',').
    """
    df = pd.read_csv(csv_path)
    df.to_csv(txt_path, sep=delimiter, index=False, header=True) 