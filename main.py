from fastapi import FastAPI, Response, Query
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend domain if you want to restrict access
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
@app.get("/data")
def get_data(offset: int = Query(0, ge=0), limit: int = Query(10, ge=1)):
    # Read the CSV file
    df = pd.read_csv("country_aggregate.csv")
    
    # Replace NaN values with None or a suitable value
    df.fillna(value=np.nan, inplace=True)
    # Slice the DataFrame to get the specified range of records
    paginated_df = df.iloc[offset:offset+limit]
    
    # Initialize an empty list to store JSON formatted data
    json_data = []
    
    # Loop through each row in the DataFrame
    for index, row in paginated_df.iterrows():
        # Create a dictionary for the current row
        row_dict = {
            "country": row["country"],
            "errors": row.get("errors", 0),
            "grave": row.get("grave", 0),
            "misconduct": row.get("misconduct", 0),
            "normal": row.get("normal", 0),
            "grand_total": row.get("gt", 0)
        }
        # Append the row dictionary to the list
        json_data.append(row_dict)
        row_dict = json.dumps(json_data).replace('NaN', '-1')
    
    # Return the list of dictionaries as JSON
    return Response(content=row_dict, media_type="application/json")


# get_data()

# @app.get("/data")
# def get_data(offset: int = Query(0, ge=0), limit: int = Query(10, ge=1)):
#     # Read the CSV file
#     df = pd.read_csv("country_aggregate.csv")
    
#     # Replace NaN values with None or a suitable value
#     df.fillna(value=np.nan, inplace=True)
    
   
#     # Convert the sliced DataFrame to JSON format
#     json_data = paginated_df.to_json(orient="records", default_handler=str)
    
#     # Return the JSON data
#     return Response(content=json_data, media_type="application/json")

