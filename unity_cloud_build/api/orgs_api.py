# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from unity_cloud_build.api_client import ApiClient


class OrgsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_billing_plans(self, orgid, **kwargs):  # noqa: E501
        """Get billing plan  # noqa: E501

        Get the billing plan for the specified organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_plans(orgid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str orgid: Organization identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_billing_plans_with_http_info(orgid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_billing_plans_with_http_info(orgid, **kwargs)  # noqa: E501
            return data

    def get_billing_plans_with_http_info(self, orgid, **kwargs):  # noqa: E501
        """Get billing plan  # noqa: E501

        Get the billing plan for the specified organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_plans_with_http_info(orgid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str orgid: Organization identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['orgid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_plans" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'orgid' is set
        if ('orgid' not in params or
                params['orgid'] is None):
            raise ValueError("Missing the required parameter `orgid` when calling `get_billing_plans`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orgid' in params:
            path_params['orgid'] = params['orgid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'permissions']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgid}/billingplan', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ssh_key_for_org(self, orgid, **kwargs):  # noqa: E501
        """Get SSH Key  # noqa: E501

        Get the ssh public key for the specified org  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ssh_key_for_org(orgid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str orgid: Organization identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ssh_key_for_org_with_http_info(orgid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ssh_key_for_org_with_http_info(orgid, **kwargs)  # noqa: E501
            return data

    def get_ssh_key_for_org_with_http_info(self, orgid, **kwargs):  # noqa: E501
        """Get SSH Key  # noqa: E501

        Get the ssh public key for the specified org  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ssh_key_for_org_with_http_info(orgid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str orgid: Organization identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['orgid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ssh_key_for_org" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'orgid' is set
        if ('orgid' not in params or
                params['orgid'] is None):
            raise ValueError("Missing the required parameter `orgid` when calling `get_ssh_key_for_org`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orgid' in params:
            path_params['orgid'] = params['orgid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'permissions']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgid}/sshkey', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regenerate_ssh_key(self, orgid, **kwargs):  # noqa: E501
        """Regenerate SSH Key  # noqa: E501

        Regenerate the ssh key for the specified org *WARNING* this is a destructive operation that will permanently remove your current SSH key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regenerate_ssh_key(orgid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str orgid: Organization identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regenerate_ssh_key_with_http_info(orgid, **kwargs)  # noqa: E501
        else:
            (data) = self.regenerate_ssh_key_with_http_info(orgid, **kwargs)  # noqa: E501
            return data

    def regenerate_ssh_key_with_http_info(self, orgid, **kwargs):  # noqa: E501
        """Regenerate SSH Key  # noqa: E501

        Regenerate the ssh key for the specified org *WARNING* this is a destructive operation that will permanently remove your current SSH key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regenerate_ssh_key_with_http_info(orgid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str orgid: Organization identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['orgid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regenerate_ssh_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'orgid' is set
        if ('orgid' not in params or
                params['orgid'] is None):
            raise ValueError("Missing the required parameter `orgid` when calling `regenerate_ssh_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orgid' in params:
            path_params['orgid'] = params['orgid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey', 'permissions']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgid}/sshkey', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
