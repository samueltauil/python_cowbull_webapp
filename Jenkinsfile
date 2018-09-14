pipeline {
    agent {
        docker {
            image 'python:latest' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'pwd',
                sh 'ls'
                sh 'python -m unittest -v tests'
            }
        }
    }
}
