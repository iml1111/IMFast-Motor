![imfast](https://user-images.githubusercontent.com/29897277/178490130-561c60cd-5e77-47c8-a5a4-239c908a1b13.png)
# IMFast-Motor
**Boilerplate for Large Scale FastAPI Web Backend Structure with Motor(Mongodb) (Edited 2022-07-13)**

This implementation is an extension structure of `IMFast` optimized for Motor(Mongodb async library).

[Here](https://github.com/iml1111/IMFast) you can see the basic implementation concept of IMFast.

## Model Implementation

```shell
...
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       └── sample_model.py # Sample API with Mongodb
│   └── depends
│      └── context.py # Context depends for easy db access
│
├── model
│   ├── __init__.py
│   ├── appmodel
│   │   └── log.py # CRUD Pydantic Model
│   └── mongodb
│       ├── __init__.py # Mongodb Connector & Init.
│       ├── collection
│       │   ├── __init__.py # Base Model
│       │   ├── app_config.py # AppConfig Collection Model
│       │   └── log.py # Log Collection Model
│       └── initializer.py # Mongodb Initializer
...
```

## References

- https://github.com/iml1111/IMFast
