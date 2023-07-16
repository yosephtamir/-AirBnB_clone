# AirBnB_clone
![hbnb](hbnb.png)

## The following is what this project works
    • A parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
    • simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    • lasses used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    • abstracted storage engine of the project: File storage.
    • unittests to validate all our classes and storage engine

## Command Interpreter
### This makes us able to manage this project:
    • Create a new object (ex: a new User or a new Place)
    • Retrieve an object from a file, a database etc…
    • Do operations on objects (count, compute stats, etc…)
    • Update attributes of an object
    • Destroy an object

## Files and Directories
    • models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
    • tests directory will contain all unit tests.
    • console.py file is the entry point of our command interpreter.
    • models/base_model.py file is the base class of all our models. It contains common elements:
        ◦ attributes: id, created_at and updated_at
        ◦ methods: save() and to_json()
    • models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

