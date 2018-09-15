node {
    stage('Initialize') {
        env.PYTHONPATH="tests"
    }

    stage('checkout') {
        checkout scm
    }
    stage('build') {
        sh 'docker-compose -f docker-compose-jenkins.yml build'
    }
}