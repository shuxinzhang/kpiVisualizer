"""Hello Analytics Reporting API V4."""

import argparse

from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import login_helper as login


ANALYTICS = login.initialize_analyticsreporting()

def get_report(viewId,startDate='today',endDate='today'):
  # Use the Analytics Service Object to query the Analytics Reporting API V4.
  return ANALYTICS.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': viewId,
          'dateRanges': [{'startDate': startDate, 'endDate': endDate}],
          'metrics': [{'expression': 'ga:sessions'},{'expression': 'ga:users'}]
        }]
      }
  ).execute()

def get_data(viewId):
  reports = get_report(viewId).get('reports',[])
  report = reports[0]
  rows = report.get('data',{}).get('rows',[])
  dataValues = rows[0]
  return dataValues.get('metrics',[])[0].get('values',[])

def get_session(pageName):
  viewId = login.getCredentials('google-analytics',pageName)
  return get_data(viewId)[0]

def get_user(pageName):
  viewId = login.getCredentials('google-analytics',pageName)
  return get_data(viewId)[1]

'''
def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response"""

  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print header + ': ' + dimension

      for i, values in enumerate(dateRangeValues):
        print 'Date range (' + str(i) + ')'
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print metricHeader.get('name') + ': ' + value
'''