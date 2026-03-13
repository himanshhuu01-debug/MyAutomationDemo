pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
        VENV_DIR = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/himanshhuu01-debug/MyAutomationDemo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    IF NOT EXIST "%VENV_DIR%\\Scripts\\python.exe" (
                        echo Creating virtual environment...
                        "%PYTHON%" -m venv "%VENV_DIR%"
                    ) ELSE (
                        echo Venv already exists, skipping creation...
                    )
                    "%VENV_DIR%\\Scripts\\python.exe" -m pip install --upgrade pip --quiet
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%VENV_DIR%\\Scripts\\python.exe" -m pip install -r requirements.txt --quiet'
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