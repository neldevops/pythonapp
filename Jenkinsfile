pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                 echo 'this is check out' 
                checkout scmGit(branches: [[name: '*/test']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/neldevops/pythonapp.git']])
            }
        }

        stage('Docker Build') {
            steps {
                
                    sh 'docker ps'
                    sh 'docker build -t flaskapp01 .'
                    
        
            }
        }

        // stage('deploy') {
        //     steps {
        //        echo 'this is the deploy stage'
        //     }
        // }
    }
}
