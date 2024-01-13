pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh 'this is check out'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'this is build'
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    sh 'this is deploy'
                }
            }
        }
    }
}
