# Medical-Chatbot
GenAI Medical Chatbot   


# How to run?
### STEP 01: Create Repository in github and clone repository in local system

Create a new repository in the GitHub

Create a new folder `GenAI_Projects` in the local system.

Change the directory to the `GenAI_Projects`

```bash
cd  GenAI_Projects
```

Clone the repository

```bash
git clone  <repo from https://github.com/>
```
### STEP 02: Create a conda environment after opening the repository

```bash
conda create --prefix ./venv python=3.11 -y
```

```bash
conda activate <venv_path>
```


### STEP 03: install the requirements
```bash
pip install -r requirements.txt
```


### STEP 04- create a project folder structure

create a `template.py` file for creating project folder structure

```bash
python template.py
```

### STEP 05- Commit the changes to the github repository

To push the changes to github

Create `Personal Access Token(PAT)` in the GitHub account

Github ==> Settings ==> Developer Settings ==> Personal Access Tokens ==> Tokens(classic)
create the Token with scopes like "repo, user, and workflow"
Note the Token



```bash
git config --list
git config --global --list
git config --global user.name "<github-username>"
git config --global user.email "<github-user_email>"
git add .
git commit -m "project structure is added"
git push origin main
```

If it asks for the login into `github` then login with passkey and provide the `PAT`

### STEP 06: Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```



```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GROQ
- Pinecone

