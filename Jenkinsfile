pipeline {
    agent any

    environment {
        PYTHON = "C:\\Python39\\python.exe"    // Adjust to your installed Python path
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
                bat "${PYTHON} -m venv ${VENV_DIR}"
                bat "${VENV_DIR}\\Scripts\\activate && pip install --upgrade pip"
                bat "${VENV_DIR}\\Scripts\\activate && pip install -r requirements.txt"
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                bat "${VENV_DIR}\\Scripts\\activate && pytest --alluredir=${ALLURE_RESULTS}"
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
                bat "${VENV_DIR}\\Scripts\\activate && pytest --html=report.html --self-contained-html"
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
