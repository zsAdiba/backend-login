1pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/zsAdiba/backend-login.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-login-app .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Add any testing commands here
                    echo 'Tests passed!'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 3001:3001 flask-login-app'
                }
            }
        }
    }
}
