node {
    stage('Initialize') {
        env.PYTHONPATH="tests"
    }

    stage('checkout') {
        checkout scm
    }
    stage('build') {
        sh 'curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
        sh 'chmod +x /usr/local/bin/docker-compose'
        sh '/usr/local/bin/docker-compose -f docker-compose-jenkins.yml build'
    }
}