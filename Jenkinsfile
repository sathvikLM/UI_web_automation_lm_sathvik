pipeline {
    agent any

    tools {
        allure 'Default-Allure'
    }

    environment {
        PYTHON_VERSION = '3.9.18'
        ALLURE_RESULTS = "allure-results"
        ALLURE_REPORT = "allure-report"
        PYENV_ROOT = "$HOME/.pyenv"
        PATH = "$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
    }

    stages {
        stage('Setup Python & Dependencies') {
            steps {
                sh '''
                    set -e

                    echo "--- Loading pyenv ---"
                    export PYENV_ROOT="$HOME/.pyenv"
                    export PATH="$PYENV_ROOT/bin:$PATH"
                    eval "$(pyenv init -)"
                    pyenv shell "${PYTHON_VERSION}"

                    echo "--- Python version ---"
                    python --version

                    echo "--- Setting up venv ---"
                    python -m venv venv
                    . venv/bin/activate

                    echo "--- Installing requirements ---"
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --alluredir=${ALLURE_RESULTS}
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    export PATH="$ALLURE_HOME/bin:$PATH"
                    allure --version
                    allure generate ${ALLURE_RESULTS} --clean -o ${ALLURE_REPORT}
                '''
            }
        }

        stage('Publish Allure HTML Report') {
            steps {
                publishHTML([
                    reportDir: "${ALLURE_REPORT}",
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
                    body: "Allure report available at: ${env.BUILD_URL}allure-report",
                    to: "vidya.hampiholi@lightmetrics.co"
                )
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace and virtual environment..."
            sh 'rm -rf venv'
            archiveArtifacts artifacts: '**/*.png', fingerprint: true
            deleteDir()
        }
    }
}
