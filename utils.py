from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import numpy as np
import seaborn as sns
from shapely.geometry import Point
import shapely
import json

    
def calculate_feature_importance(model, X, y):
    model.fit(X, y)

    perm_importance = permutation_importance(model, X, y, scoring='roc_auc')

    return pd.DataFrame({'feature': X.columns,
                         'importance': perm_importance.importances_mean}).sort_values('importance', ascending=False)


def evaluate_model(model, X, y):
    cross_val_scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')

    model.fit(X, y)

    auc_roc = roc_auc_score(y, model.predict_proba(X)[:, 1])

    return cross_val_scores.mean(), auc_roc


def merge_categories(data, keyword, target_category):
    categories_containing_keyword = data['Inspection Type'].str.lower().str.contains(keyword)
    data.loc[categories_containing_keyword, 'Inspection Type'] = target_category


# Replaces values in Inspection Type for records with keywords found in them with the specified replacement value
def standardize_by_finding_keyword(data, inspection_types, keywords, replacement):
    to_replace = np.array([])
    inspection_types_lower = np.char.lower(inspection_types)
    for keyword in keywords:
        to_replace = np.append(to_replace, inspection_types[np.char.find(inspection_types_lower, keyword) != -1])
    data['Inspection Type'] = data['Inspection Type'].replace(to_replace, value=replacement)


# Function that creates points from Latitude and Longitude
def create_points(df):
    coords = list(zip(df['Longitude'], df['Latitude']))
    res = []
    for coord in coords:
        res.append(shapely.geometry.Point(coord))
    return res


# Method which checks whether the points are in area described in geojson file and returns data with zip value for found points
def populate_missing_zip(points, geojson_filename):
    # load GeoJSON file containing sectors
    state_geo_path = r'{0}'.format(geojson_filename)
    geo_json_data = json.load(open(state_geo_path))

    zip_found = []
    # check each polygon to see if it contains the point
    for feature in geo_json_data['features']:
        polygon = shapely.geometry.shape(feature['geometry'])
        for point in points:
            if polygon.contains(point):
                point_complete = {'Longitude': point.x, 'Latitude': point.y,
                                  'Zip': feature.get('properties', {}).get('zip')}
                zip_found.append(point_complete)
    return zip_found


# Function that returns all Chicago Zips frem geojson file
def create_chicago_zip_list():
    state_geo_path = "chicago-zip.geojson"
    geo_json_data = json.load(open(state_geo_path))

    zips = []

    for feature in geo_json_data['features']:
        zips.append(str(feature.get('properties', {}).get('zip')))
    return set(zips)


def extract_violation_codes(violation):
    if 'No Violations' in violation:
        return [0]  # return list with 0 as violation code
    else:
        # Splitting at '.' and taking the first part (the violation code)
        return [int(v.split('.')[0].strip()) for v in violation.split('|') if v.strip()]


def calculate_distance(lat, lon, city_center):
    return ((lat - city_center[0]) ** 2 + (lon - city_center[1]) ** 2) ** 0.5
