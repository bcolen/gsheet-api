# gsheet-api
Easily and efficiently manage a Google Sheet.

## Notes
- Credentials required are the Google Service account json file
  - [Creating a Google Serivice Key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
- Sheet must be shared with edit access to the `client_email` found the the service account
- Credentials can be entered as a dictionary or a file path to a json file, both will work.

## Usage Example
```python
gsheet = GSheetAPI(..)        # initialize the class
gsheet.sheet_to_df(..)        # import data from the sheet to a Pandas DataFrame

gsheet.change_gsheet(..)      # switch to a new Google Sheet to work off of
gsheet.get_cell(..)           # get the contents of a single cell

gsheet.change_tab(..)         # switch to a new tab in the current working Google Sheet
gsheet.set_cell(..)           # set the value of a single cell
gsheet.df_to_sheet(..)        # export a Pandas DataFrame to the current working sheet
gsheet.timestamp_to_cell(..)  # export a timestamp to a single cell in the sheet
```