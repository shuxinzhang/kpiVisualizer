import login_helper as login

service = login.gspread_auth()
spreadsheet_id = "19KvaY04qRaUYvk_rPWC5qHUgzdwr06Eq4b37VGuHjgY"
spreadsheet = service.spreadsheets().values()

def add_new_row(dataArray,sheetName,Range):
	row_range = sheetName+"!"+Range
	input_option = 'RAW'
	insert_option = 'INSERT_ROWS'
	data_value=[dataArray]
	data_body = {
		'values':data_value
	}
	request = spreadsheet.append(
		spreadsheetId=spreadsheet_id,
		range=Range,
		valueInputOption=input_option,
		insertDataOption=insert_option,
		body=data_body)
	return request






