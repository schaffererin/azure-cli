# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.pipeline_operations import PipelineOperations
from .operations.recurrence_operations import RecurrenceOperations
from .operations.job_operations import JobOperations
from . import models


class DataLakeAnalyticsJobManagementClientConfiguration(AzureConfiguration):
    """Configuration for DataLakeAnalyticsJobManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param adla_job_dns_suffix: Gets the DNS suffix used as the base for all
     Azure Data Lake Analytics Job service requests.
    :type adla_job_dns_suffix: str
    """

    def __init__(
            self, credentials, adla_job_dns_suffix):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if adla_job_dns_suffix is None:
            raise ValueError("Parameter 'adla_job_dns_suffix' must not be None.")
        if not isinstance(adla_job_dns_suffix, str):
            raise TypeError("Parameter 'adla_job_dns_suffix' must be str.")
        base_url = 'https://{accountName}.{adlaJobDnsSuffix}'

        super(DataLakeAnalyticsJobManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('datalakeanalyticsjobmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.adla_job_dns_suffix = adla_job_dns_suffix


class DataLakeAnalyticsJobManagementClient(object):
    """Creates an Azure Data Lake Analytics job client.

    :ivar config: Configuration for client.
    :vartype config: DataLakeAnalyticsJobManagementClientConfiguration

    :ivar pipeline: Pipeline operations
    :vartype pipeline: azure.mgmt.datalake.analytics.job.operations.PipelineOperations
    :ivar recurrence: Recurrence operations
    :vartype recurrence: azure.mgmt.datalake.analytics.job.operations.RecurrenceOperations
    :ivar job: Job operations
    :vartype job: azure.mgmt.datalake.analytics.job.operations.JobOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param adla_job_dns_suffix: Gets the DNS suffix used as the base for all
     Azure Data Lake Analytics Job service requests.
    :type adla_job_dns_suffix: str
    """

    def __init__(
            self, credentials, adla_job_dns_suffix):

        self.config = DataLakeAnalyticsJobManagementClientConfiguration(credentials, adla_job_dns_suffix)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-11-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.pipeline = PipelineOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recurrence = RecurrenceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job = JobOperations(
            self._client, self.config, self._serialize, self._deserialize)