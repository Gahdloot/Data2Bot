# Data2Bot
The `Schema` class is designed to facilitate the processing and transformation of JSON schema data into a customizable Python dictionary format. This README.md provides an overview of how to use the `Schema` class and its methods.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
    - [Instantiation](#instantiation)
    - [Processing and Saving Data](#processing-and-saving-data)
    - [Previewing Results](#previewing-results)
- [Extended Parameter](#extended-parameter)
- [Example](#example)


## Installation

Clone the repository or download the `schema.py` file. Ensure that you have Python installed on your machine.

## Usage

### Instantiation

Instantiate the `Schema` class by providing the location of the JSON schema file as the first argument. Optionally, you can specify the `extended` parameter as the second argument, indicating whether the schema processing should include nested objects. 

```python
from schema import Schema

# Example instantiation with an extended schema
schema_instance = Schema("data/new_data.json", extended=False)
```

# Example processing and saving data to a file
```python
schema_instance.process_data('data/data_2.json')
```
Previewing Results
To preview the result as a Python dictionary, use the run_loop method.
```python
# Example previewing results
result_dictionary = schema_instance.run_loop()
print(result_dictionary)
```
### Extended Parameter
The extended parameter in the Schema class is optional and set to False by default. When set to True, the class will process each object within the JSON schema, allowing for a more detailed analysis of nested structures.

Please note that the reason for including the extended parameter is to account for scenarios where there may be a need to process each object within an object. The default behavior is to process only the top-level objects in the schema.

```python
from schema import Schema

# Example instantiation and usage
schema_instance = Schema('data/data_1.json', extended=False)
result_dictionary = schema_instance.run_loop()
print(result_dictionary)
```
