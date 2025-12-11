# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

## 2. Design the Class System

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car.

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


```


```python

class Tyre():

    def __init__():
        parameters: none
        output: none
        side-effect: creates an empty dictionary
    
    def record_pressure():
        parameters: the pressure, an an intiger
        output: none
        side-effect: adds tyre pressure to the tyre dict
    
    def record_tread_depth():
        parameters: the tread depth, an an intiger
        output: none
        side-effect: adds tyre tread depth to the tyre dict
    
    {LF tyre: {pressure: 38psi, tread_depth: 5c},
    RF tyre: {pressure: 38psi, tread_depth: 5cm},
    LR tyre: {pressure: 38psi, tread_depth: 5cm},
    RR tyre: {pressure: 38psi, tread_depth: 5cm}}

    history = {11/12/2025:
    {LF tyre: {pressure: 38psi, tread_depth: 5cm},
    RF tyre: {pressure: 38psi, tread_depth: 5cm},
    LR tyre: {pressure: 38psi, tread_depth: 5cm},
    RR tyre: {pressure: 38psi, tread_depth: 5cm}},
    
    11/12/2025:
    {LF tyre: {pressure: 38psi, tread_depth: 5cm},
    RF tyre: {pressure: 38psi, tread_depth: 5cm},
    LR tyre: {pressure: 38psi, tread_depth: 5cm},
    RR tyre: {pressure: 38psi, tread_depth: 5cm}}
    }






```

## 3. Create Examples as Integration Tests

```python
# EXAMPLE

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
