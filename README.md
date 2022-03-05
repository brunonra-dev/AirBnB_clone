![AirBnB](https://raw.githubusercontent.com/brunonra-dev/AirBnB_clone/main/hbnb.png)

# AirBnB clone - The console
Command interpreter to manage AirBnB objects.

This is the first step towards building the first full web application: the AirBnB clone.

What does the console do? 
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Update attributes of an object
- Destroy an object
## How to start it

`$ ./console.py`

## How to use it

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Examples

- Create & Show all objects
```
(hbnb) create BaseModel
418f7c76-ad4d-4152-9df1-588a473e2c49
(hbnb) create User
e0a07ac7-f5d6-4dc0-a7b2-11a5697898c8
(hbnb) all
[BaseModel] (3bc31c3d-6738-4a2c-aeb3-38030ed5fa58) {'id': '3bc31c3d-6738-4a2c-aeb3-38030ed5fa58', 'created_at': datetime.datetime(2022, 3, 5, 18, 3, 51, 716956), 'updated_at': datetime.datetime(2022, 3, 5, 18, 3, 51, 716956)}
[BaseModel] (2c530433-633a-4c95-bc43-8b8730715940) {'id': '2c530433-633a-4c95-bc43-8b8730715940', 'created_at': datetime.datetime(2022, 3, 5, 18, 4, 42, 43897), 'updated_at': datetime.datetime(2022, 3, 5, 18, 4, 42, 43897)}
[User] (cd64880a-d3b1-4fed-9a6b-4ceaf6e3d9a5) {'id': 'cd64880a-d3b1-4fed-9a6b-4ceaf6e3d9a5', 'created_at': datetime.datetime(2022, 3, 5, 18, 4, 47, 20789), 'updated_at': datetime.datetime(2022, 3, 5, 18, 4, 47, 20789)}
[BaseModel] (418f7c76-ad4d-4152-9df1-588a473e2c49) {'id': '418f7c76-ad4d-4152-9df1-588a473e2c49', 'created_at': datetime.datetime(2022, 3, 5, 18, 5, 10, 229097), 'updated_at': datetime.datetime(2022, 3, 5, 18, 5, 10, 229097)}
[User] (e0a07ac7-f5d6-4dc0-a7b2-11a5697898c8) {'id': 'e0a07ac7-f5d6-4dc0-a7b2-11a5697898c8', 'created_at': datetime.datetime(2022, 3, 5, 18, 5, 17, 468140), 'updated_at': datetime.datetime(2022, 3, 5, 18, 5, 17, 468140)}
(hbnb)
```

- Create & Destroy objects
```
(hbnb) create BaseModel
330d38ab-fcda-4622-9fef-d37dd2edc119
(hbnb) create BaseModel
a069bbd1-d5a5-4a2e-b99d-cb0ed074dd3f
(hbnb) all
[BaseModel] (330d38ab-fcda-4622-9fef-d37dd2edc119) {'id': '330d38ab-fcda-4622-9fef-d37dd2edc119', 'created_at': datetime.datetime(2022, 3, 5, 18, 8, 36, 147767), 'updated_at': datetime.datetime(2022, 3, 5, 18, 8, 36, 147767)}
[BaseModel] (a069bbd1-d5a5-4a2e-b99d-cb0ed074dd3f) {'id': 'a069bbd1-d5a5-4a2e-b99d-cb0ed074dd3f', 'created_at': datetime.datetime(2022, 3, 5, 18, 8, 37, 156818), 'updated_at': datetime.datetime(2022, 3, 5, 18, 8, 37, 156818)}
(hbnb) destroy BaseModel 330d38ab-fcda-4622-9fef-d37dd2edc119 
(hbnb) all
[BaseModel] (a069bbd1-d5a5-4a2e-b99d-cb0ed074dd3f) {'id': 'a069bbd1-d5a5-4a2e-b99d-cb0ed074dd3f', 'created_at': datetime.datetime(2022, 3, 5, 18, 8, 37, 156818), 'updated_at': datetime.datetime(2022, 3, 5, 18, 8, 37, 156818)}
(hbnb)
```

## Tests

```
$ python3 -m unittest discover tests
.....................................................
----------------------------------------------------------------------
Ran 53 tests in 0.227s

OK
```

## Created by:

- [Angel Piva](https://github.com/AngelPiva/)
- [Bruno Rodríguez](https://github.com/brunonra-dev/)
