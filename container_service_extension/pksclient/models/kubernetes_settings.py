# coding: utf-8

"""
    PKS

    PKS API  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class KubernetesSettings(object):
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
        'kubelet_drain_timeout': 'str',
        'kubelet_drain_grace_period': 'str',
        'kubelet_drain_force': 'str',
        'kubelet_drain_ignore_daemonsets': 'str',
        'kubelet_drain_delete_local_data': 'str',
        'kubelet_drain_force_node': 'str'
    }

    attribute_map = {
        'kubelet_drain_timeout': 'kubelet_drain_timeout',
        'kubelet_drain_grace_period': 'kubelet_drain_grace_period',
        'kubelet_drain_force': 'kubelet_drain_force',
        'kubelet_drain_ignore_daemonsets': 'kubelet_drain_ignore_daemonsets',
        'kubelet_drain_delete_local_data': 'kubelet_drain_delete_local_data',
        'kubelet_drain_force_node': 'kubelet_drain_force_node'
    }

    def __init__(self, kubelet_drain_timeout=None, kubelet_drain_grace_period=None, kubelet_drain_force=None, kubelet_drain_ignore_daemonsets=None, kubelet_drain_delete_local_data=None, kubelet_drain_force_node=None):  # noqa: E501
        """KubernetesSettings - a model defined in Swagger"""  # noqa: E501

        self._kubelet_drain_timeout = None
        self._kubelet_drain_grace_period = None
        self._kubelet_drain_force = None
        self._kubelet_drain_ignore_daemonsets = None
        self._kubelet_drain_delete_local_data = None
        self._kubelet_drain_force_node = None
        self.discriminator = None

        if kubelet_drain_timeout is not None:
            self.kubelet_drain_timeout = kubelet_drain_timeout
        if kubelet_drain_grace_period is not None:
            self.kubelet_drain_grace_period = kubelet_drain_grace_period
        if kubelet_drain_force is not None:
            self.kubelet_drain_force = kubelet_drain_force
        if kubelet_drain_ignore_daemonsets is not None:
            self.kubelet_drain_ignore_daemonsets = kubelet_drain_ignore_daemonsets
        if kubelet_drain_delete_local_data is not None:
            self.kubelet_drain_delete_local_data = kubelet_drain_delete_local_data
        if kubelet_drain_force_node is not None:
            self.kubelet_drain_force_node = kubelet_drain_force_node

    @property
    def kubelet_drain_timeout(self):
        """Gets the kubelet_drain_timeout of this KubernetesSettings.  # noqa: E501


        :return: The kubelet_drain_timeout of this KubernetesSettings.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_timeout

    @kubelet_drain_timeout.setter
    def kubelet_drain_timeout(self, kubelet_drain_timeout):
        """Sets the kubelet_drain_timeout of this KubernetesSettings.


        :param kubelet_drain_timeout: The kubelet_drain_timeout of this KubernetesSettings.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_timeout = kubelet_drain_timeout

    @property
    def kubelet_drain_grace_period(self):
        """Gets the kubelet_drain_grace_period of this KubernetesSettings.  # noqa: E501


        :return: The kubelet_drain_grace_period of this KubernetesSettings.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_grace_period

    @kubelet_drain_grace_period.setter
    def kubelet_drain_grace_period(self, kubelet_drain_grace_period):
        """Sets the kubelet_drain_grace_period of this KubernetesSettings.


        :param kubelet_drain_grace_period: The kubelet_drain_grace_period of this KubernetesSettings.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_grace_period = kubelet_drain_grace_period

    @property
    def kubelet_drain_force(self):
        """Gets the kubelet_drain_force of this KubernetesSettings.  # noqa: E501


        :return: The kubelet_drain_force of this KubernetesSettings.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_force

    @kubelet_drain_force.setter
    def kubelet_drain_force(self, kubelet_drain_force):
        """Sets the kubelet_drain_force of this KubernetesSettings.


        :param kubelet_drain_force: The kubelet_drain_force of this KubernetesSettings.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_force = kubelet_drain_force

    @property
    def kubelet_drain_ignore_daemonsets(self):
        """Gets the kubelet_drain_ignore_daemonsets of this KubernetesSettings.  # noqa: E501


        :return: The kubelet_drain_ignore_daemonsets of this KubernetesSettings.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_ignore_daemonsets

    @kubelet_drain_ignore_daemonsets.setter
    def kubelet_drain_ignore_daemonsets(self, kubelet_drain_ignore_daemonsets):
        """Sets the kubelet_drain_ignore_daemonsets of this KubernetesSettings.


        :param kubelet_drain_ignore_daemonsets: The kubelet_drain_ignore_daemonsets of this KubernetesSettings.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_ignore_daemonsets = kubelet_drain_ignore_daemonsets

    @property
    def kubelet_drain_delete_local_data(self):
        """Gets the kubelet_drain_delete_local_data of this KubernetesSettings.  # noqa: E501


        :return: The kubelet_drain_delete_local_data of this KubernetesSettings.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_delete_local_data

    @kubelet_drain_delete_local_data.setter
    def kubelet_drain_delete_local_data(self, kubelet_drain_delete_local_data):
        """Sets the kubelet_drain_delete_local_data of this KubernetesSettings.


        :param kubelet_drain_delete_local_data: The kubelet_drain_delete_local_data of this KubernetesSettings.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_delete_local_data = kubelet_drain_delete_local_data

    @property
    def kubelet_drain_force_node(self):
        """Gets the kubelet_drain_force_node of this KubernetesSettings.  # noqa: E501


        :return: The kubelet_drain_force_node of this KubernetesSettings.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_force_node

    @kubelet_drain_force_node.setter
    def kubelet_drain_force_node(self, kubelet_drain_force_node):
        """Sets the kubelet_drain_force_node of this KubernetesSettings.


        :param kubelet_drain_force_node: The kubelet_drain_force_node of this KubernetesSettings.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_force_node = kubelet_drain_force_node

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
        if issubclass(KubernetesSettings, dict):
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
        if not isinstance(other, KubernetesSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
