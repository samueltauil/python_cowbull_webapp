pipeline {
    agent {
        docker {
            image 'python:latest' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python -m unittest -v tests'
            }
        }
    }
}
