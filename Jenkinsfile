pipeline {
    agent { dockerfile true } 

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python3 /tmp/zip_job.py'
                }
            }
        }
    }
}
