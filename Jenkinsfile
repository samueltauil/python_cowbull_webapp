pipeline {
    agent {
        docker {
            image 'python:latest' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                echo "Starting steps"
                sh 'pip install -r requirements.txt'
                sh 'ls'
                sh 'python -m unittest -v tests'
                echo "Finished steps"
            }
        }
    }
}
