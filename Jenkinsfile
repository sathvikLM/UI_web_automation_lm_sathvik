pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.9.18"
        PYTHON_DIR = "${WORKSPACE}/python39"
        VENV_DIR = ".venv"
        ALLURE_RESULTS = "allure-results"
    }

    stages {

        stage('Install Python 3.9') {
            steps {
                sh '''
                    set -e
                    if ! ${PYTHON_DIR}/bin/python3.9 --version 2>/dev/null; then
                        echo "Installing Python 3.9..."
                        sudo apt-get update
                        sudo apt-get install -y wget build-essential zlib1g-dev \
                            libncurses5-dev libgdbm-dev libnss3-dev libssl-dev \
                            libreadline-dev libffi-dev libsqlite3-dev libbz2-dev

                        wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
                        tar -xf Python-${PYTHON_VERSION}.tgz
                        cd Python-${PYTHON_VERSION}
                        ./configure --prefix=${PYTHON_DIR} --enable-optimizations
                        make -j$(nproc)
                        make install
                        cd ..
                        rm -rf Python-${PYTHON_VERSION}*
                    else
                        echo "Python 3.9 already installed"
                    fi
                '''
            }
        }

        stage('Setup Python Virtual Env') {
            steps {
                sh '''
                    set -e
                    ${PYTHON_DIR}/bin/python3.9 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    python -m ensurepip --upgrade
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest --alluredir=${ALLURE_RESULTS}
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate ${ALLURE_RESULTS} --clean -o allure-report'
            }
        }

        stage('Publish Allure HTML Report') {
            steps {
                publishHTML([
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
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
            sh "rm -rf ${VENV_DIR}"
        }
    }
}
