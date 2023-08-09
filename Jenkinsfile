pipeline {
    agent { dockerfile true } 
        
    
    #environment {
        ARTIFACTORY_URL = 'https://artifactory-xx'
        ARTIFACTORY_USER = 'superman'
        ARTIFACTORY_PASSWORD = 'P@ssw0rd123$'
        ARTIFACTORY_REPO = "store-artifacts/${VERSION}"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python3 /tmp/zip_job.py'
                }
            }
        }
        
        #stage('Publish') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    dir('/tmp') {
                        def zipFiles = sh(script: 'ls *.zip', returnStdout: true).trim().split('\n')
                        for (def zipFile in zipFiles) {
                            sh "curl -u ${ARTIFACTORY_USER}:${ARTIFACTORY_PASSWORD} -X PUT ${ARTIFACTORY_URL}/${ARTIFACTORY_REPO}/${zipFile} --upload-file ${zipFile}"
                        }
                    }
                }
            }
        }

        #stage('Report') {
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
