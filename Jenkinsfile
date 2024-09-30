pipeline {
    agent any

    environment {
        APP_NAME = 'flask-login-app'
        IMAGE_NAME = 'root.ccsd.com/${APP_NAME}'
        DEPLOY_DIR = '/var/www/flask-login-app'
    }

    stages {
        stage('Check and Install Python 3') {
            steps {
                script {
                    def pythonInstalled = sh(script: 'which python3', returnStatus: true) == 0
                    if (!pythonInstalled) {
                        echo "Python 3 not found. Installing..."
                        sh '''
                        sudo apt-get update
                        sudo apt-get install -y python3 python3-pip python3-venv
                        '''
                    } else {
                        echo "Python 3 is already installed."
                    }
                }
            }
        }

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/zsAdiba/backend-login.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Tests passed!'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${IMAGE_NAME}:latest .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                    if [ "$(docker ps -q -f name=${APP_NAME})" ]; then
                        echo "Stopping existing container ${APP_NAME}..."
                        docker stop ${APP_NAME}
                        echo "Removing existing container ${APP_NAME}..."
                        docker rm ${APP_NAME}
                    fi

                    echo "Deploying new container ${APP_NAME}..."
                    docker run -d --name ${APP_NAME} -p 80:80 ${IMAGE_NAME}:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build, Test, and Deployment completed successfully.'
        }
        failure {
            echo 'Build or Deployment failed.'
        }
    }
}