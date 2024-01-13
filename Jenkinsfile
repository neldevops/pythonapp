pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                 echo 'this is check out' 
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/neldevops/pythonapp.git']])
            }
        }

        stage('Build') {
            steps {
                script {
                    
                    docker ps
                    docker build --rm -it flaskapp01 .
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                     
                }
            }
        }
    }
}
