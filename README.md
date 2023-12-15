# Tokenizer
This api gives a token count for a particular string and OpenAI model. 

### JSON Schema
```
{
  "text": "Example text ...",
  "model_name": "gpt-4"
}
```

### Setup

---

Here is the deployed [Multipage Async Flet App using the new FletFastAPI server](https://flet-route-async.fly.dev/) on [Fly.io](https://fly.io/).

To run this locally, [clone the repo](https://github.com/polae/flet-route-async) to your `PROJECT_ROOT_DIRECTORY`.

Navigate to this directory in your terminal.


```
cd path_to/project_root_directory/
```
Now in the project root directory, create your virtual environment.

```
python3.11 -m venv .venv
```
> You may use a different version of python, but the Docker container (below) uses `python:3.10-slim-bullseye`.

Activate the virtual environment.
```
source .venv/bin/activate 
```


And install the required packages:


```
pip install -r requirements.txt
```


You should now be able to run the app:

```
uvicorn main:app --port 8085 --reload
```

View the app at localhost: http://0.0.0.0:8085.






