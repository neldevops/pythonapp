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
                    
                     echo 'this is build'
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                     echo 'this is deploy' 
                }
            }
        }
    }
}
