pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh ``` echo 'this is check out' ```
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
