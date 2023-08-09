pipeline {
    agent none
    
    stages {
        stage('image build){
              agent any
              steps {
                  script{
                     dockerImage = docker.build my-zip-image + ":$BUILD_NUMBER"
                  }
              }
         }
              
        stage('Build') {
            agent {
        docker {
            image 'my-zip-image'
            label 'zip-job-docker'
            args '-u root:root --privileged'
        }
    }
            steps {
                script {
                    sh 'python3 /tmp/zip_job.py'
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
