# unity_cloud_build_api.UserdevicesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](UserdevicesApi.md#create_device) | **POST** /users/me/devices | Create iOS device profile
[**list_devices_for_user**](UserdevicesApi.md#list_devices_for_user) | **GET** /users/me/devices | List iOS device profiles

# **create_device**
> object create_device(body)

Create iOS device profile

Create iOS device profile for the current user

### Example
```python
from __future__ import print_function
import time
import unity_cloud_build_api
from unity_cloud_build_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: apikey
configuration = unity_cloud_build_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'# Configure HTTP basic authorization: filetoken
configuration = unity_cloud_build_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = unity_cloud_build_api.UserdevicesApi(unity_cloud_build_api.ApiClient(configuration))
body = unity_cloud_build_api.MeDevicesBody() # MeDevicesBody | 

try:
    # Create iOS device profile
    api_response = api_instance.create_device(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserdevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeDevicesBody**](MeDevicesBody.md)|  | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices_for_user**
> list[InlineResponse2004] list_devices_for_user()

List iOS device profiles

List all iOS device profiles for the current user

### Example
```python
from __future__ import print_function
import time
import unity_cloud_build_api
from unity_cloud_build_api.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: apikey
configuration = unity_cloud_build_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'# Configure HTTP basic authorization: filetoken
configuration = unity_cloud_build_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = unity_cloud_build_api.UserdevicesApi(unity_cloud_build_api.ApiClient(configuration))

try:
    # List iOS device profiles
    api_response = api_instance.list_devices_for_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserdevicesApi->list_devices_for_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

