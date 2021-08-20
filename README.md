# Flask API with deployment to [Deta.sh](https://deta.sh) and [Semgrep](https://semgrep.dev/) CI configuration

## Development

### Deta.sh setup

1. Login to [web.deta.sh](https://web.deta.sh/) (Create an account if you don't have one)
2. Create a project
3. Make a note of the API key

### Local Setup

1. Clone this repo
2. Ensure python and pip is installed
3. Install venv `pip3 install virtualenv`
4. Create a virtual environment `virtualenv venv`
5. Activate the virtual environment `source venv/bin/activate`
6. Install the code dependencies `pip3 install -r requirements.txt`
7. Add the API key from Deta to the project through an environment variable DETA_API_KEY
    * For example: `$ export DETA_API_KEY=abcdefghijk`
    >Note: in the repository an API key will be hardcoded intentionally to demonstrate Semgrep. For security purpose the key has been revoked.
8. Run the application with `python3 main.py`

### Semgrep setup

1. Login to [semgrep.dev/login](https://semgrep.dev/login)
2. Authorize and add the Git repository to Semgrep
3. Add custom policies and rules if needed. Sample rule to identify Deta API key is available in this repository [here](rules).
4. Trigger the CI job as you wish and find the results on Semgrep dashboard. Two workflows are provided for use. A token from Semgrep needs to be added as a secret to the repository.

>Note: Semgrep is configured with Github Actions to run on manual trigger (workflow_dispatch). The CI job directly reports findings tothe Semgrep App. If you want to run Semgre for pull requests you will have to modify the workflow accordingly. Please refer to [this documentation](https://semgrep.dev/docs/semgrep-ci/sample-ci-configs/#github-actions) to configure for Pull Requests.

Please feel free to fork and play with the repo. Although contributions are not planned, you may still send a PR if you'd like :)
