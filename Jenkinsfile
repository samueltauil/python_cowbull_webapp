pipeline {
    agent any
    environment {
        PYTHONPATH="tests"
    }
    stages {
        stage('Build') { 
            steps {
                step(
                    [
                        $class: 'DockerComposeBuilder', 
                        dockerComposeFile: 'docker-compose-jenkins.yml', 
                        option: [$class: 'StartAllServices'], 
                        useCustomDockerComposeFile: true]
                    )
            }
        }
    }
}
