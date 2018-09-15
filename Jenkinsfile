node {
    stage('Initialize') {
        env.PYTHONPATH="tests"
    }

    stage('checkout') {
        checkout scm
    }
    stage('build') {
        sh 'curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o ./docker-compose; chmod +x ./docker-compose; ./docker-compose -f docker-compose-jenkins.yml build'
    }
}