# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrgsorgidprojectsprojectidbuildtargetsTestResults(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'unit_test': 'object',
        'unit_test_editmode': 'object',
        'unit_test_playmode': 'object'
    }

    attribute_map = {
        'unit_test': 'unit_test',
        'unit_test_editmode': 'unit_test_editmode',
        'unit_test_playmode': 'unit_test_playmode'
    }

    def __init__(self, unit_test=None, unit_test_editmode=None, unit_test_playmode=None):  # noqa: E501
        """OrgsorgidprojectsprojectidbuildtargetsTestResults - a model defined in Swagger"""  # noqa: E501

        self._unit_test = None
        self._unit_test_editmode = None
        self._unit_test_playmode = None
        self.discriminator = None

        if unit_test is not None:
            self.unit_test = unit_test
        if unit_test_editmode is not None:
            self.unit_test_editmode = unit_test_editmode
        if unit_test_playmode is not None:
            self.unit_test_playmode = unit_test_playmode

    @property
    def unit_test(self):
        """Gets the unit_test of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501


        :return: The unit_test of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501
        :rtype: object
        """
        return self._unit_test

    @unit_test.setter
    def unit_test(self, unit_test):
        """Sets the unit_test of this OrgsorgidprojectsprojectidbuildtargetsTestResults.


        :param unit_test: The unit_test of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501
        :type: object
        """

        self._unit_test = unit_test

    @property
    def unit_test_editmode(self):
        """Gets the unit_test_editmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501


        :return: The unit_test_editmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501
        :rtype: object
        """
        return self._unit_test_editmode

    @unit_test_editmode.setter
    def unit_test_editmode(self, unit_test_editmode):
        """Sets the unit_test_editmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.


        :param unit_test_editmode: The unit_test_editmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501
        :type: object
        """

        self._unit_test_editmode = unit_test_editmode

    @property
    def unit_test_playmode(self):
        """Gets the unit_test_playmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501


        :return: The unit_test_playmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501
        :rtype: object
        """
        return self._unit_test_playmode

    @unit_test_playmode.setter
    def unit_test_playmode(self, unit_test_playmode):
        """Sets the unit_test_playmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.


        :param unit_test_playmode: The unit_test_playmode of this OrgsorgidprojectsprojectidbuildtargetsTestResults.  # noqa: E501
        :type: object
        """

        self._unit_test_playmode = unit_test_playmode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrgsorgidprojectsprojectidbuildtargetsTestResults, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsTestResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
