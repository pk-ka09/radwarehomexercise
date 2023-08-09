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
        
     stage('Report') {
            post {
                always {
                    emailext(
                        subject: "Zip Job Build ${currentBuild.result}",
                        to: "${env.BUILD_USER_EMAIL}",
                        body: "${currentBuild.result}: ${env.BUILD_URL}"
                    )
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
