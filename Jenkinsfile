pipeline {
    agent any

    environment {
        PYTHON = "python3.9"
        VENV_DIR = ".venv"
        ALLURE_RESULTS = "allure-results"
        PATH = "/var/lib/jenkins/.pyenv/shims:/var/lib/jenkins/.pyenv/bin:${env.PATH}"
        PYENV_VERSION = "3.9.18"
        DISPLAY = ':99'
    }

    stages {
        stage('Start Xvfb') {
            steps {
                sh '''
                    Xvfb :99 -screen 0 1920x1080x24 &
                    sleep 3
                '''
            }
        }

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

        stage('Run Pytest with Allure') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pytest --alluredir=$ALLURE_RESULTS
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate $ALLURE_RESULTS --clean -o allure-report'
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
            sh 'pkill Xvfb || true'
        }
    }
}
