# Cookiecutter FastAPI Blueprint

## Features
- [X] Basic api router


## Usage
- Step 1: Create template
```
cookiecutter FastAPI-Blueprint
```
- Step 2: Change to project directory
```
cd <Project Name>/backend
```
- Step 3: [Optional] Initalize git repository
```
git init
```
- Step 4: Run scripts
```
./scripts/dev_build.sh
```
- Step 5: Building images and run images up
```
# Check root endpoint
curl 127.0.0.1:{{ cookiecutter.application_port }}
# Check get me endpoint
curl 127.0.0.1:{{ cookiecutter.application_port }}/users/me 
# Check healthy check endpoint
curl 127.0.0.1:{{ cookiecutter.application_port }}/status/health
```
- Step 6: Now you are totally create your own develop workspace, enjoy your project!!



## Python Version
- 3.8.10