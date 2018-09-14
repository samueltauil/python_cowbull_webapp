pipeline {
    agent {
        docker {
            image 'python:latest' 
        }
    }
    environment {
        PYTHONPATH="tests"
    }
    stages {
        stage('Build') { 
            steps {
                script {
                    def testImage = docker.build("test-image", "./vendor/docker")
                }
                echo "Starting steps"
                sh 'pip install -r requirements.txt'
                sh 'ls'
                sh 'python -m unittest -v tests'
                echo "Finished steps"
            }
        }
    }
}
