pipeline {
    agent any

    environment {
        IMAGE_NAME = 'audioprepender'
        CONTAINER_NAME = 'audioprepender_container'
    }

    stages {
        stage('Checkout Repo') {
            steps {
                // Explicitly specify the main branch
                git branch: 'main', url: 'https://github.com/asrahmann/AudioPrepender.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container (Optional)') {
            steps {
                // Stop and remove container if it exists, then run the new one
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }
}
