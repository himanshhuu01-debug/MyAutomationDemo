pipeline {
    agent any

    stages {

        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest tests --alluredir=allure-results
                '''
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
            archiveArtifacts artifacts: 'allure-results/*', fingerprint: true
        }
    }
}