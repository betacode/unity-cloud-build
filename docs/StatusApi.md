# unity_cloud_build.StatusApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Get Cloud Build Status


# **get_status**
> list[InlineResponse20011] get_status()

Get Cloud Build Status

### Example
```python
from __future__ import print_function
import time
import unity_cloud_build
from unity_cloud_build.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
configuration = unity_cloud_build.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure HTTP basic authorization: filetoken
configuration = unity_cloud_build.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = unity_cloud_build.StatusApi(unity_cloud_build.ApiClient(configuration))

try:
    # Get Cloud Build Status
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20011]**](InlineResponse20011.md)

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

