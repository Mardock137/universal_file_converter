import streamlit as st
from file_converter import (
    csv_to_excel,
    excel_to_csv,
    csv_to_json,
    json_to_csv,
    txt_to_csv,
    csv_to_txt
)
import tempfile
import os
import pathlib

st.set_page_config(page_title="Universal File Converter", page_icon="🔄")
st.title("🔄 Universal File Converter")
st.write("Convert your files between CSV, Excel, JSON, and TXT formats directly in your browser.")

conversion_options = {
    "CSV to Excel (.xlsx)": ("csv_to_excel", ".xlsx"),
    "Excel (.xlsx) to CSV": ("excel_to_csv", ".csv"),
    "CSV to JSON": ("csv_to_json", ".json"),
    "JSON to CSV": ("json_to_csv", ".csv"),
    "TXT to CSV": ("txt_to_csv", ".csv"),
    "CSV to TXT": ("csv_to_txt", ".txt")
}

conversion = st.selectbox("Select conversion type:", list(conversion_options.keys()))

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx", "json", "txt"])

delimiter = None
if conversion in ["TXT to CSV", "CSV to TXT"]:
    delimiter = st.text_input("Delimiter (default: comma)", value="," if conversion == "CSV to TXT" else "\t")
    st.caption("The delimiter is the character that separates columns in your file. Common delimiters: comma ',' (CSV), tab '\\t' (TXT), semicolon ';'. If unsure, leave the default value.")

conversion_input_extensions = {
    "CSV to Excel (.xlsx)": [".csv"],
    "Excel (.xlsx) to CSV": [".xlsx"],
    "CSV to JSON": [".csv"],
    "JSON to CSV": [".json"],
    "TXT to CSV": [".txt"],
    "CSV to TXT": [".csv"]
}

if st.button("Convert") and uploaded_file is not None:
    # Check file extension matches conversion type
    allowed_exts = conversion_input_extensions[conversion]
    uploaded_ext = pathlib.Path(uploaded_file.name).suffix.lower()
    if uploaded_ext not in allowed_exts:
        st.error(f"Invalid file type for this conversion. Please upload a file with extension: {', '.join(allowed_exts)}.")
        st.stop()
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, uploaded_file.name)
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # Get output file name based on input file name and new extension
        input_stem = pathlib.Path(uploaded_file.name).stem
        new_ext = conversion_options[conversion][1]
        output_filename = input_stem + new_ext
        output_path = os.path.join(tmpdir, output_filename)
        # Perform conversion
        if conversion == "CSV to Excel (.xlsx)":
            csv_to_excel(input_path, output_path)
        elif conversion == "Excel (.xlsx) to CSV":
            excel_to_csv(input_path, output_path)
        elif conversion == "CSV to JSON":
            csv_to_json(input_path, output_path)
        elif conversion == "JSON to CSV":
            json_to_csv(input_path, output_path)
        elif conversion == "TXT to CSV":
            txt_to_csv(input_path, output_path, delimiter=delimiter or "\t")
        elif conversion == "CSV to TXT":
            csv_to_txt(input_path, output_path, delimiter=delimiter or ",")
        else:
            st.error("Unknown conversion type.")
            st.stop()
        with open(output_path, "rb") as f:
            st.success("Conversion completed! Download your file below.")
            st.download_button(
                label="Download converted file",
                data=f,
                file_name=output_filename
            ) 