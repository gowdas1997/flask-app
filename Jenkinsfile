pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-redis-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/gowdas1997/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Deploy Locally (docker-compose)') {
            steps {
                sh "docker-compose down || true"
                sh "docker-compose up -d --build"
            }
        }

        stage('Verify') {
            steps {
                sh "sleep 5 && curl -s http://localhost:5000 || true"
            }
        }
    }

    post {
        success {
            echo 'Build and deploy succeeded!'
        }
    }
}
