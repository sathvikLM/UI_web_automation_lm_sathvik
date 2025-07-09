pipeline {
    agent any

    environment {
        PYTHON = "python3.9"
        VENV_DIR = ".venv"
        ALLURE_RESULTS = "allure-results"
        PATH = "/var/lib/jenkins/.pyenv/shims:/var/lib/jenkins/.pyenv/bin:${env.PATH}"
        PYENV_VERSION = "3.9.18"
    }

    stages {
        stage('Setup Python Virtual Env') {
            steps {
                sh '''
                    set -e
                    echo "Creating Python virtual environment..."
                    $PYTHON -m venv $VENV_DIR
                    echo "Activating virtual environment..."
                    . $VENV_DIR/bin/activate
                    echo "Upgrading pip and installing dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Email Report') {
            steps {
                emailext(
                    subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "Allure report for build: ${env.BUILD_URL}allure-report",
                    to: "sathviksecond@gmail.vom"
                )
            }
        }
    }

    post {
        always {
            echo "Cleaning up virtual environment"
            sh "rm -rf $VENV_DIR"
        }
    }
}
