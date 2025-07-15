pipeline {
    agent any

    tools {
        allure 'Default-Allure'
    }

    environment {
        ALLURE_RESULTS = "allure-results"
        PYTHON_VERSION = '3.9.18'
    }

    stages {
        stage('Setup, Test & Generate Results') {
            steps {
                sh '''
                    set -e
                    export PYENV_ROOT="$HOME/.pyenv"
                    export PATH="$PYENV_ROOT/bin:$PATH"
                    eval "$(pyenv init -)"
                    pyenv shell "${PYTHON_VERSION}"
                    export PATH="$ALLURE_HOME/bin:$PATH"

                    echo "--- Verifying tool versions ---"
                    python --version
                    allure --version

                    echo "--- Setting up project ---"
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt

                    echo "--- Running tests ---"
                    pytest --alluredir=$ALLURE_RESULTS
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure report: 'allure-report', results: [[path: ALLURE_RESULTS]]
            }
        }

        stage('Email Report') {
            steps {
                emailext(
                    subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "Allure report for build: ${env.BUILD_URL}allure",
                    to: "vidya.hampiholi@lightmetrics.co"
                )
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            deleteDir()
        }
    }
}
