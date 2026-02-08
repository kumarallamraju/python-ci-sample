pipeline {
	agent any
	stages {
		stage("Setup") {
			steps {
				sh "python3 -m venv venv"
				sh ". venv/bin/activate && pip install -e ."
				sh ". venv/bin/activate && pip install -r requirements-dev.txt"
			}
		}
		stage("Test") {
			steps {
				sh ". venv/bin/activate && pytest"
			}
		}
	}
}