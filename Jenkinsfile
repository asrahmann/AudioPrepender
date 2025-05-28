pipeline {
    agent any

    environment {
        IMAGE_NAME = "audioprepender"
        CONTAINER_NAME = "audioprepender_container"
    }

    stages {
        stage('Checkout Repo') {
            steps {
                git 'https://github.com/asrahmann/AudioPrepender.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Use host network so Docker build has outbound internet
                sh 'docker build --network=host -t $IMAGE_NAME .'
            }
        }

        stage('Run Container (Optional)') {
            steps {
                // Stop and remove existing container if running
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                // Start the new container
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }
}
