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
        ALLURE_REPORT_FOLDER = 'allure-report'
        ALLURE_SINGLE_FILE_DIR = 'allure-report.html'
        ALLURE_FINAL_REPORT = 'allure-test-report.html'  // Clean filename
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
                    sh '''
                        set -e
                        echo "--- Generating Allure Report folder ---"
                        export PATH="$ALLURE_HOME/bin:$PATH"
                        allure generate "$ALLURE_RESULTS" --clean -o "$ALLURE_REPORT_FOLDER"
                    '''
                    allure(
                        report: "${ALLURE_REPORT_FOLDER}",
                        results: [[path: "${ALLURE_RESULTS}"]]
                    )
                }
            }
        }

        stage('Create & Email Single-File Report') {
            steps {
                script {
                    // Step 1: Combine the report into a single HTML file
                    echo 'Combining report into a single HTML file...'
                    sh '''
                        set -e
                        . venv/bin/activate
                        
                        # Create the combined report
                        allure-combine "$ALLURE_REPORT_FOLDER" --dest "$ALLURE_SINGLE_FILE_DIR" --auto-create-folders
                        
                        # Move and rename the file to workspace root with a clean name
                        mv "$ALLURE_SINGLE_FILE_DIR/complete.html" "$ALLURE_FINAL_REPORT"
                        
                        echo "--- Verifying final report ---"
                        ls -la "$ALLURE_FINAL_REPORT"
                        echo "File size: $(du -h "$ALLURE_FINAL_REPORT" | cut -f1)"
                    '''

                    // Archive the clean filename
                    echo "Archiving ${ALLURE_FINAL_REPORT}..."
                    archiveArtifacts artifacts: "${ALLURE_FINAL_REPORT}"
                    
                    // Send email with both internal and external options
                    emailext(
                        from: "sathvik.bhat@lightmetrics.co",
                        to: "sathvik.bhat@lightmetrics.co",
                        subject: "[${params.ENVIRONMENT}] Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER} – SUCCESS",
                        body: """
                            Hi Team,<br><br>
                            The latest automation run for <b>${env.JOB_NAME}</b> has completed successfully.<br>
                            <b>Status:</b> SUCCESS<br>
                            <b>Environment:</b> ${params.ENVIRONMENT}<br>
                            <b>Build Number:</b> ${env.BUILD_NUMBER}<br><br>
                            
                            <b>📊 View Results:</b><br>
                            • <a href="${env.BUILD_URL}allure">Interactive Allure Report (Jenkins Users)</a><br>
                            • <a href="${env.BUILD_URL}artifact/${ALLURE_FINAL_REPORT}">Download Standalone HTML Report</a><br><br>
                            
                            <b>📝 Note:</b> The standalone HTML report can be downloaded and opened in any browser without needing Jenkins access.<br><br>

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
