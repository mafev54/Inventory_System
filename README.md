# Project Inventory System- FastAPI

## Description

This project is an example of a RESTful API developed with FastAPI that allows to perform CRUD (Create, Read, Update, Delete) operations on a movie model. It is designed with an academic approach so that backend programming trainees can use it as a starting point and start working on it.

## Functionalities

- Get tables of products, supplier and supplies
- Get the three tables their ID
- Create tables of products, supplier, supplies
- Update tables of products, supplier, supplies 
- Delete tables of products, supplier, supplies

##  Technologies used

- Python
- FastAPI
- Pydantic

## Installation

1. Clone this repository on your local machine:
   (cloned from )

git clone git@github.com:JSand89/my-movie-app-c9.git


2. Navigate to the project directory:

cd my-movie-app-c9

3. You or one of your partners should change the source of the repository 

git remote -v

git remote remove origin

git remote add origin <new_repository_url>.

4. Now, your peers must clone your repository and you must give them permission to edit it

From the repository on GitHub, go to "Settings" and then to the "Collaborators" section to add them. This is to allow them to make changes. Don't worry, we'll go through this process in class."

5. Install the required dependencies:

pip install -r requirements.txt


## Usage

1. Start the application:

uvicorn main:app --reload


2. Access the API documentation in your browser:

http://localhost:8000/docs


3. Try the different paths available to perform CRUD operations on movies.

end.