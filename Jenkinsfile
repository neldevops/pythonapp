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
                    sh 'docker system prune --all --force'
                    sh 'docker build -t flaskapp01:${BUILD_NUMBER} .'
                    sh 'echo ${BUILD_NUMBER}'
                    
            }
        }

        stage('deploy') {
            steps {
               sh 'docker run -d --rm -p 8000:8000 flaskapp01:${BUILD_NUMBER}'
            }
        }
     
    //  stage('cleanup') {
    //         steps {
                   
    //            sh 'docker system prune --all --force'
    //         }
    //     }

    }
}
