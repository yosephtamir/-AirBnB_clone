# AirBnB_clone
![hbnb](hbnb.png)

## The following is what this project works
    • A parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
    • simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    • lasses used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    • abstracted storage engine of the project: File storage.
    • unittests to validate all our classes and storage engine

## Command Interpreter
This makes us able to manage this project
    • Create a new object (ex: a new User or a new Place)
    • Retrieve an object from a file, a database etc…
    • Do operations on objects (count, compute stats, etc…)
    • Update attributes of an object
    • Destroy an object

