pipeline {
    agent any

    tools {
        allure 'Default-Allure'
    }

    environment {
        PYTHON_VERSION  = '3.9.18'
        ALLURE_RESULTS  = 'allure-results'
        ALLURE_REPORT   = 'allure-report'
        PYENV_ROOT      = "$HOME/.pyenv"
        PATH            = "$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
    }

    stages {

        stage('Setup Python & Dependencies') {
            steps {
                sh '''
                    set -e
                    echo "--- Setting up pyenv and Python ---"
                    export PYENV_ROOT="$HOME/.pyenv"
                    export PATH="$PYENV_ROOT/bin:$PATH"
                    eval "$(pyenv init -)"
                    pyenv shell "${PYTHON_VERSION}"

                    echo "--- Python version ---"
                    python --version

                    echo "--- Creating virtual environment ---"
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

        stage('Generate Allure Report (CLI)') {
            steps {
                sh '''
                    echo "--- Generating Allure Report ---"
                    export PATH="$ALLURE_HOME/bin:$PATH"
                    allure --version
                    allure generate ${ALLURE_RESULTS} --clean -o ${ALLURE_REPORT}
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure(
                    report: "${ALLURE_REPORT}",
                    results: [[path: "${ALLURE_RESULTS}"]]
                )
            }
        }

        stage('Email Report') {
            steps {
                emailext(
                    subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        Hi Team,<br><br>
                        The latest automation run for <b>${env.JOB_NAME}</b> has completed.<br>
                        <b>Status:</b> ${currentBuild.currentResult}<br>
                        <b>Allure Report:</b> <a href="${env.BUILD_URL}allure">Click here to view</a><br><br>
                        Regards,<br>QA Automation Team
                    """,
                    mimeType: 'text/html',
                    to: "vidya.hampiholi@lightmetrics.co, divya.gajanana@lightmetrics.co"
                )
            }
        }
    }

    post {
        failure {
            emailext(
                subject: "❌ FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Hi Team,<br><br>
                    The automation run for <b>${env.JOB_NAME}</b> has failed.<br>
                    <b>Status:</b> ${currentBuild.currentResult}<br>
                    <b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a><br><br>
                    Regards,<br>QA Automation Team
                """,
                mimeType: 'text/html',
                to: "vidya.hampiholi@lightmetrics.co, divya.gajanana@lightmetrics.co"
            )
        }

        always {
            echo 'Cleaning up workspace and virtual environment...'
            sh 'rm -rf venv'
            archiveArtifacts artifacts: '**/*.png', fingerprint: true
            deleteDir()
        }
    }
}
