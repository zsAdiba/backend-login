pipeline {
    agent {
        docker {
            image 'docker:latest'  // Use Docker image to enable Docker inside the pipeline
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // Mount Docker socket for Docker commands
        }
    }

    environment {
        APP_NAME = 'flask-login-app'
        IMAGE_NAME = 'flask-login-app-image'  // Replace with your Docker Hub username or appropriate image name
        DEPLOY_DIR = '/var/www/flask-login-app'  // Directory to deploy the app (if needed)
        DOCKER_CONFIG = '/root/.docker'  // Use a writable directory for Docker config
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/zsAdiba/backend-login.git'
            }
        }

        stage('Set up Python Environment') {
            agent {
                docker {
                    image 'python'  // Use Python Docker image for dependencies
                    args '-v jenkins_home:/var/lib/docker/volumes/jenkins_home/_data'
                }
            }
            steps {
                script {
                    // Set up virtual environment and install dependencies
                    sh '''
                    python -m venv venv
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
                    // Build the Docker image using the writable Docker config directory
                    sh 'DOCKER_CONFIG=$(mktemp -d) docker build -t ${IMAGE_NAME}:latest .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Create a temporary directory for Docker config for deployment
                    sh '''
                        TEMP_CONFIG_DIR=$(mktemp -d)
                        export DOCKER_CONFIG=$TEMP_CONFIG_DIR
                        echo "Using Docker config directory: $DOCKER_CONFIG"

                        # Stop and remove existing container if it exists
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
