pipeline {
    agent any

    tools {
        allure 'Default-Allure'
    }

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['QA', 'PROD', 'BETA'],
            description: 'Select environment to run tests'
        )
    }

    environment {
        PYTHON_VERSION  = '3.9.18'
        ALLURE_RESULTS  = 'allure-results'
        ALLURE_REPORT   = 'allure-report'
        PYENV_ROOT      = "$HOME/.pyenv"
        // Note: PATH modifications in the environment block can be tricky.
        // It's more robust to set it inside the sh steps as you are doing.
        TEST_ENV        = "${params.ENVIRONMENT}"
    }

    stages {

        stage('Print Build Parameters') {
            steps {
                echo "▶ Selected environment: ${params.ENVIRONMENT}"
            }
        }

        stage('Setup Python & Dependencies') {
            steps {
                sh '''
                    set -e
                    echo "--- Setting up pyenv and Python ---"
                    export PYENV_ROOT="$HOME/.pyenv"
                    export PATH="$PYENV_ROOT/bin:$PATH"
                    eval "$(pyenv init -)" // Using full init for 'pyenv shell'
                    pyenv install -s "$PYTHON_VERSION"
                    pyenv shell "$PYTHON_VERSION"

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
                    set -e
                    . venv/bin/activate
                    echo "--- Running tests in $TEST_ENV environment ---"
                    pytest --env="$TEST_ENV" --alluredir="$ALLURE_RESULTS"
                '''
            }
        }

        stage('Generate Allure Report (CLI)') {
            steps {
                sh '''
                    set -e
                    echo "--- Generating Allure Report ---"
                    export PATH="$ALLURE_HOME/bin:$PATH"
                    allure --version
                    allure generate "$ALLURE_RESULTS" --clean -o "$ALLURE_REPORT"
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

        // The main success email is sent here, as part of the stages
        stage('Email Success Report') {
            // This stage will only run if all previous stages succeeded
            steps {
                script {
                    // We must zip the report here, before the post block runs
                    echo 'Zipping Allure report for email attachment...'
                    sh 'zip -r allure-report.zip allure-report'
                    archiveArtifacts artifacts: 'allure-report.zip'

                    // Now send the email
                    emailext(
                        subject: "[${params.ENVIRONMENT}] Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER} – SUCCESS",
                        body: """
                            Hi Team,<br><br>
                            The latest automation run for <b>${env.JOB_NAME}</b> has completed successfully.<br>
                            <b>Environment:</b> ${params.ENVIRONMENT}<br>
                            <b>Allure Report (view):</b> <a href="${env.BUILD_URL}allure">Click here to view</a><br>
                            <b>Allure Report (download):</b> <a href="${env.BUILD_URL}artifact/allure-report.zip">Click here to download ZIP</a><br><br>
                            Regards,<br>QA Automation Team
                        """,
                        mimeType: 'text/html',
                        to: "sathvik.bhat@lightmetrics.co"
                    )
                }
            }
        }
    }

    // The post block is now ONLY for failure notifications and cleanup
    post {
        failure {
            emailext(
                subject: "[${params.ENVIRONMENT}] FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Hi Team,<br><br>
                    The automation run for <b>${env.JOB_NAME}</b> has failed.<br>
                    <b>Status:</b> ${currentBuild.currentResult}<br>
                    <b>Environment:</b> ${params.ENVIRONMENT}<br>
                    <b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a><br><br>
                    Regards,<br>QA Automation Team
                """,
                mimeType: 'text/html',
                to: "sathvik.bhat@lightmetrics.co"
            )
        }

        always {
            // This block runs last, after all stages and other post-conditions.
            echo 'Cleaning up workspace...'
            deleteDir()
        }
    }
}
