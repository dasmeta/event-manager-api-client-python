# Python Client for Event Manager API (event-manager-api-client-python)

## Table of contents
 * [Introduction](#introduction)
 * [Requirements](#requirements)
 * [Set Up](#set-up)

## Introduction
The service is based on [Python Flask](https://flask.palletsprojects.com/en/2.2.x/) framework.

## Requirements
- CPU cores >= 1
- RAM >= 256MB
- [Git 2.*](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker 20.*](https://docs.docker.com/engine/install/)
- [Python 3.*](https://www.python.org/downloads/)
  
## Set Up
- Set up git to have ssh access to the repository
- Clone the source into local machine
```shell
git clone git@github.com:dasmeta/event-manager-api-client-python.git
```
- Go to the project source `$ cd event-manager-api-client-python`
- Create an environment file `.env` or copy `.env.sample` and define variables
```text
# Access to API

API_HOST=
API_USER_ID=
API_USER_GUID=
API_USER_ROLE_NAME=
API_USER_ROLE_TYPE=

# JWT Token Validation Settings

JWT_SECRET=
JWT_ALGORITHM="HS256"
```
- Build docker image
```shell
docker-compose build [--no-cache]
```
- Start development environment
```shell
docker-compose up -d
```
- The service will be accessible on http://0.0.0.0:8000
- `publish` resource can be used for testing purposes:
```text
curl --location --request POST 'http://0.0.0.0:8000/publish' \
--header 'Content-Type: application/json' \
--data-raw '{
    "topic" : "partner.student.add",
    "data" : {
        "token" : "85d8b128-4c1f-426e-a748-d10d12df20a3",
        "createdAt" : "2022-10-20T15:31:32.968Z",
        "updatedAt" : "2022-10-20T15:31:32.968Z",
        "id" : "635169d4f2fd2d4fce9ac23d",
        "firstName" : "Vahagn",
        "middleName" : "",
        "lastName" : "Energy",
        "fullName" : "Vahagn Energy",
        "company" : "",
        "passport" : null,
        "avatar" : null,
        "birthday" : null,
        "fullNameItems" : [],
        "emails" : [ 
            "vahagn+1@dasmeta.com"
        ],
        "emailItems" : [ 
            {
                "email" : "vahagn+1@dasmeta.com",
                "studentId" : null
            }
        ],
        "phoneNumbers" : [ 
            "37455000019"
        ],
        "inGroups" : [],
        "groupCount" : 0,
        "avgProgress" : null,
        "currentlyInGroup" : false,
        "isConflictStudents" : false,
        "labels" : [],
        "note" : "",
        "additionalUrl" : "",
        "contactId" : null,
        "lastTrainingDate" : null,
        "emisStudentId" : null,
        "emisSchoolId" : null,
        "inactive" : false,
        "createdBy" : "5e45403dc89d1a001dff0bc5",
        "updatedBy" : null,
        "partnerId" : "5db1a674a34dc0001ceced4d",
        "divisionId" : null,
        "studentId" : null,
        "date" : "2022-10-20T15:31:32.992Z"
    },
    "dataSource" : "LMS",
    "traceId" : "84f1300e-f345-4d2d-8b35-8235d1575d55",
    "entityProps" : {
        "entity" : "student",
        "entityId" : "635169d4f2fd2d4fce9ac23d"
    }
}'
```
- To follow the logs run command
```shell
docker-compose logs -f event-manager-api-client-python
```
