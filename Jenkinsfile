pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  // Use the Python Docker image for the pipeline
            args '-v jenkins_home:/var/lib/docker/volumes/jenkins_home/_data'
        }
    }

    environment {
        APP_NAME = 'flask-login-app'
        IMAGE_NAME = 'root.ccsd.com/${APP_NAME}'  // Replace with your Docker Hub username or appropriate image name
        DEPLOY_DIR = '/var/www/flask-login-app'  // Directory to deploy the app (if needed)
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository from the remote URL
                git branch: 'main', url: 'https://github.com/zsAdiba/backend-login.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependencies with user permissions
                    sh 'pip install --user -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // This step can be customized if you have unit tests for your Python app
                    echo 'Tests passed!'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    docker build -t ${IMAGE_NAME}:latest .
                    '''
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

                    // Run the new container
                    echo "Deploying new container ${APP_NAME}..."
                    docker run -d --name ${APP_NAME} -p 80:80 ${IMAGE_NAME}:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
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
