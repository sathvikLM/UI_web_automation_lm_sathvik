pipeline {
    agent any

    environment {
        PYTHON = "python3"             // Assumes python3 is installed and in PATH
        VENV_DIR = ".venv"
        ALLURE_RESULTS = "allure-results"
    }

    triggers {
        // Every Monday at 11:00 AM
        cron('0 11 * * 1')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Lightmetrics/UI_web_automation_lm.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh """
                    ${PYTHON} -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    pytest --alluredir=${ALLURE_RESULTS}
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: "${ALLURE_RESULTS}"]]
            }
        }

        stage('Publish HTML Report') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    pytest --html=report.html --self-contained-html
                """
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'HTML Test Report'
                ])
            }
        }

        stage('Send Success Email') {
            steps {
                emailext (
                    subject: "✅ UI Test Passed - Jenkins Weekly Run",
                    body: "The Jenkins weekly UI test run passed successfully. Check Allure/HTML reports for details.",
                    to: 'vidya.hampiholi@lightmetrics.co',
                    attachLog: true
                )
            }
        }
    }

    post {
        failure {
            emailext (
                subject: "❌ UI Test Failed - Jenkins Weekly Run",
                body: "The Jenkins job failed. Please check the logs and report.",
                to: 'vidya.hampiholi@lightmetrics.co',
                attachLog: true
            )
        }
    }
}
