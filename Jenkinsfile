pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3"
    }

   triggers {
    // Every Monday at 11:00 AM
    cron('0 11 * * 1')
  }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/Lightmetrics/UI_web_automation_lm.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=report.html'
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
