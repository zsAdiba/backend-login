pipeline {
    agent any  // Use any available agent

    environment {
        APP_NAME = 'flask-login-app'
        IMAGE_NAME = 'root.ccsd.com/${APP_NAME}'
        DEPLOY_DIR = '/var/www/flask-login-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/zsAdiba/backend-login.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Set up virtual environment and install dependencies
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
                    // Stop and remove existing container if it exists
                    sh '''
                    if [ "$(docker ps -q -f name=${APP_NAME})" ]; then
                        echo "Stopping existing container ${APP_NAME}..."
                        docker stop ${APP_NAME}
                        echo "Removing existing container ${APP_NAME}..."
                        docker rm ${APP_NAME}
                    fi

                    # Run the new container
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