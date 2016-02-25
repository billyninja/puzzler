# PUZZLER
---



----

## Basic Idea

This service provides image puzzles (and its solutions) from [slapchopped](https://github.com/billyninja/slapchop) images through a REST API.

## Testing

`py.test`


---

## Actions/Endpoints

`/solutions`
- **GET**  -> Retrieves a list with all the puzzles

- **GET** `/id` -> Retrieves a single puzzle instance and its **ordered** puzzle-pieces.

`/puzzles`

- **POST**  -> Creates a new puzzle/solution entry

- **OPTIONS** `/id` -> Retrieves a puzzle and its **randomized** pieces.

- **PUT** `/id` -> Informs if a possible solution to the puzzle is valid or not.
    - example of expect json data:
        `{"sequence": [ "6c80fb4251d559b79a347a2ab003d46b",
                        "ec8f237b7d906cb1df3d16a134f352ba",
                        "52cd790885d273c1e6140805b0c6d664",
                        ...]}`
