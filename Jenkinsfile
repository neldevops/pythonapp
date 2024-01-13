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
            
                    sh 'docker ps'
                    sh 'docker build --rm -it -p 8000:8000 flaskapp01 .'
                    
        
            }
        }

        stage('deploy') {
            steps {
               echo 'this is the deploy stage
            }
        }
    }
}
