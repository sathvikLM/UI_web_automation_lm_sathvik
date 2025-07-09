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
                    $PYTHON -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    python -m ensurepip --upgrade
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest with Allure (Xvfb)') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    xvfb-run -a pytest --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results --clean -o allure-report'
            }
        }

        stage('Publish Allure HTML Report') {
            steps {
                publishHTML([
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report',
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true
                ])
            }
        }

        stage('Email Report') {
            steps {
                emailext(
                    subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "Allure report for build: ${env.BUILD_URL}allure-report",
                    to: "vidya.hampiholi@lightmetrics.co"
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
