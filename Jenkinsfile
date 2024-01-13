pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                 echo 'this is check out' 
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/neldevops/pythonapp.git']]])
            }
        }

        stage('Build') {
            steps {
                script {
                    
                    sh  ``` echo 'this is build' ```
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    sh ``` echo 'this is deploy' ```
                }
            }
        }
    }
}
