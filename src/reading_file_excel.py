import pandas as pd
import json


transactions_reading = pd.read_excel(r"C:\Users\acer\Downloads\transactions_excel.xlsx")
pd.set_option('display.width', None)


def get_transactions(df: pd.DataFrame) -> int:
    d_f = df.iloc[0:]
    json_str = d_f.to_json(orient="records", indent=4)
    json_data = json.loads(json_str)
    formatted_json = json.dumps(json_data, ensure_ascii=False, indent=4)
    return formatted_json


if __name__ == "__main__":
    print(get_transactions(transactions_reading))
