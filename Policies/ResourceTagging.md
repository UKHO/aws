# Resource tagging 

## Version Control

| Version Number | Date             | Comments        |
|----------------|------------------|-----------------|
| 0.1            | February 2020    | Initial version |

## Introduction 

One of AWS Best Practices is Resource Tagging. Tagging allows metadata to be added to resources
which can help allocate costs, aid support and help classify resources within an AWS Account.

## Mandatory tags
On all resources where tagging is possible they should have the minimum of the following tags:

* `service_name` - Name of the service
* `service_owner` - Contact email for the team supporting the service
* `team_responsible` - The name of the team supporting the service
* `environment` - The name of the environment that the resource relates to  