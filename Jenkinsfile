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
                pwd
                ls
                sh 'python -m unittest -v tests'
                echo "Finished steps"
            }
        }
    }
}
