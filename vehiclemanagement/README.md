## Vehicle Service Management System


### Setup
1. Clone the Repository
2. Install Pipenv
3. Run `pipenv install`
4. Run `python manage.py migrate`


### Usage
All APIs are accessible through Django REST framework UI, but here is the detailed API usage.

#### Vehicles
**GET** `/vehicles/`

Lists all vehicles in the system.
```[
    {
        "id": 1,
        "vin": "Car 1",
        "make": "BMW",
        "model": "BMW",
        "year": 2000
    },
    {
        "id": 2,
        "vin": "Car 2",
        "make": "BMW 2",
        "model": "BMW 2",
        "year": 2000
    },
    {
        "id": 3,
        "vin": "Car 3",
        "make": "BMW 3",
        "model": "BMW 3",
        "year": 3000
    }
]
```

**GET** `/vehicles/{PK}/`

Retrieve a specific vehicle information from the system.

Sample Response:
```
{
    "id": 1,
    "vin": "Car 1",
    "make": "BMW",
    "model": "BMW",
    "year": 2000
}
```

**POST** `/vehicles/`

Creates a vehicle in the system.

Sample Request:
```
{
    "vin": "test",
    "make": "test",
    "model": "test",
    "year": 2000,
}
```

Sample Response:
```
{
    "id": 4,
    "vin": "test",
    "make": "test",
    "model": "test",
    "year": 2000
}
```

**PUT**  `/vehicles/{PK}/`

Updates a specific vehicle information in the system.

Sample Request:

```
{
    "vin": "test",
    "make": "test",
    "model": "test",
    "year": 2000
}
```

Sample Response:

```
{
    "id": 1,
    "vin": "test",
    "make": "test",
    "model": "test",
    "year": 2000
}
```

**DELETE** `/vehicles/{PK}/`

Deletes a vehicle from the system, returns 204.

Returns this when an object does not match.
```
{
    "detail": "No Vehicle matches the given query."
}
```

#### Services

**GET** `/services/`

Lists all services in the system.

Sample Response:
```
[
    {
        "id": 2,
        "description": "Test Car Two Fix",
        "cost": 2000.0,
        "date": "1111-12-11",
        "vehicle": 2
    },
    {
        "id": 4,
        "description": "Another fix for the docs",
        "cost": 312.0,
        "date": "2024-09-02",
        "vehicle": 2
    }
]
```

**GET** `/services/{PK}`

Gets a singular service information.

Sample Response:
```
{
    "id": 2,
    "description": "Test Car Two Fix",
    "cost": 2000.0,
    "date": "1111-12-11",
    "vehicle": 2
}
```

**POST** `/services/`

Creates a new service in the system.

Sample Request:

```
{
    "description": "description",
    "cost": 2000,
    "date": "2000-12-12",
    "vehicle": 2
}
```

Sample Response:

```
{
    "id": 6,
    "description": "description",
    "cost": 2000.0,
    "date": "2000-12-12",
    "vehicle": 2
}
```

**PUT** `/services/{PK}/`

Updates existing service.

Sample Request:

```
{
    "description": "description",
    "cost": 2000,
    "date": "2000-12-12",
    "vehicle": 2
}
```

Sample Response:

```
{
    "id": 2,
    "description": "description",
    "cost": 2000.0,
    "date": "2000-12-12",
    "vehicle": 2
}
```

**DELETE** `/services/{PK}/`

Delete a service from the system.



#### Mechanic

**GET** `/mechanics/`

Lists all mechanics in the system

Sample response:
```
[
    {
        "id": 1,
        "name": "Ahmad",
        "specialization": "Mechanic",
        "services": [
            2
        ]
    },
    {
        "id": 2,
        "name": "Banana",
        "specialization": "Mechanic",
        "services": [
            2
        ]
    },
    {
        "id": 3,
        "name": "Fananana",
        "specialization": "Banana",
        "services": [
            2
        ]
    }
]
```


**GET** `/mechanics/{PK}`

Retrieves specific mechanic information

Sample Response:
```
{
    "id": 1,
    "name": "Ahmad",
    "specialization": "Mechanic",
    "services": [
        2
    ]
}
```

**GET** `/mechanics/count_by_specialization/`

Sample Response:
``` 
[
    {
        "specialization": "Banana",
        "total": 1
    },
    {
        "specialization": "Mechanic",
        "total": 2
    }
]
```


**GET** `/mechanics/{PK}/vehicles_serviced`

Sample Response:
```
[
    {
        "id": 4,
        "vin": "test",
        "make": "test",
        "model": "test",
        "year": 2000
    },
    {
        "id": 2,
        "vin": "Car 2",
        "make": "BMW 2",
        "model": "BMW 2",
        "year": 2000
    },
    {
        "id": 5,
        "vin": "asd",
        "make": "qwe",
        "model": "asdqwd",
        "year": 23112
    },
    {
        "id": 6,
        "vin": "new",
        "make": "new23",
        "model": "231",
        "year": 12312
    }
]
```

**DELETE**  `/mechanics/{PK}`

Same as above

**UPDATE** `/mechanics/{PK}`

Same as above



#### Leads

**GET** `/leads/`

Lists all leads in the system.

Sample Response:

```
[
    {
        "id": 1,
        "creation_date": "2024-09-12T15:35:11.681221Z",
        "first_name": "Saif",
        "last_name": "Zakarnih",
        "email": "saifzak2012@gmail.com",
        "phone": "12344442",
        "vehicles": [
            2,
            3
        ]
    },
    {
        "id": 2,
        "creation_date": "2024-09-12T15:35:50.436809Z",
        "first_name": "Saif",
        "last_name": "Zak",
        "email": "saifzak2012@gmail.com",
        "phone": "12344442",
        "vehicles": [
            3
        ]
    }
]
```

This can also accept a PK to target a specific lead. Also supports **PUT** and **DELETE** as above

#### Contact

**GET** `/contact/`


Sample Response:
```
[
    {
        "id": 1,
        "contact_type": "phone",
        "contact_value": "not gonna dox my number",
        "lead": 1
    }
]
```


This also supports a specific PK target, **PUT** and **DELETE**.