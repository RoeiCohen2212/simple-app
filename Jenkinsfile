pipeline {
    agent any

    environment {
        IMAGE = "tcohen123/simple-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE}:latest ."
            }
        }

        stage('Test App') {
            steps {
                sh """
                docker run -d -p 5000:5000 --name test-app ${IMAGE}:latest
                sleep 3
                curl -f http://localhost:5000
                docker rm -f test-app
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin
                docker push ${IMAGE}:latest
                """
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh "ansible-playbook -i inventory.ini deploy_app.yml"
            }
        }
    }
}