pipeline {
    agent any

    environment {
        IMAGE_NAME = "roei2212/simple-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Test App') {
            steps {
                sh '''
                    docker run -d -p 5000:5000 --name test-app $IMAGE_NAME
                    sleep 3
                    curl -f http://localhost:5000
                    docker rm -f test-app
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh '''
                    ansible-playbook -i inventory.ini deploy.yml
                '''
            }
        }
    }
}