
pipeline {
    agent any
    
    environment {
        SSH_HOST = 'microservice.auth.ratchaphon1412.co'
        SSH_PORT = '22'
        SSH_USER = 'root'
    }
    
    stages {
        stage('SSH to Target Server') {
            steps {
                script {
                  
                    sh """
                        ssh ${SSH_USER}@${SSH_HOST} -y <<EOF
                        cd ~/microservice-django-auth-service
                        docker compose  -f docker-compose.prod.yml down
                        git pull
                        docker compose -f docker-compose.prod.yml up -d --build
                        docker compose exec -it app-auth-server bash <<EOF
                        poetry run pyhon3 manage.py collectstatic --no-input --clear
                        poetry run python3 manage.py makemigrations --no-input
                        poetry run python3 manage.py migrate --no-input
EOF
                        docker system prune -f
                        docker compose -f docker-compose.prod.yml restart
EOF
                    """
                    
                }
            }
        }
    }
}
