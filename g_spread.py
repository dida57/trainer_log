import gspread

gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
wks = gc.open("train_log").sheet1

# Update a range of cells using the top left corner address
wks.update(range_name="A1", values=[[1, 2, 3, 4]])

# Or update a single cell
wks.update_acell("B42", "it's down there somewhere, let me take another look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})
