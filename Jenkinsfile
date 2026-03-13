pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
        VENV_DIR = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat '''
                    "%PYTHON%" -m venv "%VENV_DIR%"
                    "%VENV_DIR%\\Scripts\\python.exe" -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%VENV_DIR%\\Scripts\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%VENV_DIR%\\Scripts\\python.exe" -m pytest tests --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }
    }
}