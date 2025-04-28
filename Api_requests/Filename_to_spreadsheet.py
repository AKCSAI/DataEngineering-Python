import os
from openpyxl import Workbook

def files_to_spreadsheet(folder_path, output_excel):
    # Get list of files
    files = os.listdir(folder_path)
    
    # Filter to only files (optional, remove if you want folders too)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Create a new Excel workbook and select the active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "File List"

    # Write header
    ws.append(["Filename"])

    # Write file names
    for file_name in files:
        ws.append([file_name])

    # Save the workbook
    wb.save(output_excel)
    print(f"Spreadsheet saved successfully at: {output_excel}")

# Example usage
if __name__ == "__main__":
    folder_path = "/users/azizkhan/desktop/work/photos"  # <-- Change this
    output_excel = "/users/azizkhan/desktop/work/file_list.xlsx"      # <-- Or give a full path if you want
    files_to_spreadsheet(folder_path, output_excel)
