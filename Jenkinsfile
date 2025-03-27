pipeline {
    agent any 

    environment {
        DOCKER_COMPOSE_VERSION = '3.8'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sheila-Kambou01/Projet_devOps.git'
            }
        }

        stage('Build and Deploy with Docker Compose') {
            steps {
                script {
                    bat 'dir'

                    bat 'docker-compose up --build -d'
                }
            }
        }

        stage('Test Application') {
            steps {
                script {
                    bat 'curl --fail http://localhost:8000 || exit 1'
                }
            }
        }

        stage('Notify Success') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    emailext(
                        subject: "Deployment Successful",
                        body: "Your application has been successfully deployed.",
                        to: "shei.kambou16@gmail.com"
                    )
                }
            }
        }

        stage('Notify Failure') {
            when {
                expression { currentBuild.result == 'FAILURE' }
            }
            steps {
                script {
                    // Envoi de la notification par email en cas d'échec
                    emailext(
                        subject: "Deployment Failed",
                        body: "Your application deployment has failed. Please check the logs.",
                        to: "recipient-email@domain.com"
                    )
                }
            }
        }
    }

    post {
        always {
            // Nettoyer si nécessaire après l'exécution
            cleanWs()  // Nettoyer l'espace de travail après chaque exécution
        }
    }
}
