pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh 'python -m unittest -v tests'
            }
        }
    }
}
