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
        ALLURE_REPORT_FOLDER = 'allure-report'  // Renamed for clarity
        ALLURE_SINGLE_FILE = 'allure-report.html' // The new final artifact
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
                    #!/bin/bash
                    set -e

                    echo "--- Setting up pyenv and Python ---"
                    export PYENV_ROOT="$HOME/.pyenv"
                    export PATH="$PYENV_ROOT/bin:$PATH"
                    eval "$(pyenv init -)"

                    if ! pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then
                      pyenv install "$PYTHON_VERSION"
                    fi
                    pyenv shell "$PYTHON_VERSION"

                    echo "--- Using Python version: $(python --version) ---"
                    echo "--- Creating virtual environment ---"
                    python -m venv venv
                    . venv/bin/activate

                    echo "--- Installing requirements ---"
                    # This now installs allure-combine automatically from your requirements.txt
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

        stage('Generate Allure Report') {
            steps {
                script {
                    // Generate the standard multi-file report first
                    sh '''
                        set -e
                        echo "--- Generating Allure Report folder ---"
                        export PATH="$ALLURE_HOME/bin:$PATH"
                        allure generate "$ALLURE_RESULTS" --clean -o "$ALLURE_REPORT_FOLDER"
                    '''
                    // Then publish it to the Jenkins UI for online viewing
                    allure(
                        report: "${ALLURE_REPORT_FOLDER}",
                        results: [[path: "${ALLURE_RESULTS}"]]
                    )
                }
            }
        }

        // --- NEW/MODIFIED STAGES START HERE ---

        stage('Create & Email Single-File Report') {
            steps {
                script {
                    // Step 1: Combine the report into a single HTML file
                    echo 'Combining report into a single HTML file...'
                    sh '''
                        set -e
                        . venv/bin/activate
                        allure-combine "$ALLURE_REPORT_FOLDER" --dest "$ALLURE_SINGLE_FILE" --auto-create-folders
                    '''

                    // Step 2: Archive the new single file artifact
                    echo "Archiving ${ALLURE_SINGLE_FILE}..."
                    archiveArtifacts artifacts: "${ALLURE_SINGLE_FILE}"
                    
                    // Step 3: Send the email with the updated link
                    emailext(
                        from: "sathvik.bhat@lightmetrics.co",
                        to: "sathvik.bhat@lightmetrics.co",
                        subject: "[${params.ENVIRONMENT}] Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER} – SUCCESS",
                        body: """
                            Hi Team,<br><br>
                            The latest automation run for <b>${env.JOB_NAME}</b> has completed successfully.<br>
                            <b>Status:</b> SUCCESS<br>
                            <b>Environment:</b> ${params.ENVIRONMENT}<br>
                            <b>Allure Report (view online on Jenkins):</b> <a href="${env.BUILD_URL}allure">Click here to view</a><br>
                            
                            <!-- THIS LINK IS NOW CHANGED -->
                            <b>Allure Report (download clickable file):</b> <a href="${env.BUILD_URL}artifact/${ALLURE_SINGLE_FILE}">Click here to download HTML</a><br><br>

                            Regards,<br>QA Automation Team
                        """,
                        mimeType: 'text/html'
                    )
                }
            }
        }
    }

    post {
        failure {
            emailext(
                from: "sathvik.bhat@lightmetrics.co",
                to: "sathvik.bhat@lightmetrics.co",
                subject: "[${params.ENVIRONMENT}] FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Hi Team,<br><br>
                    The automation run for <b>${env.JOB_NAME}</b> has failed.<br>
                    <b>Status:</b> ${currentBuild.currentResult}<br>
                    <b>Environment:</b> ${params.ENVIRONMENT}<br>
                    <b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a><br><br>
                    Regards,<br>QA Automation Team
                """,
                mimeType: 'text/html'
            )
        }
        always {
            echo 'Final cleanup...'
            deleteDir()
        }
    }
}
