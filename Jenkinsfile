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
                echo "Starting steps"
                docker run --name redis -d dsanderscan/python_cowbull_redis:4.0.6 redis-server
                sh 'pip install -r requirements.txt'
                sh 'ls'
                sh 'python -m unittest -v tests'
                echo "Finished steps"
            }
        }
    }
}
