node {
    stage('Initialize') {
        env.PYTHONPATH="tests"
    }

    stage('checkout') {
        checkout scm
    }
    stage('build') {
        sh 'curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose; chmod +x /usr/local/bin/docker-compose; export PATH="/usr/local/bin:$PATH"; docker-compose -f docker-compose-jenkins.yml build'
    }
}