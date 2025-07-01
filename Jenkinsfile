pipeline {
    agent any

    environment {
        PYTHON = "C:\\Python39\\python.exe"  // Adjust this path if needed
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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}
