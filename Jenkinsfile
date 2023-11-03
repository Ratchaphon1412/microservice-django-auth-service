
pipeline {
    agent any
    
    environment {
        SSH_HOST = ${SSH_HOST}
        SSH_PORT = '22'
        SSH_USER = ${SSH_USER}
    }
    
    stages {
        stage('SSH to Target Server') {
            steps {
                script {
                    sshagent(['SSH_KEY']) {
                        sh """
                            ssh ${SSH_USER}@${SSH_HOST} -y << EOF
                        	cd ~/microservice-django-auth-service
                            docker compose  -f docker-compose.prod.yml down
                            git pull
                            docker compose -f docker-compose.prod.yml up -d --build
                            docker system prune -f
                            docker compose -f docker-compose.prod.yml restart
                            EOF
                        """
                    }
                }
            }
        }
    }
}
